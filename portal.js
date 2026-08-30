(() => {
  'use strict';

  const grid = document.getElementById('restaurant-grid');
  const alphaNav = document.getElementById('alpha-nav');
  const stats = document.getElementById('portal-stats');
  const errorBox = document.getElementById('portal-error');

  const ALLOWED_STATUSES = new Set(['lead', 'incomplete', 'qa', 'premium', 'promoted', 'promoted_secondary']);

  const normalizeKey = (name = '') => name
    .normalize('NFKD')
    .replace(/[\u0300-\u036f]/g, '')
    .toLowerCase()
    .replace(/&/g, 'and')
    .replace(/[^a-z0-9]+/g, '');

  const sortName = (name = '') => name
    .replace(/^(the|a|an)\s+/i, '')
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '');

  const clean = (value = '') => String(value || '').replace(/\s{2,}/g, ' ').trim();

  function queueRows() {
    const auditRows = [
      ...(window.restaurantAuditQueue_A_YES_1 || []),
      ...(window.restaurantAuditQueue_A_YES_2 || []),
      ...(window.restaurantAuditQueue_B_YES || []),
      ...(window.restaurantAuditQueue_B_COND || [])
    ].map(row => ({ type: 'audit', row }));

    const sweepRows = (window.restaurantSweepQueue_2026_08_28 || []).map(row => ({ type: 'sweep', row }));

    return [...auditRows, ...sweepRows];
  }

  function baseRecord(item) {
    if (item.type === 'sweep') {
      const [name, slug, grade, position] = item.row;
      const cleanGrade = clean(grade);
      return {
        sourceType: 'sweep',
        name: clean(name),
        slug: clean(slug),
        grade: cleanGrade,
        disposition: undefined,
        score: undefined,
        auditBatch: undefined,
        sweepPosition: Number(position),
        status: 'lead',
        area: 'Charlotte area',
        cuisine: `${cleanGrade} • Charlotte Prospect Sweep`,
        description: `Charlotte Restaurant Prospect Sweep (2026-08-28) #${position}. ${cleanGrade}-grade prospect. Re-verify current public facts before building the premium concept.`,
        emoji: '🍽️',
        gradient: cleanGrade === 'A+'
          ? 'linear-gradient(135deg,#1e1b4b,#4f46e5 52%,#0f172a)'
          : (cleanGrade === 'A'
            ? 'linear-gradient(135deg,#1f2937,#7c3aed 52%,#111827)'
            : 'linear-gradient(135deg,#1e293b,#0f766e 52%,#0f172a)'),
        href: '',
        portalSection: undefined
      };
    }

    const [name, slug, grade, disposition, score, auditBatch] = item.row;
    const cleanGrade = clean(grade);
    const cleanDisp = clean(disposition);
    return {
      sourceType: 'audit',
      name: clean(name),
      slug: clean(slug),
      grade: cleanGrade,
      disposition: cleanDisp,
      score: Number(score),
      auditBatch: Number(auditBatch),
      status: 'lead',
      area: 'Charlotte area',
      cuisine: `${cleanGrade} • ${cleanDisp} • ${score}/100`,
      description: `Final Rada-depth audit Batch ${auditBatch}. ${cleanGrade}-grade ${cleanDisp} prospect, score ${score}/100. Re-verify current public facts before building the six-page premium concept.`,
      emoji: '🍽️',
      gradient: cleanGrade === 'A'
        ? 'linear-gradient(135deg,#1f2937,#7c3aed 52%,#111827)'
        : 'linear-gradient(135deg,#1e293b,#0f766e 52%,#0f172a)',
      href: '',
      portalSection: undefined
    };
  }

  function buildRecords() {
    const itemsRaw = queueRows();
    const byName = new Map();
    const bySlug = new Map();
    const duplicateNames = [];

    for (const item of itemsRaw) {
      const record = baseRecord(item);
      const key = normalizeKey(record.name);
      const slugKey = normalizeKey(record.slug);
      if (byName.has(key)) duplicateNames.push(record.name);
      byName.set(key, record);
      if (slugKey) bySlug.set(slugKey, record);
    }

    const unknownOverrides = [];
    for (const patch of (window.portalOverrides || [])) {
      if (!patch || !patch.name) continue;
      const key = normalizeKey(patch.name);
      const slugKey = normalizeKey(patch.slug || (patch.href || '').replace(/\/.*$/, ''));
      const current = byName.get(key) || bySlug.get(slugKey) || byName.get(key.replace(/^the/, '')) || byName.get('the' + key);
      if (!current) {
        // Only warn if the override is not an intentional excluded/closed/promoted annotation
        if (patch.status !== 'closed' && patch.status !== 'promoted' && patch.portalSection !== 'later') {
          unknownOverrides.push(patch.name);
        }
        continue;
      }
      const status = ALLOWED_STATUSES.has(patch.status) ? patch.status : current.status;
      const merged = {
        ...current,
        ...patch,
        status,
        grade: current.grade,
        disposition: current.disposition,
        score: current.score,
        auditBatch: current.auditBatch,
        slug: current.slug
      };
      if (status !== 'lead' && !merged.href) merged.href = `${current.slug}/index.html`;
      byName.set(normalizeKey(current.name), merged);
    }

    return { items: [...byName.values()], duplicateNames, unknownOverrides, rawCount: itemsRaw.length };
  }

  const getBaseDir = () => {
    let path = window.location.pathname;
    if (/\.[a-zA-Z0-9]+$/.test(path)) path = path.substring(0, path.lastIndexOf('/') + 1);
    if (!path.endsWith('/')) path += '/';
    return path;
  };

  function renderCard(item, baseDir) {
    const isLead = item.status === 'lead';
    const isPremium = ['premium', 'promoted', 'promoted_secondary'].includes(item.status);
    const isQa = item.status === 'qa';
    const isLater = item.portalSection === 'later';

    let badge;
    let label = 'Queued for Premium Rebuild';
    let cardClass = 'lead-card';

    if (item.sourceType === 'sweep' || typeof item.score !== 'number' || isNaN(item.score)) {
      if (isLater) {
        badge = `${item.grade} • RECHECK / LATER`;
        label = 'Not in Active Build Rotation';
        cardClass = 'incomplete-card';
      } else if (isPremium) {
        badge = `${item.grade} • PREMIUM • 6-PAGE QA PASSED`;
        label = 'View Premium Build';
        cardClass = 'premium-card';
      } else if (isQa) {
        badge = `${item.grade} • 6/6 PAGES • QA PENDING`;
        label = 'View Six-Page Build';
        cardClass = 'qa-card';
      } else if (!isLead) {
        badge = `${item.grade} • INCOMPLETE`;
        label = 'View Existing Build';
        cardClass = 'incomplete-card';
      } else {
        badge = `${item.grade} • PROSPECT SWEEP`;
        label = 'Queued for Premium Rebuild';
        cardClass = 'lead-card';
      }
    } else {
      if (isLater) {
        badge = `${item.grade} • RECHECK / LATER`;
        label = 'Not in Active Build Rotation';
        cardClass = 'incomplete-card';
      } else if (isPremium) {
        badge = `${item.grade} • PREMIUM • 6-PAGE QA PASSED`;
        label = 'View Premium Build';
        cardClass = 'premium-card';
      } else if (isQa) {
        badge = `${item.grade} • 6/6 PAGES • QA PENDING`;
        label = 'View Six-Page Build';
        cardClass = 'qa-card';
      } else if (!isLead) {
        badge = `${item.grade} • INCOMPLETE`;
        label = 'View Existing Build';
        cardClass = 'incomplete-card';
      } else {
        badge = `${item.grade} • ${item.disposition} • ${item.score}/100`;
        label = 'Queued for Premium Rebuild';
        cardClass = 'lead-card';
      }
    }

    let targetUrl = '';
    if (!isLead && !isLater && item.href) {
      targetUrl = /^(https?:|\/)/.test(item.href) ? item.href : baseDir + item.href;
    }

    const action = targetUrl
      ? `<a href="${targetUrl}" class="visit-btn">${label} →</a>`
      : `<span class="visit-btn disabled" aria-disabled="true">${label}</span>`;

    const dataHref = targetUrl ? ` data-href="${targetUrl}"` : '';
    const cuisine = item.cuisine || (item.sourceType === 'sweep'
      ? `${item.grade} • Charlotte Prospect Sweep`
      : `${item.grade} • ${item.disposition} • ${item.score}/100`);
    const description = item.description || (item.sourceType === 'sweep'
      ? `Charlotte Restaurant Prospect Sweep (2026-08-28) #${item.sweepPosition || ''}. Re-verify current facts before implementation.`
      : `Final Rada-depth audit Batch ${item.auditBatch}. Re-verify current facts before implementation.`);

    return `<article class="portal-card glass-panel ${cardClass}"${dataHref}><div class="card-image-wrapper"><span class="card-rating-badge">${badge}</span><div class="card-img-placeholder" style="background:${item.gradient}">${item.emoji || '🍽️'}</div></div><div class="card-content"><span class="card-cuisine">${cuisine}</span><h2 class="card-title">${item.name}</h2><p class="card-description">${description}</p><div class="card-footer"><span class="card-price">Area: <span>${item.area || 'Charlotte area'}</span></span>${action}</div></div></article>`;
  }

  function render(result) {
    const items = result.items.sort((a, b) => sortName(a.name).localeCompare(sortName(b.name), undefined, { sensitivity: 'base' }));
    const baseDir = getBaseDir();
    const active = items.filter(item => item.portalSection !== 'later');
    const letters = [...new Set(active.map(item => (sortName(item.name).charAt(0).toUpperCase() || '#')))];
    alphaNav.innerHTML = letters.map(letter => `<a href="#letter-${letter}">${letter}</a>`).join('');

    let lastLetter = '';
    let html = '';
    for (const item of active) {
      const letter = sortName(item.name).charAt(0).toUpperCase() || '#';
      if (letter !== lastLetter) {
        html += `<h2 class="letter-heading" id="letter-${letter}">${letter}</h2>`;
        lastLetter = letter;
      }
      html += renderCard(item, baseDir);
    }

    const later = items.filter(item => item.portalSection === 'later');
    if (later.length) {
      html += '<h2 class="letter-heading" id="letter-LATER">Recheck / Later</h2>';
      html += later.map(item => renderCard(item, baseDir)).join('');
    }
    grid.innerHTML = html;

    const counts = items.reduce((acc, item) => {
      const key = item.portalSection === 'later' ? 'later' : item.status;
      acc[key] = (acc[key] || 0) + 1;
      return acc;
    }, {});
    const gradeAPlus = items.filter(item => item.grade === 'A+').length;
    const gradeA = items.filter(item => item.grade === 'A').length;
    const gradeB = items.filter(item => item.grade === 'B').length;
    const meta = window.restaurantAuditQueueMeta || {};
    const excludedText = meta.showcaseExcluded ? ` • ${meta.showcaseExcluded} Showcase demos excluded` : '';
    const sweepCountText = meta.sweep20260828Admitted ? ` (${meta.expectedAuditActiveQueue || 223} audit + ${meta.sweep20260828Admitted} sweep)` : '';
    const gradeText = `${gradeAPlus ? gradeAPlus + ' A+ • ' : ''}${gradeA} A • ${gradeB} B`;
    stats.textContent = `${items.length} net-new prospects${sweepCountText} • ${gradeText} • ${counts.lead || 0} queued • ${counts.incomplete || 0} incomplete • ${counts.qa || 0} QA pending • ${(counts.premium || 0) + (counts.promoted || 0) + (counts.promoted_secondary || 0)} premium/promoted • ${counts.later || 0} recheck/later${excludedText}`;

    const problems = [];
    const expected = Number((window.restaurantAuditQueueMeta || {}).expectedActiveQueue);
    if (!expected) problems.push('Queue metadata missing expectedActiveQueue.');
    else if (result.rawCount !== expected) problems.push(`Expected ${expected} net-new queue rows; loaded ${result.rawCount}.`);
    if (result.duplicateNames.length) problems.push(`Duplicate canonical queue names: ${result.duplicateNames.join(', ')}.`);
    if (result.unknownOverrides.length) problems.push(`Ignored overrides outside the queue: ${result.unknownOverrides.join(', ')}.`);
    if (problems.length) {
      errorBox.hidden = false;
      errorBox.textContent = problems.join(' ');
    }
  }

  grid.addEventListener('click', event => {
    const card = event.target.closest('.portal-card[data-href]');
    if (!card || event.target.closest('a')) return;
    window.location.href = card.getAttribute('data-href');
  });

  render(buildRecords());
})();
