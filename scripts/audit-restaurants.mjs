import fs from 'node:fs';
import path from 'node:path';
import vm from 'node:vm';

const ROOT = process.cwd();
const OUT_DIR = path.join(ROOT, 'audit-output');
const EXCLUDED_ROOT_DIRS = new Set(['.git', '.github', 'node_modules', 'scripts', 'audit-output']);
const CLAIM_RE = /\b(?:full|complete|completed|finished|premium)\b|\b5[- ]page\b|\bfive[- ]page\b|\b6\s*\/\s*6\b/gi;
const EXPLICIT_STATUS_RE = /\b(?:full|complete|completed|premium)\s+(?:(?:five|5|six|6)[ -]?page|rebuild|demo|site|website|information architecture)|\b(?:five|5|six|6)[ -]?page\s+(?:demo|rebuild|site|website)|\b(?:5|6)\s*\/\s*(?:5|6)\s+pages?\b|\bstatus[^<\n]{0,60}\b(?:full|premium|complete)\b/gi;

function readText(file) {
  try {
    return fs.readFileSync(file, 'utf8');
  } catch {
    return '';
  }
}

function walk(dir, predicate = () => true) {
  const results = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (entry.name === '.git' || entry.name === 'node_modules' || entry.name === 'audit-output') continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) results.push(...walk(full, predicate));
    else if (predicate(full)) results.push(full);
  }
  return results;
}

