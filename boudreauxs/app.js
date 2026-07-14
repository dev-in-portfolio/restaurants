(() => {
  const toggle = document.querySelector('[data-nav-toggle]');
  const nav = document.querySelector('[data-nav-links]');

  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const open = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', String(open));
    });

    nav.addEventListener('click', event => {
      if (event.target.closest('a')) {
        nav.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
      }
    });
  }

  const revealItems = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    const observer = new IntersectionObserver(entries => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12 });
    revealItems.forEach(item => observer.observe(item));
  } else {
    revealItems.forEach(item => item.classList.add('is-visible'));
  }

  const menuButtons = document.querySelectorAll('[data-menu-filter]');
  const menuGroups = document.querySelectorAll('[data-menu-group]');
  if (menuButtons.length && menuGroups.length) {
    menuButtons.forEach(button => {
      button.addEventListener('click', () => {
        const filter = button.dataset.menuFilter;
        menuButtons.forEach(item => item.setAttribute('aria-pressed', String(item === button)));
        menuGroups.forEach(group => {
          const visible = filter === 'all' || group.dataset.menuGroup === filter;
          group.hidden = !visible;
        });
      });
    });
  }

  const planner = document.querySelector('[data-planner]');
  if (planner) {
    const occasion = planner.querySelector('[data-occasion]');
    const party = planner.querySelector('[data-party]');
    const pace = planner.querySelector('[data-pace]');
    const title = document.querySelector('[data-plan-title]');
    const copy = document.querySelector('[data-plan-copy]');
    const list = document.querySelector('[data-plan-list]');

    const plans = {
      'Dinner with friends': {
        title: 'A relaxed table with room to share',
        copy: 'Start easy, leave space for the table to pass plates, and keep the night moving at a comfortable pace.',
        items: ['Plan on a mix of shareable starters and individual mains', 'Ask the restaurant about the best seating fit for your group', 'Confirm current menu availability before the visit']
      },
      'Birthday gathering': {
        title: 'A lively celebration without the scramble',
        copy: 'A little planning up front keeps the table focused on the birthday instead of logistics.',
        items: ['Share the final headcount before arrival', 'Ask about cake, dessert and decoration policies', 'Confirm whether one check or separate checks works best']
      },
      'Game-day meal': {
        title: 'Comfort food and an easy game-day rhythm',
        copy: 'Build the visit around arrival time, seating and a menu pace that works from kickoff through the final whistle.',
        items: ['Arrive early for the smoothest seating options', 'Ask about current television placement and sound', 'Confirm current drink and food specials directly']
      },
      'Neighborhood meetup': {
        title: 'A casual NoDa meetup',
        copy: 'Keep the plan flexible, choose a clear arrival window and let the group settle in without over-scheduling the night.',
        items: ['Choose one point person for the group', 'Set a fifteen-minute arrival window', 'Use the directions link before heading to 36th Street']
      }
    };

    const updatePlan = () => {
      const selected = plans[occasion.value] || plans['Dinner with friends'];
      const size = Math.max(1, Number(party.value) || 1);
      const speed = pace.value.toLowerCase();
      title.textContent = selected.title;
      copy.textContent = `${selected.copy} Your preview is set for ${size} ${size === 1 ? 'guest' : 'guests'} with a ${speed} pace.`;
      list.innerHTML = selected.items.map(item => `<li>${item}</li>`).join('');
    };

    [occasion, party, pace].forEach(input => input.addEventListener('input', updatePlan));
    updatePlan();
  }
})();
