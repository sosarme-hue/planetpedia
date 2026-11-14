# Genera index.html (español) y en/index.html (inglés).
# Con --preview DEST [es|en] genera la vista previa con imágenes incrustadas.
import base64, html, re, sys, pathlib

ROOT = pathlib.Path(__file__).parent

# (clave, nombre ES, subtítulo ES, nombre EN, subtítulo EN, webs)
# web: (nombre, dominio, descripción ES, descripción EN)
AMBITOS = [
    ("musica", "Música y artes", "Compositores, pintura y cine", "Music and arts", "Composers, painting and film", [
        ("Classicapedia", "classicapedia.com", "Compositores, obras y épocas de la música clásica, explicados para disfrutarla más.", "Composers, works and periods of classical music, explained so you can enjoy it more."),
        ("Pinacopedia", "pinacopedia.com", "Pintores, cuadros y museos: la historia del arte, obra a obra.", "Painters, paintings and museums: art history, one work at a time."),
        ("Cinematopedia", "cinematopedia.com", "Películas, directores y géneros para entender y disfrutar el cine.", "Films, directors and genres to understand and enjoy cinema."),
    ]),
    ("ciencia", "Ciencia y salud", "Del laboratorio a la consulta", "Science and health", "From the lab to the clinic", [
        ("Newtonpedia", "newtonpedia.com", "Física, química y matemáticas contadas con claridad, de las leyes a sus descubridores.", "Physics, chemistry and maths told clearly, from the laws to the people who found them."),
        ("Medicapedia", "medicapedia.org", "Enfermedades, síntomas y tratamientos explicados en lenguaje claro.", "Diseases, symptoms and treatments explained in plain language."),
        ("Farmacos.ai", "farmacos.ai", "Medicamentos: para qué sirven, cómo se toman y qué precauciones tienen.", "Medicines: what they are for, how to take them and what to watch out for."),
        ("Enfermería Sí", "enfermeria.si", "Recursos, técnicas y oposiciones para profesionales y estudiantes de enfermería.", "Resources, techniques and exam preparation for nurses and nursing students."),
    ]),
    ("humanidades", "Humanidades", "Ideas, mitos y símbolos", "Humanities", "Ideas, myths and symbols", [
        ("Filopedia", "filopedia.com", "Filósofos, corrientes y grandes preguntas, de la Antigüedad a hoy.", "Philosophers, schools of thought and big questions, from antiquity to today."),
        ("Mythicapedia", "mythicapedia.com", "Dioses, héroes y leyendas de las mitologías del mundo.", "Gods, heroes and legends from the world's mythologies."),
        ("Zodiacopedia", "zodiacopedia.com", "Signos, planetas y cartas astrales: la astrología como cultura.", "Signs, planets and birth charts: astrology as culture."),
    ]),
    ("educacion", "Educación y sociedad", "Aprender, entender y decidir", "Education and society", "Learn, understand and decide", [
        ("Escolapedia", "escolapedia.com", "Apuntes y guías de estudio para primaria, ESO y bachillerato.", "Notes and study guides for primary and secondary school."),
        ("Leypedia", "leypedia.com", "Leyes, derechos y trámites explicados para cualquier persona.", "Laws, rights and paperwork explained for everyone."),
        ("Saber para Invertir", "saberparainvertir.com", "Finanzas personales e inversión, desde lo básico y sin promesas fáciles.", "Personal finance and investing, from the basics and without easy promises."),
        ("Celebraciones", "celebraciones.org", "Fiestas, tradiciones y fechas señaladas, con su origen y cómo celebrarlas.", "Festivals, traditions and special dates, with their origins and how to celebrate them."),
    ]),
    ("gastronomia", "Gastronomía y vino", "Cocinas y bodegas", "Food and wine", "Kitchens and wineries", [
        ("Culinapedia", "culinapedia.com", "Recetas, ingredientes y técnicas de las cocinas del mundo.", "Recipes, ingredients and techniques from the world's cuisines."),
        ("WorldWinePedia", "worldwinepedia.com", "Uvas, regiones y bodegas para conocer el vino de todo el mundo.", "Grapes, regions and wineries to get to know wine from around the world."),
    ]),
    ("aficiones", "Aficiones y vida cotidiana", "Deporte, juego y compañía", "Hobbies and everyday life", "Sport, games and pets", [
        ("Tenispedia", "tenispedia.com", "Jugadores, torneos y técnica: el tenis en vivo y en su historia.", "Players, tournaments and technique: tennis live and through its history."),
        ("Catdogpedia", "catdogpedia.com", "Razas, salud y cuidados de perros y gatos.", "Breeds, health and care for dogs and cats."),
        ("Ludicopedia", "ludicopedia.com", "Juegos de mesa, de cartas y de ingenio: reglas, historia y estrategia.", "Board, card and puzzle games: rules, history and strategy."),
    ]),
]

