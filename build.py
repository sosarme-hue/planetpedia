# Genera index.html (web real) y, con --preview, la vista previa con imágenes incrustadas.
import base64, html, sys, pathlib

ROOT = pathlib.Path(__file__).parent

AMBITOS = [
    ("musica", "Música y artes", "Compositores, pintura y cine", [
        ("Classicapedia", "classicapedia.com", "Compositores, obras y épocas de la música clásica, explicados para disfrutarla más."),
        ("Pinacopedia", "pinacopedia.com", "Pintores, cuadros y museos: la historia del arte, obra a obra."),
        ("Cinematopedia", "cinematopedia.com", "Películas, directores y géneros para entender y disfrutar el cine."),
    ]),
    ("ciencia", "Ciencia y salud", "Del laboratorio a la consulta", [
        ("Newtonpedia", "newtonpedia.com", "Física, química y matemáticas contadas con claridad, de las leyes a sus descubridores."),
        ("Medicapedia", "medicapedia.org", "Enfermedades, síntomas y tratamientos explicados en lenguaje claro."),
        ("Farmacos.ai", "farmacos.ai", "Medicamentos: para qué sirven, cómo se toman y qué precauciones tienen."),
        ("Enfermería Sí", "enfermeria.si", "Recursos, técnicas y oposiciones para profesionales y estudiantes de enfermería."),
    ]),
    ("humanidades", "Humanidades", "Ideas, mitos y símbolos", [
        ("Filopedia", "filopedia.com", "Filósofos, corrientes y grandes preguntas, de la Antigüedad a hoy."),
        ("Mythicapedia", "mythicapedia.com", "Dioses, héroes y leyendas de las mitologías del mundo."),
        ("Zodiacopedia", "zodiacopedia.com", "Signos, planetas y cartas astrales: la astrología como cultura."),
    ]),
    ("educacion", "Educación y sociedad", "Aprender, entender y decidir", [
        ("Escolapedia", "escolapedia.com", "Apuntes y guías de estudio para primaria, ESO y bachillerato."),
        ("Leypedia", "leypedia.com", "Leyes, derechos y trámites explicados para cualquier persona."),
        ("Saber para Invertir", "saberparainvertir.com", "Finanzas personales e inversión, desde lo básico y sin promesas fáciles."),
        ("Celebraciones", "celebraciones.org", "Fiestas, tradiciones y fechas señaladas, con su origen y cómo celebrarlas."),
    ]),
    ("gastronomia", "Gastronomía y vino", "Cocinas y bodegas", [
        ("Culinapedia", "culinapedia.com", "Recetas, ingredientes y técnicas de las cocinas del mundo."),
        ("WorldWinePedia", "worldwinepedia.com", "Uvas, regiones y bodegas para conocer el vino de todo el mundo."),
    ]),
    ("aficiones", "Aficiones y vida cotidiana", "Deporte, juego y compañía", [
        ("Tenispedia", "tenispedia.com", "Jugadores, torneos y técnica: el tenis en vivo y en su historia."),
        ("Catdogpedia", "catdogpedia.com", "Razas, salud y cuidados de perros y gatos."),
        ("Ludicopedia", "ludicopedia.com", "Juegos de mesa, de cartas y de ingenio: reglas, historia y estrategia."),
    ]),
]

GUIAS = [
    ("Sitges", "sitges.si", "Municipio", "sitges.jpg", "Playas, la iglesia de la Punta, el Carnaval y la vida del pueblo todo el año.", "Howard Walsh"),
    ("Sant Pere de Ribes", "santperederibes.si", "Municipio", None, "Viñas, masías y fiestas mayores entre el Garraf y el Penedès.", None),
    ("Castelldefels", "castelldefels.si", "Municipio", "castelldefels.jpg", "Del castillo a la playa: qué ver, dónde comer y la agenda local.", "Manuel Torres Garcia"),
    ("Vilanova i la Geltrú", "vilanova.si", "Municipio", "vilanova.jpg", "Puerto, rambla y museos, con los servicios y la agenda ciudadana.", "Chema Photo"),
    ("Sant Cugat", "santcugat.si", "Municipio", "santcugat.jpg", "El monasterio, Collserola y una ciudad para vivir y pasear.", "Manuel Torres Garcia"),
    ("Garraf", "garraf.si", "Comarca", "garraf.jpg", "Playas, pueblos y viñas de la comarca, con la guía de cada municipio.", "Max"),
    ("Eivissa", "eivissa.si", "Isla", "eivissa.jpg", "Dalt Vila, calas, ferris y vida local de Eivissa y Formentera.", "Alejandra Camacho Álvarez"),
]

PROXIMAS = ["Badalona", "Cadaqués", "Calafell", "Girona", "Lleida", "Salou", "Tarragona", "Vilafranca"]

SELECCION = [
    ("Classicapedia", "classicapedia.com", "Biografía", "Quién fue Bach y por qué sigue siendo el punto de partida"),
    ("Newtonpedia", "newtonpedia.com", "Ciencia", "La gravedad explicada sin fórmulas"),
    ("Escolapedia", "escolapedia.com", "Estudio", "Cómo preparar un examen de historia en una semana"),
    ("Sitges Sí", "sitges.si", "Escapada", "Un día en Sitges: de la Punta al paseo marítimo"),
]


