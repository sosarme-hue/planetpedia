# Genera las páginas legales (aviso legal, privacidad, cookies) en español e inglés.
# Uso: python3 legal.py
import pathlib, html

ROOT = pathlib.Path(__file__).parent
# Datos del titular. Si se rellenan NOMBRE y NIF, aparecen en el aviso legal.
NOMBRE = ""
NIF = ""
EMAIL = "partenopides@gmail.com"
FECHA = ("14 de noviembre de 2026", "14 November 2026")

PAGS = {
    "aviso-legal": ("legal-notice", "Aviso legal", "Legal notice"),
    "privacidad": ("privacy", "Política de privacidad", "Privacy policy"),
    "cookies": ("cookies", "Política de cookies", "Cookie policy"),
}


def titular(lang):
    es = lang == "es"
    filas = []
    if NOMBRE: filas.append(("Titular" if es else "Owner", NOMBRE))
    if NIF: filas.append(("NIF", NIF))
    filas.append(("Sitio web" if es else "Website", "planetpedia.net"))
    filas.append(("Contacto" if es else "Contact", f'<a href="mailto:{EMAIL}">{EMAIL}</a>'))
    return "<dl>" + "".join(f"<dt>{a}</dt><dd>{b}</dd>" for a, b in filas) + "</dl>"


