/* IApedia: comportamiento común. Sin dependencias. */
(function () {
  "use strict";

  function guardar(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} }
  function leer(k, d) { try { var v = localStorage.getItem(k); return v ? JSON.parse(v) : d; } catch (e) { return d; } }
  function escapar(t) { return String(t).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); }

  // Aviso breve
  var aviso;
  function mostrarAviso(texto) {
    if (!aviso) { aviso = document.createElement("div"); aviso.className = "aviso"; aviso.setAttribute("role", "status"); document.body.appendChild(aviso); }
    aviso.textContent = texto; aviso.hidden = false;
    clearTimeout(mostrarAviso.t);
    mostrarAviso.t = setTimeout(function () { aviso.hidden = true; }, 2600);
  }
  document.addEventListener("click", function (e) {
    var a = e.target.closest("a[data-pronto]");
    if (a) { e.preventDefault(); mostrarAviso("Esta sección está en preparación. ¡Muy pronto!"); }
    var b = e.target.closest("[data-pdf]");
    if (b) { e.preventDefault(); window.print(); }
  });

  // Corrección de tests
  function corregir(form) {
    var preguntas = form.querySelectorAll(".pregunta");
    var aciertos = 0, respondidas = 0;
    preguntas.forEach(function (q) {
      var marcada = q.querySelector("input:checked");
      var explica = q.querySelector(".explica");
      q.classList.remove("bien", "mal");
      if (!marcada) { explica.hidden = true; return; }
      respondidas++;
      var ok = marcada.value === q.dataset.correcta;
      if (ok) aciertos++;
      q.classList.add(ok ? "bien" : "mal");
      explica.textContent = ok ? explica.dataset.bien : explica.dataset.mal;
      explica.hidden = false;
    });
    return { aciertos: aciertos, respondidas: respondidas, total: preguntas.length };
  }
  function enlazarTest(form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var r = corregir(form);
      var res = form.querySelector(".resultado");
      if (r.respondidas < r.total) { res.textContent = "Te faltan " + (r.total - r.respondidas) + " preguntas por responder."; return; }
      var msg = r.aciertos === r.total ? "¡Perfecto! " : r.aciertos >= Math.ceil(r.total * 0.7) ? "¡Muy bien! " : "Vas por buen camino. Repasa las lecciones y vuelve a intentarlo. ";
      res.textContent = msg + "Has acertado " + r.aciertos + " de " + r.total + ".";
      form.dispatchEvent(new CustomEvent("corregido", { detail: r }));
    });
  }
  document.querySelectorAll("form[data-prueba]").forEach(enlazarTest);

  // Vídeos ligeros: YouTube solo se carga al pulsar
  function enlazarVideo(marco) {
    var btn = marco.querySelector("button");
    if (!btn) return;
    btn.addEventListener("click", function () {
      var f = document.createElement("iframe");
      f.src = "https://www.youtube-nocookie.com/embed/" + marco.dataset.video + "?autoplay=1&rel=0";
      f.title = btn.getAttribute("aria-label").replace("Reproducir: ", "");
      f.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture";
      f.allowFullscreen = true;
      marco.innerHTML = ""; marco.appendChild(f);
    });
  }
  document.querySelectorAll(".video-marco[data-video]").forEach(enlazarVideo);

  // Vídeos actuales (lista que el servidor renueva cada día)
  var vivos = document.querySelector("[data-videos-vivos]");
  if (vivos && window.fetch) {
    fetch(vivos.getAttribute("data-src"), { cache: "no-cache" }).then(function (r) { if (!r.ok) throw 0; return r.json(); }).then(function (d) {
      if (!d || !d.videos || !d.videos.length) return;
      var html = d.videos.slice(0, 12).map(function (v) {
        var vis = Number(v.visitas || 0).toLocaleString("es-ES");
        return '<article class="video"><div class="video-marco" data-video="' + escapar(v.id) + '"><img src="https://i.ytimg.com/vi/' + escapar(v.id) + '/hqdefault.jpg" alt="" loading="lazy"><button type="button" aria-label="Reproducir: ' + escapar(v.titulo) + '"></button></div>' +
          '<span class="duracion">' + escapar(v.fecha || "") + '</span><h3>' + escapar(v.titulo) + '</h3><span class="dato">' + escapar(v.canal) + ' · ' + vis + ' visitas</span></article>';
      }).join("");
      var cont = vivos.querySelector(".videos");
      cont.innerHTML = html;
      cont.querySelectorAll(".video-marco[data-video]").forEach(enlazarVideo);
      var est = vivos.querySelector("[data-estado]");
      if (est && d.actualizado) est.textContent = "Actualizado el " + d.actualizado;
    }).catch(function () {});
  }

  // Progreso de los cursos (se guarda solo en este navegador)
  var curso = document.querySelector("[data-curso]");
  if (curso) {
    var clave = "iapedia-curso-" + curso.dataset.curso;
    var hechas = leer(clave, []);
    var botones = curso.querySelectorAll(".hecho");
    var pintar = function () {
      botones.forEach(function (b) {
        var id = b.dataset.leccion, ok = hechas.indexOf(id) !== -1;
        b.setAttribute("aria-pressed", ok ? "true" : "false");
        b.textContent = ok ? "✓ Lección completada" : "Marcar como completada";
        var li = curso.querySelector('.indice li[data-leccion="' + id + '"]');
        if (li) li.classList.toggle("hecha", ok);
      });
      var pct = Math.round(hechas.length / botones.length * 100);
      var barra = curso.querySelector(".barra span"); if (barra) barra.style.width = pct + "%";
      var txt = curso.querySelector(".progreso-txt"); if (txt) txt.textContent = hechas.length + " de " + botones.length + " lecciones";
    };
    botones.forEach(function (b) {
      b.addEventListener("click", function () {
        var id = b.dataset.leccion, i = hechas.indexOf(id);
        if (i === -1) hechas.push(id); else hechas.splice(i, 1);
        guardar(clave, hechas); pintar();
      });
    });
    pintar();
  }

  // Diccionario: filtro por texto
  var filtro = document.querySelector("[data-filtro]");
  if (filtro) {
    var terminos = document.querySelectorAll(".termino");
    var vacio = document.querySelector(".sin-resultados");
    var normal = function (t) { return t.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, ""); };
    filtro.addEventListener("input", function () {
      var q = normal(filtro.value.trim()), n = 0;
      terminos.forEach(function (t) { var ok = !q || normal(t.textContent).indexOf(q) !== -1; t.hidden = !ok; if (ok) n++; });
      if (vacio) vacio.hidden = n !== 0;
    });
  }

  // Línea del tiempo: filtro por etapas
  var chips = document.querySelectorAll("[data-era]");
  if (chips.length) {
    chips.forEach(function (c) {
      c.addEventListener("click", function () {
        chips.forEach(function (o) { o.setAttribute("aria-pressed", o === c ? "true" : "false"); });
        var era = c.dataset.era;
        document.querySelectorAll(".linea [data-etapa]").forEach(function (h) { h.hidden = era !== "todas" && h.dataset.etapa !== era; });
      });
    });
  }

  // Exámenes semanales: cada semana salen preguntas distintas del banco
  var examen = document.querySelector("[data-examen]");
  if (examen) {
    var banco = JSON.parse(document.getElementById("banco").textContent);
    var n = Number(examen.dataset.numero || 15);
    var hoy = new Date();
    var t = new Date(Date.UTC(hoy.getFullYear(), hoy.getMonth(), hoy.getDate()));
    var dia = t.getUTCDay() || 7; t.setUTCDate(t.getUTCDate() + 4 - dia);
    var inicioAno = new Date(Date.UTC(t.getUTCFullYear(), 0, 1));
    var semana = Math.ceil(((t - inicioAno) / 86400000 + 1) / 7);
    var semilla = t.getUTCFullYear() * 100 + semana + Number(examen.dataset.nivel) * 7919;
    var azar = function () { semilla |= 0; semilla = semilla + 0x6D2B79F5 | 0; var x = Math.imul(semilla ^ semilla >>> 15, 1 | semilla); x = x + Math.imul(x ^ x >>> 7, 61 | x) ^ x; return ((x ^ x >>> 14) >>> 0) / 4294967296; };
    var orden = banco.map(function (_, i) { return i; });
    for (var i = orden.length - 1; i > 0; i--) { var j = Math.floor(azar() * (i + 1)); var tmp = orden[i]; orden[i] = orden[j]; orden[j] = tmp; }
    var elegidas = orden.slice(0, n).map(function (i) { return banco[i]; });
    var letras = "abcd";
    var html = elegidas.map(function (p, k) {
      var ops = p.o.map(function (o, m) { return '<label><input type="radio" name="ex-' + k + '" value="' + letras[m] + '"> ' + escapar(o) + '</label>'; }).join("");
      return '<fieldset class="pregunta" data-correcta="' + letras[p.c] + '"><legend>' + (k + 1) + '. ' + escapar(p.q) + '</legend>' + ops +
        '<p class="explica" hidden data-bien="¡Correcto! ' + escapar(p.e) + '" data-mal="La respuesta correcta es «' + escapar(p.o[p.c]) + '». ' + escapar(p.e) + '"></p></fieldset>';
    }).join("");
    var form = examen.querySelector("form");
    form.insertAdjacentHTML("afterbegin", html);
    var etiquetaSemana = examen.querySelector("[data-semana]");
    if (etiquetaSemana) etiquetaSemana.textContent = "Semana " + semana + " de " + t.getUTCFullYear();
    enlazarTest(form);
    form.addEventListener("corregido", function (e) {
      var r = e.detail, cert = examen.querySelector(".certificado-form");
      var aprobado = r.aciertos >= Math.ceil(r.total * 0.7);
      if (cert) cert.hidden = !aprobado;
      examen.dataset.nota = r.aciertos + " de " + r.total;
      if (aprobado) cert.scrollIntoView({ behavior: "smooth", block: "center" });
    });
    var bc = examen.querySelector("[data-generar]");
    if (bc) bc.addEventListener("click", function () {
      var nombre = (examen.querySelector("#nombre-certificado").value || "").trim();
      if (!nombre) { mostrarAviso("Escribe tu nombre para el certificado."); return; }
      var c = document.querySelector(".certificado");
      if (c.parentNode !== document.body) document.body.appendChild(c);
      c.querySelector(".c-nombre").textContent = nombre;
      c.querySelector(".c-nota").textContent = examen.dataset.nota;
      c.querySelector(".c-fecha").textContent = hoy.toLocaleDateString("es-ES", { day: "numeric", month: "long", year: "numeric" });
      document.body.classList.add("imprimiendo-certificado");
      window.print();
      setTimeout(function () { document.body.classList.remove("imprimiendo-certificado"); }, 800);
    });
  }

  // Copiar prompts
  document.addEventListener("click", function (e) {
    var bt = e.target.closest("[data-copiar]");
    if (!bt) return;
    var txt = bt.parentNode.querySelector(".prompt-texto").textContent;
    function hecho() { bt.textContent = "¡Copiado!"; bt.classList.add("copiado"); setTimeout(function () { bt.textContent = "Copiar"; bt.classList.remove("copiado"); }, 1800); }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(txt).then(hecho, function () { copiarViejo(txt); hecho(); });
    } else { copiarViejo(txt); hecho(); }
  });
  function copiarViejo(t) {
    var a = document.createElement("textarea"); a.value = t; a.style.position = "fixed"; a.style.opacity = "0";
    document.body.appendChild(a); a.select(); try { document.execCommand("copy"); } catch (e) {} document.body.removeChild(a);
  }

  // Comparador de asistentes
  var comp = document.querySelector("[data-comparador]");
  if (comp) {
    var datos = JSON.parse(document.getElementById("datos-comparador").textContent);
    var caja = document.querySelector("[data-recomendacion]");
    comp.addEventListener("change", function () {
      var marcadas = [].map.call(comp.querySelectorAll("input:checked"), function (i) { return i.value; });
      document.querySelectorAll(".tabla-comparador tr[data-nec]").forEach(function (tr) { tr.classList.toggle("marcada", marcadas.indexOf(tr.dataset.nec) >= 0); });
      if (!marcadas.length) { caja.innerHTML = '<p class="dato">Marca al menos una opción y te diremos qué asistente encaja mejor.</p>'; return; }
      var pts = {};
      Object.keys(datos.asis).forEach(function (k) { pts[k] = 0; });
      marcadas.forEach(function (n) { var p = datos.nec[n]; Object.keys(p).forEach(function (k) { pts[k] += p[k]; }); });
      var orden = Object.keys(pts).sort(function (a, b) { return pts[b] - pts[a]; }).filter(function (k) { return pts[k] > 0; }).slice(0, 3);
      if (!orden.length) { caja.innerHTML = '<p class="dato">Ningún asistente destaca en eso.</p>'; return; }
      var base = document.querySelector("link[rel=stylesheet]").getAttribute("href").replace(/assets\/estilo\.css.*$/, "");
      caja.innerHTML = '<h2>Te recomendamos</h2><ol class="podio">' + orden.map(function (k, i) {
        var a = datos.asis[k], guia = base + "guias/" + k + "/" + (location.protocol === "file:" || /index\.html$/.test(location.pathname) ? "index.html" : "");
        return '<li><img class="logo-ia" src="' + base + 'assets/logos/' + k + '.svg" alt="" width="40" height="40"><div><strong>' + (i + 1) + '. ' + escapar(a.n) + '</strong><span class="dato">' + (i === 0 ? "La mejor opción para lo que buscas" : "También encaja") + '</span></div><a href="' + guia + '">Guía</a><a href="https://' + a.w + '" target="_blank" rel="noopener">Abrir ↗</a></li>';
      }).join("") + "</ol>";
    });
  }

  // Test «¿Qué asistente es para ti?»
  var testA = document.querySelector("[data-test-asistente]");
  if (testA) {
    var res = document.querySelector("[data-resultado]");
    function mostrar(gan, seg) {
      res.hidden = false; testA.hidden = true;
      res.querySelectorAll("[data-r]").forEach(function (d) { d.hidden = d.dataset.r !== gan; });
      var s2 = res.querySelector("[data-segundo]");
      var nombre2 = seg ? res.querySelector('[data-r="' + seg + '"] h3') : null;
      s2.textContent = nombre2 ? "Segunda opción: " + nombre2.textContent + "." : "";
      res.dataset.gan = gan;
      try { history.replaceState(null, "", "#resultado=" + gan); } catch (e) {}
      res.scrollIntoView({ behavior: "smooth", block: "start" });
    }
    testA.addEventListener("submit", function (e) {
      e.preventDefault();
      var pts = {};
      testA.querySelectorAll("input:checked").forEach(function (i) { var p = JSON.parse(i.value); Object.keys(p).forEach(function (k) { pts[k] = (pts[k] || 0) + p[k]; }); });
      var orden = Object.keys(pts).sort(function (a, b) { return pts[b] - pts[a]; });
      mostrar(orden[0], orden[1]);
    });
    var m = location.hash.match(/resultado=([a-z-]+)/);
    if (m && res.querySelector('[data-r="' + m[1] + '"]')) mostrar(m[1]);
    res.querySelector("[data-repetir]").addEventListener("click", function () {
      testA.reset(); testA.hidden = false; res.hidden = true;
      try { history.replaceState(null, "", location.pathname); } catch (e) {}
      testA.scrollIntoView({ behavior: "smooth" });
    });
    res.querySelector("[data-compartir]").addEventListener("click", function () {
      var nombre = res.querySelector('[data-r="' + res.dataset.gan + '"] h3').textContent;
      var url = location.href, texto = "Según el test de IApedia, mi asistente de IA ideal es " + nombre + ". ¿Y el tuyo?";
      var aviso2 = res.querySelector("[data-compartido]");
      if (navigator.share) { navigator.share({ title: "¿Qué asistente de IA es para ti?", text: texto, url: url }).catch(function () {}); }
      else if (navigator.clipboard) { navigator.clipboard.writeText(texto + " " + url).then(function () { aviso2.textContent = "Enlace copiado. Pégalo donde quieras compartirlo."; }); }
      else { aviso2.textContent = texto + " " + url; }
    });
  }


})();