def e(s):
    return html.escape(s, quote=True)


def img_src(name, preview):
    p = ROOT / "img" / name
    if preview:
        return "data:image/jpeg;base64," + base64.b64encode(p.read_bytes()).decode()
    return "img/" + name


def build(preview=False):
    n_enc = sum(len(a[3]) for a in AMBITOS)
    enc_html = []
    for key, nombre, sub, webs in AMBITOS:
        cards = []
        for n, dom, desc in webs:
            ini = n[0]
            cards.append(f'''<li class="web" data-search="{e((n + ' ' + dom + ' ' + desc + ' ' + nombre).lower())}">
  <a href="https://{dom}/" class="web-link">
    <span class="mono mono-{key}" aria-hidden="true">{e(ini)}</span>
    <span class="web-body">
      <span class="web-name">{e(n)}</span>
      <span class="web-desc">{e(desc)}</span>
      <span class="web-dom">{e(dom)} <span aria-hidden="true">↗</span></span>
    </span>
  </a>
</li>''')
        enc_html.append(f'''<section class="ambito" aria-labelledby="amb-{key}">
  <header class="ambito-head">
    <h3 id="amb-{key}"><span class="dot dot-{key}" aria-hidden="true"></span>{e(nombre)}</h3>
    <p>{e(sub)}</p>
  </header>
  <ul class="webs">{''.join(cards)}</ul>
</section>''')

    guia_html = []
    for nombre, dom, tipo, foto, desc, autor in GUIAS:
        if foto:
            media = f'<img src="{img_src(foto, preview)}" alt="{e(nombre)}" loading="lazy" width="400" height="260">'
        else:
            media = '''<svg viewBox="0 0 400 260" preserveAspectRatio="xMidYMid slice" role="img" aria-label="Colinas y viñas">
  <rect width="400" height="260" fill="#cfe3ea"/>
  <circle cx="300" cy="70" r="28" fill="#f2c14e"/>
  <path d="M0 170 C80 120 160 140 230 150 C300 160 350 120 400 130 V260 H0Z" fill="#6f9a74"/>
  <path d="M0 200 C90 170 180 190 260 195 C320 199 370 180 400 185 V260 H0Z" fill="#4c7a57"/>
  <g stroke="#3a6346" stroke-width="3" stroke-linecap="round" fill="none">
    <path d="M20 240 Q120 215 220 228"/><path d="M40 252 Q150 228 260 240"/><path d="M180 255 Q290 230 390 238"/>
  </g>
  <path d="M90 168 v-18 h22 v18" fill="#e9dcc4"/><path d="M86 152 l15 -12 l15 12z" fill="#b5563b"/>
</svg>'''
        etiqueta = f'<span class="tag tag-{tipo.lower()}">{e(tipo)}</span>'
        verbo = "Explora" if tipo != "Municipio" else "Descubre"
        cred = f'<span class="cred">Foto: {e(autor)} / Unsplash</span>' if autor else ''
        guia_html.append(f'''<li class="guia" data-search="{e((nombre + ' ' + dom + ' ' + desc + ' ' + tipo + ' guía local destino').lower())}">
  <a href="https://{dom}/">
    <span class="guia-media">{media}{etiqueta}{cred}</span>
    <span class="guia-body">
      <span class="guia-kicker">{verbo}</span>
      <span class="guia-name">{e(nombre)}</span>
      <span class="guia-desc">{e(desc)}</span>
      <span class="guia-dom">{e(dom)}</span>
    </span>
  </a>
</li>''')

    sel_html = []
    for web, dom, tipo, titulo in SELECCION:
        sel_html.append(f'''<li class="pieza">
  <a href="https://{dom}/">
    <span class="pieza-tipo">{e(tipo)}</span>
    <span class="pieza-titulo">{e(titulo)}</span>
    <span class="pieza-origen">en {e(web)}</span>
  </a>
</li>''')

    prox_html = "".join(f'<li>{e(n)}</li>' for n in PROXIMAS)
    tpl = (ROOT / "plantilla.html").read_text()
    out = (tpl.replace("{{ENCICLOPEDIAS}}", "\n".join(enc_html))
              .replace("{{GUIAS}}", "\n".join(guia_html))
              .replace("{{SELECCION}}", "\n".join(sel_html))
              .replace("{{PROXIMAS}}", prox_html)
              .replace("{{N_ENC}}", str(n_enc))
              .replace("{{N_GUIAS}}", str(len(GUIAS))))
    if preview:
        # El visor de artefactos pone su propio esqueleto: quitamos doctype/html/head/body.
        import re
        head = re.search(r"<head>(.*)</head>", out, re.S).group(1)
        body = re.search(r"<body>(.*)</body>", out, re.S).group(1)
        head = "\n".join(l for l in head.splitlines() if "charset" not in l and 'name="viewport"' not in l)
        out = head + body
    return out


if __name__ == "__main__":
    if "--preview" in sys.argv:
        dest = pathlib.Path(sys.argv[sys.argv.index("--preview") + 1])
        dest.write_text(build(True))
    else:
        (ROOT / "index.html").write_text(build(False))
