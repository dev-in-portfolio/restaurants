/* --------------------------------------------------
   1900 MEXICAN GRILL & CANTINA — INTERACTIVE ENGINE
   -------------------------------------------------- */

document.addEventListener('DOMContentLoaded', () => {
  initMobileMenu();
  initModals();
  initMenuSearchAndFilter();
  initMezcalFlightBuilder();
  initCateringCalculator();
  initLocationSwitcher();
});

/* 1. Mobile Menu Toggle */
function initMobileMenu() {
  const toggleBtn = document.querySelector('.mobile-toggle');
  const navLinks = document.querySelector('.nav-links');

  if (toggleBtn && navLinks) {
    toggleBtn.addEventListener('click', () => {
      const isOpen = navLinks.classList.contains('is-open');
      navLinks.classList.toggle('is-open');
      toggleBtn.setAttribute('aria-expanded', !isOpen);
      toggleBtn.innerHTML = !isOpen ? '✕' : '☰';
    });
  }
}

/* 2. Modal Helper & Safe Demo Submissions */
function initModals() {
  const modalOverlay = document.getElementById('demo-modal');
  const closeBtns = document.querySelectorAll('.modal-close, .modal-dismiss');

  if (modalOverlay) {
    closeBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        closeModal(modalOverlay);
      });
    });

    modalOverlay.addEventListener('click', (e) => {
      if (e.target === modalOverlay) closeModal(modalOverlay);
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && modalOverlay.classList.contains('is-active')) {
        closeModal(modalOverlay);
      }
    });
  }
}

function openDemoModal(title, text) {
  const modalOverlay = document.getElementById('demo-modal');
  if (modalOverlay) {
    const titleEl = modalOverlay.querySelector('.modal-title');
    const bodyEl = modalOverlay.querySelector('.modal-body-text');
    if (titleEl) titleEl.textContent = title;
    if (bodyEl) bodyEl.textContent = text;
    modalOverlay.classList.add('is-active');
    modalOverlay.querySelector('.modal-dismiss')?.focus();
  }
}

function closeModal(modalOverlay) {
  modalOverlay.classList.remove('is-active');
}

/* 3. Menu Search and Category Filter (menu.html) */
function initMenuSearchAndFilter() {
  const searchInput = document.getElementById('menu-search');
  const catTabs = document.querySelectorAll('.cat-tab');
  const menuRows = document.querySelectorAll('.menu-item-row');

  if (!menuRows.length) return;

  let activeCategory = 'all';

  function filterMenu() {
    const query = searchInput ? searchInput.value.toLowerCase().trim() : '';

    menuRows.forEach(row => {
      const category = row.dataset.category || 'all';
      const text = row.textContent.toLowerCase();

      const matchesCat = (activeCategory === 'all' || category === activeCategory);
      const matchesQuery = (!query || text.includes(query));

      if (matchesCat && matchesQuery) {
        row.style.display = 'flex';
      } else {
        row.style.display = 'none';
      }
    });
  }

  if (searchInput) {
    searchInput.addEventListener('input', filterMenu);
  }

  catTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      catTabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      activeCategory = tab.dataset.category || 'all';
      filterMenu();
    });
  });
}

