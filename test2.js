
// MOBILE MENU
const hamburger = document.getElementById('hamburger');
const navLinks = document.querySelector('.nav-links');
hamburger.addEventListener('click', () => {
  navLinks.classList.toggle('active');
});
navLinks.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => navLinks.classList.remove('active'));
});
document.addEventListener('click', (e) => {
  if (navLinks.classList.contains('active') && !navLinks.contains(e.target) && !hamburger.contains(e.target)) {
    navLinks.classList.remove('active');
  }
});
// ── NAV
const nav=document.getElementById('mainNav');
window.addEventListener('scroll',()=>nav.classList.toggle('scrolled',window.scrollY>60));

// ── SCROLL REVEAL
const obs=new IntersectionObserver(entries=>{
  entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('visible');obs.unobserve(e.target);}});
},{threshold:0.08,rootMargin:'0px 0px -30px 0px'});
document.querySelectorAll('.reveal').forEach(el=>obs.observe(el));

// ── PRODUCTS & PRICING
const PRODUCTS={
  nkolomoka_330:{basePrice:16000},
  nkolo_mboka_330:{basePrice:15000},
  ola_kombucha_330:{basePrice:14500},
  ginger_punch_330:{basePrice:14000},
  hard_rock_330:{basePrice:18000},
};
// Current quote state (used by contact form)
let quoteData=null;

function updateCalc(e){
  let qty=parseInt(document.getElementById('quantitySlider').value,10);
  if(e && e.target.id === 'quantityInput') {
    qty = parseInt(document.getElementById('quantityInput').value, 10) || 0;
    if (qty >= 10) {
      document.getElementById('quantitySlider').value = qty;
    }
  } else {
    document.getElementById('quantityInput').value = qty;
  }
  
  const warn = document.getElementById('qtyWarning');
  const btn = document.getElementById('enquiryBtn');
  
  if (qty < 10) {
    warn.style.display = 'block';
    warn.style.animation = 'none';
    warn.offsetHeight; // trigger reflow
    warn.style.animation = 'shake 0.4s';
    btn.disabled = true;
    btn.style.opacity = '0.5';
    btn.style.cursor = 'not-allowed';
    document.getElementById('freeCasesVal').textContent = '0';
    quoteData = null;
    return;
  }
  
  warn.style.display = 'none';
  btn.disabled = false;
  btn.style.opacity = '1';
  btn.style.cursor = 'pointer';
  
  const prod=PRODUCTS[document.getElementById('productSelect').value];
  const freeCases = Math.floor(qty / 100) * 7;
  const sel=document.getElementById('productSelect');
  const pname=sel.options[sel.selectedIndex].text;

  document.getElementById('freeCasesVal').textContent=freeCases > 0 ? '+'+freeCases : '0';

  // Store for form use
  quoteData={pname,qty,freeCases};
}
document.getElementById('quantitySlider').addEventListener('input',updateCalc);
document.getElementById('quantityInput').addEventListener('input',updateCalc);
document.getElementById('productSelect').addEventListener('change',updateCalc);
updateCalc();

// ── CREATE ENQUIRY: scroll to form + pre-fill message
function createEnquiry(){
  if(!quoteData)return;
  const {pname,qty,freeCases}=quoteData;
  const msg=`I'd like to enquire about: ${pname} × ${qty} cases.${freeCases>0?' (Includes '+freeCases+' FREE cases!)':''}`;

  // Fill message field
  document.getElementById('fMessage').value=msg;

  // Show quote banner
  const banner=document.getElementById('quoteBanner');
  document.getElementById('quoteBannerText').textContent=
    pname+' × '+qty+' cases'+(freeCases>0?' (+' + freeCases + ' FREE cases)':'');
  banner.style.display='block';

  // Highlight the enquiry button briefly
  const btn=document.getElementById('enquiryBtn');
  btn.classList.add('quote-loaded');

  // Smooth scroll to contact form
  document.getElementById('contact').scrollIntoView({behavior:'smooth',block:'start'});

  // Focus first empty required field after scroll
  setTimeout(()=>{
    const first=['fFirstName','fLastName','fEmail','fCompany','fType'].find(id=>!document.getElementById(id).value.trim());
    if(first)document.getElementById(first).focus();
  },700);
}

