# Genera la sección Universo (castellano en /universo/, inglés en /en/universe/),
# el índice de búsqueda, el sitemap y robots.txt.
# Uso: python3 build_universo.py
import html, json, re, sys, pathlib, importlib

ROOT = pathlib.Path(__file__).parent
sys.path.insert(0, str(ROOT / "contenido"))
DOM = "https://planetpedia.net"
CRED = json.loads((ROOT / "img/universo/creditos.json").read_text())

ORDEN = ["sistema_solar", "estrellas", "galaxias", "cosmologia", "exploracion", "observar", "curiosidades"]
SECCIONES = [importlib.import_module("universo." + m) for m in ORDEN]

L = {
    "es": dict(base="universo", inicio="Inicio", uni="Universo", fichas="fichas", datos="Ficha técnica",
               indice="En esta página", relacionadas="Más en", anterior="Anterior", siguiente="Siguiente",
               foto="Foto", sabias="¿Sabías que…?", buscar="Busca en el Universo: Saturno, agujero negro, eclipse…",
               buscar_lbl="Buscar en Universo", sin="No hay resultados para", otras="Ver la sección",
               lede="Una enciclopedia del cosmos: del Sol a las galaxias más lejanas, con fotos reales de telescopios y sondas, cifras, curiosidades y simuladores.",
               h1="Universo", eyebrow="Enciclopedia del cosmos", secciones="Secciones",
               creditos="Fotografías de Wikimedia Commons (NASA, ESA, ESO y otros autores), con su licencia en cada imagen.",
               leer="Leer", cifras="Cifras para empezar", otro="English", otro_lbl="Read in English",
               actualizado="Actualizado", pie="Planetpedia · Conocimiento y lugares por descubrir",
               volver="Volver a Planetpedia"),
    "en": dict(base="en/universe", inicio="Home", uni="Universe", fichas="articles", datos="Key facts",
               indice="On this page", relacionadas="More in", anterior="Previous", siguiente="Next",
               foto="Photo", sabias="Did you know?", buscar="Search the Universe: Saturn, black hole, eclipse…",
               buscar_lbl="Search the Universe", sin="No results for", otras="Open the section",
               lede="An encyclopedia of the cosmos: from the Sun to the most distant galaxies, with real images from telescopes and probes, figures, curiosities and simulators.",
               h1="Universe", eyebrow="Encyclopedia of the cosmos", secciones="Sections",
               creditos="Photographs from Wikimedia Commons (NASA, ESA, ESO and other authors), with each image's licence.",
               leer="Read", cifras="Numbers to start with", otro="Español", otro_lbl="Leer en español",
               actualizado="Updated", pie="Planetpedia · Knowledge and places to discover",
               volver="Back to Planetpedia"),
}
FECHA = "2026-11-14"
i = lambda lang: 0 if lang == "es" else 1
e = lambda s: html.escape(s, quote=True)


def ruta(lang, sec=None, ficha=None):
    p = L[lang]["base"] + "/"
    if sec: p += sec.SLUG[i(lang)] + "/"
    if ficha: p += ficha["slug"][i(lang)] + "/"
    return p


def rel(desde, hasta):
    """Ruta relativa entre dos rutas de carpeta del sitio (terminadas en /)."""
    n = desde.count("/")
    return "../" * n + hasta


TODAS = {}
FALTAN = set()
for s in SECCIONES:
    for f in s.FICHAS:
        TODAS[f["slug"][0]] = (s, f)


def inline(t, lang, aqui):
    t = e(t).replace("\\*", "&#42;")
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?!\w)", r"<em>\1</em>", t)
    def enlace(m):
        txt, dest = m.group(1), m.group(2)
        if dest.startswith("@"):
            if dest[1:] not in TODAS:
                FALTAN.add(dest[1:]); return txt
            s, f = TODAS[dest[1:]]
            return f'<a href="{rel(aqui, ruta(lang, s, f))}">{txt}</a>'
        if dest.startswith("#"):
            s = next(x for x in SECCIONES if x.SLUG[0] == dest[1:])
            return f'<a href="{rel(aqui, ruta(lang, s))}">{txt}</a>'
        return f'<a href="{dest}" rel="noopener">{txt}</a>'
    return re.sub(r"\[(.+?)\]\((.+?)\)", enlace, t)


