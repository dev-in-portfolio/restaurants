import { chromium } from 'playwright';
import { mkdir } from 'node:fs/promises';

const base = 'http://127.0.0.1:4173/boudreauxs';
const pages = ['index.html', 'menu.html', 'story.html', 'gatherings.html', 'visit.html'];
const views = [
  { name: 'desktop', width: 1440, height: 1100 },
  { name: 'mobile', width: 390, height: 844 },
];

await mkdir('qa-artifacts/boudreauxs', { recursive: true });
const browser = await chromium.launch({ headless: true });

for (const view of views) {
  const context = await browser.newContext({ viewport: { width: view.width, height: view.height } });
  const page = await context.newPage();
  const consoleErrors = [];
  page.on('console', message => {
    if (message.type() === 'error') consoleErrors.push(message.text());
  });
  page.on('pageerror', error => consoleErrors.push(error.message));

  for (const filename of pages) {
    const response = await page.goto(`${base}/${filename}`, { waitUntil: 'networkidle' });
    if (!response?.ok()) throw new Error(`${filename} returned ${response?.status()}`);
    await page.screenshot({ path: `qa-artifacts/boudreauxs/${filename.replace('.html', '')}-${view.name}.png`, fullPage: true });

    const broken = await page.locator('a[href]').evaluateAll((links, origin) => links
      .map(link => link.getAttribute('href'))
      .filter(href => href && !href.startsWith('#') && !href.startsWith('http') && !href.startsWith('mailto:') && !href.startsWith('tel:'))
      .filter(href => !href.includes('.html') && !href.endsWith('/')), base);
    if (broken.length) throw new Error(`${filename} has suspicious internal links: ${broken.join(', ')}`);
  }

  if (consoleErrors.length) throw new Error(`${view.name} console errors: ${consoleErrors.join(' | ')}`);
  await context.close();
}

await browser.close();
console.log('Boudreaux visual QA screenshots completed.');