/* 4. Mezcal Flight & Salt Builder (cantina.html) */
function initMezcalFlightBuilder() {
  const glassElements = document.querySelectorAll('.flight-glass-item');
  const agaveChips = document.querySelectorAll('.agave-chip');
  const saltChips = document.querySelectorAll('.salt-chip');

  const displayTitle = document.getElementById('flight-title-display');
  const displayPrice = document.getElementById('flight-price-display');
  const displayDesc = document.getElementById('flight-desc-display');

  if (!glassElements.length) return;

  let activeIndex = 0;

  // Selected state
  const flightPours = [
    { name: 'Espadín (Oaxaca)', price: 10.00, abv: '45%', notes: 'Wood smoke, roasted agave & citrus zest' },
    { name: 'Tobalá (Highland Wild)', price: 14.00, abv: '47%', notes: 'Floral, sweet oak & delicate smoke finish' },
    { name: 'Tepeztate (25-Yr Wild)', price: 15.00, abv: '48%', notes: 'Herbal, peppery, mineral & complex' }
  ];

  let selectedSalt = { name: 'Sal de Gusano (Artisanal Worm Salt)', price: 2.00 };

  function renderFlight() {
    // Update glass buttons
    glassElements.forEach((glass, idx) => {
      const nameEl = glass.querySelector('.glass-name');
      if (nameEl) nameEl.textContent = flightPours[idx].name.split(' ')[0];
      if (idx === activeIndex) {
        glass.classList.add('active');
      } else {
        glass.classList.remove('active');
      }
    });

    // Update Agave chip highlights
    const currentAgave = flightPours[activeIndex].name;
    agaveChips.forEach(chip => {
      if (chip.dataset.name && currentAgave.startsWith(chip.dataset.name.split(' ')[0])) {
        chip.classList.add('active');
      } else {
        chip.classList.remove('active');
      }
    });

    // Calculate Totals
    const total = flightPours.reduce((sum, p) => sum + p.price, 0) + selectedSalt.price;
    if (displayPrice) displayPrice.textContent = `$${total.toFixed(2)}`;

    if (displayTitle) {
      displayTitle.textContent = `${flightPours[0].name.split(' ')[0]} • ${flightPours[1].name.split(' ')[0]} • ${flightPours[2].name.split(' ')[0]}`;
    }

    if (displayDesc) {
      displayDesc.textContent = `Custom 3-pour tasting flight: ${flightPours[0].name}, ${flightPours[1].name}, and ${flightPours[2].name}. Served on an agave wood platter with fresh orange wedges and ${selectedSalt.name}.`;
    }
  }

  // Click on glass to pick which pour to edit
  glassElements.forEach((glass, idx) => {
    glass.addEventListener('click', () => {
      activeIndex = idx;
      const label = document.getElementById('current-glass-label');
      if (label) label.textContent = `Selecting Pour #${idx + 1}`;
      renderFlight();
    });
  });

  // Click agave chip
  agaveChips.forEach(chip => {
    chip.addEventListener('click', () => {
      const name = chip.dataset.name;
      const price = parseFloat(chip.dataset.price);
      const notes = chip.dataset.notes;
      const abv = chip.dataset.abv;

      flightPours[activeIndex] = { name, price, notes, abv };
      renderFlight();
    });
  });

  // Click salt chip
  saltChips.forEach(chip => {
    chip.addEventListener('click', () => {
      saltChips.forEach(s => s.classList.remove('active'));
      chip.classList.add('active');
      selectedSalt = {
        name: chip.dataset.name,
        price: parseFloat(chip.dataset.price)
      };
      renderFlight();
    });
  });

  renderFlight();
}

/* 5. Catering & Taco Bar Party Estimator (catering.html) */
function initCateringCalculator() {
  const guestsInput = document.getElementById('guest-count');
  const eventTypeSelect = document.getElementById('event-type');
  const proteinCheckboxes = document.querySelectorAll('.protein-check');

  const outTacos = document.getElementById('calc-tacos');
  const outSides = document.getElementById('calc-sides');
  const outChips = document.getElementById('calc-chips');
  const outPrice = document.getElementById('calc-total');
  const calcForm = document.getElementById('catering-calc-form');

  if (!guestsInput || !calcForm) return;

  function calculateEstimate() {
    const guests = parseInt(guestsInput.value, 10) || 15;
    
    // Tacos per person: default 3 tacos per guest
    const totalTacos = guests * 3;
    
    // Sides (pints/quart trays): 1 tray per 10 guests
    const sideTrays = Math.ceil(guests / 10);

    // Chips & salsa: 1 gallon chip bag & salsa pint per 8 guests
    const chipPacks = Math.ceil(guests / 8);

    // Price per person: base $17.50 / person for taco bar
    const costPerPerson = 17.50;
    const totalCost = guests * costPerPerson;

    if (outTacos) outTacos.textContent = `${totalTacos} Tacos (${Math.ceil(totalTacos/10)} Platter Trays)`;
    if (outSides) outSides.textContent = `${sideTrays} Rice & ${sideTrays} Beans Trays`;
    if (outChips) outChips.textContent = `${chipPacks} Gallons Fresh Chips & Salsas`;
    if (outPrice) outPrice.textContent = `$${totalCost.toFixed(2)}`;
  }

  guestsInput.addEventListener('input', calculateEstimate);
  if (eventTypeSelect) eventTypeSelect.addEventListener('change', calculateEstimate);
  proteinCheckboxes.forEach(chk => chk.addEventListener('change', calculateEstimate));

  calcForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const guests = guestsInput.value;
    openDemoModal(
      'Demo Catering Quote Request',
      `Thank you! This non-submitting demo calculated a Fiesta Catering estimate for ${guests} guests. To arrange official catering with 1900 Mexican Grill, please contact Midtown at (704) 334-4677 or South Park at (704) 523-1554.`
    );
  });

  calculateEstimate();
}

/* 6. Multi-Location Switcher (visit.html & index.html) */
function initLocationSwitcher() {
  const switchBtns = document.querySelectorAll('.switch-btn');
  const locationCards = document.querySelectorAll('.location-card-hub');

  if (!switchBtns.length) return;

  switchBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      switchBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const targetLoc = btn.dataset.location;

      locationCards.forEach(card => {
        if (targetLoc === 'all' || card.dataset.location === targetLoc) {
          card.style.display = 'block';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
}
