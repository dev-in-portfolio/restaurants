const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const workRoot = path.resolve(process.env.WORK_ROOT || '.');
const outDir = path.resolve(process.env.OUT_DIR || 'out');
const baseUrl = process.env.BASE_URL || 'http://127.0.0.1:4173';
const staticReport = JSON.parse(fs.readFileSync(path.join(outDir, 'phase2-static-report.json'), 'utf8'));
const viewports = [
  { name: 'desktop', width: 1440, height: 900 },
  { name: 'tablet', width: 1024, height: 768 },
  { name: 'mobile', width: 390, height: 844 },
];

function walkHtml(dir) {
  const results = [];
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (['.git', '.github', 'node_modules'].includes(entry.name)) continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) results.push(...walkHtml(full));
    else if (entry.name.toLowerCase().endsWith('.html')) results.push(full);
  }
  return results.sort();
}

function urlPath(value) {
  return value.split(path.sep).map(encodeURIComponent).join('/');
}

async function inspectPage(page, url, label, viewportName) {
  const failures = [];
  const warnings = [];
  const pageErrors = [];
  const localResponses = [];
  page.on('pageerror', error => pageErrors.push(error.message));
  page.on('response', response => {
    const responseUrl = response.url();
    if (responseUrl.startsWith(`${baseUrl}/`) && response.status() >= 400 && !responseUrl.endsWith('/favicon.ico')) {
      localResponses.push(`${response.status()} ${responseUrl}`);
    }
  });
  const response = await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 25000 });
  await page.waitForTimeout(80);
  if (!response || response.status() >= 400) failures.push(`${label}: navigation failed (${response?.status() ?? 'no response'})`);
  const checks = await page.evaluate(() => {
    const visible = element => !!(element.offsetWidth || element.offsetHeight || element.getClientRects().length);
    const ids = [...document.querySelectorAll('[id]')].map(element => element.id).filter(Boolean);
    const controls = [...document.querySelectorAll('button, input, select, textarea, a[href]')].filter(visible);
    const accessibleName = element => {
      const aria = element.getAttribute('aria-label') || element.getAttribute('title') || '';
      const labelledBy = (element.getAttribute('aria-labelledby') || '').split(/\s+/).filter(Boolean)
        .map(id => document.getElementById(id)?.textContent || '').join(' ');
      const label = element.id ? document.querySelector(`label[for="${CSS.escape(element.id)}"]`)?.textContent || '' : '';
      const wrappingLabel = element.closest('label')?.textContent || '';
      const text = element.textContent || element.value || element.getAttribute('placeholder') || '';
      const imageAlt = element.querySelector?.('img')?.getAttribute('alt') || '';
      return [aria, labelledBy, label, wrappingLabel, text, imageAlt].join(' ').trim();
    };
    const unnamedControls = controls.filter(element => {
      if (element.tagName === 'INPUT' && ['hidden', 'submit', 'button', 'reset'].includes((element.type || '').toLowerCase())) return false;
      return !accessibleName(element);
    }).length;
    const missingAlt = [...document.querySelectorAll('img')].filter(image => !image.hasAttribute('alt')).length;
    const skipTargetsMissing = [...document.querySelectorAll('a[href^="#"]')]
      .filter(link => /skip/i.test(link.className || '') || /skip/i.test(link.textContent || ''))
      .filter(link => {
        const id = decodeURIComponent(link.getAttribute('href').slice(1));
        return id && !document.getElementById(id);
      }).length;
    return {
      title: document.title.trim(),
      lang: document.documentElement.lang.trim(),
      mainCount: document.querySelectorAll('main').length,
      mainIdCount: document.querySelectorAll('main#main').length,
      bodyTextLength: document.body.innerText.replace(/\s+/g, ' ').trim().length,
      horizontalOverflow: document.documentElement.scrollWidth - window.innerWidth,
      duplicateIds: [...new Set(ids.filter((id, index) => ids.indexOf(id) !== index))],
      unnamedControls,
      missingAlt,
      skipTargetsMissing,
    };
  });
  if (!checks.title) failures.push(`${label}: empty title`);
  if (!checks.lang) failures.push(`${label}: missing html lang`);
  if (checks.mainCount !== 1 || checks.mainIdCount !== 1) failures.push(`${label}: expected exactly one main#main, found main=${checks.mainCount}, main#main=${checks.mainIdCount}`);
  if (checks.bodyTextLength < 180) failures.push(`${label}: insufficient visible content (${checks.bodyTextLength})`);
  if (checks.horizontalOverflow > 12) failures.push(`${label}: horizontal overflow ${checks.horizontalOverflow}px at ${viewportName}`);
  if (checks.duplicateIds.length) failures.push(`${label}: duplicate ids ${checks.duplicateIds.join(', ')}`);
  if (checks.skipTargetsMissing) failures.push(`${label}: ${checks.skipTargetsMissing} skip links target missing elements`);
  if (checks.unnamedControls) warnings.push(`${label}: ${checks.unnamedControls} visible controls have no accessible name`);
  if (checks.missingAlt) warnings.push(`${label}: ${checks.missingAlt} images are missing alt attributes`);
  failures.push(...pageErrors.map(error => `${label}: pageerror ${error}`));
  failures.push(...localResponses.map(error => `${label}: local response ${error}`));
  return { checks, failures, warnings };
}

(async () => {
  fs.mkdirSync(outDir, { recursive: true });
  const report = { startedAt: new Date().toISOString(), viewports, restaurants: [], failures: [], warnings: [] };
  const browser = await chromium.launch({ headless: true });
  try {
    for (const target of staticReport.targets) {
      const siteDir = path.join(workRoot, target.path);
      const pages = walkHtml(siteDir);
      const restaurant = { name: target.name, group: target.group, slug: target.slug, path: target.path, pages: pages.length, viewports: {} };
      for (const viewport of viewports) {
        const context = await browser.newContext({ viewport: { width: viewport.width, height: viewport.height } });
        const page = await context.newPage();
        const results = [];
        for (const file of pages) {
          const relRoot = path.relative(workRoot, file);
          const relSite = path.relative(siteDir, file);
          const url = `${baseUrl}/${urlPath(relRoot)}`;
          const result = await inspectPage(page, url, relSite, viewport.name);
          results.push({ file: relSite, ...result });
          if (result.failures.length) report.failures.push({ name: target.name, viewport: viewport.name, file: relSite, failures: result.failures });
          if (result.warnings.length) report.warnings.push({ name: target.name, viewport: viewport.name, file: relSite, warnings: result.warnings });
        }
        restaurant.viewports[viewport.name] = results;
        await context.close();
      }
      report.restaurants.push(restaurant);
      console.log(`[QA] ${target.name}: ${pages.length} pages across ${viewports.length} viewports`);
    }
  } finally {
    await browser.close();
  }
  report.completedAt = new Date().toISOString();
  fs.writeFileSync(path.join(outDir, 'phase2-browser-report.json'), JSON.stringify(report, null, 2) + '\n');
  console.log(JSON.stringify({ restaurants: report.restaurants.length, pageLoads: report.restaurants.reduce((sum, r) => sum + r.pages * viewports.length, 0), failures: report.failures.length, warnings: report.warnings.length }, null, 2));
  if (report.failures.length) process.exit(1);
})().catch(error => {
  console.error(error);
  process.exit(1);
});
