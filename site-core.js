(function() {
  'use strict';

  // Mobile nav toggle
  const toggle = document.querySelector('.nav-toggle');
  const links = document.querySelector('.nav-links');
  if (toggle && links) {
    toggle.addEventListener('click', function() {
      const expanded = this.getAttribute('aria-expanded') === 'true' ? false : true;
      this.setAttribute('aria-expanded', expanded);
      links.classList.toggle('open');
      this.innerHTML = expanded ? '&#10005;' : '&#9776;';
    });
  }

  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(function(a) {
    a.addEventListener('click', function(e) {
      var id = this.getAttribute('href');
      if (id === '#') return;
      var target = document.querySelector(id);
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  // Demo forms — non-submitting, shows feedback
  document.querySelectorAll('.demo-form').forEach(function(form) {
    form.addEventListener('submit', function(e) {
      e.preventDefault();
      var feedback = form.querySelector('.form-feedback');
      var submitBtn = form.querySelector('[type="submit"]');
      if (submitBtn) submitBtn.disabled = true;
      if (feedback) {
        feedback.className = 'form-feedback success';
        var msg = form.getAttribute('data-demo-form') || 'Thanks! This is a demo — your message would be sent in production.';
        feedback.textContent = msg;
      }
      setTimeout(function() {
        if (submitBtn) submitBtn.disabled = false;
        form.reset();
      }, 3000);
    });
  });

  // Current page nav highlight
  var currentPath = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links a').forEach(function(a) {
    var href = a.getAttribute('href');
    if (href === currentPath) {
      a.setAttribute('aria-current', 'page');
    }
  });

})();