# (nombre, dominio, tipo, foto, desc ES, desc EN, autor foto, nombre EN)
GUIAS = [
    ("Sitges", "sitges.si", "municipio", "sitges.jpg", "Playas, la iglesia de la Punta, el Carnaval y la vida del pueblo todo el año.", "Beaches, the church on the Punta, Carnival and town life all year round.", "Howard Walsh", "Sitges"),
    ("Sant Pere de Ribes", "santperederibes.si", "municipio", None, "Viñas, masías y fiestas mayores entre el Garraf y el Penedès.", "Vineyards, farmhouses and town festivals between the Garraf and the Penedès.", None, "Sant Pere de Ribes"),
    ("Castelldefels", "castelldefels.si", "municipio", "castelldefels.jpg", "Del castillo a la playa: qué ver, dónde comer y la agenda local.", "From the castle to the beach: what to see, where to eat and what's on.", "Manuel Torres Garcia", "Castelldefels"),
    ("Vilanova i la Geltrú", "vilanova.si", "municipio", "vilanova.jpg", "Puerto, rambla y museos, con los servicios y la agenda ciudadana.", "Harbour, promenade and museums, plus local services and events.", "Chema Photo", "Vilanova i la Geltrú"),
    ("Sant Cugat", "santcugat.si", "municipio", "santcugat.jpg", "El monasterio, Collserola y una ciudad para vivir y pasear.", "The monastery, Collserola park and a town made for living and walking.", "Manuel Torres Garcia", "Sant Cugat"),
    ("Garraf", "garraf.si", "comarca", "garraf.jpg", "Playas, pueblos y viñas de la comarca, con la guía de cada municipio.", "Beaches, villages and vineyards of the district, with a guide to each town.", "Max", "Garraf"),
    ("Eivissa", "eivissa.si", "isla", "eivissa.jpg", "Dalt Vila, calas, ferris y vida local de Eivissa y Formentera.", "Dalt Vila, coves, ferries and local life on Ibiza and Formentera.", "Alejandra Camacho Álvarez", "Ibiza (Eivissa)"),
]
TIPOS = {"es": {"municipio": "Municipio", "comarca": "Comarca", "isla": "Isla"},
         "en": {"municipio": "Town", "comarca": "District", "isla": "Island"}}

PROXIMAS = ["Badalona", "Cadaqués", "Calafell", "Girona", "Lleida", "Salou", "Tarragona", "Vilafranca"]

# (web, dominio, tipo ES, título ES, tipo EN, título EN)
SELECCION = [
    ("Classicapedia", "classicapedia.com", "Biografía", "Quién fue Bach y por qué sigue siendo el punto de partida", "Biography", "Who Bach was and why he is still the starting point"),
    ("Newtonpedia", "newtonpedia.com", "Ciencia", "La gravedad explicada sin fórmulas", "Science", "Gravity explained without formulas"),
    ("Escolapedia", "escolapedia.com", "Estudio", "Cómo preparar un examen de historia en una semana", "Study", "How to prepare a history exam in one week"),
    ("Sitges Sí", "sitges.si", "Escapada", "Un día en Sitges: de la Punta al paseo marítimo", "Day trip", "A day in Sitges: from the Punta to the seafront"),
]

