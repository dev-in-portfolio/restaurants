import { chromium } from 'playwright';
import fs from 'node:fs/promises';

const base = 'http://127.0.0.1:8080/boudreauxs/';
const routes = ['index.html','menu.html','story.html','gatherings.html','visit.html'];
const sizes = {
  desktop: { width: 1440, height: 1000 },
  mobile: { width: 390, height: 844 }
};

await fs.mkdir('qa/boudreauxs-v2', { recursive: true });
const browser = await chromium.launch({ headless: true });
const report = [];
let failed = false;

for (const [label, viewport] of Object.entries(sizes)) {
  const context = await browser.newContext({ viewport, deviceScaleFactor: 1 });
  for (const route of routes) {
    const page = await context.newPage();
    const errors = [];
    page.on('console', msg => { if (msg.type() === 'error') errors.push(msg.text()); });
    page.on('pageerror', err => errors.push(err.message));
    const response = await page.goto(base + route, { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts?.ready);
    await page.waitForTimeout(250);
    const metrics = await page.evaluate(() => {
      const h1 = document.querySelector('h1');
      const rect = h1?.getBoundingClientRect();
      return {
        title: document.title,
        scrollWidth: document.documentElement.scrollWidth,
        clientWidth: document.documentElement.clientWidth,
        h1: rect ? {
          left: rect.left,
          right: rect.right,
          top: rect.top,
          bottom: rect.bottom,
          width: rect.width,
          scrollWidth: h1.scrollWidth,
          clientWidth: h1.clientWidth
        } : null,
        currentNav: document.querySelectorAll('[aria-current="page"]').length,
        textLength: document.body.innerText.trim().length
      };
    });
    const overflow = metrics.scrollWidth > metrics.clientWidth + 1;
    const clipped = metrics.h1 && metrics.h1.scrollWidth > metrics.h1.clientWidth + 1;
    const ok = response?.ok() && !overflow && !clipped && metrics.currentNav === 1 && metrics.textLength > 650 && errors.length === 0;
    if (!ok) failed = true;
    report.push({ label, route, status: response?.status(), overflow, clipped, errors, ...metrics, ok });
    await page.screenshot({ path: `qa/boudreauxs-v2/${route.replace('.html','')}-${label}.png`, fullPage: true });
    await page.close();
  }
  const interactive = await context.newPage();
  await interactive.goto(base + 'menu.html', { waitUntil: 'networkidle' });
  await interactive.click('[data-filter="seafood"]');
  const visibleSeafood = await interactive.locator('[data-category]:visible').count();
  if (visibleSeafood !== 2) failed = true;
  await interactive.goto(base + 'gatherings.html', { waitUntil: 'networkidle' });
  await interactive.selectOption('[data-occasion]', { label: 'Birthday table' });
  await interactive.fill('[data-group]', '12');
  const plannerCopy = await interactive.locator('[data-plan-copy]').innerText();
  if (!plannerCopy.includes('12 guests')) failed = true;
  if (label === 'mobile') {
    await interactive.goto(base + 'index.html', { waitUntil: 'networkidle' });
    await interactive.click('[data-nav-toggle]');
    if (!(await interactive.locator('[data-nav-links]').isVisible())) failed = true;
  }
  await interactive.close();
  await context.close();
}
await browser.close();
await fs.writeFile('qa/boudreauxs-v2/report.json', JSON.stringify(report, null, 2));
if (failed) {
  console.error(JSON.stringify(report, null, 2));
  process.exit(1);
}
console.log('Boudreaux\'s v2 browser QA passed.');
