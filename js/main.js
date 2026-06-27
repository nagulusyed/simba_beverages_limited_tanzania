// ============================================
//  SIMBA BEVERAGES LIMITED — Main JS
// ============================================

document.addEventListener('DOMContentLoaded', () => {

  // ── NAV SCROLL EFFECT ──
  const nav = document.querySelector('nav');
  if (nav) {
    window.addEventListener('scroll', () => {
      nav.classList.toggle('scrolled', window.scrollY > 60);
    });
  }

  // ── ACTIVE NAV LINK ──
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links a').forEach(link => {
    if (link.getAttribute('href') === currentPage) link.classList.add('active');
  });

  // ── SCROLL REVEAL ──
  const reveals = document.querySelectorAll('.reveal');
  if (reveals.length) {
    const revealObserver = new IntersectionObserver((entries) => {
      entries.forEach(e => {
        if (e.isIntersecting) {
          e.target.classList.add('visible');
          revealObserver.unobserve(e.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });
    reveals.forEach(r => revealObserver.observe(r));
  }

  // ── MOBILE NAV TOGGLE ──
  const hamburger = document.querySelector('.nav-hamburger');
  const navLinks = document.querySelector('.nav-links');
  if (hamburger && navLinks) {
    hamburger.addEventListener('click', () => {
      const open = navLinks.classList.toggle('mobile-open');
      hamburger.setAttribute('aria-expanded', open);
    });
  }

  // ── PRICING CALCULATOR (wholesale page) ──
  const quantitySlider = document.getElementById('quantitySlider');
  if (quantitySlider) {
    initPricingCalculator();
  }

  // ── CONTACT FORM ──
  const contactForm = document.getElementById('contactForm');
  if (contactForm) {
    contactForm.addEventListener('submit', handleContactForm);
  }

});

// ────────────────────────────────────────────
//  PRICING CALCULATOR
// ────────────────────────────────────────────
const PRODUCTS = {
  nkolomoka_250: { name: 'Vin Nkolomoka 250ml', basePrice: 8.50, currency: 'USD' },
  nkolomoka_500: { name: 'Vin Nkolomoka 500ml', basePrice: 14.50, currency: 'USD' },
  nkolomoka_1l:  { name: 'Vin Nkolomoka 1 Litre', basePrice: 22.00, currency: 'USD' },
};

const DISCOUNT_TIERS = [
  { min: 1,    max: 99,   pct: 0  },
  { min: 100,  max: 499,  pct: 5  },
  { min: 500,  max: 999,  pct: 10 },
  { min: 1000, max: Infinity, pct: 15 },
];

function getDiscount(qty) {
  const tier = DISCOUNT_TIERS.find(t => qty >= t.min && qty <= t.max);
  return tier ? tier.pct : 0;
}

function initPricingCalculator() {
  const slider      = document.getElementById('quantitySlider');
  const casesLabel  = document.getElementById('casesLabel');
  const productSel  = document.getElementById('productSelect');
  const basePriceEl = document.getElementById('basePrice');
  const unitPriceEl = document.getElementById('unitPrice');
  const discountEl  = document.getElementById('discountPct');
  const savingsEl   = document.getElementById('totalSavings');
  const grandTotalEl= document.getElementById('grandTotal');
  const tierCards   = document.querySelectorAll('.tier-card');
  const enquiryBtn  = document.getElementById('enquiryBtn');

  function updateCalc() {
    const qty = parseInt(slider.value, 10);
    const product = PRODUCTS[productSel.value];
    const discPct = getDiscount(qty);
    const discounted = product.basePrice * (1 - discPct / 100);
    const total = discounted * qty;
    const savings = (product.basePrice - discounted) * qty;

    casesLabel.textContent  = qty + ' cases';
    basePriceEl.textContent = '$' + product.basePrice.toFixed(2);
    unitPriceEl.textContent = '$' + discounted.toFixed(2);
    discountEl.textContent  = discPct + '%';
    savingsEl.textContent   = '$' + savings.toFixed(2);
    grandTotalEl.textContent= '$' + total.toFixed(2);

    // Highlight active tier
    tierCards.forEach(card => {
      const cardPct = parseInt(card.dataset.pct, 10);
      card.classList.toggle('active', cardPct === discPct);
    });

    // Update enquiry button href (pre-fills mailto)
    if (enquiryBtn) {
      const subject = encodeURIComponent('Wholesale Enquiry — ' + product.name);
      const body = encodeURIComponent(
        `Product: ${product.name}\nQuantity: ${qty} cases\nUnit Price: $${discounted.toFixed(2)}\nDiscount: ${discPct}%\nEstimated Total: $${total.toFixed(2)}\n\nPlease contact me to confirm this order.`
      );
      enquiryBtn.href = `mailto:sales@simba-beverages.co.tz?subject=${subject}&body=${body}`;
    }
  }

  slider.addEventListener('input', updateCalc);
  productSel.addEventListener('change', updateCalc);

  updateCalc(); // init
}

// ────────────────────────────────────────────
//  CONTACT FORM
// ────────────────────────────────────────────
function handleContactForm(e) {
  e.preventDefault();
  const form = e.target;
  const btn = form.querySelector('button[type="submit"]');
  const successMsg = document.getElementById('formSuccess');

  // Basic validation
  const required = form.querySelectorAll('[required]');
  let valid = true;
  required.forEach(field => {
    if (!field.value.trim()) {
      field.style.borderColor = '#E24B4A';
      valid = false;
    } else {
      field.style.borderColor = '';
    }
  });
  if (!valid) return;

  // Simulate send (replace with real backend/formspree/emailjs)
  btn.disabled = true;
  btn.textContent = 'Sending...';

  setTimeout(() => {
    btn.disabled = false;
    btn.textContent = 'Send Enquiry';
    form.reset();
    if (successMsg) {
      successMsg.style.display = 'block';
      setTimeout(() => successMsg.style.display = 'none', 5000);
    }
  }, 1400);
}
