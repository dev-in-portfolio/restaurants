import fs from 'node:fs';
import path from 'node:path';

const ROOT = process.cwd();
const WRITE = process.argv.includes('--write');
const EXCLUDED = new Set(['.git', '.github', 'node_modules', 'scripts', 'audit-output']);
const changed = [];
const deleted = [];

function replaceAllTargeted(text) {
  const replacements = [
    [/Unofficial full five-page redesign demo/gi, 'Unofficial restaurant website presentation — incomplete under the six-page standard'],
    [/Unofficial five-page redesign demo/gi, 'Unofficial restaurant website presentation — incomplete under the six-page standard'],
    [/Unofficial five-page demo for/gi, 'Unofficial restaurant website presentation for'],
    [/Full five-page demo/gi, 'Incomplete under the six-page standard'],
    [/Complete information architecture/gi, 'Current information architecture'],
    [/Five real pages\. Five distinct jobs\./gi, 'Five current pages. A sixth substantive page is still required.'],
    [/5\/5 substantive pages built and published\./gi, 'Five substantive pages are currently built and published.'],
    [/premium visual QA pending/gi, 'six-page standard and visual QA pending'],
    [/Premium Website Concept/g, 'Website Concept'],
    [/premium website concept/gi, 'website concept']
  ];

  let output = text;
  for (const [pattern, replacement] of replacements) output = output.replace(pattern, replacement);
  return output;
}

function updateFile(file, transform) {
  const before = fs.readFileSync(file, 'utf8');
  const after = transform(before);
  if (after === before) return;
  changed.push(path.relative(ROOT, file).replaceAll(path.sep, '/'));
  if (WRITE) fs.writeFileSync(file, after, 'utf8');
}

for (const entry of fs.readdirSync(ROOT, { withFileTypes: true })) {
  if (!entry.isDirectory() || EXCLUDED.has(entry.name)) continue;
  const dir = path.join(ROOT, entry.name);
  if (!fs.existsSync(path.join(dir, 'index.html'))) continue;
  for (const file of fs.readdirSync(dir, { withFileTypes: true })) {
    if (file.isFile() && file.name.toLowerCase().endsWith('.html')) {
      updateFile(path.join(dir, file.name), replaceAllTargeted);
    }
  }
}

const legacyPortal = path.join(ROOT, 'portal-concepts-source.html');
if (fs.existsSync(legacyPortal)) {
  updateFile(legacyPortal, text => text
    .replace(/\{\{name:/g, '{name:')
    .replace(/status:"(?:premium|full|prototype)"/g, 'status:"incomplete"')
    .replace(/description:"Full rebuild:/g, 'description:"Existing build:'));
}

const workflowDir = path.join(ROOT, '.github', 'workflows');
if (fs.existsSync(workflowDir)) {
  for (const entry of fs.readdirSync(workflowDir, { withFileTypes: true })) {
    if (!entry.isFile() || !/\.ya?ml$/i.test(entry.name)) continue;
    const file = path.join(workflowDir, entry.name);
    const text = fs.readFileSync(file, 'utf8');
    if (/^name:\s*Build next 20 restaurant demos\s*$/mi.test(text)) {
      deleted.push(path.relative(ROOT, file).replaceAll(path.sep, '/'));
      if (WRITE) fs.unlinkSync(file);
    }
  }
}

console.log(JSON.stringify({ mode: WRITE ? 'write' : 'check', changedFileCount: changed.length, changed, deletedFileCount: deleted.length, deleted }, null, 2));
if (!WRITE && (changed.length || deleted.length)) process.exitCode = 2;