def cuerpo(clave, lang):
    es = lang == "es"
    if clave == "aviso-legal":
        return (f"""
<p>En cumplimiento de la Ley 34/2002, de servicios de la sociedad de la información y de comercio electrónico (LSSI-CE), se informa de los datos del responsable de este sitio web:</p>
{titular(lang)}
<h2>Objeto</h2>
<p>Planetpedia es un sitio divulgativo y gratuito que reúne enciclopedias temáticas, guías y fichas sobre el universo y el planeta Tierra. Su uso no requiere registro.</p>
<h2>Contenidos</h2>
<p>Los textos de Planetpedia se han redactado con fines informativos y educativos. Aunque se revisan con cuidado, pueden contener errores o quedar desactualizados; si encuentras alguno, escríbenos y lo corregiremos. Los contenidos no sustituyen el consejo de un profesional.</p>
<h2>Propiedad intelectual</h2>
<p>Los textos y el diseño de Planetpedia pertenecen a su titular. Puedes citarlos con un enlace a la página original. Las fotografías proceden de Wikimedia Commons y tienen licencias libres (dominio público, CC0, CC BY o CC BY-SA): en cada imagen se indican su autor y su licencia, que rigen su reutilización.</p>
<h2>Enlaces y vídeos de terceros</h2>
<p>Planetpedia enlaza a otras webs y muestra vídeos de YouTube que pertenecen a sus autores. No somos responsables de sus contenidos ni de sus políticas. Los vídeos solo se cargan cuando pulsas sobre ellos.</p>
<h2>Legislación aplicable</h2>
<p>Este aviso se rige por la legislación española.</p>
""" if es else f"""
<p>In accordance with Spanish Law 34/2002 on information society services and e-commerce (LSSI-CE), the details of the party responsible for this website are:</p>
{titular(lang)}
<h2>Purpose</h2>
<p>Planetpedia is a free, educational website bringing together themed encyclopedias, guides and articles about the universe and planet Earth. No registration is required.</p>
<h2>Content</h2>
<p>Planetpedia's texts are written for information and education. Although they are carefully checked, they may contain errors or become outdated; if you spot one, write to us and we will fix it. The content is no substitute for professional advice.</p>
<h2>Intellectual property</h2>
<p>Planetpedia's texts and design belong to its owner. You may quote them with a link to the original page. Photographs come from Wikimedia Commons under free licences (public domain, CC0, CC BY or CC BY-SA): each image shows its author and licence, which govern its reuse.</p>
<h2>Third-party links and videos</h2>
<p>Planetpedia links to other websites and shows YouTube videos that belong to their creators. We are not responsible for their content or policies. Videos only load when you click them.</p>
<h2>Applicable law</h2>
<p>This notice is governed by Spanish law.</p>
""")
    if clave == "privacidad":
        return (f"""
<p>Planetpedia respeta tu privacidad: <b>no pedimos datos personales, no hay registro ni formularios, y no usamos herramientas de analítica ni publicidad.</b></p>
<h2>Responsable</h2>
{titular(lang)}
<h2>Qué datos se tratan</h2>
<ul>
<li><b>Correo electrónico.</b> Si nos escribes, usaremos tu dirección y tu mensaje solo para responderte. No los cedemos a nadie. La base legal es tu consentimiento al escribirnos.</li>
<li><b>Datos técnicos del servidor.</b> Nuestro proveedor de alojamiento (Hostinger) registra, como cualquier servidor web, la dirección IP y la página visitada, por seguridad y durante un tiempo limitado.</li>
<li><b>Tipografías.</b> Las letras de la web se cargan desde Google Fonts, por lo que tu navegador se conecta a los servidores de Google, que reciben tu dirección IP.</li>
<li><b>Vídeos.</b> Si pulsas un vídeo, se carga desde YouTube (Google) en modo de privacidad mejorada. A partir de ese momento se aplica la <a href="https://policies.google.com/privacy?hl=es" rel="noopener">política de privacidad de Google</a>.</li>
</ul>
<h2>Tus derechos</h2>
<p>Puedes pedir acceso, rectificación o supresión de tus datos, o oponerte a su tratamiento, escribiendo a <a href="mailto:{EMAIL}">{EMAIL}</a>. También puedes reclamar ante la <a href="https://www.aepd.es" rel="noopener">Agencia Española de Protección de Datos</a>.</p>
""" if es else f"""
<p>Planetpedia respects your privacy: <b>we do not ask for personal data, there is no registration or forms, and we use no analytics or advertising tools.</b></p>
<h2>Data controller</h2>
{titular(lang)}
<h2>What data is processed</h2>
<ul>
<li><b>Email.</b> If you write to us, we will use your address and message only to reply. We do not share them with anyone. The legal basis is your consent in writing to us.</li>
<li><b>Server logs.</b> Our hosting provider (Hostinger), like any web server, logs IP addresses and pages visited, for security and for a limited time.</li>
<li><b>Fonts.</b> The site's fonts load from Google Fonts, so your browser connects to Google's servers, which receive your IP address.</li>
<li><b>Videos.</b> If you click a video, it loads from YouTube (Google) in privacy-enhanced mode. From then on, <a href="https://policies.google.com/privacy?hl=en" rel="noopener">Google's privacy policy</a> applies.</li>
</ul>
<h2>Your rights</h2>
<p>You can request access to, correction or deletion of your data, or object to its processing, by writing to <a href="mailto:{EMAIL}">{EMAIL}</a>. You can also complain to the Spanish Data Protection Agency (<a href="https://www.aepd.es" rel="noopener">AEPD</a>).</p>
""")
    return (f"""
<p><b>Planetpedia no instala cookies propias ni de terceros mientras navegas</b>, y no usa analítica ni publicidad. Por eso no te mostramos ningún aviso para aceptarlas.</p>
<h2>Vídeos de YouTube</h2>
<p>Los vídeos no se cargan hasta que los pulsas. Al pulsar uno, se reproduce desde <b>youtube-nocookie.com</b>, el modo de privacidad mejorada de YouTube. Durante la reproducción, YouTube puede guardar en tu navegador cookies o datos similares para que el vídeo funcione y para medir su uso. Puedes consultarlo en la <a href="https://policies.google.com/technologies/cookies?hl=es" rel="noopener">política de cookies de Google</a>. Si prefieres evitarlo, no pulses los vídeos.</p>
<h2>Cómo borrar o bloquear cookies</h2>
<p>Puedes ver, borrar o bloquear las cookies desde la configuración de tu navegador (Chrome, Firefox, Safari, Edge…), normalmente en el apartado de privacidad.</p>
<h2>Cambios</h2>
<p>Si algún día añadimos cookies que no sean imprescindibles, te lo pediremos antes y actualizaremos esta página.</p>
""" if es else f"""
<p><b>Planetpedia does not set any first-party or third-party cookies while you browse</b>, and uses no analytics or advertising. That is why we do not show you a cookie banner.</p>
<h2>YouTube videos</h2>
<p>Videos do not load until you click them. When you click one, it plays from <b>youtube-nocookie.com</b>, YouTube's privacy-enhanced mode. During playback, YouTube may store cookies or similar data in your browser to make the video work and measure its use. See <a href="https://policies.google.com/technologies/cookies?hl=en" rel="noopener">Google's cookie policy</a>. If you prefer to avoid this, do not play the videos.</p>
<h2>How to delete or block cookies</h2>
<p>You can view, delete or block cookies in your browser settings (Chrome, Firefox, Safari, Edge…), usually under privacy.</p>
<h2>Changes</h2>
<p>If we ever add non-essential cookies, we will ask you first and update this page.</p>
""")


