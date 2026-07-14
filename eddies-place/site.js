(() => {
  const toggle = document.querySelector('[data-nav-toggle]');
  const nav = document.querySelector('[data-nav]');
  if (toggle && nav) {
    toggle.addEventListener('click', () => {
      const open = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', String(open));
    });
    nav.addEventListener('click', e => {
      if (e.target.closest('a')) {
        nav.classList.remove('is-open');
        toggle.setAttribute('aria-expanded','false');
      }
    });
  }

  const chips = [...document.querySelectorAll('[data-filter]')];
  const groups = [...document.querySelectorAll('[data-group]')];
  chips.forEach(chip => chip.addEventListener('click', () => {
    const filter = chip.dataset.filter;
    chips.forEach(c => c.setAttribute('aria-pressed', String(c === chip)));
    groups.forEach(group => {
      group.hidden = filter !== 'all' && group.dataset.group !== filter;
    });
  }));

  const builder = document.querySelector('[data-breakfast-builder]');
  if (builder) {
    const mood = builder.querySelector('[data-mood]');
    const appetite = builder.querySelector('[data-appetite]');
    const resultTitle = builder.querySelector('[data-result-title]');
    const resultCopy = builder.querySelector('[data-result-copy]');
    const picks = {
      'classic-light': ['Eggs Your Way', 'Straightforward, familiar and easy to pair with the side and bread that sound right today.'],
      'classic-hearty': ['Country Fried Breakfast', 'A biscuit, country-fried chicken, sausage gravy and eggs make this the full neighborhood-diner move.'],
      'sweet-light': ['French Toast', 'Powdered-sugar comfort with your choice of bread, meat and side.'],
      'sweet-hearty': ['Chicken & Waffle', 'Pecan-fried chicken, a fresh waffle and honey-cinnamon butter bring sweet and savory together.'],
      'creole-light': ['Breakfast Burrito', 'Seasoned chicken or beef, eggs, peppers and pepper jack with red beans and rice on the side.'],
      'creole-hearty': ['Shrimp & Grits', 'Garlic-herb shrimp, tasso ham and parmesan grits for a signature Eddie’s plate any time of day.']
    };
    const update = () => {
      const [title, copy] = picks[`${mood.value}-${appetite.value}`];
      resultTitle.textContent = title;
      resultCopy.textContent = copy;
    };
    [mood, appetite].forEach(el => el.addEventListener('change', update));
    update();
  }
})();
