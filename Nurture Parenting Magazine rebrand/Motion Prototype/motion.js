/* ==========================================================================
   Nurture — motion system JS (scroll reveals, cover-stack assembly, ambient
   loop pausing). Paste this whole file into Avada → Options → Advanced →
   Custom JS (or a footer "Code Block" if you only want it on one page).

   This is deliberately dependency-free vanilla JS — nothing to install,
   nothing that can conflict with Avada/jQuery. It only ever *adds* CSS
   classes; if it fails to run for any reason, the page still looks and
   works exactly like a normal static page (see the ".js-motion" bootstrap
   snippet in the README — that one line is what makes this "progressive
   enhancement" instead of "hide content behind JS").
   ========================================================================== */
(function () {
  "use strict";
  var reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var hasIO = 'IntersectionObserver' in window;

  // ---- Scroll reveals (any element with class "reveal" or "reveal-photo") ----
  var revealEls = document.querySelectorAll('.reveal, .reveal-photo');
  if (reduceMotion || !hasIO) {
    revealEls.forEach(function (el) { el.classList.add('is-visible'); });
  } else {
    var revealIO = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          revealIO.unobserve(entry.target);
        }
      });
    }, { threshold: 0.16, rootMargin: '0px 0px -60px 0px' });
    revealEls.forEach(function (el) { revealIO.observe(el); });
  }

  // ---- Magazine cover stack: scatter -> fly together once in view ----
  // Expects: <div class="shelf">...<div class="cov cv1" style="--rest:...">
  var shelf = document.querySelector('.shelf');
  if (shelf) {
    var covers = shelf.querySelectorAll('.cov');
    if (reduceMotion || !hasIO) {
      shelf.classList.add('in-view');
      covers.forEach(function (c) { c.classList.add('settled'); });
    } else {
      covers.forEach(function (cov) {
        cov.addEventListener('animationend', function () { cov.classList.add('settled'); }, { once: true });
      });
      var shelfIO = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add('in-view');
            shelfIO.unobserve(entry.target);
          }
        });
      }, { threshold: 0.3 });
      shelfIO.observe(shelf);
    }
  }

  // ---- Ambient loops (".glow", ".brand-dot") pause when scrolled out of view ----
  if (!reduceMotion && hasIO) {
    var ambientEls = document.querySelectorAll('.glow, .brand-dot');
    var ambientIO = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        entry.target.style.animationPlayState = entry.isIntersecting ? 'running' : 'paused';
      });
    }, { threshold: 0 });
    ambientEls.forEach(function (el) { ambientIO.observe(el); });
  }
})();
