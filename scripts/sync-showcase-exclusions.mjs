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
  try {
    return parseQueueText(await fetchText(`${ORIGINAL_QUEUE_BASE}/${path}`), path);
  } catch (err) {
    // Offline / fallback to audit-ab-master.json if available
    const master = JSON.parse(await fs.readFile('queue/audit-ab-master.json', 'utf8'));
    const key = QUEUES.find(q => q[0] === path)?.[1];
    if (master.buckets && master.buckets[key]) return master.buckets[key];
    throw err;
  }
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
  canonicalSweepSource: {
    file: 'queue/charlotte-prospect-sweep-2026-08-28.json',
    checkpointDate: '2026-08-28',
    totalRecords: 94,
    reason: 'Preserves the authoritative 94-record supplemental Charlotte prospect sweep with supplied grades (A+, A, B).',
  },
  originalQueueCount: 0,
  excludedCount: 0,
  excludedActiveCount: 0,
  excludedHoldCount: 0,
  netQueueCount: 0,
  excluded: [],
  remainingByBucket: {},
  masterRows: {},
  sweep: {
    total: 0,
    excludedShowcase: 0,
    existingAudit: 0,
    admitted: 0,
    byGrade: {},
    exclusions: []
  }
};

const auditIndexByName = new Map();
const auditIndexBySlug = new Map();

for (const [path, variable] of QUEUES) {
  const rows = await readOriginalQueue(path);
  report.originalQueueCount += rows.length;
  report.masterRows[variable] = rows;
  const keep = [];

  for (const row of rows) {
    auditIndexByName.set(normalize(row[0]), row);
    auditIndexBySlug.set(normalizeSlug(row[1]), row);

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

// Reconcile supplemental prospect sweep
const sweepSourceRaw = JSON.parse(await fs.readFile('queue/charlotte-prospect-sweep-2026-08-28.json', 'utf8'));
const sweepRows = sweepSourceRaw.records || [];
report.sweep.total = sweepRows.length;

const admittedSweepRows = [];
for (const item of sweepRows) {
  const match = matchShowcase([item.name, item.slug], indexes, showcase);
  const auditMatch = auditIndexByName.get(normalize(item.name)) || auditIndexBySlug.get(normalizeSlug(item.slug));

  if (match) {
    report.sweep.excludedShowcase++;
    report.sweep.exclusions.push({
      position: item.position,
      restaurant: item.name,
      slug: item.slug,
      grade: item.grade,
      reason: 'showcase_exclusion',
      showcaseName: match.item.name,
      showcaseSlug: match.item.slug,
      showcaseSource: match.item.source,
      matchMethod: match.method,
    });
  } else if (auditMatch) {
    report.sweep.existingAudit++;
    report.sweep.exclusions.push({
      position: item.position,
      restaurant: item.name,
      slug: item.slug,
      grade: item.grade,
      reason: 'existing_audit_lead',
      auditName: auditMatch[0],
      auditSlug: auditMatch[1],
      auditGrade: auditMatch[2],
      auditDisposition: auditMatch[3],
    });
  } else {
    admittedSweepRows.push([item.name, item.slug, item.grade, item.position]);
    report.sweep.byGrade[item.grade] = (report.sweep.byGrade[item.grade] || 0) + 1;
  }
}

report.sweep.admitted = admittedSweepRows.length;

await fs.writeFile(
  'queue/sweep-2026-08-28.js',
  `window.restaurantSweepQueue_2026_08_28=${JSON.stringify(admittedSweepRows)};\n`,
  'utf8'
);

await fs.writeFile('queue/audit-ab-master.json', JSON.stringify({
  sourceRef: ORIGINAL_QUEUE_REF,
  total: report.originalQueueCount,
  buckets: report.masterRows,
}, null, 2) + '\n', 'utf8');

const totalExpectedActive = report.netQueueCount + report.sweep.admitted;

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
    expectedAuditActiveQueue: report.netQueueCount,
    aYes: remainingA,
    bYes: remainingBYes,
    bConditional: remainingBConditional,
    sweep20260828Total: report.sweep.total,
    sweep20260828ExcludedShowcase: report.sweep.excludedShowcase,
    sweep20260828ExistingAudit: report.sweep.existingAudit,
    sweep20260828Admitted: report.sweep.admitted,
    sweep20260828_APlus: report.sweep.byGrade['A+'] || 0,
    sweep20260828_A: report.sweep.byGrade['A'] || 0,
    sweep20260828_B: report.sweep.byGrade['B'] || 0,
    expectedActiveQueue: totalExpectedActive,
    showcaseActiveDemoCount: activeRaw.length,
    showcaseHoldDemoCount: holdRaw.length,
  })};\n`,
  'utf8'
);

// Update index.html
let index = await fs.readFile('index.html', 'utf8');
index = index.replace(/<div class="concept-notice"><strong>[\s\S]*?<\/div>/,
  `<div class="concept-notice"><strong>Active demo queue:</strong> the canonical queue combines ${report.netQueueCount} net-new prospects from the 407-row Rada-depth audit (${remainingA} A-grade YES, ${remainingBYes} B-grade YES, ${remainingBConditional} B-grade CONDITIONAL; ${report.excludedCount} Showcase excluded) plus ${report.sweep.admitted} net-new prospects from the Charlotte Prospect Sweep (${report.sweep.byGrade['A+'] || 0} A+, ${report.sweep.byGrade['A'] || 0} A, ${report.sweep.byGrade['B'] || 0} B; ${report.sweep.excludedShowcase + report.sweep.existingAudit} reconciled/excluded). Total active build queue: ${totalExpectedActive} restaurants.</div>`);

if (!index.includes('queue/meta.js')) {
  index = index.replace('  <script src="queue/a-yes-1.js"></script>', '  <script src="queue/meta.js"></script>\n  <script src="queue/a-yes-1.js"></script>');
}
if (!index.includes('queue/sweep-2026-08-28.js')) {
  index = index.replace('  <script src="queue/b-conditional.js"></script>', '  <script src="queue/b-conditional.js"></script>\n  <script src="queue/sweep-2026-08-28.js"></script>');
}
await fs.writeFile('index.html', index, 'utf8');

// Update STATUS.md
await fs.writeFile('STATUS.md', `# Restaurant Demo Status

