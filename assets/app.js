/* IApedia: comportamiento común (avisos de secciones en preparación, pruebas tipo test y vídeos ligeros). */
(function () {
  "use strict";

  // Enlaces a secciones que aún no existen: aviso en lugar de error 404.
  var aviso;
  function mostrarAviso(texto) {
    if (!aviso) {
      aviso = document.createElement("div");
      aviso.className = "aviso";
      aviso.setAttribute("role", "status");
      document.body.appendChild(aviso);
    }
    aviso.textContent = texto;
    aviso.hidden = false;
    clearTimeout(mostrarAviso.t);
    mostrarAviso.t = setTimeout(function () { aviso.hidden = true; }, 2600);
  }
  document.addEventListener("click", function (e) {
    var a = e.target.closest("a[data-pronto]");
    if (!a) return;
    e.preventDefault();
    mostrarAviso("Esta sección está en preparación. ¡Muy pronto!");
  });

  // Pruebas tipo test: corrige, explica y da la nota.
  document.querySelectorAll("form[data-prueba]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
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
      var res = form.querySelector(".resultado");
      if (respondidas < preguntas.length) {
        res.textContent = "Te faltan " + (preguntas.length - respondidas) + " por responder.";
        return;
      }
      var total = preguntas.length;
      var msg = aciertos === total ? "¡Perfecto! " : aciertos >= Math.ceil(total * 0.7) ? "¡Muy bien! " : "Vas por buen camino. ";
      res.textContent = msg + "Has acertado " + aciertos + " de " + total + ".";
    });
  });

  // Vídeos: solo se carga YouTube cuando se pulsa (más rápido y sin cookies hasta entonces).
  document.querySelectorAll(".video-marco[data-video]").forEach(function (marco) {
    var btn = marco.querySelector("button");
    if (!btn) return;
    btn.addEventListener("click", function () {
      var f = document.createElement("iframe");
      f.src = "https://www.youtube-nocookie.com/embed/" + marco.dataset.video + "?autoplay=1&rel=0";
      f.title = btn.getAttribute("aria-label").replace("Reproducir: ", "");
      f.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture";
      f.allowFullscreen = true;
      marco.innerHTML = "";
      marco.appendChild(f);
    });
  });
})();