// Menú desplegable en el móvil
(function () {
  var top = document.querySelector(".top"), boton = document.querySelector(".menu-boton");
  if (!top || !boton) return;
  document.documentElement.classList.add("con-js");
  var poner = function (abierto) {
    top.classList.toggle("abierto", abierto);
    boton.setAttribute("aria-expanded", abierto ? "true" : "false");
    boton.setAttribute("aria-label", abierto ? "Cerrar el menú" : "Abrir el menú");
  };
  boton.addEventListener("click", function () { poner(!top.classList.contains("abierto")); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape" && top.classList.contains("abierto")) { poner(false); boton.focus(); } });
  document.addEventListener("click", function (e) { if (top.classList.contains("abierto") && !top.contains(e.target)) poner(false); });
  top.querySelectorAll(".nav a").forEach(function (a) { a.addEventListener("click", function () { poner(false); }); });
})();

// Buscador de fichas de Quién es quién
(function () {
  var input = document.querySelector("[data-buscar-fichas]");
  if (!input) return;
  var quitar = function (t) { return t.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, ""); };
  var fichas = [].slice.call(document.querySelectorAll(".ficha-enlace"));
  var grupos = [].slice.call(document.querySelectorAll(".persona-grupo"));
  var vacio = document.querySelector("[data-sin-resultados]");
  input.addEventListener("input", function () {
    var q = quitar(input.value.trim()), hay = 0;
    fichas.forEach(function (f) { var ok = !q || quitar(f.textContent).indexOf(q) !== -1; f.hidden = !ok; if (ok) hay++; });
    grupos.forEach(function (g) { g.hidden = !g.querySelector(".ficha-enlace:not([hidden])"); });
    vacio.hidden = hay > 0;
  });
})();
