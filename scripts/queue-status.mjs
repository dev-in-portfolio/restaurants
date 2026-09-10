import fs from 'fs';

const queueCode = fs.readFileSync('queue/sweep-2026-08-28.js', 'utf8');
const sandbox = {};
const fn = new Function('window', queueCode);
fn(sandbox);
const queue = sandbox.restaurantSweepQueue_2026_08_28;
const excl = JSON.parse(fs.readFileSync('queue/showcase-exclusions.json', 'utf8'));
const overrides = fs.readFileSync('portal-overrides.js', 'utf8');

console.log('--- SWEEP QUEUE STATUS ---');
for (const [name, slug, grade, pos] of queue) {
  const isExcl = excl.excluded.some(e => e.slug === slug || e.showcaseSlug === slug);
  const existsLocally = fs.existsSync(slug);
  const inOverrides = overrides.includes(slug);
  if (!isExcl && !inOverrides) {
    console.log(`#${pos} [${grade}] ${name} (${slug}) | existsLocally: ${existsLocally}`);
  }
}
