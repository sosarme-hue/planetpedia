/* Universo: buscador con sugerencias desde 3 letras y simuladores. */
(function () {
  var B = document.body, RAIZ = B.getAttribute('data-raiz') || '', EN = B.getAttribute('data-lang') === 'en';
  var T = EN ? { sin: 'No results for', todo: 'results' } : { sin: 'No hay resultados para', todo: 'resultados' };

  /* ---------- Buscador ---------- */
  var q = document.getElementById('q'), lista = document.getElementById('sug'), datos = null, act = -1, res = [];
  function norm(s) { return (s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, ''); }
  function cargar(cb) {
    if (datos) return cb();
    fetch(RAIZ + 'assets/indice-' + (EN ? 'en' : 'es') + '.json').then(function (r) { return r.json(); }).then(function (d) {
      datos = d.map(function (x) { x.nt = norm(x.t); x.nd = norm(x.d); x.nc = norm(x.c); return x; }); cb();
    }).catch(function () {});
  }
  function puntua(x, t) {
    var palabras = t.split(/\s+/).filter(Boolean), total = 0;
    for (var i = 0; i < palabras.length; i++) {
      var p = palabras[i], s = -1;
      if (x.nt.indexOf(p) === 0) s = 0;
      else if ((' ' + x.nt).indexOf(' ' + p) >= 0) s = 1;
      else if (x.nt.indexOf(p) >= 0) s = 2;
      else if ((' ' + x.nc).indexOf(' ' + p) >= 0 || x.nc.indexOf(p) >= 0) s = 3;
      else if (x.nd.indexOf(p) >= 0) s = 4;
      if (s < 0) return -1;
      total += s;
    }
    return total;
  }
  function marca(txt, t) {
    var i = norm(txt).indexOf(t.split(/\s+/)[0]);
    var esc = function (s) { return s.replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); };
    if (i < 0) return esc(txt);
    var n = t.split(/\s+/)[0].length;
    return esc(txt.slice(0, i)) + '<mark>' + esc(txt.slice(i, i + n)) + '</mark>' + esc(txt.slice(i + n));
  }
  function pinta() {
    var t = norm(q.value.trim());
    if (t.length < 3) { cerrar(); return; }
    cargar(function () {
      res = datos.map(function (x) { return [puntua(x, t), x]; }).filter(function (a) { return a[0] >= 0; })
        .sort(function (a, b) { return a[0] - b[0] || a[1].t.length - b[1].t.length; }).slice(0, 10).map(function (a) { return a[1]; });
      act = -1;
      if (!res.length) { lista.innerHTML = '<li class="vacio">' + T.sin + ' «' + q.value.replace(/</g, '&lt;') + '»</li>'; }
      else lista.innerHTML = res.map(function (x, i) {
        return '<li role="option" id="op' + i + '" data-i="' + i + '"><img src="' + RAIZ + 'img/' + x.f + '.jpg" alt="" loading="lazy"><b>' + marca(x.t, t) + '</b><small>' + x.s + ' · ' + x.d.replace(/</g, '&lt;') + '</small></li>';
      }).join('');
      lista.hidden = false; q.setAttribute('aria-expanded', 'true');
    });
  }
  function cerrar() { lista.hidden = true; q.setAttribute('aria-expanded', 'false'); q.removeAttribute('aria-activedescendant'); act = -1; }
  function ir(i) { if (res[i]) location.href = RAIZ + res[i].u; }
  function mueve(d) {
    if (!res.length) return;
    act = (act + d + res.length) % res.length;
    [].forEach.call(lista.children, function (li, i) { li.setAttribute('aria-selected', i === act ? 'true' : 'false'); });
    q.setAttribute('aria-activedescendant', 'op' + act);
    var el = lista.children[act]; if (el && el.scrollIntoView) el.scrollIntoView({ block: 'nearest' });
  }
  if (q) {
    q.addEventListener('input', pinta);
    q.addEventListener('focus', function () { cargar(function () {}); if (q.value.trim().length >= 3) pinta(); });
    q.addEventListener('keydown', function (ev) {
      if (ev.key === 'ArrowDown') { ev.preventDefault(); mueve(1); }
      else if (ev.key === 'ArrowUp') { ev.preventDefault(); mueve(-1); }
      else if (ev.key === 'Enter') { ev.preventDefault(); ir(act >= 0 ? act : 0); }
      else if (ev.key === 'Escape') cerrar();
    });
    lista.addEventListener('mousedown', function (ev) { var li = ev.target.closest('li[data-i]'); if (li) { ev.preventDefault(); ir(+li.getAttribute('data-i')); } });
    document.addEventListener('click', function (ev) { if (!ev.target.closest('.buscar-mini')) cerrar(); });
  }

  /* ---------- Datos para simuladores ---------- */
  // nombre ES, nombre EN, gravedad (m/s²), periodo orbital (días terrestres), distancia media al Sol (millones de km), diámetro (km), color
  var CUERPOS = [
    ['Sol', 'Sun', 274, 0, 0, 1392700, '#ffcf3a'],
    ['Mercurio', 'Mercury', 3.7, 87.97, 57.9, 4879, '#b9b2a8'],
    ['Venus', 'Venus', 8.87, 224.7, 108.2, 12104, '#e8c98b'],
    ['Tierra', 'Earth', 9.81, 365.25, 149.6, 12742, '#4fa3e0'],
    ['Luna', 'Moon', 1.62, 0, 0, 3474, '#c9c9c9'],
    ['Marte', 'Mars', 3.71, 686.98, 227.9, 6779, '#d9663f'],
    ['Júpiter', 'Jupiter', 24.79, 4332.6, 778.5, 139820, '#d8b48a'],
    ['Saturno', 'Saturn', 10.44, 10759, 1433.5, 116460, '#e7d29c'],
    ['Urano', 'Uranus', 8.69, 30687, 2872.5, 50724, '#9fdfe6'],
    ['Neptuno', 'Neptune', 11.15, 60190, 4495.1, 49244, '#4f7ce8'],
    ['Plutón', 'Pluto', 0.62, 90560, 5906.4, 2377, '#d8c3a5']
  ];
  var nom = function (c) { return EN ? c[1] : c[0]; };
  var fmt = function (n, d) { return n.toLocaleString(EN ? 'en-GB' : 'es-ES', { maximumFractionDigits: d === undefined ? 1 : d }); };
  function el(html) { var d = document.createElement('div'); d.innerHTML = html; return d; }

  var SIMS = {
    peso: function (box) {
      box.innerHTML = '<h3>' + (EN ? 'How much would you weigh?' : '¿Cuánto pesarías?') + '</h3><p class="ayuda">' +
        (EN ? 'Your mass does not change, but the pull of gravity does. Enter your weight on Earth.' : 'Tu masa no cambia, pero la fuerza con que te atrae cada mundo sí. Escribe tu peso en la Tierra.') +
        '</p><div class="fila"><label for="peso-kg">' + (EN ? 'Weight on Earth (kg)' : 'Peso en la Tierra (kg)') + '</label><input id="peso-kg" type="number" min="1" max="500" value="70"></div><div class="res"></div>';
      var inp = box.querySelector('input'), out = box.querySelector('.res');
      function calc() {
        var kg = Math.max(0, +inp.value || 0);
        out.innerHTML = CUERPOS.map(function (c) { return '<div><span>' + nom(c) + '</span><b>' + fmt(kg * c[2] / 9.81) + ' kg</b></div>'; }).join('');
      }
      inp.addEventListener('input', calc); calc();
    },
    edad: function (box) {
      box.innerHTML = '<h3>' + (EN ? 'Your age on other planets' : 'Tu edad en otros planetas') + '</h3><p class="ayuda">' +
        (EN ? 'A "year" is one trip around the Sun. Each planet takes a different time.' : 'Un «año» es una vuelta alrededor del Sol, y cada planeta tarda un tiempo distinto.') +
        '</p><div class="fila"><label for="edad-f">' + (EN ? 'Date of birth' : 'Fecha de nacimiento') + '</label><input id="edad-f" type="date" value="1990-01-01"></div><div class="res"></div>';
      var inp = box.querySelector('input'), out = box.querySelector('.res');
      function calc() {
        var f = new Date(inp.value); if (isNaN(f)) return;
        var dias = (Date.now() - f.getTime()) / 864e5;
        out.innerHTML = CUERPOS.filter(function (c) { return c[3] > 0; }).map(function (c) {
          return '<div><span>' + nom(c) + '</span><b>' + fmt(dias / c[3], dias / c[3] < 10 ? 2 : 1) + '</b><span>' + (EN ? 'years' : 'años') + '</span></div>';
        }).join('');
      }
      inp.addEventListener('input', calc); calc();
    },
    viaje: function (box) {
      var DEST = [
        ['La Luna', 'The Moon', 384400], ['El Sol', 'The Sun', 149.6e6], ['Marte (media)', 'Mars (average)', 225e6],
        ['Júpiter (media)', 'Jupiter (average)', 778e6], ['Plutón (media)', 'Pluto (average)', 5.9e9],
        ['Voyager 1 (2026)', 'Voyager 1 (2026)', 25.4e9], ['Próxima Centauri', 'Proxima Centauri', 4.013e13],
        ['Centro de la Vía Láctea', 'Centre of the Milky Way', 2.47e17], ['Galaxia de Andrómeda', 'Andromeda Galaxy', 2.4e19]];
      var VEL = [['Luz', 'Light', 299792.458 * 3600], ['Sonda Parker (récord)', 'Parker Solar Probe (record)', 692000], ['Voyager 1', 'Voyager 1', 61200],
        ['Avión de línea', 'Airliner', 900], ['Coche por autopista', 'Car on a motorway', 120], ['A pie', 'Walking', 5]];
      box.innerHTML = '<h3>' + (EN ? 'How long would the trip take?' : '¿Cuánto se tarda en llegar?') + '</h3><p class="ayuda">' +
        (EN ? 'Pick a destination and compare travel times at different speeds, without stopping.' : 'Elige un destino y compara cuánto se tardaría a distintas velocidades, sin parar.') +
        '</p><div class="fila"><label for="viaje-d">' + (EN ? 'Destination' : 'Destino') + '</label><select id="viaje-d">' +
        DEST.map(function (d, i) { return '<option value="' + i + '">' + (EN ? d[1] : d[0]) + '</option>'; }).join('') + '</select></div><div class="res"></div>';
      var sel = box.querySelector('select'), out = box.querySelector('.res');
      function dur(h) {
        var a = h / 8766;
        if (h < 1 / 60) return fmt(h * 3600, 1) + ' s';
        if (h < 1) return fmt(h * 60, 1) + ' min';
        if (h < 48) return fmt(h, 1) + (EN ? ' hours' : ' horas');
        if (a < 2) return fmt(h / 24, 0) + (EN ? ' days' : ' días');
        if (a < 1e6) return fmt(a, a < 100 ? 1 : 0) + (EN ? ' years' : ' años');
        return fmt(a / 1e6, 1) + (EN ? ' million years' : ' millones de años');
      }
      function calc() {
        var km = DEST[+sel.value][2];
        out.innerHTML = '<div><span>' + (EN ? 'Distance' : 'Distancia') + '</span><b>' + (km > 1e9 ? fmt(km / 1e9, 1) + (EN ? ' billion km' : ' mil millones de km') : fmt(km / 1e6 >= 1 ? km / 1e6 : km, 1) + (km / 1e6 >= 1 ? (EN ? ' million km' : ' millones de km') : ' km')) + '</b></div>' +
          VEL.map(function (v) { return '<div><span>' + (EN ? v[1] : v[0]) + '</span><b>' + dur(km / v[2]) + '</b></div>'; }).join('');
      }
      sel.addEventListener('change', calc); calc();
    },
    escala: function (box) {
      box.innerHTML = '<h3>' + (EN ? 'The solar system to scale' : 'El sistema solar a escala') + '</h3><p class="ayuda">' +
        (EN ? 'Distances from the Sun, to scale. Slide sideways: the empty space is the real protagonist.' : 'Distancias al Sol, a escala. Desliza de lado: el vacío es el verdadero protagonista.') +
        '</p><div class="fila"><label for="esc-s">' + (EN ? 'If the Sun were a ball of' : 'Si el Sol fuera una bola de') + '</label><select id="esc-s"><option value="0.3">30 cm</option><option value="1" selected>1 m</option><option value="0.05">5 cm</option></select></div><div class="escala"><div class="escala-pista"></div></div><div class="res"></div>';
      var sel = box.querySelector('select'), pista = box.querySelector('.escala-pista'), out = box.querySelector('.res');
      var planetas = CUERPOS.filter(function (c) { return c[4] > 0; });
      pista.style.width = '2400px';
      pista.innerHTML = '<span style="left:8px"><i style="width:14px;height:14px;background:#ffcf3a"></i>' + nom(CUERPOS[0]) + '</span>' + planetas.map(function (c) {
        var x = 8 + c[4] / 5906.4 * 2370, d = Math.max(4, Math.min(16, Math.sqrt(c[5] / 1000) * 1.3));
        return '<span style="left:' + x + 'px"><i style="width:' + d + 'px;height:' + d + 'px;background:' + c[6] + '"></i>' + nom(c) + '</span>';
      }).join('');
      function calc() {
        var sol = +sel.value; // metros
        var k = sol / 1392700; // m por km
        out.innerHTML = planetas.map(function (c) {
          var dist = c[4] * 1e6 * k, tam = c[5] * k * 1000; // dist en m, tam en mm
          return '<div><span>' + nom(c) + '</span><b>' + (dist >= 1000 ? fmt(dist / 1000, 1) + ' km' : fmt(dist, 0) + ' m') + '</b><span>' +
            (EN ? 'size ' : 'tamaño ') + (tam >= 10 ? fmt(tam / 10, 1) + ' cm' : fmt(tam, 1) + ' mm') + '</span></div>';
        }).join('');
      }
      sel.addEventListener('change', calc); calc();
    },
    tamanos: function (box) {
      box.innerHTML = '<h3>' + (EN ? 'Planet sizes compared' : 'Los tamaños comparados') + '</h3><p class="ayuda">' +
        (EN ? 'Diameters to scale. Jupiter would hold 11 Earths across its width.' : 'Diámetros a escala. En el ancho de Júpiter caben 11 Tierras.') + '</p><div class="tamanos"></div><div class="barras"></div>';
      var t = box.querySelector('.tamanos'), b = box.querySelector('.barras');
      var lista = CUERPOS.filter(function (c) { return c[0] !== 'Sol'; });
      t.innerHTML = lista.map(function (c) { var d = Math.max(3, c[5] / 139820 * 150); return '<div><i style="width:' + d + 'px;height:' + d + 'px;background:' + c[6] + '"></i>' + nom(c) + '</div>'; }).join('');
      b.innerHTML = lista.map(function (c) { return '<div class="barra"><span>' + nom(c) + '</span><i style="width:' + (c[5] / 139820 * 100) + '%;background:' + c[6] + '"></i><span>' + fmt(c[5], 0) + ' km</span></div>'; }).join('');
    },
    orbitas: function (box) {
      box.innerHTML = '<h3>' + (EN ? 'Orbits in motion' : 'Las órbitas en movimiento') + '</h3><p class="ayuda">' +
        (EN ? 'Each second is a number of Earth days. Inner planets lap the outer ones again and again.' : 'Cada segundo equivale a varios días terrestres. Los planetas interiores adelantan una y otra vez a los exteriores.') +
        '</p><div class="fila"><label for="orb-v">' + (EN ? 'Speed' : 'Velocidad') + '</label><select id="orb-v"><option value="10">10 ' + (EN ? 'days/s' : 'días/s') + '</option><option value="60" selected>60 ' + (EN ? 'days/s' : 'días/s') + '</option><option value="365">1 ' + (EN ? 'year/s' : 'año/s') + '</option><option value="3650">10 ' + (EN ? 'years/s' : 'años/s') + '</option></select><span class="contador"></span></div><canvas width="700" height="700"></canvas>';
      var cv = box.querySelector('canvas'), ctx = cv.getContext('2d'), sel = box.querySelector('select'), cont = box.querySelector('.contador');
      var pl = CUERPOS.filter(function (c) { return c[3] > 0 && c[0] !== 'Plutón'; }), dias = 0, prev = performance.now(), vis = false;
      function dib(now) {
        var dt = Math.min(0.1, (now - prev) / 1000); prev = now; dias += dt * +sel.value;
        var W = cv.width, c = W / 2; ctx.clearRect(0, 0, W, W);
        ctx.fillStyle = '#ffcf3a'; ctx.beginPath(); ctx.arc(c, c, 10, 0, 6.283); ctx.fill();
        pl.forEach(function (p, i) {
          var r = 30 + i * 40; ctx.strokeStyle = 'rgba(255,255,255,.15)'; ctx.beginPath(); ctx.arc(c, c, r, 0, 6.283); ctx.stroke();
          var a = dias / p[3] * 6.283; ctx.fillStyle = p[6]; ctx.beginPath(); ctx.arc(c + r * Math.cos(a), c - r * Math.sin(a), 4 + Math.sqrt(p[5] / 12742) * 2.5, 0, 6.283); ctx.fill();
          ctx.fillStyle = 'rgba(255,255,255,.7)'; ctx.font = '13px Inter, sans-serif'; ctx.fillText(nom(p), c + r * Math.cos(a) + 9, c - r * Math.sin(a) - 7);
        });
        cont.textContent = (EN ? 'Elapsed: ' : 'Transcurrido: ') + fmt(dias / 365.25, 1) + (EN ? ' years' : ' años');
        if (vis) requestAnimationFrame(dib);
      }
      new IntersectionObserver(function (e) { vis = e[0].isIntersecting; if (vis) { prev = performance.now(); requestAnimationFrame(dib); } }).observe(cv);
    }
  };
  SIMS.magnitud = function (box) {
    var EJ = [[5.1, 'Lorca (2011)', 'Lorca, Spain (2011)'], [6.9, 'Loma Prieta (1989)', 'Loma Prieta (1989)'], [7.8, 'Turquía y Siria (2023)', 'Turkey and Syria (2023)'],
              [8.5, 'Lisboa (1755)', 'Lisbon (1755)'], [9.0, 'Japón (2011)', 'Japan (2011)'], [9.5, 'Chile (1960)', 'Chile (1960)']];
    box.appendChild(el('<label>' + (EN ? 'Magnitude: ' : 'Magnitud: ') + '<b class="mv"></b><input type="range" min="2" max="9.5" step="0.1" value="6"></label><div class="res"></div><div class="barras"></div>'));
    var r = box.querySelector('input'), mv = box.querySelector('.mv'), out = box.querySelector('.res'), bars = box.querySelector('.barras');
    function E(m) { return Math.pow(10, 1.5 * m + 4.8); }
    function pinta() {
      var m = +r.value, j = E(m), tnt = j / 4.184e9, hir = tnt / 15000;
      mv.textContent = fmt(m, 1);
      var tx = tnt >= 1e6 ? fmt(tnt / 1e6, 1) + (EN ? ' million tonnes of TNT' : ' millones de toneladas de TNT') : fmt(tnt, tnt < 10 ? 2 : 0) + (EN ? ' tonnes of TNT' : ' toneladas de TNT');
      out.innerHTML = '<p>' + (EN ? 'Energy released: ' : 'Energía liberada: ') + '<b>' + tx + '</b>' + (hir >= 0.01 ? ' · ' + (EN ? 'about ' : 'unas ') + '<b>' + fmt(hir, hir < 10 ? 1 : 0) + '</b> ' + (fmt(hir, hir < 10 ? 1 : 0) === '1' ? (EN ? 'Hiroshima bomb' : 'bomba de Hiroshima') : (EN ? 'Hiroshima bombs' : 'bombas de Hiroshima')) : '') + '</p><p>' +
        (EN ? 'One point more (' : 'Un punto más (') + fmt(m + 1, 1) + ') = ' + (EN ? '≈ 32 times more energy; two points more = ≈ 1,000 times.' : '≈ 32 veces más energía; dos puntos más = ≈ 1.000 veces.') + '</p>';
      var max = Math.log10(E(9.5));
      bars.innerHTML = EJ.concat([[m, EN ? 'Your choice' : 'Tu elección', EN ? 'Your choice' : 'Tu elección']]).sort(function (a, b) { return a[0] - b[0]; }).map(function (x) {
        var w = Math.max(2, (Math.log10(E(x[0])) - 10) / (max - 10) * 100);
        return '<div class="barra' + (x[1] === (EN ? 'Your choice' : 'Tu elección') ? ' tuya' : '') + '"><span>' + (EN ? x[2] : x[1]) + ' · ' + fmt(x[0], 1) + '</span><i style="width:' + w + '%"></i></div>';
      }).join('') + '<small>' + (EN ? 'Bars on a logarithmic scale.' : 'Barras en escala logarítmica.') + '</small>';
    }
    r.addEventListener('input', pinta); pinta();
  };
  SIMS.reloj = function (box) {
    var EV = [[4540, 'Se forma la Tierra', 'The Earth forms'], [4500, 'Un choque gigante forma la Luna', 'A giant impact forms the Moon'], [4400, 'Primeros océanos', 'First oceans'],
      [3700, 'Primeras señales de vida', 'First signs of life'], [3500, 'Estromatolitos', 'Stromatolites'], [2400, 'Gran Oxidación: llega el oxígeno', 'Great Oxidation: oxygen arrives'],
      [1800, 'Células complejas (eucariotas)', 'Complex cells (eukaryotes)'], [700, 'Tierra bola de nieve', 'Snowball Earth'], [539, 'Explosión cámbrica', 'Cambrian explosion'],
      [470, 'Las plantas colonizan la tierra', 'Plants colonise the land'], [375, 'Los primeros animales salen del agua', 'The first animals leave the water'],
      [252, 'La Gran Mortandad', 'The Great Dying'], [230, 'Primeros dinosaurios', 'First dinosaurs'], [130, 'Primeras flores', 'First flowers'],
      [66, 'Un asteroide extingue a los dinosaurios', 'An asteroid wipes out the dinosaurs'], [7, 'Primeros homininos', 'First hominins'],
      [0.3, 'Aparece Homo sapiens', 'Homo sapiens appears'], [0.012, 'Nace la agricultura', 'Farming begins'], [0.0045, 'Pirámides de Guiza', 'Pyramids of Giza'],
      [0.000534, 'Colón llega a América', 'Columbus reaches America'], [0, 'Hoy', 'Today']];
    var MES = EN ? ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] : ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic'];
    var T0 = Date.UTC(2001, 0, 1), ANIO = 365 * 864e5;
    function fecha(ma) {
      var ms = (4540 - ma) / 4540 * ANIO, d = new Date(T0 + Math.min(ms, ANIO - 1));
      var dia = d.getUTCDate() + ' ' + MES[d.getUTCMonth()];
      if (ma < 30) { var h = d.getUTCHours(), mi = d.getUTCMinutes(), se = d.getUTCSeconds(); dia += ', ' + (h < 10 ? '0' : '') + h + ':' + (mi < 10 ? '0' : '') + mi + ':' + (se < 10 ? '0' : '') + se; }
      return ma === 0 ? (EN ? '31 Dec, midnight' : '31 dic, medianoche') : dia;
    }
    function hace(ma) { return ma === 0 ? '' : ma >= 1 ? fmt(ma, 0) + (EN ? ' million years ago' : ' millones de años') : fmt(ma * 1e6, 0) + (EN ? ' years ago' : ' años'); }
    box.appendChild(el('<p>' + (EN ? 'If the Earth\'s 4.54 billion years were one calendar year, starting on 1 January:' : 'Si los 4.540 millones de años de la Tierra fueran un año del calendario, empezando el 1 de enero:') + '</p><ol class="reloj">' +
      EV.map(function (x) { return '<li><b>' + fecha(x[0]) + '</b><span>' + (EN ? x[2] : x[1]) + '</span><small>' + (x[0] ? (EN ? '' : 'hace ') + hace(x[0]) : '') + '</small></li>'; }).join('') + '</ol>'));
  };
  SIMS.centro = function (box) {
    // [km desde, km hasta, capa es, capa en, T min, T max (°C), descripción es, descripción en]
    var C = [[0, 35, 'Corteza', 'Crust', 15, 500, 'Roca sólida: granito en los continentes, basalto bajo los océanos.', 'Solid rock: granite under continents, basalt under oceans.'],
      [35, 660, 'Manto superior', 'Upper mantle', 500, 1900, 'Roca caliente que fluye muy despacio, como plastilina, y mueve las placas.', 'Hot rock that flows very slowly, like putty, and moves the plates.'],
      [660, 2900, 'Manto inferior', 'Lower mantle', 1900, 3700, 'Roca sólida sometida a presiones enormes.', 'Solid rock under enormous pressure.'],
      [2900, 5150, 'Núcleo externo', 'Outer core', 3700, 5200, 'Hierro y níquel líquidos: sus corrientes crean el campo magnético.', 'Liquid iron and nickel: its currents create the magnetic field.'],
      [5150, 6371, 'Núcleo interno', 'Inner core', 5200, 5400, 'Una bola de hierro sólido tan caliente como la superficie del Sol.', 'A ball of solid iron as hot as the surface of the Sun.']];
    var HITOS = [[3.9, 'Mina más profunda del mundo (Mponeng, Sudáfrica)', 'Deepest mine in the world (Mponeng, South Africa)'],
      [11, 'Profundidad de la fosa de las Marianas', 'Depth of the Mariana Trench'], [12.3, 'Pozo de Kola, el agujero más profundo jamás perforado', 'Kola borehole, the deepest hole ever drilled']];
    box.appendChild(el('<label>' + (EN ? 'Depth: ' : 'Profundidad: ') + '<b class="mv"></b><input type="range" min="0" max="6371" step="1" value="0"></label><div class="corte"><i></i></div><div class="res"></div>'));
    var r = box.querySelector('input'), mv = box.querySelector('.mv'), out = box.querySelector('.res'), mk = box.querySelector('.corte i');
    function pinta() {
      var km = +r.value, c = C.filter(function (x) { return km >= x[0] && km <= x[1]; })[0] || C[4];
      var t = c[4] + (c[5] - c[4]) * (km - c[0]) / (c[1] - c[0]);
      var gpa = km < 35 ? km * 0.03 : km < 2900 ? 1 + (km - 35) / 2865 * 135 : 136 + (km - 2900) / 3471 * 224;
      mv.textContent = fmt(km, 0) + ' km';
      mk.style.left = (km / 6371 * 100) + '%';
      var h = km >= 2 && km <= 20 ? HITOS.reduce(function (a, x) { return Math.abs(x[0] - km) < Math.abs(a[0] - km) ? x : a; }) : null;
      out.innerHTML = '<p><b>' + (EN ? c[3] : c[2]) + '</b> · ' + (EN ? c[7] : c[6]) + '</p><p>' + (EN ? 'Temperature: about ' : 'Temperatura: unos ') + '<b>' + fmt(Math.round(t / 10) * 10, 0) + ' °C</b> · ' +
        (EN ? 'Pressure: about ' : 'Presión: unas ') + '<b>' + fmt(Math.max(1, gpa * 9869), 0) + '</b> ' + (EN ? 'times that at the surface' : 'veces la de la superficie') + '</p>' +
        '<p>' + (EN ? 'Walking non-stop at 5 km/h, you would take ' : 'Caminando sin parar a 5 km/h tardarías ') + '<b>' + fmt(km / 5 / 24, km / 5 / 24 < 10 ? 1 : 0) + (EN ? ' days' : ' días') + '</b>' + (EN ? ' to get here.' : ' en llegar aquí.') + '</p>' +
        (h ? '<p class="hito">' + (EN ? h[2] : h[1]) + ' · ' + fmt(h[0], 1) + ' km</p>' : '');
    }
    r.addEventListener('input', pinta); pinta();
  };
  [].forEach.call(document.querySelectorAll('.sim[data-sim]'), function (box) { var f = SIMS[box.getAttribute('data-sim')]; if (f) f(box); });
  // Vídeos de YouTube: se cargan al pulsar
  document.addEventListener('click', function (ev) {
    var b = ev.target.closest && ev.target.closest('button[data-yt]'); if (!b) return;
    var f = document.createElement('iframe');
    f.src = 'https://www.youtube-nocookie.com/embed/' + encodeURIComponent(b.getAttribute('data-yt')) + '?autoplay=1&rel=0';
    f.title = b.getAttribute('aria-label') || 'YouTube'; f.allow = 'accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture; fullscreen'; f.allowFullscreen = true;
    b.replaceWith(f);
  });
})();