# Traducción de los textos fijos de la plantilla (la plantilla en español es la maestra).
EN = [
    ('<html lang="es">', '<html lang="en">'),
    ('content="Planetpedia: una red de enciclopedias temáticas y guías locales independientes para aprender, explorar intereses y conocer lugares."',
     'content="Planetpedia: a network of independent encyclopedias and local guides to learn, follow your interests and discover places."'),
    ('aria-label="Planetpedia, inicio"', 'aria-label="Planetpedia, home"'),
    ('aria-label="Principal"', 'aria-label="Main"'),
    ('>Universo</a>', '>Universe</a>'),
    ('>Planeta Tierra</a>', '>Planet Earth</a>'),
    ('>Enciclopedias</a>', '>Encyclopedias</a>'),
    ('>Guías locales</a>', '>Local guides</a>'),
    ('>El proyecto</a>', '>The project</a>'),
    ('<span class="eyebrow">Conocimiento y lugares por descubrir</span>', '<span class="eyebrow">Knowledge and places to discover</span>'),
    ('<h1>Explora tus intereses. <span>Descubre nuevos lugares.</span></h1>', '<h1>Explore your interests. <span>Discover new places.</span></h1>'),
    ('Planetpedia reúne una red de enciclopedias y guías independientes para aprender, seguir tus aficiones y conocer ciudades. Cada web tiene su propio dominio y su propia voz; aquí las encuentras todas.',
     'Planetpedia brings together a network of independent encyclopedias and guides to learn, follow your hobbies and get to know towns and cities. Each site has its own domain and its own voice; here you can find them all. Most sites are in Spanish.'),
    ('<strong>Explorar el conocimiento</strong><small>{{N_ENC}} enciclopedias temáticas</small>', '<strong>Explore knowledge</strong><small>{{N_ENC}} subject encyclopedias</small>'),
    ('<strong>Descubrir destinos</strong><small>{{N_GUIAS}} guías locales</small>', '<strong>Discover destinations</strong><small>{{N_GUIAS}} local guides</small>'),
    ('<label for="q">Buscar en la red</label>', '<label for="q">Search the network</label>'),
    ('placeholder="Busca una web, un tema o un lugar: vino, Sitges…"', 'placeholder="Search for a site, a topic or a place: wine, Sitges…"'),
    ('<span class="contador">Del universo a nuestro entorno</span><h2>Mira al cielo. Vuelve a la Tierra.</h2>', '<span class="contador">From the universe to our surroundings</span><h2>Look up at the sky. Come back to Earth.</h2>'),
    ('<p>Dos áreas propias de Planetpedia para descubrir con imágenes, fichas y recorridos de lectura. Las explicaciones a fondo siguen en las enciclopedias de la red.</p>',
     '<p>Two areas of Planetpedia\'s own, to explore through images, fact sheets and reading paths. In-depth explanations stay in the network\'s encyclopedias.</p>'),
    ('<span class="eyebrow">Sistema solar · Estrellas · Galaxias · Exploración</span>', '<span class="eyebrow">Solar system · Stars · Galaxies · Exploration</span>'),
    ('<h3>Universo</h3>', '<h3>Universe</h3>'),
    ('<p>Mira más allá. Descubre el cosmos, de nuestra estrella a las galaxias más lejanas.</p>', '<p>Look further. Discover the cosmos, from our own star to the most distant galaxies.</p>'),
    ('<span class="ir">Explorar el universo →</span>', '<span class="ir">Explore the universe →</span>'),
    ('<span class="eyebrow">Océanos · Clima · Geología · Ecosistemas</span>', '<span class="eyebrow">Oceans · Climate · Geology · Ecosystems</span>'),
    ('<h3>Planeta Tierra</h3>', '<h3>Planet Earth</h3>'),
    ('<p>Conoce el mundo que habitamos: sus paisajes, sus fuerzas y su vida.</p>', '<p>Get to know the world we live in: its landscapes, its forces and its life.</p>'),
    ('<span class="ir">Explorar la Tierra →</span>', '<span class="ir">Explore the Earth →</span>'),
    ('<p>Por dónde empezar a mirar el cielo.</p>', '<p>Where to start looking at the sky.</p>'),
    ('<strong>Sistema solar</strong><span>El Sol, los ocho planetas y sus lunas, asteroides y cometas.</span>', '<strong>Solar system</strong><span>The Sun, the eight planets and their moons, asteroids and comets.</span>'),
    ('<strong>Estrellas y galaxias</strong><span>Cómo nacen, cambian y mueren las estrellas, y cómo se agrupan en galaxias como la Vía Láctea.</span>', '<strong>Stars and galaxies</strong><span>How stars are born, change and die, and how they gather in galaxies like the Milky Way.</span>'),
    ('<strong>Cosmología</strong><span>El origen y la expansión del universo, contados de forma accesible.</span>', '<strong>Cosmology</strong><span>The origin and expansion of the universe, told in an accessible way.</span>'),
    ('<strong>Exploración espacial</strong><span>Misiones, sondas, telescopios y las personas que las hicieron posibles.</span>', '<strong>Space exploration</strong><span>Missions, probes, telescopes and the people who made them possible.</span>'),
    ('<strong>Observar el cielo</strong><span>Constelaciones, prismáticos y telescopios: una guía para empezar.</span>', '<strong>Stargazing</strong><span>Constellations, binoculars and telescopes: a guide to get started.</span>'),
    ('<strong>Actualidad astronómica</strong><span>Eclipses, lluvias de estrellas y descubrimientos recientes.</span>', '<strong>Astronomy news</strong><span>Eclipses, meteor showers and recent discoveries.</span>'),
    ('Muy pronto en <b>planetpedia.net/universo/</b>', 'Coming soon at <b>planetpedia.net/en/universe/</b>'),
    ('<p>Los procesos que dan forma a nuestro planeta.</p>', '<p>The processes that shape our planet.</p>'),
    ('<strong>La Tierra por dentro</strong><span>Capas del planeta, placas tectónicas, volcanes y terremotos.</span>', '<strong>Inside the Earth</strong><span>The planet\'s layers, tectonic plates, volcanoes and earthquakes.</span>'),
    ('<strong>Océanos y agua</strong><span>Mares, ríos, glaciares y el ciclo del agua.</span>', '<strong>Oceans and water</strong><span>Seas, rivers, glaciers and the water cycle.</span>'),
    ('<strong>Atmósfera y clima</strong><span>El tiempo, los fenómenos meteorológicos y el cambio climático.</span>', '<strong>Atmosphere and climate</strong><span>Weather, extreme events and climate change.</span>'),
    ('<strong>Vida y ecosistemas</strong><span>Biodiversidad, hábitats y relaciones entre especies.</span>', '<strong>Life and ecosystems</strong><span>Biodiversity, habitats and how species interact.</span>'),
    ('<strong>Geografía del mundo</strong><span>Continentes, paisajes y grandes regiones.</span>', '<strong>World geography</strong><span>Continents, landscapes and major regions.</span>'),
    ('<strong>Nuestro impacto</strong><span>Recursos, contaminación y conservación.</span>', '<strong>Our impact</strong><span>Resources, pollution and conservation.</span>'),
    ('Muy pronto en <b>planetpedia.net/tierra/</b>', 'Coming soon at <b>planetpedia.net/en/earth/</b>'),
    ('<span class="contador">{{N_ENC}} webs · 6 ámbitos</span><h2>Conocer un tema</h2>', '<span class="contador">{{N_ENC}} sites · 6 areas</span><h2>Learn about a subject</h2>'),
    ('<p>Enciclopedias temáticas, cada una dedicada a un campo. No todas se llaman «pedia»: lo que las une es que explican bien su tema.</p>',
     '<p>Subject encyclopedias, each devoted to one field. Not all of them are called "pedia": what they share is that they explain their subject well.</p>'),
    ('Ninguna enciclopedia coincide con tu búsqueda.', 'No encyclopedia matches your search.'),
    ('<span class="contador">{{N_GUIAS}} destinos · Catalunya e Illes Balears</span><h2>Descubrir un lugar</h2>', '<span class="contador">{{N_GUIAS}} destinations · Catalonia and the Balearic Islands</span><h2>Discover a place</h2>'),
    ('<p>Guías ciudadanas hechas para quien vive allí y para quien llega: qué ver, dónde comer, agenda y servicios, con información comprobada.</p>',
     '<p>Local guides for people who live there and for visitors: what to see, where to eat, what\'s on and local services, with checked information.</p>'),
    ('<span class="proximas-t">Próximas guías</span>', '<span class="proximas-t">Coming soon</span>'),
    ('Ninguna guía coincide con tu búsqueda.', 'No guide matches your search.'),
    ('<span class="contador">Selección editorial</span><h2>Esta semana en nuestra red</h2>', '<span class="contador">Editor\'s picks</span><h2>This week across the network</h2>'),
    ('<p>Cuatro lecturas elegidas de distintas webs. Cada una te lleva al artículo original.</p>', '<p>Four reads picked from different sites. Each one takes you to the original article.</p>'),
    ('<span class="contador">Sobre el proyecto</span>', '<span class="contador">About the project</span>'),
    ('<p>Planetpedia es el trabajo de una sola persona que ha ido construyendo, web a web, una red de recursos sobre temas muy distintos.</p>',
     '<p>Planetpedia is the work of one person who has built, site by site, a network of resources on very different subjects.</p>'),
    ('<p>Empezó con la curiosidad: la música clásica, el vino, el tenis, la filosofía. Después llegaron las guías locales de Catalunya y de Eivissa. Cada proyecto tiene su dominio y su identidad, y todos comparten la misma idea: explicar las cosas con claridad, citar las fuentes y ser útiles para quien llega buscando algo concreto.</p>',
     '<p>It started with curiosity: classical music, wine, tennis, philosophy. Then came the local guides to Catalonia and Ibiza. Each project has its own domain and identity, and they all share the same idea: explain things clearly, cite sources and be useful to anyone looking for something specific.</p>'),
    ('<p>Una iniciativa de <strong>Alejandro Rosàs Navarro</strong>.</p>', '<p>A project by <strong>Alejandro Rosàs Navarro</strong>.</p>'),
    ('<p>Este portal es la puerta de entrada. Aquí puedes ver todo lo que forma parte de la red y elegir tu camino: aprender o explorar.</p>',
     '<p>This portal is the way in. Here you can see everything in the network and choose your path: learn or explore.</p>'),
    ('<h3 id="contacto-t">Contacto</h3>', '<h3 id="contacto-t">Contact</h3>'),
    ('<p>Sugerencias, correcciones o propuestas de colaboración para cualquiera de las webs de la red:</p>', '<p>Suggestions, corrections or ideas for working together on any site in the network:</p>'),
    ('Copiar dirección', 'Copy address'),
    ('Dirección copiada', 'Address copied'),
    ('<span><strong>Planetpedia</strong> · Conocimiento y lugares por descubrir</span>', '<span><strong>Planetpedia</strong> · Knowledge and places to discover</span>'),
    ('<span>Fotografías de las guías: autores indicados en cada imagen, vía Unsplash.</span>', '<span>Guide photos: photographers credited on each image, via Unsplash.</span>'),
    ("' enciclopedias y '", "' encyclopedias and '"),
    ("' guías coinciden con «'", "' guides match \"'"),
    ("+ '».'", "+ '\".'"),
]


