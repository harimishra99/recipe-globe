// ============================================================
//  SWAD — Main JavaScript
// ============================================================

document.addEventListener('DOMContentLoaded', () => {
  initNavbar();
  initHamburger();
  initDropdowns();
  initIngredientChecks();
  initScrollAnimations();
  initRegionTabs();
  autoCloseAlerts();
});

// ── Navbar scroll shadow ──────────────────────────────────────
function initNavbar() {
  const nav = document.getElementById('navbar');
  if (!nav) return;
  const update = () => nav.classList.toggle('scrolled', window.scrollY > 20);
  window.addEventListener('scroll', update, { passive: true });
  update();
}

// ── Hamburger — full screen mobile menu ──────────────────────
function initHamburger() {
  const btn   = document.getElementById('hamburger');
  const links = document.getElementById('navLinks');
  if (!btn || !links) return;

  function openMenu() {
    links.classList.add('open');
    btn.classList.add('open');
    btn.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden';
  }

  function closeMenu() {
    links.classList.remove('open');
    btn.classList.remove('open');
    btn.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  }

  btn.addEventListener('click', (e) => {
    e.stopPropagation();
    links.classList.contains('open') ? closeMenu() : openMenu();
  });

  // Close when any nav link (non-dropdown) is clicked
  links.querySelectorAll('a:not(.nav-drop a)').forEach(a => {
    a.addEventListener('click', () => closeMenu());
  });

  // Close on outside tap
  document.addEventListener('click', (e) => {
    if (!btn.contains(e.target) && !links.contains(e.target)) {
      closeMenu();
    }
  });

  // Close on Escape key
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeMenu();
  });
}

// ── Mobile dropdown toggles ───────────────────────────────────
function initDropdowns() {
  // Only run toggle behaviour on mobile
  if (window.innerWidth > 768) return;

  document.querySelectorAll('.nav-drop > .nav-link').forEach(trigger => {
    trigger.addEventListener('click', (e) => {
      e.preventDefault();
      const drop = trigger.closest('.nav-drop');
      const wasOpen = drop.classList.contains('open');
      // close all others
      document.querySelectorAll('.nav-drop').forEach(d => d.classList.remove('open'));
      if (!wasOpen) drop.classList.add('open');
    });
  });
}

// ── Ingredient checkbox persistence ──────────────────────────
function initIngredientChecks() {
  document.querySelectorAll('.ing-row input[type=checkbox]').forEach((cb, i) => {
    const key = `ing-${location.pathname}-${i}`;
    cb.checked = localStorage.getItem(key) === '1';
    cb.addEventListener('change', () =>
      localStorage.setItem(key, cb.checked ? '1' : '0'));
  });
}

// ── Scroll-triggered fade-in animations ──────────────────────
function initScrollAnimations() {
  if (!('IntersectionObserver' in window)) return;

  const items = document.querySelectorAll(
    '.recipe-card, .state-card, .cat-pill, .cuisine-card'
  );

  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.style.opacity    = '1';
        e.target.style.transform  = 'translateY(0)';
        io.unobserve(e.target);
      }
    });
  }, { threshold: 0.08, rootMargin: '0px 0px -30px 0px' });

  items.forEach((el, i) => {
    el.style.opacity    = '0';
    el.style.transform  = 'translateY(14px)';
    el.style.transition = `opacity .4s ease ${i * 0.04}s, transform .4s ease ${i * 0.04}s`;
    io.observe(el);
  });
}

// ── State region tabs on homepage ────────────────────────────
function initRegionTabs() {
  const tabs   = document.querySelectorAll('.region-tab');
  const panels = document.querySelectorAll('.region-panel');
  if (!tabs.length) return;

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      const region = tab.dataset.region;
      tabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');
      panels.forEach(p => {
        p.style.display = p.dataset.region === region ? '' : 'none';
      });
    });
  });
}

// ── Auto-dismiss alert pills ──────────────────────────────────
function autoCloseAlerts() {
  setTimeout(() => {
    document.querySelectorAll('.alert-pill').forEach(a => {
      a.style.transition = 'opacity .4s';
      a.style.opacity    = '0';
      setTimeout(() => a.remove(), 400);
    });
  }, 4500);
}