def figura(clave, pie, lang, aqui, clase="", eager=False):
    c = CRED[clave]
    autor = re.sub(r"\s*\(.*?\)\s*$", "", c["autor"])[:90]
    lic = c["licencia"].replace("Public domain", "Dominio público" if lang == "es" else "Public domain")
    src = rel(aqui, f"img/universo/{clave}.jpg")
    carga = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    return (f'<figure class="fig {clase}"><img src="{src}" alt="{e(pie)}" width="{c["w"]}" height="{c["h"]}" {carga}>'
            f'<figcaption>{inline(pie, lang, aqui)} <span class="cred">{L[lang]["foto"]}: {e(autor)} · '
            f'<a href="{e(c["url"])}" rel="noopener">{e(lic)}</a></span></figcaption></figure>')


def cuerpo(md, lang, aqui):
    out, toc, lista, n = [], [], [], 0
    def cierra():
        if lista:
            out.append("<ul>" + "".join(f"<li>{x}</li>" for x in lista) + "</ul>"); lista.clear()
    for bloque in re.split(r"\n\s*\n", md.strip()):
        b = bloque.strip()
        if not b: continue
        lineas = b.splitlines()
        if all(l.strip().startswith("- ") for l in lineas):
            cierra(); out.append("<ul>" + "".join(f"<li>{inline(l.strip()[2:], lang, aqui)}</li>" for l in lineas) + "</ul>"); continue
        if b.startswith("## "):
            n += 1; ancla = f"s{n}"; tit = b[3:].strip()
            toc.append((ancla, tit)); out.append(f'<h2 id="{ancla}">{inline(tit, lang, aqui)}</h2>'); continue
        if b.startswith("### "):
            out.append(f"<h3>{inline(b[4:].strip(), lang, aqui)}</h3>"); continue
        if b.startswith("!foto "):
            for l in lineas:
                cl, _, pie = l[6:].partition("|")
                out.append(figura(cl.strip(), pie.strip(), lang, aqui))
            continue
        if b.startswith("!sim "):
            out.append(f'<div class="sim" data-sim="{e(b[5:].strip())}"></div>'); continue
        if b.startswith("> "):
            out.append(f'<aside class="sabias"><b>{L[lang]["sabias"]}</b><p>{inline(" ".join(l[2:] for l in lineas), lang, aqui)}</p></aside>'); continue
        if b.startswith("|"):
            filas = [[c.strip() for c in l.strip().strip("|").split("|")] for l in lineas if not re.match(r"^\|[\s\-|]+\|$", l.strip())]
            th = "".join(f"<th>{inline(c, lang, aqui)}</th>" for c in filas[0])
            tb = "".join("<tr>" + "".join(f"<td>{inline(c, lang, aqui)}</td>" for c in r) + "</tr>" for r in filas[1:])
            out.append(f'<div class="tabla"><table><thead><tr>{th}</tr></thead><tbody>{tb}</tbody></table></div>'); continue
        out.append(f"<p>{inline(' '.join(l.strip() for l in lineas), lang, aqui)}</p>")
    cierra()
    return "\n".join(out), toc


LOGO = '''<svg viewBox="0 0 40 40" aria-hidden="true"><circle cx="20" cy="20" r="11" fill="#ffffff"/><path d="M13 16c4-1 9 0 14 3M12 22c5 1 10 2 15 0" stroke="#0d2b55" stroke-width="1.6" fill="none" stroke-linecap="round" opacity=".35"/><ellipse cx="20" cy="20" rx="18" ry="6.5" fill="none" stroke="#2ec4c4" stroke-width="2.4" transform="rotate(-22 20 20)"/><circle cx="35.5" cy="13.5" r="2.4" fill="#2ec4c4"/></svg>'''