// ── VALIDATE FORM
function getFormValues(){
  const firstName=document.getElementById('fFirstName').value.trim();
  const lastName=document.getElementById('fLastName').value.trim();
  const email=document.getElementById('fEmail').value.trim();
  const phone=document.getElementById('fPhone').value.trim();
  const company=document.getElementById('fCompany').value.trim();
  const type=document.getElementById('fType').value.trim();
  const message=document.getElementById('fMessage').value.trim();
  return{firstName,lastName,email,phone,company,type,message};
}
function validateForm(){
  const f=getFormValues();
  let valid=true;
  ['fFirstName','fLastName','fEmail','fCompany','fType'].forEach(id=>{
    const el=document.getElementById(id);
    const ok=el.value.trim()!=='';
    el.style.borderColor=ok?'':'#E24B4A';
    if(!ok)valid=false;
  });
  return valid;
}

// ── SEND VIA WHATSAPP
function sendViaWhatsApp(){
  if(!validateForm()){
    document.getElementById('formError').style.display='block';
    setTimeout(()=>document.getElementById('formError').style.display='none',4000);
    return;
  }
  const f=getFormValues();
  const WA_NUMBER='255713822240';
  const lines=[
    '*New Wholesale Enquiry — Simba Beverages*',
    '',
    '*Name:* '+f.firstName+' '+f.lastName,
    '*Company:* '+f.company,
    '*Email:* '+f.email,
    f.phone?'*Phone:* '+f.phone:'',
    '*Partnership Type:* '+f.type,
    '',
    f.message||'(No additional message)',
  ].filter(l=>l!==undefined);
  const waText=encodeURIComponent(lines.join('\n'));
  window.open('https://wa.me/'+WA_NUMBER+'?text='+waText,'_blank');
  showSuccess();
}

// ── SEND VIA EMAIL (Formspree)
// Replace YOUR_FORM_ID below with your actual Formspree form ID
// Sign up free at formspree.io → create form → copy the ID (e.g. xpwzabcd)
const FORMSPREE_ID='YOUR_FORM_ID';

document.getElementById('contactForm').addEventListener('submit',async function(e){
  e.preventDefault();
  if(!validateForm()){
    document.getElementById('formError').style.display='block';
    setTimeout(()=>document.getElementById('formError').style.display='none',4000);
    return;
  }
  const f=getFormValues();
  const btn=document.getElementById('btnEmail');
  btn.disabled=true;btn.textContent='Sending...';

  // Fall back to opening prefilled Gmail directly
  if(FORMSPREE_ID==='YOUR_FORM_ID'){
    const subject=encodeURIComponent('Wholesale Enquiry — '+f.company);
    const body=encodeURIComponent(
      'Name: '+f.firstName+' '+f.lastName+'\nEmail: '+f.email+'\nPhone: '+f.phone+
      '\nCompany: '+f.company+'\nType: '+f.type+'\n\n'+f.message
    );
    window.open('https://mail.google.com/mail/?view=cm&fs=1&to=sales@simba-beverages.co.tz&su='+subject+'&body='+body, '_blank');
    btn.disabled=false;btn.textContent='Send via Email';
    showSuccess();
    return;
  }

  // Formspree submission
  try{
    const res=await fetch('https://formspree.io/f/'+FORMSPREE_ID,{
      method:'POST',
      headers:{'Content-Type':'application/json','Accept':'application/json'},
      body:JSON.stringify({
        firstName:f.firstName,lastName:f.lastName,email:f.email,phone:f.phone,
        company:f.company,partnershipType:f.type,message:f.message,
        _subject:'Wholesale Enquiry — '+f.company
      })
    });
    if(res.ok){showSuccess();}
    else{alert('There was a problem sending. Please email us directly at sales@simba-beverages.co.tz');}
  }catch{
    alert('Network error. Please email us directly at sales@simba-beverages.co.tz');
  }
  btn.disabled=false;btn.textContent='Send via Email';
});

