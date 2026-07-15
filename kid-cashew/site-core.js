(function(){
  // Nav toggle
  const toggle=document.querySelector('.nav-toggle');
  const nav=document.querySelector('.nav');
  if(toggle&&nav){
    toggle.addEventListener('click',function(){
      nav.classList.toggle('open');
      toggle.setAttribute('aria-expanded',nav.classList.contains('open'));
    });
    document.addEventListener('click',function(e){
      if(!toggle.contains(e.target)&&!nav.contains(e.target)) nav.classList.remove('open');
    });
  }

  // Demo forms — non-submitting
  document.querySelectorAll('.demo-form').forEach(function(form){
    form.addEventListener('submit',function(e){
      e.preventDefault();
      var btn=form.querySelector('[type="submit"]');
      var orig=btn&&btn.value?btn.value:'Submit';
      if(btn) btn.value='✓ Sent (demo)';
      setTimeout(function(){
        form.querySelectorAll('input,textarea,select').forEach(function(el){el.value=''});
        if(btn) btn.value=orig;
      },1500);
    });
  });

  // Crave Matcher
  var matcher=document.getElementById('crave-matcher');
  if(matcher){
    var steps=matcher.querySelectorAll('.crave-step');
    var opts=matcher.querySelectorAll('.crave-opt');
    var result=matcher.getElementById('crave-result');
    var dishEl=matcher.getElementById('crave-dish');
    var descEl=matcher.getElementById('crave-desc');
    var resetBtn=matcher.getElementById('crave-reset');
    var selections={};

    var data={
      hungry:{dish:'Smash Burger',desc:'Juicy double smash, cheddar, caramelized onions, house sauce on brioche.'},
      healthy:{dish:'Super Grains Bowl',desc:'Farro, quinoa, kale, roasted sweet potato, tahini dressing, pickled onion.'},
      adventurous:{dish:'Grilled Octopus',desc:'Tender wood-fire grilled octopus, lemon-oregano, smoked paprika, olive oil.'},
      cozy:{dish:'Spicy Feta Spread',desc:'Whipped feta with Calabrian chilies, wood-fired pita, honey drizzle.'},
      thirsty:{dish:'Cucumber Mint Cooler',desc:'Craft cocktail — vodka, fresh cucumber, mint, lime, agave.'}
    };

    opts.forEach(function(opt){
      opt.addEventListener('click',function(){
        var parent=opt.closest('.crave-step');
        var stepIdx=Array.from(steps).indexOf(parent);
        var val=opt.getAttribute('data-value');
        selections['step'+(stepIdx+1)]=val;
        parent.querySelectorAll('.crave-opt').forEach(function(o){o.classList.remove('selected')});
        opt.classList.add('selected');

        // Check if all steps answered
        var allAnswered=true;
        steps.forEach(function(s){if(!s.querySelector('.crave-opt.selected')) allAnswered=false});

        if(allAnswered){
          var mood=selections['step2'];
          var match=data[mood]||data.hungry;
          dishEl.textContent=match.dish;
          descEl.textContent=match.desc;
          result.classList.add('show');
          steps.forEach(function(s){s.classList.remove('active')});
        }else{
          var nextIdx=stepIdx+1;
          while(nextIdx<steps.length){
            if(!steps[nextIdx].querySelector('.crave-opt.selected')){steps[nextIdx].classList.add('active');break}
            nextIdx++;
          }
        }
      });
    });

    if(resetBtn){
      resetBtn.addEventListener('click',function(){
        selections={};
        result.classList.remove('show');
        steps.forEach(function(s,i){
          s.classList.toggle('active',i===0);
          s.querySelectorAll('.crave-opt').forEach(function(o){o.classList.remove('selected')});
        });
      });
    }

    // Init first step
    steps.forEach(function(s,i){s.classList.toggle('active',i===0)});
  }
})();