## Active Queue Architecture

The canonical demo queue combines two authoritative sources minus all existing demos in \`dev-in-portfolio/restaurant-showcase\` (both active and HOLD):

1. **Original Rada-Depth Audit (407 A/B rows):**
   - **${report.netQueueCount} active net-new prospects**
   - **${remainingA} A-grade YES**
   - **${remainingBYes} B-grade YES**
   - **${remainingBConditional} B-grade CONDITIONAL**
   - **${report.excludedCount} audited A/B prospects removed because a Showcase demo already exists** (${report.excludedActiveCount} active Showcase, ${report.excludedHoldCount} Showcase HOLD)

2. **Charlotte Restaurant Prospect Sweep (2026-08-28) (94 rows):**
   - **${report.sweep.admitted} active net-new prospects admitted**
   - **${report.sweep.byGrade['A+'] || 0} A+ prospects**
   - **${report.sweep.byGrade['A'] || 0} A prospects**
   - **${report.sweep.byGrade['B'] || 0} B prospects**
   - **${report.sweep.excludedShowcase + report.sweep.existingAudit} records reconciled/excluded** (${report.sweep.excludedShowcase} active Showcase demos: Mert’s Heart & Soul, Homestyle Kitchn LLC, Exotica Indian Kitchen & Bar, Deluxe Fun Dining; ${report.sweep.existingAudit} existing audit record & premium build: The Public House)

**Combined Active Queue Total: ${totalExpectedActive} net-new prospects**

Showcase inventory checked: **${activeRaw.length} active + ${holdRaw.length} hold = ${activeRaw.length + holdRaw.length} existing demos**

Exact removals and reconciliations are recorded in \`queue/showcase-exclusions.json\`.
Immutable sources: \`queue/audit-ab-master.json\` and \`queue/charlotte-prospect-sweep-2026-08-28.json\`.

## Build-status rule

\`portal-overrides.js\` tracks build status only for restaurants still present in the active queue. Existing Showcase demos are not reintroduced through overrides.

## Selection order

1. A-grade YES (Audit) / A+ (Sweep)
2. A (Sweep)
3. B-grade YES (Audit)
4. B-grade CONDITIONAL (Audit) / B (Sweep)

Within a tier, sort alphabetically ignoring leading \`The\`, \`A\`, and \`An\`. Before selecting, run \`node scripts/sync-showcase-exclusions.mjs\` so a newly added Showcase demo cannot be rebuilt accidentally.

## Completion standard

A restaurant may be marked \`premium\` only after the current README standard, anti-template gate, factual evidence, desktop/mobile browser QA, machine validation, and accessibility baseline all pass. If browser QA is unavailable, the highest honest status is \`qa\`.
`, 'utf8');