function showSuccess(){
  sessionStorage.setItem('sbl_form_submitted', 'true');
  document.getElementById('contactForm').reset();
  document.getElementById('quoteBanner').style.display='none';
  document.getElementById('enquiryBtn').classList.remove('quote-loaded');
  quoteData=null;
  const s=document.getElementById('formSuccess');
  s.style.display='block';
  setTimeout(()=>s.style.display='none',6000);
}

// ── CUSTOM SELECT REPLACEMENT ──
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('select').forEach(select => {
    const wrapper = document.createElement('div');
    wrapper.className = 'custom-select-wrapper';
    select.parentNode.insertBefore(wrapper, select);
    wrapper.appendChild(select);
    select.style.display = 'none';

    const trigger = document.createElement('div');
    trigger.className = 'custom-select-trigger ' + select.className;
    trigger.innerHTML = `<span>${select.options[select.selectedIndex]?.text || ''}</span><svg xmlns="http://www.w3.org/2000/svg" width="12" height="8" viewBox="0 0 12 8"><path d="M1 1l5 5 5-5" stroke="#F5A623" stroke-width="1.5" fill="none" stroke-linecap="round"/></svg>`;
    wrapper.appendChild(trigger);

    const options = document.createElement('div');
    options.className = 'custom-options';
    Array.from(select.options).forEach(opt => {
      const option = document.createElement('div');
      option.className = 'custom-option' + (opt.selected ? ' selected' : '');
      option.textContent = opt.text;
      option.dataset.value = opt.value;
      
      if(opt.disabled) {
        option.classList.add('disabled');
      } else {
        option.addEventListener('click', function() {
          select.value = this.dataset.value;
          trigger.querySelector('span').textContent = this.textContent;
          options.querySelectorAll('.custom-option').forEach(o => o.classList.remove('selected'));
          this.classList.add('selected');
          wrapper.classList.remove('open');
          select.dispatchEvent(new Event('change'));
        });
      }
      options.appendChild(option);
    });
    wrapper.appendChild(options);

    trigger.addEventListener('click', function(e) {
      e.stopPropagation();
      document.querySelectorAll('.custom-select-wrapper').forEach(w => {
        if(w !== wrapper) w.classList.remove('open');
      });
      wrapper.classList.toggle('open');
    });
  });

  document.addEventListener('click', () => {
    document.querySelectorAll('.custom-select-wrapper').forEach(w => w.classList.remove('open'));
  });
});
// ── AGE GATE LOGIC ──
function initAgeGate(){
  if(!localStorage.getItem('sbl_age_verified')){
    document.body.style.overflow = 'hidden';
    document.getElementById('ageGate').classList.remove('hidden');
  } else {
    document.getElementById('ageGate').classList.add('hidden');
    document.body.style.overflow = '';
  }
}
function verifyAge(isAdult){
  if(isAdult){
    localStorage.setItem('sbl_age_verified','true');
    document.getElementById('ageGate').classList.add('hidden');
    document.body.style.overflow = '';
  } else {
    window.location.href = 'https://www.google.com';
  }
}

// ── PRELOADER LOGIC ──
function hidePreloader() {
  const p = document.getElementById('sitePreloader');
  if(p) p.classList.add('loaded');
}
window.addEventListener('load', hidePreloader);
setTimeout(hidePreloader, 2000);

// ── FAQ TOGGLE ──
function toggleFaq(el){
  const item = el.parentElement;
  item.classList.toggle('active');
}

// ── LANGUAGE TOGGLE ──
let currentLang = 'en';