// ── CSRF helper ───────────────────────────────────────────────
function getCookie(name) {
  return document.cookie
    .split(';')
    .map(c => c.trim())
    .find(c => c.startsWith(name + '='))
    ?.split('=')[1] || '';
}

// ── Language switcher (recipe detail) ────────────────────────
async function switchLang(langCode, slug) {
  // Highlight active button immediately
  document.querySelectorAll('.lang-btn').forEach(b =>
    b.classList.toggle('active', b.dataset.lang === langCode));

  // Remove previous notice if any
  document.getElementById('lang-notice')?.remove();

  try {
    const res  = await fetch(`/recipes/${slug}/translation/?lang=${langCode}`);
    const data = await res.json();

    const titleEl = document.getElementById('recipeTitle');
    const descEl  = document.getElementById('recipeDesc');
    if (titleEl) titleEl.textContent = data.title;
    if (descEl)  descEl.textContent  = data.description;

    // Show yellow notice when no translation exists yet
    if (!data.found && langCode !== 'en') {
      const notice       = document.createElement('div');
      notice.id          = 'lang-notice';
      notice.style.cssText = [
        'background:#FFF8E6',
        'border-left:3px solid #F5A623',
        'padding:.6rem 1rem',
        'border-radius:0 8px 8px 0',
        'font-size:.82rem',
        'color:#7A6010',
        'margin-top:.75rem',
      ].join(';');
      notice.textContent = '⚠️ Translation not available yet for this language. Showing original English.';
      if (descEl) descEl.parentElement?.insertBefore(notice, descEl);
    }
  } catch (e) {
    console.error('Translation fetch failed:', e);
  }
}

// ── Save / Bookmark recipe ────────────────────────────────────
async function toggleSave(slug, btn) {
  try {
    const res  = await fetch(`/recipes/${slug}/save/`, {
      method:  'POST',
      headers: { 'X-CSRFToken': getCookie('csrftoken') },
    });
    const data = await res.json();
    btn.classList.toggle('saved', data.saved);
    const label = btn.querySelector('.save-label');
    if (label) label.textContent = data.saved ? '✓ Saved' : 'Save Recipe';
    showToast(data.saved ? '✅ Recipe saved!' : 'Removed from saved.');
  } catch (e) {
    console.error('Save failed:', e);
  }
}

// ── Star rating ───────────────────────────────────────────────
async function submitRating(val, slug) {
  try {
    const res  = await fetch(`/recipes/${slug}/rate/`, {
      method:  'POST',
      headers: {
        'X-CSRFToken':  getCookie('csrftoken'),
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: `rating=${val}`,
    });
    const data = await res.json();
    document.querySelectorAll('.star-btn').forEach((b, i) =>
      b.classList.toggle('on', i < val));
    const avgEl = document.querySelector('.rating-avg');
    if (avgEl) avgEl.textContent = `Avg: ${data.avg} / 5`;
    showToast(`⭐ Rated ${val}/5 — thank you!`);
  } catch (e) {
    console.error('Rating failed:', e);
  }
}

// ── Copy link to clipboard ────────────────────────────────────
function copyLink(url) {
  navigator.clipboard.writeText(url)
    .then(() => showToast('🔗 Link copied to clipboard!'))
    .catch(() => showToast('Could not copy link.'));
}

// ── Toast notification ────────────────────────────────────────
function showToast(msg) {
  const t = document.createElement('div');
  t.className    = 'alert-pill alert-success';
  t.style.cssText = [
    'position:fixed',
    'bottom:5.5rem',
    'left:50%',
    'transform:translateX(-50%)',
    'z-index:9999',
    'white-space:nowrap',
    'pointer-events:none',
  ].join(';');
  t.textContent = msg;
  document.body.appendChild(t);
  setTimeout(() => {
    t.style.transition = 'opacity .35s';
    t.style.opacity    = '0';
    setTimeout(() => t.remove(), 350);
  }, 2000);
}