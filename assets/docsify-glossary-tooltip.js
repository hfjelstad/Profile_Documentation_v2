/**
 * docsify-glossary-tooltip.js
 *
 * Parses Guides/Glossary/Glossary.md at startup, then wraps matching terms
 * in every page with <span class="glossary-tip"> elements that show
 * the definition on hover via a CSS ::after pseudo-element.
 *
 * Structure expected in Glossary.md:
 *   ## TermName
 *   <blank line>
 *   Definition paragraph (first non-empty line after heading)
 */
(function () {
  'use strict';

  var glossary = {};        // { term: definition }
  var defined  = false;     // true once glossary is loaded
  var defined_promise;      // resolves when glossary is ready

  // ---- helpers ----

  function escapeHtml(s) {
    return s.replace(/&/g, '&amp;').replace(/"/g, '&quot;')
            .replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }

  function escapeRegex(s) {
    return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  }

  // Parse Glossary.md text into { term: definition } map
  function parseGlossary(md) {
    var entries = {};
    // Split on ## headings
    var parts = md.split(/^## /m);
    for (var i = 1; i < parts.length; i++) {
      var block = parts[i];
      var nlIdx = block.indexOf('\n');
      if (nlIdx === -1) continue;
      var term = block.substring(0, nlIdx).trim();
      // First non-empty, non-blockquote, non-link line after the heading
      var lines = block.substring(nlIdx + 1).split('\n');
      var def = '';
      for (var j = 0; j < lines.length; j++) {
        var line = lines[j].trim();
        if (line === '' || line === '---') continue;
        if (line.charAt(0) === '>') continue;          // skip blockquotes (XSD/Transmodel)
        if (line.substring(0, 2) === '->') continue;   // skip arrow links
        if (line.charAt(0) === '\u2192') continue;      // → arrow links
        def = line;
        break;
      }
      if (term && def) {
        // Strip any trailing markdown link syntax
        def = def.replace(/\[([^\]]+)\]\([^)]+\)/g, '$1');
        entries[term] = def;
      }
    }
    return entries;
  }

  // Build a single regex matching all terms (longest first for greedy match)
  function buildTermRegex(terms) {
    // Sort longest term first so "DatedServiceJourney" beats "ServiceJourney"
    var sorted = terms.slice().sort(function (a, b) { return b.length - a.length; });
    var escaped = sorted.map(escapeRegex);
    // Word-boundary match — but many NeTEx terms are CamelCase,
    // so we use lookahead/behind for non-word characters or string edges
    return new RegExp('(?<![\\w/])(' + escaped.join('|') + ')(?![\\w/])', 'g');
  }

  // Wrap matched terms in the rendered HTML, skipping code/links/headings/tables
  // Only the FIRST occurrence of each term is annotated per page.
  function annotateHtml(html, regex) {
    // Split HTML into "inside-tag" and "text" tokens so we never modify tags
    var tokens = html.split(/(<[^>]+>)/);
    var skip = 0;          // depth counter for elements we must not touch
    var skipTags = /^<(code|pre|a|h[1-6]|script|style|span[^>]*glossary|th)\b/i;
    var skipClose = /^<\/(code|pre|a|h[1-6]|script|style|span|th)/i;
    var seen = {};         // track which terms have already been annotated

    for (var i = 0; i < tokens.length; i++) {
      var t = tokens[i];
      if (t.charAt(0) === '<') {
        if (skipTags.test(t)) skip++;
        else if (skipClose.test(t) && skip > 0) skip--;
        continue;
      }
      if (skip > 0) continue;              // inside a protected element
      if (t.trim() === '') continue;        // whitespace-only text node

      tokens[i] = t.replace(regex, function (match) {
        if (seen[match]) return match;      // already annotated this term
        var tip = glossary[match];
        if (!tip) return match;
        seen[match] = true;
        return '<span class="glossary-tip" data-tip="' + escapeHtml(tip) + '">' + match + '</span>';
      });
    }
    return tokens.join('');
  }

  // ---- Docsify plugin ----

  function glossaryTooltipPlugin(hook) {

    // Fetch and parse Glossary.md once on init
    hook.init(function () {
      defined_promise = new Promise(function (resolve) {
        // Use Docsify's relative path base — works on GitHub Pages or local
        var base = window.$docsify.basePath || '';
        var url = base + 'Guides/Glossary/Glossary.md';

        fetch(url)
          .then(function (r) { return r.text(); })
          .then(function (md) {
            glossary = parseGlossary(md);
            defined = true;
            resolve();
          })
          .catch(function () {
            // Glossary not found — plugin silently becomes a no-op
            defined = true;
            resolve();
          });
      });
    });

    // After Docsify converts markdown → HTML, annotate terms
    hook.afterEach(function (html, next) {
      if (!defined) {
        defined_promise.then(function () { next(doAnnotate(html)); });
      } else {
        next(doAnnotate(html));
      }
    });

    function doAnnotate(html) {
      var terms = Object.keys(glossary);
      if (terms.length === 0) return html;

      // Don't annotate the Glossary page itself
      var path = window.location.hash || '';
      if (path.indexOf('Glossary') !== -1) return html;

      var regex = buildTermRegex(terms);
      return annotateHtml(html, regex);
    }

    // Create a single floating tooltip element and bind hover events
    hook.doneEach(function () {
      var tip = document.getElementById('glossary-tooltip');
      if (!tip) {
        tip = document.createElement('div');
        tip.id = 'glossary-tooltip';
        document.body.appendChild(tip);
      }

      var spans = document.querySelectorAll('.glossary-tip');
      for (var i = 0; i < spans.length; i++) {
        spans[i].addEventListener('mouseenter', showTip);
        spans[i].addEventListener('mouseleave', hideTip);
      }

      function showTip(e) {
        var el = e.currentTarget;
        var text = el.getAttribute('data-tip');
        if (!text) return;
        tip.textContent = text;
        tip.classList.add('visible');

        // Position above the term, using fixed coordinates
        var rect = el.getBoundingClientRect();
        var tipRect = tip.getBoundingClientRect();

        var left = rect.left;
        var top  = rect.top - tipRect.height - 8;

        // Keep within viewport horizontally
        if (left + tipRect.width > window.innerWidth - 12) {
          left = window.innerWidth - tipRect.width - 12;
        }
        if (left < 4) left = 4;

        // If no room above, show below
        if (top < 4) {
          top = rect.bottom + 8;
          tip.style.setProperty('--arrow', 'bottom');
        } else {
          tip.style.setProperty('--arrow', 'top');
        }

        tip.style.left = left + 'px';
        tip.style.top  = top + 'px';
      }

      function hideTip() {
        tip.classList.remove('visible');
      }
    });
  }

  // Register
  window.$docsify = window.$docsify || {};
  window.$docsify.plugins = [].concat(
    glossaryTooltipPlugin,
    window.$docsify.plugins || []
  );
})();