function toggleLanguage() {
  currentLang = currentLang === 'en' ? 'sw' : 'en';
  setLang(currentLang);
  // Also translate the WhatsApp Widget textarea explicitly
  const waTextArea = document.getElementById('waWidgetMsg');
  if(waTextArea) {
    if(currentLang === 'sw') {
      waTextArea.value = "Habari Simba Beverages, ningependa kuulizia bei ya jumla ya Vin Nkolo Mboka.";
    } else {
      waTextArea.value = "Hi Simba Beverages, I'd like to enquire about wholesale pricing for Vin Nkolo Mboka.";
    }
  }
}

function setLang(lang){
  currentLang = lang;
  document.querySelectorAll('.lang-btn').forEach(btn => btn.classList.remove('active'));
  document.querySelector(`.lang-btn[data-lang="${lang}"]`).classList.add('active');
  
  document.querySelectorAll('[data-en][data-sw]').forEach(el => {
    if(el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
      el.placeholder = el.getAttribute(`data-${lang}`);
    } else {
      el.innerHTML = el.getAttribute(`data-${lang}`);
    }
  });
}

// ── WHATSAPP WIDGET ──
function toggleWaPopover(e) {
  if(e) e.stopPropagation();
  const popover = document.getElementById('waPopover');
  popover.classList.toggle('open');
}

function sendWaWidget() {
  const msg = document.getElementById('waWidgetMsg').value;
  const WA_NUMBER = '255713822240';
  window.open('https://wa.me/' + WA_NUMBER + '?text=' + encodeURIComponent(msg), '_blank');
  document.getElementById('waPopover').classList.remove('open');
}

document.addEventListener('click', (e) => {
  const popover = document.getElementById('waPopover');
  const widget = document.getElementById('waWidget');
  if (popover && popover.classList.contains('open') && widget && !widget.contains(e.target)) {
    popover.classList.remove('open');
  }
});
document.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') {
    const popover = document.getElementById('waPopover');
    if (popover && popover.classList.contains('open')) {
      popover.classList.remove('open');
    }
    closeExitIntent();
  }
});

// ── EXIT INTENT LOGIC ──
let exitIntentTriggered = false;
document.addEventListener('mouseleave', (e) => {
  if (e.clientY < 0 && !exitIntentTriggered && !localStorage.getItem('sbl_exit_shown') && !sessionStorage.getItem('sbl_form_submitted')) {
    document.getElementById('exitIntentPopup').classList.add('show');
    exitIntentTriggered = true;
    localStorage.setItem('sbl_exit_shown', 'true');
  }
});
function closeExitIntent() {
  const p = document.getElementById('exitIntentPopup');
  if(p) p.classList.remove('show');
}

// ── VISUAL POLISH: SCROLL PROGRESS ──
window.addEventListener('scroll', () => {
  const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
  const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
  const scrolled = (winScroll / height) * 100;
  const p = document.getElementById('scrollProgress');
  if(p) p.style.width = scrolled + '%';
});

// ── VISUAL POLISH: CURSOR TRAIL ──
if (window.matchMedia("(hover: hover) and (pointer: fine)").matches) {
  const trailCount = 8;
  const dots = [];
  for (let i = 0; i < trailCount; i++) {
    const dot = document.createElement('div');
    dot.className = 'cursor-dot';
    document.body.appendChild(dot);
    dots.push({ el: dot, x: 0, y: 0 });
  }
  let mouseX = 0, mouseY = 0;
  window.addEventListener('mousemove', (e) => { mouseX = e.clientX; mouseY = e.clientY; });
  function animateTrail() {
    let x = mouseX, y = mouseY;
    dots.forEach((dot, index) => {
      const nextDot = dots[index + 1] || dots[0];
      dot.x = x; dot.y = y;
      dot.el.style.transform = `translate(${x}px, ${y}px) scale(${(trailCount - index) / trailCount})`;
      x += (nextDot.x - x) * 0.5; y += (nextDot.y - y) * 0.5;
    });
    requestAnimationFrame(animateTrail);
  }
  animateTrail();
}

// ── PWA SERVICE WORKER ──
if ('serviceWorker' in navigator) {
  navigator.serviceWorker.register('sw.js');
}
