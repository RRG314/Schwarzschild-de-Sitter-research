#!/usr/bin/env node
import fs from 'node:fs';
import path from 'node:path';

const root = path.resolve(process.argv[2] || '.');
const mdFiles = [];

function walk(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (entry.name === '.git' || entry.name === 'node_modules' || entry.name === '.venv') continue;
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) walk(full);
    if (entry.isFile() && entry.name.endsWith('.md')) mdFiles.push(full);
  }
}

walk(root);

const broken = [];
const mdLink = /\[[^\]]*\]\(([^)]+)\)/g;

for (const file of mdFiles) {
  const content = fs.readFileSync(file, 'utf8');
  for (const match of content.matchAll(mdLink)) {
    const target = match[1].trim();
    if (!target || target.startsWith('http://') || target.startsWith('https://') || target.startsWith('#') || target.startsWith('mailto:')) continue;
    if (target.includes('\\')) continue;
    if (!target.includes('/') && !target.includes('.')) continue;
    const clean = target.split('#')[0];
    if (!clean) continue;

    const resolved = clean.startsWith('/') ? clean : path.resolve(path.dirname(file), clean);
    if (!fs.existsSync(resolved)) {
      broken.push({ file: path.relative(root, file), link: target });
    }
  }
}

if (broken.length) {
  console.error(`Broken links: ${broken.length}`);
  for (const item of broken) console.error(`- ${item.file}: ${item.link}`);
  process.exit(1);
}

console.log(`OK: ${mdFiles.length} markdown files scanned, no broken local links.`);