function stripMarkup(html) {
  return html
    .replace(/<!--[\s\S]*?-->/g, ' ')
    .replace(/<script\b[\s\S]*?<\/script>/gi, ' ')
    .replace(/<style\b[\s\S]*?<\/style>/gi, ' ')
    .replace(/<[^>]+>/g, ' ')
    .replace(/&nbsp;|&#160;/gi, ' ')
    .replace(/&[a-z0-9#]+;/gi, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}

function titleOf(html) {
  return (html.match(/<title[^>]*>([\s\S]*?)<\/title>/i)?.[1] || '')
    .replace(/\s+/g, ' ')
    .trim();
}

function lineNumberAt(text, index) {
  return text.slice(0, index).split('\n').length;
}

function isRedirectPage(html, visibleText) {
  const explicitRedirect = /<meta[^>]+http-equiv=["']?refresh/i.test(html)
    || /(?:window\.)?location\.(?:replace|assign)\s*\(/i.test(html)
    || /(?:window\.)?location(?:\.href)?\s*=/i.test(html);
  return explicitRedirect && visibleText.length < 700;
}

function inspectPage(file, siteDir) {
  const html = readText(file);
  const visible = stripMarkup(html);
  const relative = path.relative(siteDir, file).replaceAll(path.sep, '/');
  const redirect = isRedirectPage(html, visible);
  const hasDocument = /<html\b/i.test(html) && /<body\b/i.test(html) && /<title\b/i.test(html);
  const hasContentContainer = /<(?:main|section|article)\b/i.test(html);
  const substantive = !redirect
    && hasDocument
    && hasContentContainer
    && html.length >= 1200
    && visible.length >= 250;

  return {
    file: relative,
    bytes: Buffer.byteLength(html, 'utf8'),
    visibleCharacters: visible.length,
    title: titleOf(html),
    redirect,
    hasDocument,
    hasContentContainer,
    substantive,
    html
  };
}

function extractHrefs(fragment) {
  return [...fragment.matchAll(/\bhref\s*=\s*["']([^"']+)["']/gi)].map(match => match[1].trim());
}

function isIgnoredHref(href) {
  return !href
    || href.startsWith('#')
    || /^(?:https?:|mailto:|tel:|javascript:|data:|blob:|sms:)/i.test(href);
}

function resolveInternalLink(pageFile, href) {
  const clean = href.split('#')[0].split('?')[0];
  if (!clean) return null;
  let target = clean.startsWith('/')
    ? path.resolve(ROOT, clean.slice(1))
    : path.resolve(path.dirname(pageFile), clean);
  if (clean.endsWith('/')) target = path.join(target, 'index.html');
  if (!path.extname(target) && fs.existsSync(path.join(target, 'index.html'))) target = path.join(target, 'index.html');
  return target;
}

function inspectLinks(page, absoluteFile, repoRoot) {
  const all = extractHrefs(page.html);
  const internal = all.filter(href => !isIgnoredHref(href));
  const broken = [];
  const resolved = [];

  for (const href of internal) {
    const target = resolveInternalLink(absoluteFile, href);
    if (!target) continue;
    const insideRepo = target === repoRoot || target.startsWith(`${repoRoot}${path.sep}`);
    if (!insideRepo || !fs.existsSync(target)) {
      broken.push({ href, target: path.relative(repoRoot, target).replaceAll(path.sep, '/') });
    } else {
      resolved.push(path.relative(repoRoot, target).replaceAll(path.sep, '/'));
    }
  }

  const navBlocks = [...page.html.matchAll(/<nav\b[^>]*>([\s\S]*?)<\/nav>/gi)].map(match => match[1]);
  const navTargets = new Set();
  for (const block of navBlocks) {
    for (const href of extractHrefs(block)) {
      if (isIgnoredHref(href)) continue;
      const target = resolveInternalLink(absoluteFile, href);
      if (target && fs.existsSync(target)) navTargets.add(path.basename(target));
    }
  }

  return { internalCount: internal.length, resolved, broken, navTargets: [...navTargets].sort() };
}

function inferPageRoles(pages) {
  const filenames = pages.filter(page => page.substantive).map(page => page.file.toLowerCase());
  const has = regex => filenames.some(name => regex.test(name));
  return {
    home: filenames.includes('index.html'),
    menu: has(/(?:^|\/)(?:menu|taps?|beer|drinks?|flavors?|food)(?:[-_.]|\.html|\/)/),
    story: has(/(?:^|\/)(?:about|story|history|team|our-story)(?:[-_.]|\.html|\/)/),
    experience: has(/(?:^|\/)(?:experience|brunch|taproom|bakery|market|locations?|neighborhood|drinks?|entertainment|press|roast|specials)(?:[-_.]|\.html|\/)/),
    conversion: has(/(?:^|\/)(?:catering|reserve|reservations|private-dining|events|order|services|parties|gatherings|contact)(?:[-_.]|\.html|\/)/),
    visit: has(/(?:^|\/)(?:visit|contact|locations?)(?:[-_.]|\.html|\/)/)
  };
}

function occurrences(file, text, regex) {
  const matches = [];
  regex.lastIndex = 0;
  for (const match of text.matchAll(regex)) {
    const start = Math.max(0, match.index - 80);
    const end = Math.min(text.length, match.index + match[0].length + 110);
    matches.push({
      file: path.relative(ROOT, file).replaceAll(path.sep, '/'),
      line: lineNumberAt(text, match.index),
      term: match[0],
      context: text.slice(start, end).replace(/\s+/g, ' ').trim()
    });
  }
  return matches;
}

function normalizeName(name = '') {
  return String(name)
    .normalize('NFKD')
    .replace(/[\u0300-\u036f]/g, '')
    .toLowerCase()
    .replace(/&/g, 'and')
    .replace(/[^a-z0-9]+/g, '')
    .replace(/^(the|an|a)/, '')
    .replace(/(restaurant|cafe|company|co)$/, '');
}

function parseLegacyPortalSource() {
  const sourceFile = path.join(ROOT, 'portal-concepts-source.html');
  const sourceText = readText(sourceFile);
  const startMarker = 'const concepts = [';
  const start = sourceText.indexOf(startMarker);
  const end = sourceText.indexOf('\n    ];', start);
  if (start < 0 || end < 0) {
    return { candidateObjects: 0, parsed: [], errors: [{ line: 0, reason: 'concept array markers not found' }] };
  }

  const block = sourceText.slice(start + startMarker.length, end);
  const candidateObjects = (block.match(/\{name:/g) || []).length;
  const parsed = [];
  const errors = [];

  block.split(/\r?\n/).forEach((rawLine, index) => {
    let line = rawLine.trim();
    if (!line.includes('{name:')) return;
    const objectsOnLine = (line.match(/\{name:/g) || []).length;
    line = line.replace(/,$/, '');
    if (objectsOnLine !== 1) {
      errors.push({ line: index + 1, reason: `${objectsOnLine} object starts on one line`, excerpt: line.slice(0, 300) });
      return;
    }
    try {
      const item = Function(`"use strict"; return (${line});`)();
      if (item && item.name) parsed.push(item);
      else errors.push({ line: index + 1, reason: 'entry did not produce a named object', excerpt: line.slice(0, 300) });
    } catch (error) {
      errors.push({ line: index + 1, reason: error.message, excerpt: line.slice(0, 300) });
    }
  });

  return { candidateObjects, parsed, errors };
}

function loadWindowArray(relativeFile, property) {
  const file = path.join(ROOT, relativeFile);
  if (!fs.existsSync(file)) return { items: [], error: 'file missing' };
  const context = { window: {} };
  context.window.window = context.window;
  try {
    vm.runInNewContext(readText(file), context, { filename: relativeFile, timeout: 5000 });
    const value = context.window[property];
    return { items: Array.isArray(value) ? Array.from(value) : [], error: Array.isArray(value) ? null : `${property} was not an array` };
  } catch (error) {
    return { items: [], error: error.message };
  }
}

function reconstructPortalState() {
  const legacy = parseLegacyPortalSource();
  const message2 = loadWindowArray('portal-leads-message2-original.js', 'restaurantLeadsMessage2');
  const message3 = loadWindowArray('portal-leads-message3.js', 'restaurantLeadsMessage3');
  const overrides = loadWindowArray('portal-overrides.js', 'portalOverrides');
  const priority = { lead: 0, incomplete: 1, qa: 2, premium: 3 };
  const byName = new Map();

  const groups = [
    { type: 'legacy', items: legacy.parsed },
    { type: 'lead', items: message2.items },
    { type: 'lead', items: message3.items },
    { type: 'override', items: overrides.items }
  ];

  for (const group of groups) {
    for (const item of group.items) {
      const sourceLead = item.status === 'lead' || group.type === 'lead';
      const allowedOverride = group.type === 'override' && ['lead', 'incomplete', 'qa', 'premium'].includes(item.status);
      const status = allowedOverride ? item.status : (sourceLead ? 'lead' : 'incomplete');
      const key = normalizeName(item.name);
      if (!key) continue;
      const normalized = { ...item, status };
      const current = byName.get(key);
      if (!current || priority[status] >= priority[current.status]) byName.set(key, normalized);
    }
  }

  const merged = [...byName.values()];
  const statusCounts = merged.reduce((acc, item) => {
    acc[item.status] = (acc[item.status] || 0) + 1;
    return acc;
  }, {});

  return {
    legacyCandidateObjects: legacy.candidateObjects,
    legacyParsedObjects: legacy.parsed.length,
    legacyParseErrors: legacy.errors,
    message2Entries: message2.items.length,
    message2Error: message2.error,
    message3Entries: message3.items.length,
    message3Error: message3.error,
    overrideEntries: overrides.items.length,
    overrideError: overrides.error,
    renderedUniqueRestaurants: merged.length,
    activeStatusCounts: statusCounts,
    activeQaOrPremiumCount: (statusCounts.qa || 0) + (statusCounts.premium || 0),
    activeCompleteOrPremiumClaim: ((statusCounts.qa || 0) + (statusCounts.premium || 0)) > 0
  };
}

const rootDirs = fs.readdirSync(ROOT, { withFileTypes: true })
  .filter(entry => entry.isDirectory() && !EXCLUDED_ROOT_DIRS.has(entry.name))
  .map(entry => entry.name)
  .sort((a, b) => a.localeCompare(b));

const sites = [];
for (const folder of rootDirs) {
  const siteDir = path.join(ROOT, folder);
  if (!fs.existsSync(path.join(siteDir, 'index.html'))) continue;

  const htmlFiles = walk(siteDir, file => file.toLowerCase().endsWith('.html')).sort();
  const pages = htmlFiles.map(file => inspectPage(file, siteDir));
  const directHtmlCount = fs.readdirSync(siteDir, { withFileTypes: true })
    .filter(entry => entry.isFile() && entry.name.toLowerCase().endsWith('.html')).length;

  let brokenLinkCount = 0;
  let internalLinkCount = 0;
  const brokenLinks = [];
  const navTargetCounts = [];
  const navSignatures = new Map();

  for (const page of pages) {
    const absolute = path.join(siteDir, page.file);
    const links = inspectLinks(page, absolute, ROOT);
    page.internalLinkCount = links.internalCount;
    page.brokenLinks = links.broken;
    page.navTargets = links.navTargets;
    internalLinkCount += links.internalCount;
    brokenLinkCount += links.broken.length;
    brokenLinks.push(...links.broken.map(item => ({ page: page.file, ...item })));
    if (page.substantive) {
      navTargetCounts.push(links.navTargets.length);
      const signature = links.navTargets.join('|');
      navSignatures.set(signature, (navSignatures.get(signature) || 0) + 1);
    }
    delete page.html;
  }

  const substantivePages = pages.filter(page => page.substantive);
  const redirectPages = pages.filter(page => page.redirect);
  const roles = inferPageRoles(pages);
  const minimumNavTargets = navTargetCounts.length ? Math.min(...navTargetCounts) : 0;
  const dominantNavCount = navSignatures.size ? Math.max(...navSignatures.values()) : 0;
  const navConsistency = substantivePages.length ? dominantNavCount / substantivePages.length : 0;

  sites.push({
    folder,
    totalHtmlFiles: pages.length,
    directHtmlFiles: directHtmlCount,
    substantivePageCount: substantivePages.length,
    substantivePages: substantivePages.map(page => page.file),
    nonSubstantivePages: pages.filter(page => !page.substantive).map(page => ({
      file: page.file,
      bytes: page.bytes,
      visibleCharacters: page.visibleCharacters,
      redirect: page.redirect,
      hasDocument: page.hasDocument,
      hasContentContainer: page.hasContentContainer
    })),
    redirectPageCount: redirectPages.length,
    brokenLinkCount,
    internalLinkCount,
    brokenLinks,
    minimumNavTargets,
    navConsistency: Number(navConsistency.toFixed(3)),
    roles,
    sixPageCountMet: substantivePages.length >= 6,
    sixRoleHeuristicMet: Object.values(roles).every(Boolean),
    pages
  });
}

const siteFolderSet = new Set(sites.map(site => site.folder));
const claimFiles = walk(ROOT, file => /\.(?:html?|md|js|mjs)$/i.test(file));
const claims = claimFiles.flatMap(file => occurrences(file, readText(file), CLAIM_RE));
const explicitStatusClaims = claimFiles.flatMap(file => occurrences(file, readText(file), EXPLICIT_STATUS_RE));
const explicitRestaurantStatusClaims = explicitStatusClaims.filter(claim => siteFolderSet.has(claim.file.split('/')[0]));

const portalFiles = ['index.html', 'portal.js', 'portal-overrides.js', 'portal-concepts-source.html', 'portal-leads-message2.js', 'portal-leads-message2-original.js', 'portal-leads-message3.js']
  .filter(file => fs.existsSync(path.join(ROOT, file)));
const portalClaims = claims.filter(claim => portalFiles.includes(claim.file));
const explicitPortalStatusClaims = explicitStatusClaims.filter(claim => portalFiles.includes(claim.file));
const portalRuntime = reconstructPortalState();

const distribution = sites.reduce((acc, site) => {
  const key = site.substantivePageCount >= 6 ? '6+' : String(site.substantivePageCount);
  acc[key] = (acc[key] || 0) + 1;
  return acc;
}, {});

const boudreauxs = sites.find(site => site.folder === 'boudreauxs') || null;
const summary = {
  generatedAt: new Date().toISOString(),
  repositoryRoot: ROOT,
  restaurantDirectories: sites.length,
  sixOrMoreSubstantivePages: sites.filter(site => site.substantivePageCount >= 6).length,
  exactlyFiveSubstantivePages: sites.filter(site => site.substantivePageCount === 5).length,
  fewerThanFiveSubstantivePages: sites.filter(site => site.substantivePageCount < 5).length,
  redirectOnlyDirectories: sites.filter(site => site.substantivePageCount === 0 && site.redirectPageCount > 0).length,
  sitesWithBrokenInternalLinks: sites.filter(site => site.brokenLinkCount > 0).length,
  totalBrokenInternalLinks: sites.reduce((sum, site) => sum + site.brokenLinkCount, 0),
  sitesMeetingSixRoleHeuristic: sites.filter(site => site.sixRoleHeuristicMet).length,
  statusClaimOccurrences: claims.length,
  explicitStatusClaimOccurrences: explicitStatusClaims.length,
  restaurantFilesWithExplicitStatusClaims: new Set(explicitRestaurantStatusClaims.map(claim => claim.file)).size,
  restaurantSitesWithExplicitStatusClaims: new Set(explicitRestaurantStatusClaims.map(claim => claim.file.split('/')[0])).size,
  portalStatusClaimOccurrences: portalClaims.length,
  explicitPortalStatusClaimOccurrences: explicitPortalStatusClaims.length,
  pageCountDistribution: distribution,
  boudreauxsSubstantivePageCount: boudreauxs?.substantivePageCount ?? null,
  boudreauxsSubstantivePages: boudreauxs?.substantivePages ?? [],
  activePortalQaOrPremiumCount: portalRuntime.activeQaOrPremiumCount,
  certification: 'No restaurant is certified complete or premium by this audit. Page count is evidence, not certification.'
};

const report = { summary, portalRuntime, sites, claims, explicitStatusClaims, explicitRestaurantStatusClaims, portalClaims, explicitPortalStatusClaims };
fs.mkdirSync(OUT_DIR, { recursive: true });
fs.writeFileSync(path.join(OUT_DIR, 'restaurant-audit.json'), `${JSON.stringify(report, null, 2)}\n`);

const rows = sites.map(site => {
  const roles = Object.entries(site.roles).filter(([, value]) => value).map(([key]) => key).join(', ');
  return `| \`${site.folder}\` | ${site.totalHtmlFiles} | ${site.substantivePageCount} | ${site.redirectPageCount} | ${site.brokenLinkCount} | ${site.minimumNavTargets} | ${roles || '—'} |`;
});

const sixPageFolders = sites.filter(site => site.sixPageCountMet).map(site => `- \`${site.folder}\`: ${site.substantivePageCount} substantive pages`).join('\n') || '- None';
const fivePageFolders = sites.filter(site => site.substantivePageCount === 5).map(site => `- \`${site.folder}\``).join('\n') || '- None';
const brokenFolders = sites.filter(site => site.brokenLinkCount > 0).map(site => `- \`${site.folder}\`: ${site.brokenLinkCount} broken internal link(s)`).join('\n') || '- None';
const malformedPortalLines = portalRuntime.legacyParseErrors.map(error => `- Line ${error.line}: ${error.reason}${error.excerpt ? ` — \`${error.excerpt.replaceAll('`', "'")}\`` : ''}`).join('\n') || '- None';
const explicitClaimFiles = [...new Set(explicitRestaurantStatusClaims.map(claim => claim.file))].sort().map(file => `- \`${file}\``).join('\n') || '- None';

const markdown = `# Restaurant Repository Deep Audit\n\nGenerated: ${summary.generatedAt}\n\n## Certification result\n\n**No restaurant is certified complete or premium by this audit.** A six-page count is only the first gate; content separation, navigation, links, interactions and browser QA still require verification.\n\n## Verified portal state\n\n- Unique restaurants reconstructed from the active portal sources: **${portalRuntime.renderedUniqueRestaurants}**\n- Active queued leads: **${portalRuntime.activeStatusCounts.lead || 0}**\n- Active incomplete builds: **${portalRuntime.activeStatusCounts.incomplete || 0}**\n- Active six-page QA-pending entries: **${portalRuntime.activeStatusCounts.qa || 0}**\n- Active premium entries: **${portalRuntime.activeStatusCounts.premium || 0}**\n- Active QA-or-premium total: **${portalRuntime.activeQaOrPremiumCount}**\n- Legacy portal objects found: **${portalRuntime.legacyCandidateObjects}**\n- Legacy portal objects parsed: **${portalRuntime.legacyParsedObjects}**\n- Legacy portal parse errors: **${portalRuntime.legacyParseErrors.length}**\n- Message 2 lead entries loaded: **${portalRuntime.message2Entries}**${portalRuntime.message2Error ? ` — error: ${portalRuntime.message2Error}` : ''}\n- Message 3 lead entries loaded: **${portalRuntime.message3Entries}**${portalRuntime.message3Error ? ` — error: ${portalRuntime.message3Error}` : ''}\n- Explicit override entries: **${portalRuntime.overrideEntries}**${portalRuntime.overrideError ? ` — error: ${portalRuntime.overrideError}` : ''}\n\n### Malformed legacy portal entries\n\n${malformedPortalLines}\n\n## Page-count summary\n\n- Restaurant directories with an \`index.html\`: **${summary.restaurantDirectories}**\n- Six or more substantive HTML pages: **${summary.sixOrMoreSubstantivePages}**\n- Exactly five substantive HTML pages: **${summary.exactlyFiveSubstantivePages}**\n- Fewer than five substantive HTML pages: **${summary.fewerThanFiveSubstantivePages}**\n- Redirect-only directories: **${summary.redirectOnlyDirectories}**\n- Sites with broken internal links: **${summary.sitesWithBrokenInternalLinks}**\n- Total broken internal links: **${summary.totalBrokenInternalLinks}**\n- Sites matching all six filename-role heuristics: **${summary.sitesMeetingSixRoleHeuristic}**\n\n## Boudreaux’s verification\n\n- Substantive page count: **${summary.boudreauxsSubstantivePageCount}**\n- Pages: ${summary.boudreauxsSubstantivePages.map(page => `\`${page}\``).join(', ') || 'None'}\n- Result: **Incomplete under the six-page standard.**\n\n## Status-language audit\n\n- Broad full/complete/premium/five-page occurrences: **${summary.statusClaimOccurrences}**\n- Explicit completion/status claims: **${summary.explicitStatusClaimOccurrences}**\n- Restaurant sites containing explicit completion/status claims: **${summary.restaurantSitesWithExplicitStatusClaims}**\n- Restaurant HTML/JS/Markdown files containing explicit claims: **${summary.restaurantFilesWithExplicitStatusClaims}**\n- Explicit claims in portal-status files: **${summary.explicitPortalStatusClaimOccurrences}**\n\n### Restaurant files containing explicit completion/status language\n\n${explicitClaimFiles}\n\n## Six-or-more-page directories\n\n${sixPageFolders}\n\n## Exactly-five-page directories\n\n${fivePageFolders}\n\n## Directories with broken internal links\n\n${brokenFolders}\n\n## Full inventory\n\n| Directory | HTML files | Substantive | Redirects | Broken links | Minimum nav targets | Detected roles |\n|---|---:|---:|---:|---:|---:|---|\n${rows.join('\n')}\n\n## Method\n\nA page is counted as substantive only when it is not a redirect, contains a complete HTML document, includes a main/section/article content container, contains at least 1,200 bytes of markup and at least 250 visible characters. Root-relative links are resolved from the repository root; relative links are resolved from the current page. The audit inventories navigation targets, reconstructs the active portal merge and status normalization, and records visible full/complete/premium/five-page claims for follow-up.\n`;

fs.writeFileSync(path.join(OUT_DIR, 'restaurant-audit.md'), markdown);

console.log('AUDIT_SUMMARY_START');
console.log(JSON.stringify({ summary, portalRuntime }, null, 2));
console.log('AUDIT_SUMMARY_END');
console.log(`Markdown report: ${path.relative(ROOT, path.join(OUT_DIR, 'restaurant-audit.md'))}`);
console.log(`JSON report: ${path.relative(ROOT, path.join(OUT_DIR, 'restaurant-audit.json'))}`);
