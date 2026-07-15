(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', function () {
    initSkipLink();
    initMobileNav();
    initDemoForms();
    initOrderBuilder();
    initCateringCalculator();
    initSmoothScroll();
    initActiveNav();
    showToast('Welcome to House of Leng — demo presentation');
  });

  function initSkipLink() {
    var link = document.querySelector('.skip-link');
    if (!link) return;
    link.addEventListener('click', function (e) {
      var target = document.querySelector('#main-content');
      if (target) {
        e.preventDefault();
        target.setAttribute('tabindex', '-1');
        target.focus({ preventScroll: true });
        window.scrollTo({ top: target.offsetTop - 10 });
      }
    });
  }

  function initMobileNav() {
    var toggle = document.querySelector('.nav-toggle');
    var navList = document.querySelector('.nav-list');
    if (!toggle || !navList) return;

    toggle.addEventListener('click', function () {
      navList.classList.toggle('open');
      var expanded = navList.classList.contains('open');
      toggle.setAttribute('aria-expanded', expanded);
      toggle.innerHTML = expanded ? '✕' : '☰';
    });

    document.addEventListener('click', function (e) {
      if (!e.target.closest('.main-nav')) {
        navList.classList.remove('open');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.innerHTML = '☰';
      }
    });
  }

  function initDemoForms() {
    var forms = document.querySelectorAll('.demo-form');
    forms.forEach(function (form) {
      form.addEventListener('submit', function (e) {
        e.preventDefault();
        var data = {};
        var inputs = form.querySelectorAll('input, select, textarea');
        inputs.forEach(function (input) {
          if (input.name) {
            data[input.name] = input.value;
          }
        });
        console.log('[Demo Form]', form.id || 'unnamed form', data);
        var formName = form.getAttribute('data-demo-form') || form.id || 'form';
        showToast(formName + ' — demo submission recorded (not actually sent)');
      });
    });
  }

  function initOrderBuilder() {
    var builder = document.querySelector('[data-demo="order-builder"]');
    if (!builder) return;

    var state = {
      size: null,
      protein: null,
      style: null,
      starch: null,
      appetizer: null,
      qty: 1
    };

    var pricing = {
      size: { Small: 8.99, Regular: 11.99, Large: 14.99 },
      protein: { Chicken: 0, Beef: 1.5, Shrimp: 3, Tofu: 0, Pork: 1, Vegetable: 0 },
      style: { 'General Tso\'s': 0, Sesame: 0, Mongolian: 0.5, Hunan: 0.5, 'Kung Pao': 0.5, 'Sweet & Sour': 0 },
      starch: { 'Fried Rice': 0, 'Lo Mein': 0, 'Steamed Rice': 0, 'Chow Mein': 0.5 },
      appetizer: { 'Egg Roll': 0, 'Crab Rangoon (2)': 1, 'Spring Roll': 0, 'Soup of the Day': 1.5, None: 0 }
    };

    var optionButtons = builder.querySelectorAll('.builder-option');
    var totalEl = builder.querySelector('.builder-total-price');
    var qtyEl = builder.querySelector('.builder-qty-value');
    var qtyMinus = builder.querySelector('.builder-qty-minus');
    var qtyPlus = builder.querySelector('.builder-qty-plus');
    var addBtn = builder.querySelector('.builder-add-btn');

    optionButtons.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var group = btn.getAttribute('data-group');
        var value = btn.getAttribute('data-value');
        if (!group || !value) return;

        var siblings = builder.querySelectorAll('[data-group="' + group + '"]');
        siblings.forEach(function (s) { s.classList.remove('selected'); });
        btn.classList.add('selected');
        state[group] = value;
        updateTotal();
      });
    });

    if (qtyMinus) {
      qtyMinus.addEventListener('click', function () {
        if (state.qty > 1) { state.qty--; updateQty(); }
      });
    }
    if (qtyPlus) {
      qtyPlus.addEventListener('click', function () {
        if (state.qty < 99) { state.qty++; updateQty(); }
      });
    }

    function calcTotal() {
      var base = 0;
      if (state.size && pricing.size[state.size]) base += pricing.size[state.size];
      if (state.protein && pricing.protein[state.protein]) base += pricing.protein[state.protein];
      if (state.style && pricing.style[state.style]) base += pricing.style[state.style];
      if (state.starch && pricing.starch[state.starch]) base += pricing.starch[state.starch];
      if (state.appetizer && pricing.appetizer[state.appetizer]) base += pricing.appetizer[state.appetizer];
      return base;
    }

    function updateTotal() {
      var total = calcTotal();
      if (totalEl) totalEl.textContent = '$' + (total * state.qty).toFixed(2);
    }

    function updateQty() {
      if (qtyEl) qtyEl.textContent = state.qty;
      updateTotal();
    }

    if (addBtn) {
      addBtn.addEventListener('click', function () {
        var missing = [];
        if (!state.size) missing.push('size');
        if (!state.protein) missing.push('protein');
        if (!state.style) missing.push('style');
        if (!state.starch) missing.push('starch');
        if (!state.appetizer) missing.push('appetizer');

        if (missing.length > 0) {
          showToast('Please select: ' + missing.join(', '));
          return;
        }

        var total = calcTotal() * state.qty;
        showToast('Added to order: ' + state.qty + 'x ' + state.size + ' Combo ($' + total.toFixed(2) + ') — demo only');
      });
    }
  }

  function initCateringCalculator() {
    var calc = document.querySelector('[data-demo="catering-calculator"]');
    if (!calc) return;

    var guestsInput = calc.querySelector('[data-calc="guests"]');
    var guestsDisplay = calc.querySelector('[data-calc="guests-display"]');
    var proteinSelect = calc.querySelector('[data-calc="protein"]');
    var entreesSelect = calc.querySelector('[data-calc="entrees"]');
    var includeAppetizer = calc.querySelector('[data-calc="appetizer"]');
    var includeRice = calc.querySelector('[data-calc="rice"]');
    var includeDessert = calc.querySelector('[data-calc="dessert"]');
    var resultsEl = calc.querySelector('[data-calc="results"]');

    if (!guestsInput || !resultsEl) return;

    var proteinPrices = { Chicken: 9.99, Beef: 12.99, Shrimp: 14.99, Vegetable: 8.99, 'Combo Platter': 11.99 };
    var entreePrices = { '1 Entree': 0, '2 Entrees': 2, '3 Entrees': 4 };
    var perPersonBase = 7.99;

    function updateCalculator() {
      var guests = parseInt(guestsInput.value) || 20;
      if (guestsDisplay) guestsDisplay.textContent = guests;
      var protein = proteinSelect ? proteinSelect.value : 'Chicken';
      var entrees = entreesSelect ? entreesSelect.value : '1 Entree';
      var hasAppetizer = includeAppetizer ? includeAppetizer.checked : false;
      var hasRice = includeRice ? includeRice.checked : false;
      var hasDessert = includeDessert ? includeDessert.checked : false;

      var ppBase = perPersonBase + (proteinPrices[protein] || 9.99) + (entreePrices[entrees] || 0);
      if (hasAppetizer) ppBase += 2.5;
      if (hasRice) ppBase += 1;
      if (hasDessert) ppBase += 1.5;

      var total = ppBase * guests;
      var minTotal = total * 0.9;
      var maxTotal = total * 1.1;
      var portionEstimate = Math.ceil(guests * 1.25);

      resultsEl.innerHTML = ''
        + '<div class="calculator-result-row">'
        + '<span>Guests</span>'
        + '<strong>' + guests + '</strong>'
        + '</div>'
        + '<div class="calculator-result-row">'
        + '<span>Protein</span>'
        + '<strong>' + protein + '</strong>'
        + '</div>'
        + '<div class="calculator-result-row">'
        + '<span>Entree selection</span>'
        + '<strong>' + entrees + '</strong>'
        + '</div>'
        + '<div class="calculator-result-row">'
        + '<span>Estimated portions needed</span>'
        + '<strong>' + portionEstimate + '</strong>'
        + '</div>'
        + '<div class="calculator-result-row">'
        + '<span>Includes appetizer</span>'
        + '<strong>' + (hasAppetizer ? 'Yes' : 'No') + '</strong>'
        + '</div>'
        + '<div class="calculator-result-row">'
        + '<span>Includes fried rice</span>'
        + '<strong>' + (hasRice ? 'Yes' : 'No') + '</strong>'
        + '</div>'
        + '<div class="calculator-result-row">'
        + '<span>Includes dessert</span>'
        + '<strong>' + (hasDessert ? 'Yes' : 'No') + '</strong>'
        + '</div>'
        + '<div class="calculator-result-row total">'
        + '<span>Estimated total</span>'
        + '<strong>$' + minTotal.toFixed(0) + ' – $' + maxTotal.toFixed(0) + '</strong>'
        + '</div>';
    }

    guestsInput.addEventListener('input', updateCalculator);
    if (proteinSelect) proteinSelect.addEventListener('change', updateCalculator);
    if (entreesSelect) entreesSelect.addEventListener('change', updateCalculator);
    if (includeAppetizer) includeAppetizer.addEventListener('change', updateCalculator);
    if (includeRice) includeRice.addEventListener('change', updateCalculator);
    if (includeDessert) includeDessert.addEventListener('change', updateCalculator);

    updateCalculator();
  }

  function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
      anchor.addEventListener('click', function (e) {
        var target = document.querySelector(this.getAttribute('href'));
        if (target) {
          e.preventDefault();
          target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      });
    });
  }

  function initActiveNav() {
    var current = location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('.nav-list a').forEach(function (link) {
      link.classList.remove('active');
      if (link.getAttribute('href') === current) {
        link.classList.add('active');
      }
    });
  }

  function showToast(message) {
    var toast = document.createElement('div');
    toast.className = 'toast';
    toast.textContent = message;
    document.body.appendChild(toast);
    requestAnimationFrame(function () {
      toast.classList.add('show');
    });
    setTimeout(function () {
      toast.classList.remove('show');
      setTimeout(function () { toast.remove(); }, 300);
    }, 3500);
  }

  window.showToast = showToast;
})();
