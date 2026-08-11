#!/usr/bin/env node

import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import { spawnSync } from 'node:child_process';

const slug = process.argv[2];
if (!slug) {
  console.error('Usage: node scripts/validate-demo.mjs <restaurant-slug>');
  process.exit(2);
}

const repoRoot = process.cwd();
const demoDir = path.resolve(repoRoot, slug);
const errors = [];
const warnings = [];
const checks = [];

function addCheck(name, passed, detail = '') {
  checks.push({ name, passed, detail });
  if (!passed) errors.push(`${name}${detail ? `: ${detail}` : ''}`);
}

function stripCssComments(css) {
  return css.replace(/\/\*[\s\S]*?\*\//g, '');
}

function checkBraceBalance(text, label) {
  const css = stripCssComments(text);
  let depth = 0;
  let quote = null;
  let escaped = false;
  for (let i = 0; i < css.length; i += 1) {
    const ch = css[i];
    if (escaped) {
      escaped = false;
      continue;
    }
    if (ch === '\\') {
      escaped = true;
      continue;
    }
    if (quote) {
      if (ch === quote) quote = null;
      continue;
    }
    if (ch === '"' || ch === "'") {
      quote = ch;
      continue;
    }
    if (ch === '{') depth += 1;
    if (ch === '}') depth -= 1;
    if (depth < 0) return `${label}: unexpected closing brace`;
  }
  if (depth !== 0) return `${label}: unbalanced braces (${depth > 0 ? `${depth} missing closing` : `${Math.abs(depth)} extra closing`})`;
  return null;
}

function localRef(value) {
  if (!value) return false;
  const v = value.trim();
  return !(
    v.startsWith('http://') ||
    v.startsWith('https://') ||
    v.startsWith('//') ||
    v.startsWith('mailto:') ||
    v.startsWith('tel:') ||
    v.startsWith('data:') ||
    v.startsWith('javascript:')
  );
}

function getAttr(tag, name) {
  const re = new RegExp(`${name}\\s*=\\s*["']([^"']*)["']`, 'i');
  return tag.match(re)?.[1] ?? null;
}

function read(file) {
  return fs.readFileSync(file, 'utf8');
}

function exactHash(text) {
  return crypto.createHash('sha256').update(text).digest('hex');
}

if (!fs.existsSync(demoDir) || !fs.statSync(demoDir).isDirectory()) {
  console.error(`Demo folder not found: ${slug}`);
  process.exit(2);
}

const entries = fs.readdirSync(demoDir, { withFileTypes: true });
const htmlFiles = entries.filter(e => e.isFile() && e.name.endsWith('.html')).map(e => e.name).sort();
const cssFiles = entries.filter(e => e.isFile() && e.name.endsWith('.css')).map(e => e.name).sort();
const jsFiles = entries.filter(e => e.isFile() && e.name.endsWith('.js')).map(e => e.name).sort();

addCheck('Minimum substantive HTML page count', htmlFiles.length >= 5, `${htmlFiles.length} HTML pages found; minimum is 5`);
addCheck('index.html exists', htmlFiles.includes('index.html'));
addCheck('menu.html exists', htmlFiles.includes('menu.html'));
addCheck('visit/contact page exists', htmlFiles.some(n => /^(visit|contact)\.html$/i.test(n)));
addCheck('evidence.md exists', fs.existsSync(path.join(demoDir, 'evidence.md')));

const placeholderPatterns = [
  /lorem ipsum/i,
  /email@example\.com/i,
  /example\.com/i,
  /555[- )]/i,
  /\bTODO\b/i,
  /\bFIXME\b/i,
  /placeholder/i,
  /coming soon/i
];

for (const cssName of cssFiles) {
  const cssPath = path.join(demoDir, cssName);
  const issue = checkBraceBalance(read(cssPath), cssName);
  addCheck(`CSS balance ${cssName}`, !issue, issue || 'balanced');
}

for (const jsName of jsFiles) {
  const jsPath = path.join(demoDir, jsName);
  const result = spawnSync(process.execPath, ['--check', jsPath], { encoding: 'utf8' });
  addCheck(`JavaScript parse ${jsName}`, result.status === 0, (result.stderr || result.stdout || '').trim());
}

