(() => {
  'use strict';

  const SOURCE_PATH = 'portal-concepts-source.html';
  const grid = document.getElementById('restaurant-grid');
  const alphaNav = document.getElementById('alpha-nav');
  const stats = document.getElementById('portal-stats');
  const errorBox = document.getElementById('portal-error');

  const normalizeName = (name = '') => name
    .normalize('NFKD')
    .replace(/[\u0300-\u036f]/g, '')
    .toLowerCase()
    .replace(/&/g, 'and')
    .replace(/[^a-z0-9]+/g, '')
    .replace(/^(the|an|a)/, '')
    .replace(/(restaurant|cafe|company|co)$/, '');

  const sortName = (name = '') => name
    .replace(/^(the|a|an)\s+/i, '')
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '');

  const cleanText = (value = '') => String(value)
    .replace(/([A-Za-z])�s\b/g, '$1’s')
    .replace(/\s�\s/g, ' • ')
    .replace(/�/g, '')
    .replace(/\s{2,}/g, ' ')
    .trim();

  const cleanEmoji = (value) => {
    const text = String(value || '');
    return /\?|�|ðŸ|â/.test(text) || !text.trim() ? '🍽️' : text;
  };

  function parseLegacyConcepts(sourceText) {
    const startMarker = 'const concepts = [';
    const start = sourceText.indexOf(startMarker);
    if (start < 0) return { items: [], errors: 1 };
    const end = sourceText.indexOf('\n    ];', start);
    if (end < 0) return { items: [], errors: 1 };

    const block = sourceText.slice(start + startMarker.length, end);
    const items = [];
    let errors = 0;

    for (const rawLine of block.split(/\r?\n/)) {
      let line = rawLine.trim();
      if (!line.startsWith('{name:')) continue;
      line = line.replace(/,$/, '');
      try {
        const item = Function(`"use strict"; return (${line});`)();
        if (item && item.name) items.push(item);
      } catch {
        errors += 1;
      }
    }

    return { items, errors };
  }

  function normalizeItem(item, sourceType) {
    const isLead = item.status === 'lead' || sourceType === 'lead';
    const allowedOverride = sourceType === 'override' && ['lead', 'incomplete', 'qa', 'premium', 'promoted'].includes(item.status);
    const status = allowedOverride ? item.status : (isLead ? 'lead' : 'incomplete');

    return {
      name: cleanText(item.name || 'Unnamed restaurant'),
      area: cleanText(item.area || 'Charlotte area'),
      cuisine: cleanText(item.cuisine || (status === 'lead' ? 'Website Lead • Not Built Yet' : 'Existing Website Build')),
      description: cleanText(item.description || ''),
      emoji: cleanEmoji(item.emoji),
      href: item.href || '',
      gradient: item.gradient || 'linear-gradient(135deg,#172033,#334155 52%,#0f172a)',
      status
    };
  }

  function mergeItems(groups) {
    const priority = { lead: 0, incomplete: 1, qa: 2, premium: 3, promoted: 4 };
    const byName = new Map();

    for (const group of groups) {
      for (const item of group.items) {
        const normalized = normalizeItem(item, group.type);
        const key = normalizeName(normalized.name);
        if (!key) continue;
        const current = byName.get(key);
        if (!current || priority[normalized.status] >= priority[current.status]) {
          byName.set(key, normalized);
        }
      }
    }

    return [...byName.values()];
  }

  function render(items, parseErrors) {
    const sorted = [...items].sort((a, b) => sortName(a.name).localeCompare(sortName(b.name), undefined, { sensitivity: 'base' }));
    const letterFor = item => (sortName(item.name).charAt(0).toUpperCase() || '#');
    
    // Separate promoted items from regular items
    const promotedItems = sorted.filter(item => item.status === 'promoted');
    const regularItems = sorted.filter(item => item.status !== 'promoted');
    
    // Get letters for regular items only
    const letters = [...new Set(regularItems.map(letterFor))];

    alphaNav.innerHTML = letters.map(letter => `<a href="#letter-${letter}">${letter}</a>`).join('');

    let lastLetter = '';
    let regularHtml = '';
    let promotedHtml = '';

    // Render regular items (alphabetical with letter headings)
    regularHtml = regularItems.map(item => {
      const lead = item.status === 'lead';
      const qa = item.status === 'qa';
      const premium = item.status === 'premium';
      const incomplete = !lead && !qa && !premium;

      const badge = premium
        ? 'PREMIUM • 6-PAGE IDENTITY REBUILD'
        : qa
          ? '6/6 PAGES • QA PENDING'
          : lead
            ? 'LEAD • NOT BUILT YET'
            : 'INCOMPLETE • 6-PAGE STANDARD NOT MET';

      const label = premium
        ? 'View Premium Build'
        : qa
          ? 'View Six-Page Build'
          : lead
            ? 'Queued for Rebuild'
            : 'View Existing Build';

      const cardClass = premium ? 'premium-card' : qa ? 'qa-card' : lead ? 'lead-card' : 'incomplete-card';
      const action = lead || !item.href
        ? `<span class="visit-btn disabled" aria-disabled="true">${label}</span>`
        : `<a href="${item.href}" class="visit-btn">${label} →</a>`;

      const letter = letterFor(item);
      const heading = letter !== lastLetter ? `<h2 class="letter-heading" id="letter-${letter}">${letter}</h2>` : '';
      lastLetter = letter;

      return `${heading}<article class="portal-card glass-panel ${cardClass}"><div class="card-image-wrapper"><span class="card-rating-badge">${badge}</span><div class="card-img-placeholder" style="background:${item.gradient}">${item.emoji}</div></div><div class="card-content"><span class="card-cuisine">${item.cuisine}</span><h2 class="card-title">${item.name}</h2><p class="card-description">${item.description}</p><div class="card-footer"><span class="card-price">Area: <span>${item.area}</span></span>${action}</div></div></article>`;
    }).join('');

    // Render promoted items (alphabetical in their own section)
    if (promotedItems.length > 0) {
      const promotedSorted = [...promotedItems].sort((a, b) => sortName(a.name).localeCompare(sortName(b.name), undefined, { sensitivity: 'base' }));
      
      promotedHtml = '<h2 class="letter-heading" id="letter-PROMOTED">Promoted</h2>' + 
        promotedSorted.map(item => {
          const badge = 'PROMOTED';
          const label = 'View Promoted Build';
          const cardClass = 'premium-card';
          const action = item.href
            ? `<a href="${item.href}" class="visit-btn">${label} →</a>`
            : `<span class="visit-btn disabled" aria-disabled="true">${label}</span>`;

          return `<article class="portal-card glass-panel ${cardClass}"><div class="card-image-wrapper"><span class="card-rating-badge">${badge}</span><div class="card-img-placeholder" style="background:${item.gradient}">${item.emoji}</div></div><div class="card-content"><span class="card-cuisine">${item.cuisine}</span><h2 class="card-title">${item.name}</h2><p class="card-description">${item.description}</p><div class="card-footer"><span class="card-price">Area: <span>${item.area}</span></span>${action}</div></div></article>`;
        }).join('');
    }

    // Combine regular and promoted HTML
    grid.innerHTML = regularHtml + promotedHtml;

    const counts = sorted.reduce((acc, item) => {
      acc[item.status] = (acc[item.status] || 0) + 1;
      return acc;
    }, {});

    stats.textContent = `${sorted.length} restaurants • ${counts.lead || 0} queued leads • ${counts.incomplete || 0} existing builds awaiting the six-page standard • ${counts.qa || 0} six-page builds awaiting QA • ${counts.premium || 0} premium • ${counts.promoted || 0} promoted`;

    if (parseErrors > 0) {
      errorBox.hidden = false;
      errorBox.textContent = `${parseErrors} legacy portal entr${parseErrors === 1 ? 'y was' : 'ies were'} malformed and skipped. The rest of the portal loaded safely.`;
    }
  }

  async function start() {
    let legacy = { items: [], errors: 0 };
    try {
      const response = await fetch(`${SOURCE_PATH}?v=${Date.now()}`, { cache: 'no-store' });
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      legacy = parseLegacyConcepts(await response.text());
    } catch (error) {
      errorBox.hidden = false;
      errorBox.textContent = `The archived portal source could not be loaded (${error.message}). Lead data is still available.`;
    }

    const message2 = Array.from(window.restaurantLeadsMessage2 || []);
    const message3 = Array.from(window.restaurantLeadsMessage3 || []);
    const overrides = Array.from(window.portalOverrides || []);

    const items = mergeItems([
      { type: 'legacy', items: legacy.items },
      { type: 'lead', items: message2 },
      { type: 'lead', items: message3 },
      { type: 'override', items: overrides }
    ]);

    render(items, legacy.errors);
  }

  start();
})();
