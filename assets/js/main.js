/* ==========================================================================
   main.js — module entry point
   Imported by every page. Orchestration plus the site-wide enhancements
   (progress bar, cursor, scanner reveals, lightbox).
   ========================================================================== */

/** Site-wide constants. */
export const SITE = Object.freeze({
  name: 'KARTIK H',
  origin: 'https://kartik-h6.github.io/Portfolio',
  email: 'kartik.h6822@gmail.com',
  links: {
    linkedin: 'https://www.linkedin.com/in/kartik-h6',
    github: 'https://github.com/kartik-h6',
  },
});

const reduceMotion = () =>
  window.matchMedia('(prefers-reduced-motion: reduce)').matches;

function make(tag, className, html) {
  const el = document.createElement(tag);
  if (className) el.className = className;
  if (html != null) el.innerHTML = html;
  return el;
}

/* --------------------------------------------------------------------------
   Scroll progress bar — fixed at the top, width tracks scroll position.
   -------------------------------------------------------------------------- */
function initProgress() {
  if (document.querySelector('.progress-bar')) return;
  const bar = make('div', 'progress-bar');
  bar.setAttribute('aria-hidden', 'true');
  document.body.append(bar);

  const update = () => {
    const max = document.documentElement.scrollHeight - window.innerHeight;
    bar.style.width = (max > 0 ? Math.min((window.scrollY / max) * 100, 100) : 0) + '%';
  };
  window.addEventListener('scroll', update, { passive: true });
  window.addEventListener('resize', update);
  update();
}

/* --------------------------------------------------------------------------
   Custom cursor — a precise dot plus a trailing ring that grows over
   interactive elements. Fine pointers only; never on touch or reduced motion.
   -------------------------------------------------------------------------- */
function initCursor() {
  if (reduceMotion()) return;
  if (!window.matchMedia('(pointer: fine)').matches) return;
  if (document.querySelector('.cursor-dot')) return;

  const dot = make('div', 'cursor-dot');
  const ring = make('div', 'cursor-ring');
  dot.setAttribute('aria-hidden', 'true');
  ring.setAttribute('aria-hidden', 'true');
  document.body.append(dot, ring);

  const root = document.documentElement;
  root.classList.add('cursor-on');

  let mx = window.innerWidth / 2, my = window.innerHeight / 2;
  let rx = mx, ry = my;

  window.addEventListener('pointermove', (e) => {
    mx = e.clientX; my = e.clientY;
    dot.style.transform = `translate(${mx}px, ${my}px) translate(-50%, -50%)`;
  }, { passive: true });

  (function trail() {
    rx += (mx - rx) * 0.18;
    ry += (my - ry) * 0.18;
    ring.style.transform = `translate(${rx}px, ${ry}px) translate(-50%, -50%)`;
    requestAnimationFrame(trail);
  })();

  const HOT = 'a, button, .chip, .scanner[data-expand], .ticker';
  document.addEventListener('pointerover', (e) => {
    ring.classList.toggle('is-hot', !!(e.target.closest && e.target.closest(HOT)));
  });

  // give the native cursor back when the window is not focused
  window.addEventListener('blur', () => root.classList.remove('cursor-on'));
  window.addEventListener('focus', () => root.classList.add('cursor-on'));
}

/* --------------------------------------------------------------------------
   Lightbox — opens a tall infographic at a readable size and lets it scroll.
   -------------------------------------------------------------------------- */
function ensureLightbox() {
  let lb = document.getElementById('lightbox');
  if (lb) return lb;

  lb = make('div', 'lightbox',
    '<button class="lightbox__close" type="button" aria-label="Close enlarged image">Close</button>' +
    '<img alt="">');
  lb.id = 'lightbox';
  lb.dataset.open = 'false';
  lb.setAttribute('role', 'dialog');
  lb.setAttribute('aria-modal', 'true');
  lb.setAttribute('aria-label', 'Enlarged image');
  document.body.append(lb);

  const close = () => {
    lb.dataset.open = 'false';
    document.documentElement.style.overflow = '';
  };
  lb.addEventListener('click', (e) => {
    if (e.target === lb || (e.target.closest && e.target.closest('.lightbox__close'))) close();
  });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') close(); });
  return lb;
}

/* --------------------------------------------------------------------------
   Scanners.
   data-expand — opens the image full size in the scrollable lightbox. It is a
                 real control, so it gets role=button, a tabindex and a label.
   data-reveal — a decorative desaturate/reveal. It gets a CLICK toggle so it
                 works on touch (where :hover never fires), but no tabindex or
                 role: it is not a control and must not be a focus stop.
   -------------------------------------------------------------------------- */
function initScanners() {
  const boxes = document.querySelectorAll('.scanner');
  if (!boxes.length) return;
  const lb = ensureLightbox();

  boxes.forEach((box) => {
    const img = box.querySelector('img');
    if (!img) return;

    if (box.hasAttribute('data-expand')) {
      box.setAttribute('role', 'button');
      box.setAttribute('tabindex', '0');
      box.setAttribute('aria-label', (img.alt || 'Image') + ' — activate to view full size');

      const open = () => {
        const big = lb.querySelector('img');
        big.src = img.currentSrc || img.src;
        big.alt = img.alt || '';
        lb.dataset.open = 'true';
        lb.scrollTop = 0;
        document.documentElement.style.overflow = 'hidden';
        lb.querySelector('.lightbox__close').focus();
      };
      box.addEventListener('click', open);
      box.addEventListener('keydown', (e) => {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(); }
      });
    } else if (box.hasAttribute('data-reveal')) {
      // touch has no hover — let a tap toggle the reveal
      box.addEventListener('click', () => box.classList.toggle('is-revealed'));
    }
  });
}

/* --------------------------------------------------------------------------
   Boot
   The current-page marker is NOT set here: every page already hardcodes
   aria-current="page" on its own nav link, so the HTML is the single source.
   -------------------------------------------------------------------------- */
function boot() {
  initProgress();
  initCursor();
  initScanners();
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', boot, { once: true });
} else {
  boot();
}
