#!/usr/bin/env node

import fs from 'node:fs';
import path from 'node:path';

const slug = process.argv[2];
if (!slug) {
  console.error('Usage: node scripts/check-design-diversity.mjs <restaurant-slug>');
  process.exit(2);
}

const repoRoot = process.cwd();
const demoDir = path.resolve(repoRoot, slug);
const recentLimit = 10;
const rejectScore = 0.72;

function read(file) {
  return fs.readFileSync(file, 'utf8');
}

function setFrom(values) {
  return new Set(values.filter(Boolean));
}

function jaccard(a, b) {
  if (!a.size && !b.size) return 1;
  if (!a.size || !b.size) return 0;
  let intersection = 0;
  for (const value of a) if (b.has(value)) intersection += 1;
  const union = a.size + b.size - intersection;
  return union ? intersection / union : 0;
}

function extractClassSet(html) {
  const values = [];
  for (const match of html.matchAll(/\bclass\s*=\s*["']([^"']+)["']/gi)) {
    values.push(...match[1].split(/\s+/).filter(Boolean).filter(v => v !== 'active' && v !== 'open' && v !== 'is-open'));
  }
  return setFrom(values);
}

function extractCssClasses(css) {
  return setFrom([...css.matchAll(/\.([A-Za-z_-][A-Za-z0-9_-]*)/g)].map(m => m[1]));
}

function extractSectionTokens(html) {
  const values = [];
  for (const match of html.matchAll(/<section\b([^>]*)>/gi)) {
    const attrs = match[1];
    const classMatch = attrs.match(/\bclass\s*=\s*["']([^"']+)["']/i);
    if (classMatch) values.push(...classMatch[1].split(/\s+/).filter(Boolean));
    else values.push('section');
  }
  return setFrom(values);
}

function extractFonts(css) {
  const values = [];
  for (const match of css.matchAll(/font-family\s*:\s*([^;}{]+)/gi)) {
    const first = match[1].split(',')[0].trim().replace(/["']/g, '').toLowerCase();
    if (first && !first.startsWith('var(')) values.push(first);
  }
  for (const match of css.matchAll(/--font-[\w-]+\s*:\s*["']?([^,"';}]+)/gi)) {
    const value = match[1].trim().toLowerCase();
    if (value) values.push(value);
  }
  return setFrom(values);
}

function extractDomNgrams(html, size = 4) {
  const tags = [...html.matchAll(/<\/?([a-z][a-z0-9-]*)\b/gi)]
    .map(m => m[1].toLowerCase())
    .filter(tag => !['meta', 'link', 'script'].includes(tag));
  const grams = [];
  for (let i = 0; i <= tags.length - size; i += 1) grams.push(tags.slice(i, i + size).join('>'));
  return setFrom(grams);
}

function fingerprint(targetSlug) {
  const dir = path.join(repoRoot, targetSlug);
  const indexPath = path.join(dir, 'index.html');
  const cssPath = path.join(dir, 'site.css');
  if (!fs.existsSync(indexPath) || !fs.existsSync(cssPath)) return null;
  const html = read(indexPath);
  const css = read(cssPath);
  return {
    slug: targetSlug,
    classes: extractClassSet(html),
    cssClasses: extractCssClasses(css),
    sectionTokens: extractSectionTokens(html),
    fonts: extractFonts(css),
    domNgrams: extractDomNgrams(html)
  };
}

function similarity(current, prior) {
  const classSimilarity = jaccard(current.classes, prior.classes);
  const cssClassSimilarity = jaccard(current.cssClasses, prior.cssClasses);
  const domSimilarity = jaccard(current.domNgrams, prior.domNgrams);
  const sectionSimilarity = jaccard(current.sectionTokens, prior.sectionTokens);
  const fontSimilarity = jaccard(current.fonts, prior.fonts);
  const score = (
    classSimilarity * 0.27 +
    cssClassSimilarity * 0.27 +
    domSimilarity * 0.24 +
    sectionSimilarity * 0.14 +
    fontSimilarity * 0.08
  );
  return {
    score,
    classSimilarity,
    cssClassSimilarity,
    domSimilarity,
    sectionSimilarity,
    fontSimilarity
  };
}

if (!fs.existsSync(demoDir)) {
  console.error(`Demo folder not found: ${slug}`);
  process.exit(2);
}

const current = fingerprint(slug);
if (!current) {
  console.error(`${slug}: index.html and site.css are required before diversity validation.`);
  process.exit(2);
}

const overridesPath = path.join(repoRoot, 'portal-overrides.js');
const recent = [];
if (fs.existsSync(overridesPath)) {
  const overrides = read(overridesPath);
  for (const match of overrides.matchAll(/href\s*:\s*["']([^"']+)\/index\.html["']/g)) {
    const candidate = match[1];
    if (candidate !== slug && !recent.includes(candidate)) recent.push(candidate);
  }
}

const recentSlugs = recent.slice(-recentLimit);
const comparisons = [];
for (const priorSlug of recentSlugs) {
  const prior = fingerprint(priorSlug);
  if (!prior) continue;
  comparisons.push({ priorSlug, ...similarity(current, prior) });
}
comparisons.sort((a, b) => b.score - a.score);

const closest = comparisons[0] || null;
const hardClone = closest && (
  closest.score >= rejectScore ||
  (closest.classSimilarity >= 0.80 && closest.cssClassSimilarity >= 0.80) ||
  (closest.domSimilarity >= 0.90 && closest.sectionSimilarity >= 0.80)
);

const serializable = {
  slug,
  generatedAt: new Date().toISOString(),
  recentCompared: comparisons.length,
  recentSlugs,
  rejectionThreshold: rejectScore,
  closestMatch: closest,
  passed: !hardClone,
  comparisons
};

fs.writeFileSync(path.join(demoDir, 'design-diversity.json'), `${JSON.stringify(serializable, null, 2)}\n`, 'utf8');

if (hardClone) {
  console.error(
    `FAIL ${slug}: design fingerprint is too close to recent demo '${closest.priorSlug}' ` +
    `(score ${closest.score.toFixed(3)}; classes ${closest.classSimilarity.toFixed(3)}; CSS ${closest.cssClassSimilarity.toFixed(3)}; DOM ${closest.domSimilarity.toFixed(3)}).`
  );
  console.error('Redesign the core composition; changing only colors, copy, cuisine nouns, or imagery is not sufficient.');
  process.exit(1);
}

if (closest) {
  console.log(`PASS ${slug}: closest recent design '${closest.priorSlug}' scored ${closest.score.toFixed(3)}.`);
} else {
  console.log(`PASS ${slug}: no comparable recent demo fingerprints were available.`);
}