def pagina(lang, aqui, otra, titulo, desc, claves, contenido, migas, og_img=None, ld=None):
    t = L[lang]
    home = rel(aqui, "" if lang == "es" else "en/")
    ld_all = [{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": n + 1, "name": nom, "item": DOM + "/" + u} for n, (nom, u) in enumerate(migas)]}]
    if ld: ld_all.append(ld)
    og = f'<meta property="og:image" content="{DOM}/img/universo/{og_img}.jpg">' if og_img else ""
    migas_html = " <span aria-hidden=\"true\">›</span> ".join(
        f'<a href="{rel(aqui, u)}">{e(nom)}</a>' if k < len(migas) - 1 else f'<span aria-current="page">{e(nom)}</span>'
        for k, (nom, u) in enumerate(migas))
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{e(titulo)}</title>
<meta name="description" content="{e(desc)}">
<meta name="keywords" content="{e(claves)}">
<link rel="canonical" href="{DOM}/{aqui}">
<link rel="alternate" hreflang="{lang}" href="{DOM}/{aqui}">
<link rel="alternate" hreflang="{'en' if lang == 'es' else 'es'}" href="{DOM}/{otra}">
<link rel="alternate" hreflang="x-default" href="{DOM}/{aqui if lang == 'es' else otra}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Planetpedia">
<meta property="og:title" content="{e(titulo)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{DOM}/{aqui}">
<meta property="og:locale" content="{'es_ES' if lang == 'es' else 'en_GB'}">
{og}
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@500;700;800&family=Inter:wght@400;500;600&display=swap">
<link rel="stylesheet" href="{rel(aqui, 'assets/universo.css')}?v={VERSION}">
<script type="application/ld+json">{json.dumps(ld_all, ensure_ascii=False)}</script>
</head>
<body data-raiz="{rel(aqui, '')}" data-lang="{lang}">
<header class="top">
  <div class="wrap">
    <a class="logo" href="{home}" aria-label="Planetpedia">{LOGO}<span>Planet<b>pedia</b></span></a>
    <form class="buscar-mini" role="search" onsubmit="return false">
      <label class="vh" for="q">{t["buscar_lbl"]}</label>
      <input id="q" type="search" placeholder="{e(t["buscar"])}" autocomplete="off" role="combobox" aria-expanded="false" aria-controls="sug" aria-autocomplete="list">
      <ul id="sug" class="sug" role="listbox" hidden></ul>
    </form>
    <a class="idioma" href="{rel(aqui, otra)}" hreflang="{'en' if lang == 'es' else 'es'}" aria-label="{t["otro_lbl"]}">{'EN' if lang == 'es' else 'ES'}</a>
  </div>
</header>
<nav class="migas wrap" aria-label="breadcrumb">{migas_html}</nav>
<main>
{contenido}
</main>
<footer class="pie">
  <div class="wrap">
    <span><a href="{home}"><strong>Planetpedia</strong></a> · {e(t["pie"].split(" · ")[1])}</span>
    <span>{e(t["creditos"])}</span>
  </div>
</footer>
<script src="{rel(aqui, 'assets/universo.js')}?v={VERSION}" defer></script>
</body>
</html>
'''


def tarjeta(lang, aqui, s, f):
    url = rel(aqui, ruta(lang, s, f))
    c = CRED[f["foto"]]
    return (f'<li class="card"><a href="{url}"><span class="card-img"><img src="{rel(aqui, "img/universo/" + f["foto"] + ".jpg")}" alt="" '
            f'width="{c["w"]}" height="{c["h"]}" loading="lazy" decoding="async"></span>'
            f'<span class="card-txt"><strong>{e(f["titulo"][i(lang)])}</strong><span>{e(f["resumen"][i(lang)])}</span></span></a></li>')


def migas_base(lang):
    return [(L[lang]["inicio"], "" if lang == "es" else "en/"), (L[lang]["uni"], ruta(lang))]


def pag_ficha(lang, s, f, prev, nxt):
    k = i(lang); t = L[lang]
    aqui = ruta(lang, s, f); otra = ruta("en" if lang == "es" else "es", s, f)
    html_c, toc = cuerpo(f[lang], lang, aqui)
    datos = ""
    if f.get("datos"):
        datos = f'<section class="caja datos"><h2>{t["datos"]}</h2><dl>' + "".join(
            f"<dt>{e(d[k])}</dt><dd>{inline(d[2 + k], lang, aqui)}</dd>" for d in f["datos"]) + "</dl></section>"
    indice = ""
    if len(toc) > 2:
        indice = f'<nav class="caja toc" aria-label="{t["indice"]}"><h2>{t["indice"]}</h2><ol>' + "".join(
            f'<li><a href="#{a}">{inline(x, lang, aqui)}</a></li>' for a, x in toc) + "</ol></nav>"
    otras = [x for x in s.FICHAS if x is not f][:6]
    rel_html = f'<section class="caja rel"><h2>{t["relacionadas"]} {e(s.TITULO[k])}</h2><ul>' + "".join(
        f'<li><a href="{rel(aqui, ruta(lang, s, x))}">{e(x["titulo"][k])}</a></li>' for x in otras) + "</ul></section>"
    nav = '<nav class="pasos">'
    if prev: nav += f'<a class="ant" href="{rel(aqui, ruta(lang, s, prev))}"><small>← {t["anterior"]}</small>{e(prev["titulo"][k])}</a>'
    else: nav += "<span></span>"
    if nxt: nav += f'<a class="sig" href="{rel(aqui, ruta(lang, s, nxt))}"><small>{t["siguiente"]} →</small>{e(nxt["titulo"][k])}</a>'
    nav += "</nav>"
    palabras = len(re.findall(r"\w+", f[lang]))
    cont = f'''<article class="ficha">
<header class="ficha-head wrap">
  <span class="eyebrow">{e(s.TITULO[k])}</span>
  <h1>{e(f["titulo"][k])}</h1>
  <p class="lede">{inline(f["resumen"][k], lang, aqui)}</p>
</header>
<div class="wrap">{figura(f["foto"], f.get("pie", (f["titulo"][0], f["titulo"][1]))[k], lang, aqui, "portada", eager=True)}</div>
<div class="wrap ficha-cols">
  <div class="texto">
{html_c}
{nav}
  </div>
  <aside class="lateral">{datos}{indice}{rel_html}</aside>
</div>
</article>'''
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": f["titulo"][k], "description": f["resumen"][k],
          "inLanguage": lang, "image": f"{DOM}/img/universo/{f['foto']}.jpg", "datePublished": FECHA, "dateModified": FECHA,
          "keywords": f["claves"][k], "wordCount": palabras, "url": f"{DOM}/{aqui}",
          "author": {"@type": "Person", "name": "Alejandro Rosàs Navarro"},
          "publisher": {"@type": "Organization", "name": "Planetpedia", "url": DOM + "/"},
          "isPartOf": {"@type": "WebPage", "name": s.TITULO[k], "url": f"{DOM}/{ruta(lang, s)}"}}
    titulo = f'{f["titulo"][k]} · {s.TITULO[k]} · Planetpedia'
    migas = migas_base(lang) + [(s.TITULO[k], ruta(lang, s)), (f["titulo"][k], aqui)]
    return aqui, pagina(lang, aqui, otra, titulo, f["resumen"][k], f["claves"][k], cont, migas, f["foto"], ld)


def pag_seccion(lang, s):
    k = i(lang); t = L[lang]
    aqui = ruta(lang, s); otra = ruta("en" if lang == "es" else "es", s)
    intro, _ = cuerpo(s.INTRO[k], lang, aqui)
    cont = f'''<section class="sec-head">
  <img class="sec-fondo" src="{rel(aqui, 'img/universo/' + s.FOTO + '.jpg')}" alt="" fetchpriority="high">
  <div class="wrap">
    <span class="eyebrow">{t["uni"]} · {len(s.FICHAS)} {t["fichas"]}</span>
    <h1>{e(s.TITULO[k])}</h1>
    <p class="lede">{e(s.RESUMEN[k])}</p>
  </div>
</section>
<div class="wrap sec-intro">{intro}</div>
<div class="wrap"><ul class="cards">{"".join(tarjeta(lang, aqui, s, f) for f in s.FICHAS)}</ul></div>'''
    ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": s.TITULO[k], "description": s.RESUMEN[k],
          "inLanguage": lang, "url": f"{DOM}/{aqui}", "hasPart": [
              {"@type": "Article", "headline": f["titulo"][k], "url": f"{DOM}/{ruta(lang, s, f)}"} for f in s.FICHAS]}
    claves = s.CLAVES[k] + ", " + ", ".join(f["titulo"][k] for f in s.FICHAS)
    migas = migas_base(lang) + [(s.TITULO[k], aqui)]
    return aqui, pagina(lang, aqui, otra, f"{s.TITULO[k]} · {t['uni']} · Planetpedia", s.RESUMEN[k], claves, cont, migas, s.FOTO, ld)


CIFRAS = [
    ("13.800 millones de años", "13.8 billion years", "edad del universo", "age of the universe"),
    ("2 billones", "2 trillion", "galaxias en el universo observable (estimación)", "galaxies in the observable universe (estimate)"),
    ("8 min 20 s", "8 min 20 s", "tarda la luz del Sol en llegar a la Tierra", "for sunlight to reach Earth"),
    ("299.792 km/s", "299,792 km/s", "velocidad de la luz en el vacío", "speed of light in a vacuum"),
    ("4,24 años luz", "4.24 light years", "hasta Próxima Centauri, la estrella más cercana", "to Proxima Centauri, the nearest star"),
    ("−270 °C", "−270 °C", "temperatura del fondo cósmico", "temperature of the cosmic background"),
]


def pag_portada(lang):
    k = i(lang); t = L[lang]
    aqui = ruta(lang); otra = ruta("en" if lang == "es" else "es")
    secs = "".join(
        f'<li class="secc"><a href="{rel(aqui, ruta(lang, s))}"><img src="{rel(aqui, "img/universo/" + s.FOTO + ".jpg")}" alt="" loading="lazy" decoding="async">'
        f'<span class="secc-txt"><small>{len(s.FICHAS)} {t["fichas"]}</small><strong>{e(s.TITULO[k])}</strong><span>{e(s.RESUMEN[k])}</span></span></a></li>'
        for s in SECCIONES)
    cifras = "".join(f'<li><b>{e(c[k])}</b><span>{e(c[2 + k])}</span></li>' for c in CIFRAS)
    listado = "".join(
        f'<section class="mapa-sec"><h3><a href="{rel(aqui, ruta(lang, s))}">{e(s.TITULO[k])}</a></h3><ul>' +
        "".join(f'<li><a href="{rel(aqui, ruta(lang, s, f))}">{e(f["titulo"][k])}</a></li>' for f in s.FICHAS) + "</ul></section>"
        for s in SECCIONES)
    n = sum(len(s.FICHAS) for s in SECCIONES)
    cont = f'''<section class="uni-hero">
  <img class="sec-fondo" src="{rel(aqui, 'img/universo/campo_webb.jpg')}" alt="" fetchpriority="high">
  <div class="wrap">
    <span class="eyebrow">{t["eyebrow"]} · {n} {t["fichas"]}</span>
    <h1>{t["h1"]}</h1>
    <p class="lede">{t["lede"]}</p>
  </div>
</section>
<div class="wrap">
  <h2 class="tit">{t["cifras"]}</h2>
  <ul class="cifras">{cifras}</ul>
  <h2 class="tit">{t["secciones"]}</h2>
  <ul class="seccs">{secs}</ul>
  <div class="mapa">{listado}</div>
</div>'''
    claves = ", ".join(s.CLAVES[k] for s in SECCIONES)
    ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": t["h1"], "description": t["lede"], "inLanguage": lang,
          "url": f"{DOM}/{aqui}"}
    return aqui, pagina(lang, aqui, otra, f"{t['h1']}: {t['eyebrow'].lower()} · Planetpedia", t["lede"], claves, cont,
                        migas_base(lang), "campo_webb", ld)


def indice(lang):
    k = i(lang); out = []
    for s in SECCIONES:
        out.append({"t": s.TITULO[k], "d": s.RESUMEN[k], "c": s.CLAVES[k], "u": ruta(lang, s), "s": L[lang]["uni"], "f": s.FOTO})
        for f in s.FICHAS:
            heads = " ".join(re.findall(r"^## (.+)$", f[lang], re.M))
            out.append({"t": f["titulo"][k], "d": f["resumen"][k], "c": f["claves"][k] + " " + heads,
                        "u": ruta(lang, s, f), "s": s.TITULO[k], "f": f["foto"]})
    return out


VERSION = "1"


def main():
    global VERSION
    import hashlib
    VERSION = hashlib.md5((ROOT / "assets/universo.css").read_bytes() + (ROOT / "assets/universo.js").read_bytes()).hexdigest()[:8]
    urls = []
    for lang in ("es", "en"):
        pags = [pag_portada(lang)]
        for s in SECCIONES:
            pags.append(pag_seccion(lang, s))
            for n, f in enumerate(s.FICHAS):
                prev = s.FICHAS[n - 1] if n else None
                nxt = s.FICHAS[n + 1] if n + 1 < len(s.FICHAS) else None
                pags.append(pag_ficha(lang, s, f, prev, nxt))
        for ruta_, contenido in pags:
            p = ROOT / ruta_ / "index.html"; p.parent.mkdir(parents=True, exist_ok=True); p.write_text(contenido)
            urls.append(ruta_)
        (ROOT / f"assets/indice-{lang}.json").write_text(json.dumps(indice(lang), ensure_ascii=False, separators=(",", ":")))
    todas = ["", "en/"] + urls
    (ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
        "".join(f"  <url><loc>{DOM}/{u}</loc><lastmod>{FECHA}</lastmod></url>\n" for u in todas) + "</urlset>\n")
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {DOM}/sitemap.xml\n")
    print(len(urls), "páginas")
    if FALTAN: print("ENLACES SIN FICHA:", sorted(FALTAN))


if __name__ == "__main__":
    main()
