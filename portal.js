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

  const clean = (value = '') => String(value).replace(/\s{2,}/g, ' ').trim();

  function queueRows() {
    return [
      ...(window.restaurantAuditQueue_A_YES_1 || []),
      ...(window.restaurantAuditQueue_A_YES_2 || []),
      ...(window.restaurantAuditQueue_B_YES || []),
      ...(window.restaurantAuditQueue_B_COND || [])
    ];
  }

  function baseRecord(row) {
    const [name, slug, grade, disposition, score, auditBatch] = row;
    return {
      name: clean(name),
      slug: clean(slug),
      grade: clean(grade),
      disposition: clean(disposition),
      score: Number(score),
      auditBatch: Number(auditBatch),
      status: 'lead',
      area: 'Charlotte area',
      cuisine: `${grade} • ${disposition} • ${score}/100`,
      description: `Final Rada-depth audit Batch ${auditBatch}. ${grade}-grade ${disposition} prospect, score ${score}/100. Re-verify current public facts before building the six-page premium concept.`,
      emoji: '🍽️',
      gradient: grade === 'A'
        ? 'linear-gradient(135deg,#1f2937,#7c3aed 52%,#111827)'
        : 'linear-gradient(135deg,#1e293b,#0f766e 52%,#0f172a)',
      href: '',
      portalSection: undefined
    };
  }

  function buildRecords() {
    const rows = queueRows();
    const byName = new Map();
    const duplicateNames = [];

    for (const row of rows) {
      const record = baseRecord(row);
      const key = normalizeKey(record.name);
      if (byName.has(key)) duplicateNames.push(record.name);
      byName.set(key, record);
    }

    const unknownOverrides = [];
    for (const patch of (window.portalOverrides || [])) {
      if (!patch || !patch.name) continue;
      const key = normalizeKey(patch.name);
      const current = byName.get(key);
      if (!current) {
        unknownOverrides.push(patch.name);
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
      byName.set(key, merged);
    }

    return { items: [...byName.values()], duplicateNames, unknownOverrides, rawCount: rows.length };
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

    let badge = `${item.grade} • ${item.disposition} • ${item.score}/100`;
    let label = 'Queued for Premium Rebuild';
    let cardClass = 'lead-card';

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
    }

    let targetUrl = '';
    if (!isLead && !isLater && item.href) {
      targetUrl = /^(https?:|\/)/.test(item.href) ? item.href : baseDir + item.href;
    }

    const action = targetUrl
      ? `<a href="${targetUrl}" class="visit-btn">${label} →</a>`
      : `<span class="visit-btn disabled" aria-disabled="true">${label}</span>`;

    const dataHref = targetUrl ? ` data-href="${targetUrl}"` : '';
    const cuisine = item.cuisine || `${item.grade} • ${item.disposition} • ${item.score}/100`;
    const description = item.description || `Final Rada-depth audit Batch ${item.auditBatch}. Re-verify current facts before implementation.`;

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
    const gradeA = items.filter(item => item.grade === 'A').length;
    const gradeB = items.filter(item => item.grade === 'B').length;
    stats.textContent = `${items.length} canonical A/B prospects • ${gradeA} A-grade • ${gradeB} B-grade • ${counts.lead || 0} queued • ${counts.incomplete || 0} incomplete • ${counts.qa || 0} QA pending • ${(counts.premium || 0) + (counts.promoted || 0) + (counts.promoted_secondary || 0)} premium/promoted • ${counts.later || 0} recheck/later`;

    const problems = [];
    if (result.rawCount !== 407) problems.push(`Expected 407 audited queue rows; loaded ${result.rawCount}.`);
    if (result.duplicateNames.length) problems.push(`Duplicate canonical queue names: ${result.duplicateNames.join(', ')}.`);
    if (result.unknownOverrides.length) problems.push(`Ignored overrides outside the audited queue: ${result.unknownOverrides.join(', ')}.`);
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