// Update PORTAL_AUDIT.md
await fs.writeFile('PORTAL_AUDIT.md', `# Portal Architecture — Canonical Two-Source Net-New Queue

## Current state

The portal combines two authoritative prospect sources, then subtracts every restaurant that already has a demo in \`dev-in-portfolio/restaurant-showcase\` (both active and HOLD):

1. **Rada-Depth Audit (Immutable 407 A/B rows):**
   - 407 total rows
   - ${report.excludedCount} Showcase exclusions
   - ${report.netQueueCount} net-new active prospects (${remainingA} A YES / ${remainingBYes} B YES / ${remainingBConditional} B CONDITIONAL)

2. **Charlotte Prospect Sweep 2026-08-28 (Authoritative 94 rows):**
   - 94 total rows
   - ${report.sweep.excludedShowcase} Showcase exclusions
   - ${report.sweep.existingAudit} Existing audit duplicate (The Public House)
   - ${report.sweep.admitted} net-new active prospects (${report.sweep.byGrade['A+'] || 0} A+ / ${report.sweep.byGrade['A'] || 0} A / ${report.sweep.byGrade['B'] || 0} B)

**Combined active queue: ${totalExpectedActive} net-new prospects**

## Canonical data

- \`queue/audit-ab-master.json\` preserves the original 407 audited A/B rows.
- \`queue/charlotte-prospect-sweep-2026-08-28.json\` preserves the authoritative 94 supplemental sweep rows with supplied grades (A+, A, B).
- \`scripts/sync-showcase-exclusions.mjs\` reconciles both sources against Showcase active and hold files.
- Active queue data: \`queue/a-yes-1.js\`, \`queue/a-yes-2.js\`, \`queue/b-yes.js\`, \`queue/b-conditional.js\`, and \`queue/sweep-2026-08-28.js\`.
- \`queue/showcase-exclusions.json\` records every removed overlap and how it matched.
- \`queue/meta.js\` supplies the portal's expected live count (${totalExpectedActive}).

## Hard rule

If a restaurant exists in Showcase active **or Showcase HOLD**, it is excluded from automatic Gemini new-demo selection. A redo requires explicit user intent.

## Integrity checks

The portal reads \`queue/meta.js\` and verifies that the number of loaded rows equals the combined net-new count (${totalExpectedActive}). It also warns on duplicate canonical names or overrides for names outside the active queue.

## Source data truthfulness

Sweep records are rendered with their authentic source and grade (A+, A, B) without fabricating numeric scores or audit batches.
`, 'utf8');

console.log(JSON.stringify({
  auditMasterTotal: report.originalQueueCount,
  auditShowcaseExcluded: report.excludedCount,
  auditNetActive: report.netQueueCount,
  sweepTotal: report.sweep.total,
  sweepExcludedShowcase: report.sweep.excludedShowcase,
  sweepExistingAudit: report.sweep.existingAudit,
  sweepAdmitted: report.sweep.admitted,
  sweepByGrade: report.sweep.byGrade,
  combinedActiveQueueTotal: totalExpectedActive,
  showcaseInventory: {
    active: activeRaw.length,
    hold: holdRaw.length,
    total: activeRaw.length + holdRaw.length,
  }
}, null, 2));
