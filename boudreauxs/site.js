const toggle=document.querySelector('[data-nav-toggle]');
const nav=document.querySelector('[data-nav]');
if(toggle&&nav){
  toggle.addEventListener('click',()=>{
    const open=nav.classList.toggle('open');
    toggle.setAttribute('aria-expanded',String(open));
  });
}
const filterButtons=[...document.querySelectorAll('[data-menu-filter]')];
const menuGroups=[...document.querySelectorAll('[data-menu-group]')];
filterButtons.forEach(button=>button.addEventListener('click',()=>{
  filterButtons.forEach(b=>b.classList.remove('active'));
  button.classList.add('active');
  const filter=button.dataset.menuFilter;
  menuGroups.forEach(group=>{
    group.hidden=filter!=='all' && group.dataset.category!==filter;
  });
}));
const builder=document.querySelector('[data-builder]');
if(builder){
  const base=builder.querySelector('[data-base]');
  const style=builder.querySelector('[data-style]');
  const heat=builder.querySelector('[data-heat]');
  const title=builder.querySelector('[data-builder-title]');
  const copy=builder.querySelector('[data-builder-copy]');
  const update=()=>{
    title.textContent=`${style.value} over ${base.value}`;
    copy.textContent=`Suggested direction: ${heat.value.toLowerCase()} heat, served as a menu-navigation preview. Exact dishes, ingredients, allergens, prices and availability require owner confirmation.`;
  };
  [base,style,heat].forEach(el=>el.addEventListener('input',update));
  update();
}
const planner=document.querySelector('[data-planner]');
if(planner){
  const guests=planner.querySelector('[data-guests]');
  const occasion=planner.querySelector('[data-occasion]');
  const service=planner.querySelector('[data-service]');
  const count=planner.querySelector('[data-plan-count]');
  const title=planner.querySelector('[data-plan-title]');
  const note=planner.querySelector('[data-plan-note]');
  const update=()=>{
    const n=Math.max(2,Math.min(80,Number(guests.value)||2));
    count.textContent=`${n} guests`;
    title.textContent=`${occasion.value} • ${service.value}`;
    const fit=n<=12?'A standard-table or small-group conversation is the likely starting point.':n<=30?'A semi-private layout or reserved section is the likely starting point.':'A larger buyout-style conversation may be required.';
    note.textContent=`${fit} This is a planning preview only; capacity, packages, deposits and availability require restaurant confirmation.`;
  };
  [guests,occasion,service].forEach(el=>el.addEventListener('input',update));
  update();
}
document.querySelectorAll('[data-demo-form]').forEach(form=>{
  form.addEventListener('submit',event=>{
    event.preventDefault();
    const note=form.querySelector('[data-form-note]');
    if(note) note.textContent='Preview complete. No information was sent, stored or shared.';
  });
});