const htmlCache = new Map();
const htmlHashes = new Map();
for (const htmlName of htmlFiles) {
  const htmlPath = path.join(demoDir, htmlName);
  const html = read(htmlPath);
  htmlCache.set(htmlName, html);

  const hash = exactHash(html);
  if (!htmlHashes.has(hash)) htmlHashes.set(hash, []);
  htmlHashes.get(hash).push(htmlName);

  addCheck(`${htmlName} has <title>`, /<title>[^<]+<\/title>/i.test(html));
  addCheck(`${htmlName} has viewport meta`, /<meta[^>]+name=["']viewport["']/i.test(html));

  const ids = [...html.matchAll(/\bid\s*=\s*["']([^"']+)["']/gi)].map(m => m[1]);
  const duplicateIds = [...new Set(ids.filter((id, i) => ids.indexOf(id) !== i))];
  addCheck(`${htmlName} duplicate IDs`, duplicateIds.length === 0, duplicateIds.join(', '));

  const imgTags = [...html.matchAll(/<img\b[^>]*>/gi)].map(m => m[0]);
  const missingAlt = imgTags.filter(tag => getAttr(tag, 'alt') === null);
  addCheck(`${htmlName} image alt attributes`, missingAlt.length === 0, `${missingAlt.length} image(s) missing alt`);

  const formCount = (html.match(/<form\b/gi) || []).length;
  addCheck(`${htmlName} automatic-demo form prohibition`, formCount === 0, `${formCount} form(s) found`);

  for (const pattern of placeholderPatterns) {
    if (pattern.test(html)) errors.push(`${htmlName}: placeholder/test residue matched ${pattern}`);
  }

  const inlineStyles = [...html.matchAll(/<style\b[^>]*>([\s\S]*?)<\/style>/gi)];
  for (let i = 0; i < inlineStyles.length; i += 1) {
    const issue = checkBraceBalance(inlineStyles[i][1], `${htmlName} inline style ${i + 1}`);
    if (issue) errors.push(issue);
  }

  if (htmlName !== 'index.html') {
    const hasHome = /href\s*=\s*["'](?:\.\/)?index\.html(?:[#?][^"']*)?["']/i.test(html);
    addCheck(`${htmlName} links back to home`, hasHome);
  }
}

const exactDuplicatePages = [...htmlHashes.values()].filter(group => group.length > 1);
addCheck(
  'No exact duplicate HTML pages',
  exactDuplicatePages.length === 0,
  exactDuplicatePages.map(group => group.join(' = ')).join('; ')
);

function resolveTarget(currentHtml, rawValue) {
  const [beforeHash, fragment = ''] = rawValue.split('#', 2);
  const [pathname] = beforeHash.split('?', 1);
  const currentDir = path.dirname(path.join(demoDir, currentHtml));
  let targetPath;
  if (!pathname) targetPath = path.join(demoDir, currentHtml);
  else targetPath = path.resolve(currentDir, decodeURIComponent(pathname));
  if (targetPath.endsWith(path.sep)) targetPath = path.join(targetPath, 'index.html');
  return { targetPath, fragment: decodeURIComponent(fragment || '') };
}

for (const htmlName of htmlFiles) {
  const html = htmlCache.get(htmlName);
  const tags = [...html.matchAll(/<(?:a|img|script|link)\b[^>]*>/gi)].map(m => m[0]);
  for (const tag of tags) {
    const raw = getAttr(tag, /^<a/i.test(tag) || /^<link/i.test(tag) ? 'href' : 'src');
    if (!raw || !localRef(raw)) continue;
    if (raw === '#') {
      errors.push(`${htmlName}: dead local reference '#'`);
      continue;
    }
    const { targetPath, fragment } = resolveTarget(htmlName, raw);
    if (!fs.existsSync(targetPath)) {
      errors.push(`${htmlName}: broken local reference '${raw}'`);
      continue;
    }
    if (fragment && targetPath.endsWith('.html')) {
      const targetHtml = read(targetPath);
      const escaped = fragment.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
      const fragmentRe = new RegExp(`(?:id|name)\\s*=\\s*["']${escaped}["']`, 'i');
      if (!fragmentRe.test(targetHtml)) {
        errors.push(`${htmlName}: fragment '${raw}' points to no matching id/name`);
      }
    }
  }
}

if (fs.existsSync(path.join(demoDir, 'evidence.md'))) {
  const evidence = read(path.join(demoDir, 'evidence.md'));
  for (const heading of ['## Creative Brief', '## Claim Ledger', '## Add-On Preservation', '## Cross-Demo Diversity']) {
    addCheck(`evidence.md contains ${heading}`, evidence.includes(heading));
  }
}

const diversityScript = path.join(repoRoot, 'scripts', 'check-design-diversity.mjs');
if (fs.existsSync(diversityScript)) {
  const diversity = spawnSync(process.execPath, [diversityScript, slug], { cwd: repoRoot, encoding: 'utf8' });
  const detail = (diversity.stderr || diversity.stdout || '').trim();
  addCheck('Cross-demo design diversity', diversity.status === 0, detail);
} else {
  addCheck('Cross-demo design diversity', false, 'scripts/check-design-diversity.mjs is missing');
}

const report = {
  slug,
  generatedAt: new Date().toISOString(),
  htmlPages: htmlFiles,
  cssFiles,
  jsFiles,
  passed: errors.length === 0,
  errors: [...new Set(errors)],
  warnings: [...new Set(warnings)],
  checks
};

fs.writeFileSync(path.join(demoDir, 'qa-report.json'), `${JSON.stringify(report, null, 2)}\n`, 'utf8');

if (report.passed) {
  console.log(`PASS ${slug}: ${htmlFiles.length} HTML pages; qa-report.json and design-diversity.json written.`);
  process.exit(0);
}

console.error(`FAIL ${slug}: ${report.errors.length} error(s).`);
for (const error of report.errors) console.error(`- ${error}`);
console.error(`Report: ${path.join(slug, 'qa-report.json')}`);
process.exit(1);