def pagina(clave, lang):
    es = lang == "es"
    slug_en, t_es, t_en = PAGS[clave]
    tit = t_es if es else t_en
    raiz = "../" if es else "../../"
    home = raiz if es else "../"
    otra = f"{raiz}en/{slug_en}/" if es else f"../../{clave}/"
    enlaces = " · ".join(
        f'<a href="{raiz if es else "../"}{(k if es else v[0])}/">{v[1] if es else v[2]}</a>' for k, v in PAGS.items())
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{tit} · Planetpedia</title>
<meta name="robots" content="noindex, follow">
<link rel="canonical" href="https://planetpedia.net/{clave + "/" if es else "en/" + slug_en + "/"}">
<link rel="alternate" hreflang="es" href="https://planetpedia.net/{clave}/">
<link rel="alternate" hreflang="en" href="https://planetpedia.net/en/{slug_en}/">
<style>
:root{{--bg:#fff;--ink:#0b1f3a;--soft:#4a5a72;--line:#dde4ee;--navy:#0d2b55;--teal:#08787a;--surface:#f3f6fa}}
@media (prefers-color-scheme:dark){{:root{{--bg:#0b1424;--ink:#e8eef7;--soft:#a9b6c8;--line:#24324a;--navy:#081a33;--teal:#4fd1c5;--surface:#121e33}}}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--ink);font:400 1.02rem/1.65 Inter,"Segoe UI",system-ui,sans-serif}}
a{{color:var(--teal)}}.wrap{{max-width:760px;margin:0 auto;padding:0 16px}}
header{{background:var(--navy)}}header .wrap{{display:flex;justify-content:space-between;align-items:center;padding-block:16px}}
header a{{color:#fff;text-decoration:none;font:800 1.15rem "Plus Jakarta Sans","Segoe UI",system-ui,sans-serif}}header a.idioma{{font-size:.85rem;font-weight:600;border:1px solid #ffffff55;border-radius:99px;padding:4px 12px}}
main{{padding:40px 0 56px}}h1{{font:800 2rem/1.2 "Plus Jakarta Sans","Segoe UI",system-ui,sans-serif;margin:0 0 8px}}h2{{font-size:1.2rem;margin:32px 0 8px}}
.fecha{{color:var(--soft);font-size:.9rem;margin:0 0 24px}}dl{{display:grid;grid-template-columns:max-content 1fr;gap:6px 16px;background:var(--surface);border:1px solid var(--line);border-radius:12px;padding:16px}}dt{{font-weight:600}}dd{{margin:0;overflow-wrap:anywhere}}
footer{{background:var(--navy);color:#b9c8de;font-size:.88rem}}footer .wrap{{padding-block:24px;display:flex;flex-wrap:wrap;gap:8px 20px;justify-content:space-between}}footer a{{color:#fff}}
</style>
</head>
<body>
<header><div class="wrap"><a href="{home}">Planetpedia</a><a class="idioma" href="{otra}" hreflang="{"en" if es else "es"}">{"EN" if es else "ES"}</a></div></header>
<main class="wrap">
<h1>{tit}</h1>
<p class="fecha">{"Última actualización" if es else "Last updated"}: {FECHA[0 if es else 1]}</p>
{cuerpo(clave, lang)}
</main>
<footer><div class="wrap"><span><a href="{home}"><strong>Planetpedia</strong></a></span><span>{enlaces}</span></div></footer>
</body>
</html>
'''


for clave, (slug_en, _, _) in PAGS.items():
    for lang, ruta in (("es", ROOT / clave), ("en", ROOT / "en" / slug_en)):
        ruta.mkdir(parents=True, exist_ok=True)
        (ruta / "index.html").write_text(pagina(clave, lang))
print("6 páginas legales")
