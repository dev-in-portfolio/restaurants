/* ===== Ink N Ivy — Site Core JS ===== */
(function () {
  'use strict';

  // --- Nav toggle ---
  const toggle = document.querySelector('.nav-toggle');
  const navLinks = document.querySelector('.nav-links');
  if (toggle && navLinks) {
    toggle.addEventListener('click', function () {
      navLinks.classList.toggle('open');
      const expanded = navLinks.classList.contains('open');
      toggle.setAttribute('aria-expanded', expanded);
    });
  }

  // --- Active nav link ---
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links a').forEach(function (link) {
    const href = link.getAttribute('href');
    if (href === currentPath) {
      link.classList.add('active');
    }
  });

  // --- Demo forms (non-submitting) ---
  document.querySelectorAll('.demo-form').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var demoType = form.getAttribute('data-demo-form') || 'generic';
      var btn = form.querySelector('.btn');
      var originalText = btn ? btn.textContent : '';

      // Gather fields
      var fields = {};
      Array.from(form.elements).forEach(function (el) {
        if (el.name) fields[el.name] = el.value;
      });

      console.log('[Demo Form] ' + demoType, fields);

      if (btn) {
        btn.textContent = 'Thanks — demo submission logged \u2705';
        btn.disabled = true;
        btn.style.opacity = '0.7';
        setTimeout(function () {
          btn.textContent = originalText;
          btn.disabled = false;
          btn.style.opacity = '1';
          form.reset();
        }, 3000);
      }
    });
  });

  // --- Game Day Configurator ---
  var configEl = document.getElementById('gameday-config');
  if (configEl) {
    var select = configEl.querySelector('select');
    var results = configEl.querySelector('.config-results');

    var specials = {
      panthers: [
        { name: 'Game Day Burger', desc: 'Double patty, bacon, pimento cheese, fried onion straws', price: '$16', meta: 'Served all game day' },
        { name: 'Pulled Pork Nachos', desc: 'House-smoked pork, queso, jalape\u00f1os, crema', price: '$14', meta: 'Serves 2\u20133' },
        { name: 'Half-Price Wings', desc: 'Choose from 6 house sauces', price: 'From $7.50', meta: 'While supplies last' },
        { name: 'Pitcher Special', desc: 'Domestic beer pitcher', price: '$12', meta: 'All game long' },
      ],
      hornets: [
        { name: 'Hornets Free Appetizer', desc: 'Free app with drink purchase \u2014 show your ticket', price: 'Free', meta: 'Game days only' },
        { name: 'Teal Lemonade Cocktail', desc: 'Vodka, blue curacao, lemonade, splash of soda', price: '$10', meta: 'Signature game drink' },
        { name: '$3 Tacos', desc: 'Choice of chicken, carnitas, or black bean', price: '$3 each', meta: 'Tuesday & game days' },
        { name: 'Popcorn Shrimp Basket', desc: 'Flash-fried with house ranch', price: '$12', meta: 'Shareable' },
      ],
      football: [
        { name: 'Game Day Burger', desc: 'Double patty, bacon, pimento cheese, fried onion straws', price: '$16', meta: 'Served all game day' },
        { name: 'Buffalo Chicken Dip', desc: 'Served with housemade tortilla chips', price: '$11', meta: 'Fan favorite' },
        { name: 'Beer Bucket', desc: 'Bucket of 6 domestic bottles', price: '$20', meta: 'Best value' },
        { name: 'Loaded Tater Tots', desc: 'Bacon, cheese, sour cream, chives', price: '$10', meta: 'Shareable' },
      ],
      'default': [
        { name: 'Blackened Chicken Pasta', desc: 'Cajun-spiced chicken, creamy alfredo, bell peppers', price: '$18', meta: 'Signature dish' },
        { name: 'Sweet & Spicy Shrimp', desc: 'Flash-fried, tossed in sweet chili glaze', price: '$15', meta: 'Small plate' },
        { name: 'Mac N Cheese', desc: 'Five-cheese blend, topped with breadcrumbs', price: '$14', meta: 'Signature side' },
        { name: 'Craft Cocktail of the Day', desc: 'Ask your server', price: 'Market', meta: 'Rotating selection' },
      ],
    };

    function renderGames(data) {
      results.innerHTML = '';
      data.forEach(function (item) {
        var div = document.createElement('div');
        div.className = 'config-result-item';
        div.innerHTML =
          '<h4>' + item.name + '</h4>' +
          '<p>' + item.desc + '</p>' +
          '<div class="meta">' + item.price + ' \u2022 ' + item.meta + '</div>';
        results.appendChild(div);
      });
    }

    function updateConfig() {
      var sport = select.value;
      var data = specials[sport] || specials['default'];
      renderGames(data);
    }

    select.addEventListener('change', updateConfig);
    updateConfig();
  }
})();
