import fs from 'node:fs/promises';

const SHOWCASE_BASE = 'https://raw.githubusercontent.com/dev-in-portfolio/restaurant-showcase/main/data';
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

async function fetchJson(url) {
  const response = await fetch(url, { headers: { 'User-Agent': 'restaurant-queue-housekeeping' } });
  if (!response.ok) throw new Error(`Fetch failed ${response.status}: ${url}`);
  return response.json();
}

async function readQueue(path) {
  const text = await fs.readFile(path, 'utf8');
  const match = text.match(/=\s*(\[[\s\S]*\])\s*;?\s*$/);
  if (!match) throw new Error(`Could not parse ${path}`);
  return JSON.parse(match[1]);
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
  originalQueueCount: 0,
  excludedCount: 0,
  netQueueCount: 0,
  excluded: [],
  remainingByBucket: {},
};

for (const [path, variable] of QUEUES) {
  const rows = await readQueue(path);
  report.originalQueueCount += rows.length;
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

report.excludedCount = report.excluded.length;
report.netQueueCount = report.originalQueueCount - report.excludedCount;
report.excluded.sort((a, b) => a.restaurant.localeCompare(b.restaurant));

const remainingA = (report.remainingByBucket.restaurantAuditQueue_A_YES_1 || 0) + (report.remainingByBucket.restaurantAuditQueue_A_YES_2 || 0);
const remainingBYes = report.remainingByBucket.restaurantAuditQueue_B_YES || 0;
const remainingBConditional = report.remainingByBucket.restaurantAuditQueue_B_COND || 0;

await fs.writeFile('queue/showcase-exclusions.json', JSON.stringify(report, null, 2) + '\n', 'utf8');
await fs.writeFile(
  'queue/meta.js',
  `window.restaurantAuditQueueMeta=${JSON.stringify({
    originalAuditAB: report.originalQueueCount,
    showcaseExcluded: report.excludedCount,
    expectedActiveQueue: report.netQueueCount,
    aYes: remainingA,
    bYes: remainingBYes,
    bConditional: remainingBConditional,
    showcaseActiveDemoCount: activeRaw.length,
    showcaseHoldDemoCount: holdRaw.length,
  })};\n`,
  'utf8'
);

console.log(JSON.stringify({
  original: report.originalQueueCount,
  showcaseActive: activeRaw.length,
  showcaseHold: holdRaw.length,
  excluded: report.excludedCount,
  net: report.netQueueCount,
  remainingA,
  remainingBYes,
  remainingBConditional,
}, null, 2));