def e(s):
    return html.escape(s, quote=True)


def img_src(name, preview, lang):
    p = ROOT / "img" / name
    if preview:
        return "data:image/jpeg;base64," + base64.b64encode(p.read_bytes()).decode()
    return ("img/" if lang == "es" else "../img/") + name


def build(lang="es", preview=False):
    en = lang == "en"
    n_enc = sum(len(a[5]) for a in AMBITOS)
    enc_html = []
    for key, nom_es, sub_es, nom_en, sub_en, webs in AMBITOS:
        nombre, sub = (nom_en, sub_en) if en else (nom_es, sub_es)
        cards = []
        for n, dom, d_es, d_en in webs:
            desc = d_en if en else d_es
            cards.append(f'''<li class="web" data-search="{e((n + ' ' + dom + ' ' + d_es + ' ' + d_en + ' ' + nom_es + ' ' + nom_en).lower())}">
  <a href="https://{dom}/" class="web-link">
    <span class="mono mono-{key}" aria-hidden="true">{e(n[0])}</span>
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
    for nom_es, dom, tipo, foto, d_es, d_en, autor, nom_en in GUIAS:
        nombre, desc = (nom_en, d_en) if en else (nom_es, d_es)
        if foto:
            media = f'<img src="{img_src(foto, preview, lang)}" alt="{e(nombre)}" loading="lazy" width="400" height="260">'
        else:
            media = f'''<svg viewBox="0 0 400 260" preserveAspectRatio="xMidYMid slice" role="img" aria-label="{'Hills and vineyards' if en else 'Colinas y viñas'}">
  <rect width="400" height="260" fill="#cfe3ea"/>
  <circle cx="300" cy="70" r="28" fill="#f2c14e"/>
  <path d="M0 170 C80 120 160 140 230 150 C300 160 350 120 400 130 V260 H0Z" fill="#6f9a74"/>
  <path d="M0 200 C90 170 180 190 260 195 C320 199 370 180 400 185 V260 H0Z" fill="#4c7a57"/>
  <g stroke="#3a6346" stroke-width="3" stroke-linecap="round" fill="none">
    <path d="M20 240 Q120 215 220 228"/><path d="M40 252 Q150 228 260 240"/><path d="M180 255 Q290 230 390 238"/>
  </g>
  <path d="M90 168 v-18 h22 v18" fill="#e9dcc4"/><path d="M86 152 l15 -12 l15 12z" fill="#b5563b"/>
</svg>'''
        etiqueta = f'<span class="tag tag-{tipo}">{e(TIPOS[lang][tipo])}</span>'
        if en:
            verbo = "Discover" if tipo == "municipio" else "Explore"
            cred = f'<span class="cred">Photo: {e(autor)} / Unsplash</span>' if autor else ''
        else:
            verbo = "Descubre" if tipo == "municipio" else "Explora"
            cred = f'<span class="cred">Foto: {e(autor)} / Unsplash</span>' if autor else ''
        busca = ' '.join([nom_es, nom_en, dom, d_es, d_en, TIPOS['es'][tipo], TIPOS['en'][tipo], 'guía local destino local guide destination'])
        guia_html.append(f'''<li class="guia" data-search="{e(busca.lower())}">
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
    for web, dom, t_es, tit_es, t_en, tit_en in SELECCION:
        tipo, titulo = (t_en, tit_en) if en else (t_es, tit_es)
        sel_html.append(f'''<li class="pieza">
  <a href="https://{dom}/">
    <span class="pieza-tipo">{e(tipo)}</span>
    <span class="pieza-titulo">{e(titulo)}</span>
    <span class="pieza-origen">{'on' if en else 'en'} {e(web)}{' (in Spanish)' if en else ''}</span>
  </a>
</li>''')

    prox_html = "".join(f'<li>{e(n)}</li>' for n in PROXIMAS)
    tpl = (ROOT / "plantilla.html").read_text()
    if en:
        for a, b in EN:
            if a not in tpl:
                raise SystemExit(f"Falta en la plantilla: {a[:70]}")
            tpl = tpl.replace(a, b)
    # Selector de idioma y enlaces hreflang
    if preview:
        cambio = '<span class="idioma" aria-current="true">EN</span>' if en else '<span class="idioma" aria-current="true">ES</span>'
    else:
        cambio = ('<a class="idioma" href="../" hreflang="es" lang="es">ES</a>' if en
                  else '<a class="idioma" href="en/" hreflang="en" lang="en">EN</a>')
    hreflang = ('<link rel="alternate" hreflang="es" href="https://planetpedia.net/">\n'
                '<link rel="alternate" hreflang="en" href="https://planetpedia.net/en/">\n'
                '<link rel="alternate" hreflang="x-default" href="https://planetpedia.net/">')
    out = (tpl.replace("{{ENCICLOPEDIAS}}", "\n".join(enc_html))
              .replace("{{GUIAS}}", "\n".join(guia_html))
              .replace("{{SELECCION}}", "\n".join(sel_html))
              .replace("{{PROXIMAS}}", prox_html)
              .replace("{{N_ENC}}", str(n_enc))
              .replace("{{N_GUIAS}}", str(len(GUIAS)))
              .replace("{{IDIOMA}}", cambio)
              .replace("{{HREFLANG}}", hreflang))
    if preview:
        # El visor de artefactos pone su propio esqueleto: quitamos doctype/html/head/body.
        head = re.search(r"<head>(.*)</head>", out, re.S).group(1)
        body = re.search(r"<body>(.*)</body>", out, re.S).group(1)
        head = "\n".join(l for l in head.splitlines() if "charset" not in l and 'name="viewport"' not in l)
        out = head + body
    return out


if __name__ == "__main__":
    if "--preview" in sys.argv:
        i = sys.argv.index("--preview")
        dest = pathlib.Path(sys.argv[i + 1])
        lang = sys.argv[i + 2] if len(sys.argv) > i + 2 else "es"
        dest.write_text(build(lang, True))
    else:
        (ROOT / "index.html").write_text(build("es"))
        (ROOT / "en").mkdir(exist_ok=True)
        (ROOT / "en" / "index.html").write_text(build("en"))
