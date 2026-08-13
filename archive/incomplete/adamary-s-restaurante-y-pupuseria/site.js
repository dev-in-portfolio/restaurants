/* ==========================================================================
   Adamary's Restaurante y Pupuseria - Client Script
   Features: Mobile Navigation Toggle, Menu Section Switching, Demo Toast
   ========================================================================== */

document.addEventListener('DOMContentLoaded', function () {
  // Mobile Navigation Toggle
  const toggleBtn = document.querySelector('.mobile-nav-toggle');
  const navMenu = document.querySelector('.nav-menu');

  if (toggleBtn && navMenu) {
    toggleBtn.addEventListener('click', function () {
      const expanded = toggleBtn.getAttribute('aria-expanded') === 'true' || false;
      toggleBtn.setAttribute('aria-expanded', !expanded);
      navMenu.classList.toggle('is-open');
    });

    // Close menu when pressing Escape
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && navMenu.classList.contains('is-open')) {
        toggleBtn.setAttribute('aria-expanded', 'false');
        navMenu.classList.remove('is-open');
        toggleBtn.focus();
      }
    });
  }

  // Demo Forms (Non-submitting concept safe handler)
  const demoForms = document.querySelectorAll('.demo-form');
  demoForms.forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      
      const statusDiv = form.querySelector('.demo-form-status') || document.createElement('div');
      statusDiv.className = 'demo-form-status';
      statusDiv.style.marginTop = '1rem';
      statusDiv.style.padding = '0.85rem 1.25rem';
      statusDiv.style.backgroundColor = '#E5A93C';
      statusDiv.style.color = '#1A1715';
      statusDiv.style.fontWeight = '600';
      statusDiv.style.borderRadius = '6px';
      statusDiv.innerHTML = '<strong>Demo Concept Note:</strong> Thank you for testing this sales concept! In production, this form connects to Adamary’s direct catering line at (704) 666-8986.';
      
      if (!form.querySelector('.demo-form-status')) {
        form.appendChild(statusDiv);
      }
      form.reset();
    });
  });

  // Simple Accordion or Tab switching if present
  const categoryTabs = document.querySelectorAll('[data-menu-tab]');
  const categorySections = document.querySelectorAll('[data-menu-section]');

  if (categoryTabs.length > 0 && categorySections.length > 0) {
    categoryTabs.forEach(function (tab) {
      tab.addEventListener('click', function () {
        const targetSection = tab.getAttribute('data-menu-tab');
        
        categoryTabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');

        categorySections.forEach(section => {
          if (targetSection === 'all' || section.getAttribute('data-menu-section') === targetSection) {
            section.style.display = 'block';
          } else {
            section.style.display = 'none';
          }
        });
      });
    });
  }
});
