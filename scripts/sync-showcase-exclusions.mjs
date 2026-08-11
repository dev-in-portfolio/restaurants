import fs from 'node:fs/promises';

const SHOWCASE_BASE = 'https://raw.githubusercontent.com/dev-in-portfolio/restaurant-showcase/main/data';
const ORIGINAL_QUEUE_REF = '99d7e3b4c809a367d230db0fc285ea44a802f662';
const ORIGINAL_QUEUE_BASE = `https://raw.githubusercontent.com/dev-in-portfolio/restaurants/${ORIGINAL_QUEUE_REF}`;
const QUEUES = [
  ['queue/a-yes-1.js', 'restaurantAuditQueue_A_YES_1'],
  ['queue/a-yes-2.js', 'restaurantAuditQueue_A_YES_2'],
  ['queue/b-yes.js', 'restaurantAuditQueue_B_YES'],
  ['queue/b-conditional.js', 'restaurantAuditQueue_B_COND'],
];

function normalize(value = '') {
  return String(value)
    .normalize('NFKD')
    .replace(/[\u0300-\u036f]/g, '')
    .toLowerCase()
    .replace(/&/g, ' and ')
    .replace(/\+/g, ' plus ')
    .replace(/[’'`]/g, '')
    .replace(/[^a-z0-9]+/g, '');
}

function normalizeSlug(value = '') {
  return normalize(String(value).replace(/-and-/g, '-').replace(/-plus-/g, '-'));
}

async function fetchText(url) {
  const response = await fetch(url, { headers: { 'User-Agent': 'restaurant-queue-housekeeping' } });
  if (!response.ok) throw new Error(`Fetch failed ${response.status}: ${url}`);
  return response.text();
}

async function fetchJson(url) {
  return JSON.parse(await fetchText(url));
}

function parseQueueText(text, path) {
  const match = text.match(/=\s*(\[[\s\S]*\])\s*;?\s*$/);
  if (!match) throw new Error(`Could not parse ${path}`);
  return JSON.parse(match[1]);
}

async function readOriginalQueue(path) {
  return parseQueueText(await fetchText(`${ORIGINAL_QUEUE_BASE}/${path}`), path);
}

function showcaseRecord(record, source) {
  return {
    source,
    name: record.name || '',
    slug: record.slug || record.id || '',
    href: record.href || record.demoRoute || '',
    status: record.status || '',
  };
}

function buildIndexes(showcase) {
  const byName = new Map();
  const bySlug = new Map();
  for (const item of showcase) {
    const nk = normalize(item.name);
    const sk = normalizeSlug(item.slug);
    if (nk) {
      const list = byName.get(nk) || [];
      list.push(item);
      byName.set(nk, list);
    }
    if (sk) {
      const list = bySlug.get(sk) || [];
      list.push(item);
      bySlug.set(sk, list);
    }
  }
  return { byName, bySlug };
}

function prefixCandidate(queueName, showcase) {
  const q = normalize(queueName);
  if (!q) return [];
  return showcase.filter(item => {
    const s = normalize(item.name);
    if (!s || Math.min(s.length, q.length) < 8) return false;
    return q.startsWith(s) || s.startsWith(q);
  });
}

function matchShowcase(row, indexes, showcase) {
  const [name, slug] = row;
  const nameMatches = indexes.byName.get(normalize(name)) || [];
  if (nameMatches.length === 1) return { item: nameMatches[0], method: 'normalized-name' };

  const slugMatches = indexes.bySlug.get(normalizeSlug(slug)) || [];
  if (slugMatches.length === 1) return { item: slugMatches[0], method: 'normalized-slug' };

  const prefix = prefixCandidate(name, showcase);
  if (prefix.length === 1) return { item: prefix[0], method: 'unique-name-prefix' };

  return null;
}

function replaceOrThrow(text, pattern, replacement, label) {
  const next = text.replace(pattern, replacement);
  if (next === text) throw new Error(`Documentation patch failed: ${label}`);
  return next;
}

const [activeRaw, holdRaw] = await Promise.all([
  fetchJson(`${SHOWCASE_BASE}/restaurants.json`),
  fetchJson(`${SHOWCASE_BASE}/hold-restaurants.json`),
]);

const showcase = [
  ...activeRaw.map(r => showcaseRecord(r, 'active')),
  ...holdRaw.map(r => showcaseRecord(r, 'hold')),
];
const indexes = buildIndexes(showcase);

const report = {
  generatedAt: new Date().toISOString(),
  source: {
    repository: 'dev-in-portfolio/restaurant-showcase',
    activeRecords: activeRaw.length,
    holdRecords: holdRaw.length,
    rule: 'Any existing Showcase demo, whether active or hold, is excluded from automatic Gemini build rotation.',
  },
  canonicalAuditSource: {
    repository: 'dev-in-portfolio/restaurants',
    immutableRef: ORIGINAL_QUEUE_REF,
    reason: 'Preserves the original 407 audited A/B rows so Showcase subtraction is reproducible on every sync.',
  },
  originalQueueCount: 0,
  excludedCount: 0,
  excludedActiveCount: 0,
  excludedHoldCount: 0,
  netQueueCount: 0,
  excluded: [],
  remainingByBucket: {},
  masterRows: {},
};

for (const [path, variable] of QUEUES) {
  const rows = await readOriginalQueue(path);
  report.originalQueueCount += rows.length;
  report.masterRows[variable] = rows;
  const keep = [];

  for (const row of rows) {
    const match = matchShowcase(row, indexes, showcase);
    if (match) {
      report.excluded.push({
        queue: path,
        restaurant: row[0],
        slug: row[1],
        grade: row[2],
        disposition: row[3],
        score: row[4],
        auditBatch: row[5],
        showcaseName: match.item.name,
        showcaseSlug: match.item.slug,
        showcaseSource: match.item.source,
        matchMethod: match.method,
      });
    } else {
      keep.push(row);
    }
  }

  report.remainingByBucket[variable] = keep.length;
  await fs.writeFile(path, `window.${variable}=${JSON.stringify(keep)};\n`, 'utf8');
}

if (report.originalQueueCount !== 407) {
  throw new Error(`Immutable audited A/B source must contain 407 rows; found ${report.originalQueueCount}.`);
}

report.excludedCount = report.excluded.length;
report.excludedActiveCount = report.excluded.filter(r => r.showcaseSource === 'active').length;
report.excludedHoldCount = report.excluded.filter(r => r.showcaseSource === 'hold').length;
report.netQueueCount = report.originalQueueCount - report.excludedCount;
report.excluded.sort((a, b) => a.restaurant.localeCompare(b.restaurant));

const remainingA = (report.remainingByBucket.restaurantAuditQueue_A_YES_1 || 0) + (report.remainingByBucket.restaurantAuditQueue_A_YES_2 || 0);
const remainingBYes = report.remainingByBucket.restaurantAuditQueue_B_YES || 0;
const remainingBConditional = report.remainingByBucket.restaurantAuditQueue_B_COND || 0;

await fs.writeFile('queue/audit-ab-master.json', JSON.stringify({
  sourceRef: ORIGINAL_QUEUE_REF,
  total: report.originalQueueCount,
  buckets: report.masterRows,
}, null, 2) + '\n', 'utf8');

const exclusionReport = { ...report };
delete exclusionReport.masterRows;
await fs.writeFile('queue/showcase-exclusions.json', JSON.stringify(exclusionReport, null, 2) + '\n', 'utf8');
await fs.writeFile(
  'queue/meta.js',
  `window.restaurantAuditQueueMeta=${JSON.stringify({
    originalAuditAB: report.originalQueueCount,
    showcaseExcluded: report.excludedCount,
    showcaseExcludedActive: report.excludedActiveCount,
    showcaseExcludedHold: report.excludedHoldCount,
    expectedActiveQueue: report.netQueueCount,
    aYes: remainingA,
    bYes: remainingBYes,
    bConditional: remainingBConditional,
    showcaseActiveDemoCount: activeRaw.length,
    showcaseHoldDemoCount: holdRaw.length,
  })};\n`,
  'utf8'
);

let index = await fs.readFile('index.html', 'utf8');
index = index.replace(/<div class="concept-notice"><strong>Canonical queue reset:<\/strong>[\s\S]*?<\/div>/,
  `<div class="concept-notice"><strong>Net-new demo queue:</strong> the completed audit produced 407 A/B prospects, but restaurants with an existing demo in <code>restaurant-showcase</code> are hard-excluded from automatic Gemini build rotation. Current net-new queue: ${report.netQueueCount} restaurants — ${remainingA} A-grade YES, ${remainingBYes} B-grade YES, and ${remainingBConditional} B-grade CONDITIONAL. ${report.excludedCount} audited A/B prospects are excluded because a Showcase demo already exists.</div>`);
if (!index.includes('queue/meta.js')) {
  index = index.replace('  <script src="queue/a-yes-1.js"></script>', '  <script src="queue/meta.js"></script>\n  <script src="queue/a-yes-1.js"></script>');
}
await fs.writeFile('index.html', index, 'utf8');

let portal = await fs.readFile('portal.js', 'utf8');
portal = portal.replace(
  "    stats.textContent = `${items.length} canonical A/B prospects • ${gradeA} A-grade • ${gradeB} B-grade • ${counts.lead || 0} queued • ${counts.incomplete || 0} incomplete • ${counts.qa || 0} QA pending • ${(counts.premium || 0) + (counts.promoted || 0) + (counts.promoted_secondary || 0)} premium/promoted • ${counts.later || 0} recheck/later`;",
  "    const meta = window.restaurantAuditQueueMeta || {};\n    const excludedText = meta.showcaseExcluded ? ` • ${meta.showcaseExcluded} Showcase demos excluded` : '';\n    stats.textContent = `${items.length} net-new A/B prospects • ${gradeA} A-grade • ${gradeB} B-grade • ${counts.lead || 0} queued • ${counts.incomplete || 0} incomplete • ${counts.qa || 0} QA pending • ${(counts.premium || 0) + (counts.promoted || 0) + (counts.promoted_secondary || 0)} premium/promoted • ${counts.later || 0} recheck/later${excludedText}`;"
);
portal = portal.replace(
  "    if (result.rawCount !== 407) problems.push(`Expected 407 audited queue rows; loaded ${result.rawCount}.`);",
  "    const expected = Number((window.restaurantAuditQueueMeta || {}).expectedActiveQueue);\n    if (!expected) problems.push('Queue metadata missing expectedActiveQueue.');\n    else if (result.rawCount !== expected) problems.push(`Expected ${expected} net-new audited queue rows; loaded ${result.rawCount}.`);"
);
await fs.writeFile('portal.js', portal, 'utf8');

let readme = await fs.readFile('README.md', 'utf8');
readme = readme.replace(
  'The active queue is **only** the final reconciled A/B set from the completed 645-record Rada-depth audit.',
  'The active build queue is the final reconciled A/B set from the completed 645-record Rada-depth audit **minus every restaurant that already has a demo in `dev-in-portfolio/restaurant-showcase`, including Showcase HOLD demos**.'
);
readme = readme.replace(/Current canonical queue:\n\n- \*\*407 active prospects total\*\*[\s\S]*?- \*\*0 merged aliases as separate leads\*\*/,
`Current net-new queue after Showcase subtraction:\n\n- **${report.netQueueCount} active net-new prospects total**\n- **${remainingA} A-grade YES**\n- **${remainingBYes} B-grade YES**\n- **${remainingBConditional} B-grade CONDITIONAL**\n- **${report.excludedCount} audited A/B prospects excluded because a Showcase demo already exists**\n- **0 HOLD audit records**\n- **0 NO audit records**\n- **0 merged aliases as separate leads**`);
readme = readme.replace(
  '- `queue/b-conditional.js`',
  '- `queue/b-conditional.js`\n- `queue/meta.js` — generated net-new counts\n- `queue/showcase-exclusions.json` — exact restaurants removed because Showcase demos already exist\n- `queue/audit-ab-master.json` — immutable 407-row audited A/B source snapshot'
);
readme = readme.replace(
  'The queue files are canonical audit data. **Do not edit them merely because a demo is built.** Build status belongs in `portal-overrides.js`.',
  'The 407-row audit master is preserved in `queue/audit-ab-master.json`. The four active queue files are generated net-new build data after Showcase subtraction. **Do not manually re-add Showcase restaurants.** Build status belongs in `portal-overrides.js`.'
);
if (!readme.includes('## Showcase exclusion is mandatory')) {
  readme = readme.replace('## Build-selection order', `## Showcase exclusion is mandatory\n\nA restaurant that already has a demo in \`dev-in-portfolio/restaurant-showcase\` is **not a new-demo candidate**, even if that Showcase record is currently in HOLD. Do not spend a Gemini run rebuilding it unless the user explicitly orders a redo.\n\nBefore selecting the next restaurant, run:\n\n\`\`\`bash\nnode scripts/sync-showcase-exclusions.mjs\n\`\`\`\n\nThe sync reads both \`restaurant-showcase/data/restaurants.json\` and \`restaurant-showcase/data/hold-restaurants.json\`, rebuilds the net-new queue from the immutable 407-row audit source, and writes \`queue/showcase-exclusions.json\`. If Showcase changed, include the resulting queue housekeeping in the same commit.\n\nNever bypass this rule because an old folder exists here, because a Showcase demo is on HOLD, or because the audit grade is A. **Existing Showcase demo = hard exclusion from automatic new-demo rotation.**\n\n## Build-selection order`);
}
readme = readme.replace('Folders for restaurants outside the canonical 407 queue are historical only and must not be selected automatically.', 'Folders for restaurants outside the current net-new queue are historical only and must not be selected automatically. Showcase restaurants remain excluded even if a similarly named folder exists here.');
await fs.writeFile('README.md', readme, 'utf8');

await fs.writeFile('STATUS.md', `# Restaurant Demo Status\n\n## Active net-new queue\n\nThe completed 645-record Rada-depth audit produced **407 A/B prospects** before Showcase reconciliation. Existing demos in \`dev-in-portfolio/restaurant-showcase\` are now a hard exclusion, including Showcase HOLD entries.\n\n- **${report.netQueueCount} active net-new prospects**\n- **${remainingA} A-grade YES**\n- **${remainingBYes} B-grade YES**\n- **${remainingBConditional} B-grade CONDITIONAL**\n- **${report.excludedCount} audited A/B prospects removed because a Showcase demo already exists** (${report.excludedActiveCount} active Showcase, ${report.excludedHoldCount} Showcase HOLD)\n- Showcase inventory checked: **${activeRaw.length} active + ${holdRaw.length} hold = ${activeRaw.length + holdRaw.length} existing demos**\n\nExact removals are recorded in \`queue/showcase-exclusions.json\`. The immutable pre-subtraction audit source is \`queue/audit-ab-master.json\`.\n\n## Build-status rule\n\n\`portal-overrides.js\` tracks build status only for restaurants still present in the net-new queue. Existing Showcase demos are not reintroduced through overrides.\n\n## Selection order\n\n1. A-grade YES\n2. B-grade YES\n3. B-grade CONDITIONAL\n\nWithin a tier, sort alphabetically ignoring leading \`The\`, \`A\`, and \`An\`. Before selecting, run \`node scripts/sync-showcase-exclusions.mjs\` so a newly added Showcase demo cannot be rebuilt accidentally.\n\n## Completion standard\n\nA restaurant may be marked \`premium\` only after the current README six-page standard, useful-interaction requirement, factual evidence, desktop/mobile browser QA, and accessibility baseline all pass. If browser QA is unavailable, the highest honest status is \`qa\`.\n`, 'utf8');

await fs.writeFile('PORTAL_AUDIT.md', `# Portal Architecture — Audited Net-New Queue\n\n## Current state\n\nThe portal starts from the completed audit's A/B prospect universe, then subtracts every restaurant that already has a demo in \`dev-in-portfolio/restaurant-showcase\`. Showcase HOLD demos are excluded too: HOLD means not currently presented there, not "needs another demo here."\n\nCurrent reconciliation:\n\n- Audit A/B universe: **407**\n- Showcase inventory checked: **${activeRaw.length} active + ${holdRaw.length} hold = ${activeRaw.length + holdRaw.length} demos**\n- Audit A/B restaurants with an existing Showcase demo: **${report.excludedCount}**\n- Net-new Gemini queue: **${report.netQueueCount}**\n- Remaining tiers: **${remainingA} A YES / ${remainingBYes} B YES / ${remainingBConditional} B CONDITIONAL**\n\n## Canonical data\n\n- \`queue/audit-ab-master.json\` preserves the original 407 audited A/B rows.\n- \`scripts/sync-showcase-exclusions.mjs\` compares that immutable source against both Showcase data files.\n- The generated active queue lives in the four \`queue/*.js\` bucket files.\n- \`queue/showcase-exclusions.json\` records every removed overlap and how it matched.\n- \`queue/meta.js\` supplies the portal's expected live count.\n\n## Hard rule\n\nIf a restaurant exists in Showcase active **or Showcase HOLD**, it is excluded from automatic Gemini new-demo selection. A redo requires explicit user intent.\n\n## Integrity checks\n\nThe portal no longer hardcodes 407 as its rendered queue size. It reads \`queue/meta.js\` and verifies that the number of loaded rows equals the latest generated net-new count. It also warns on duplicate canonical names or overrides for names outside the net-new queue.\n\n## Legacy folders and sources\n\nOld restaurant folders and the retired legacy lead/concept files remain historical/reference material only. They cannot make a restaurant eligible. Build selection comes only from the generated net-new queue.\n\n## Completion rule\n\nThe current six-page premium standard in \`README.md\` remains unchanged: restaurant-specific design, six substantive pages, two useful interactions including one conversion interaction, current evidence, responsive/browser QA, accessibility checks, and truthful demo-safe behavior.\n`, 'utf8');

console.log(JSON.stringify({
  original: report.originalQueueCount,
  showcaseActive: activeRaw.length,
  showcaseHold: holdRaw.length,
  excluded: report.excludedCount,
  excludedActive: report.excludedActiveCount,
  excludedHold: report.excludedHoldCount,
  net: report.netQueueCount,
  remainingA,
  remainingBYes,
  remainingBConditional,
}, null, 2));
