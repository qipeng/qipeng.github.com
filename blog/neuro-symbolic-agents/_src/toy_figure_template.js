(function () {
  var M = __MODEL__;
  var svg = document.getElementById('toyfig');
  var selA = document.getElementById('toyA'), selB = document.getElementById('toyB');
  var out = document.getElementById('toy-readout');
  if (!svg || !selA) return;
  var NS = 'http://www.w3.org/2000/svg';
  var vars = ['x', 'y', 'z', 'a', 'b', 'n', 'θ'];
  var idx = {}; M.vocab.forEach(function (t, i) { idx[t] = i; });
  vars.forEach(function (v) {
    [selA, selB].forEach(function (s) { var o = document.createElement('option'); o.value = v; o.textContent = v; s.appendChild(o); });
  });
  function forward(toks) {
    var x = []; toks.forEach(function (t) { x = x.concat(M.E[idx[t]]); });
    var h = M.W1.map(function (row, j) { var z = M.b1[j]; for (var i = 0; i < row.length; i++) z += row[i] * x[i]; return Math.tanh(z); });
    var lg = M.W2.map(function (row, k) { var z = M.b2[k]; for (var j = 0; j < row.length; j++) z += row[j] * h[j]; return z; });
    var m = Math.max.apply(null, lg), ex = lg.map(function (v) { return Math.exp(v - m); }), Z = ex.reduce(function (a, b) { return a + b; }, 0);
    return { h: h, p: ex.map(function (e) { return e / Z; }) };
  }
  function el(tag, attrs, text) {
    var e = document.createElementNS(NS, tag);
    for (var k in attrs) e.setAttribute(k, attrs[k]);
    if (text != null) e.textContent = text;
    return e;
  }
  function fmt(v) { return (v < 0 ? '−' : '') + Math.abs(v).toFixed(2); }
  function bar(g, x, base, v, scale, w, cls, tip) {
    var hgt = Math.max(Math.abs(v) * scale, 0.8);
    var r = el('rect', { x: x, y: v >= 0 ? base - hgt : base, width: w, height: hgt, rx: 1.5, 'class': cls });
    r.appendChild(el('title', {}, tip));
    g.appendChild(r);
  }
  function render(A, B) {
    while (svg.firstChild) svg.removeChild(svg.firstChild);
    var toks = [A, '+', B, '=', B, '+'];
    var f = forward(toks);
    var g = el('g', {}); svg.appendChild(g);
    var pr = el('text', { x: 24, y: 38, 'class': 'mono toy-prompt' }); pr.textContent = A + ' + ' + B + ' = ' + B + ' + ';
    var q = el('tspan', { 'class': 'n-txt' }, '?'); pr.appendChild(q); g.appendChild(pr);
    g.appendChild(el('text', { x: 24, y: 72, 'class': 'sm mut' }, '1 · each token’s learned vector'));
    g.appendChild(el('text', { x: 432, y: 72, 'class': 'sm mut' }, '2 · hidden layer'));
    g.appendChild(el('text', { x: 586, y: 72, 'class': 'sm mut' }, '3 · next-token probabilities'));
    var base = 140;
    toks.forEach(function (t, k) {
      var cx = 30 + k * 64, e = M.E[idx[t]], rare = (t === 'θ');
      for (var d = 0; d < 3; d++) bar(g, cx + d * 13, base, e[d], 30, 10, rare ? 'hl-fill' : 'mut-fill', t + ', dimension ' + (d + 1) + ': ' + fmt(e[d]));
      g.appendChild(el('line', { x1: cx - 3, y1: base, x2: cx + 39, y2: base, 'class': 'rule' }));
      g.appendChild(el('text', { x: cx + 18, y: 208, 'text-anchor': 'middle', 'class': 'mono lbl' + (rare ? ' hl-txt' : '') }, t));
      var c = M.counts[t];
      g.appendChild(el('text', { x: cx + 18, y: 224, 'text-anchor': 'middle', 'class': 'tiny mut' }, c != null ? 'seen ' + c.toLocaleString('en-US') + '×' : 'constant'));
    });
    g.appendChild(el('line', { x1: 404, y1: base, x2: 424, y2: base, 'class': 'ink-line', 'marker-end': 'url(#ta2)' }));
    f.h.forEach(function (v, j) { bar(g, 436 + j * 21, base, v, 46, 14, 'n-fill', 'hidden unit ' + (j + 1) + ': ' + fmt(v)); });
    g.appendChild(el('line', { x1: 432, y1: base, x2: 562, y2: base, 'class': 'rule' }));
    g.appendChild(el('text', { x: 497, y: 208, 'text-anchor': 'middle', 'class': 'tiny mut' }, 'six units, values in (−1, 1)'));
    g.appendChild(el('line', { x1: 566, y1: base, x2: 584, y2: base, 'class': 'ink-line', 'marker-end': 'url(#ta2)' }));
    var order = f.p.map(function (p, k) { return [p, k]; }).sort(function (a, b) { return b[0] - a[0]; }).slice(0, 4);
    var shown = order.map(function (o) { return o[1]; });
    if (shown.indexOf(idx[A]) < 0) { order[3] = [f.p[idx[A]], idx[A]]; }
    order.forEach(function (o, r) {
      var y = 88 + r * 30, tok = M.vocab[o[1]], w = o[0] * 150, best = (r === 0);
      g.appendChild(el('text', { x: 596, y: y + 14, 'text-anchor': 'middle', 'class': 'mono lbl' + (tok === 'θ' ? ' hl-txt' : '') }, tok));
      g.appendChild(el('rect', { x: 608, y: y, width: 150, height: 18, rx: 3, 'class': 'toy-track' }));
      g.appendChild(el('rect', { x: 608, y: y, width: Math.max(w, 1.5), height: 18, rx: 3, 'class': 'n-fill', opacity: best ? 1 : 0.45 }));
      g.appendChild(el('text', { x: 764, y: y + 14, 'class': 'sm' }, (o[0] * 100 < 1 ? '<1' : Math.round(o[0] * 100)) + '%'));
      if (tok === A) g.appendChild(el('rect', { x: 606, y: y - 2, width: 154, height: 22, rx: 4, fill: 'none', stroke: 'var(--symbolic)', 'stroke-width': 1.5, 'stroke-dasharray': '4 3' }));
    });
    var ans = M.vocab[order[0][1]], ok = (ans === A);
    g.appendChild(el('text', { x: 608, y: 222, 'class': 'sm ' + (ok ? 's-txt' : 'n-txt'), 'font-weight': 500 }, 'the network answers “' + ans + '” (' + (ok ? 'right' : 'wrong') + ')'));
    var vA = M.E[idx[A]], vB = M.E[idx[B]];
    g.appendChild(el('text', { x: 24, y: 256, 'class': 'tiny mono mut' }, A + ' = (' + vA.map(fmt).join(', ') + ')    ' + B + ' = (' + vB.map(fmt).join(', ') + ')    + and = learned all-zero vectors'));
    g.appendChild(el('rect', { x: 24, y: 266, width: 752, height: 28, rx: 7, 'class': 's-soft' }));
    var sym = el('text', { x: 38, y: 285, 'class': 'sm' });
    sym.appendChild(el('tspan', { 'class': 'mono' }, 'A + B = B + A'));
    sym.appendChild(el('tspan', {}, '  ⇒  a program gives '));
    sym.appendChild(el('tspan', { 'class': 'mono s-txt', 'font-weight': 500 }, A));
    sym.appendChild(el('tspan', {}, ', whatever the variable is called, and however often it has seen it'));
    g.appendChild(sym);
    var defs = el('defs', {}); var mk = el('marker', { id: 'ta2', viewBox: '0 0 10 10', refX: 8, refY: 5, markerWidth: 7, markerHeight: 7, orient: 'auto-start-reverse' });
    mk.appendChild(el('path', { d: 'M0,0 L10,5 L0,10 z', fill: 'currentColor' })); defs.appendChild(mk); svg.insertBefore(defs, svg.firstChild);
    var pA = Math.round(f.p[idx[A]] * 100);
    var msg;
    if (A === B) msg = 'Both variables are the same here, so any answer that copies it is right.';
    else if (A === 'θ') msg = '<code>θ</code> appeared only ' + M.counts['θ'] + ' times (in 15 examples) in the training data, against roughly 2,000 for each of the others, so its vector barely moved from where training started and sits near zero. The hidden layer sees almost nothing in the first slot and falls back on what is common: the network gives <code>' + ans + '</code> ' + Math.round(order[0][0] * 100) + '%, and the right answer <code>θ</code> only ' + (pA < 1 ? 'under 1' : pA) + '%.';
    else msg = '<code>' + A + '</code> appeared ' + M.counts[A].toLocaleString('en-US') + ' times in training, so it has a well-separated vector, and the network copies it with ' + pA + '% probability' + (B === 'θ' ? '. (The rare <code>θ</code> in the second slot does no harm, since the answer never depends on it.)' : '.');
    out.innerHTML = msg;
  }
  function go() { render(selA.value, selB.value); }
  selA.addEventListener('change', go); selB.addEventListener('change', go);
  document.getElementById('toyAlpha').addEventListener('click', function () { selA.value = 'θ'; selB.value = 'y'; go(); });
  document.getElementById('toyReset').addEventListener('click', function () { selA.value = 'x'; selB.value = 'y'; go(); });
  selA.value = 'x'; selB.value = 'y'; go();
})();
