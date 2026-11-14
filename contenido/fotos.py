# Descarga las fotos de Commons a img/<área>/ (960 px, JPEG) y guarda los créditos.
# Uso: python3 contenido/fotos.py universo|tierra [--solo-comprobar]
import json, re, html, sys, time, io, pathlib, urllib.request, urllib.parse
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import importlib
AREA = next((a for a in sys.argv[1:] if not a.startswith("--")), "universo")
FOTOS = importlib.import_module("fotos_" + AREA).FOTOS
ROOT = pathlib.Path(__file__).parent.parent
DEST = ROOT / "img" / AREA; DEST.mkdir(parents=True, exist_ok=True)
CRED = DEST / "creditos.json"
UA = {"User-Agent": "PlanetSiteBuilder/1.0 (static educational site)"}

def get(u, binary=False):
    for i in range(7):
        try:
            r = urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=60).read()
            return r if binary else json.loads(r)
        except Exception as e:
            time.sleep(6 * (i + 1))
    raise RuntimeError("fallo " + u)

def limpia(s):
    return re.sub(r"\s+", " ", re.sub("<[^>]+>", "", html.unescape(s or ""))).strip()

cred = json.loads(CRED.read_text()) if CRED.exists() else {}
pend = [(k, t) for k, t in FOTOS.items() if k not in cred or not (DEST / f"{k}.jpg").exists()]
titulos = {t.replace("_", " "): k for k, t in pend}
info = {}
lista = list(titulos)
for i in range(0, len(lista), 40):
    q = dict(action="query", format="json", titles="|".join("File:" + t for t in lista[i:i+40]),
             prop="imageinfo", iiprop="url|extmetadata|size", iiurlwidth=960)
    d = get("https://commons.wikimedia.org/w/api.php?" + urllib.parse.urlencode(q))
    norm = {n["to"]: n["from"] for n in d["query"].get("normalized", [])}
    for p in d["query"]["pages"].values():
        t = p["title"]; orig = norm.get(t, t)[5:]
        k = titulos.get(orig) or titulos.get(t[5:])
        if "missing" in p or "imageinfo" not in p:
            print("FALTA", k, t); continue
        info[k] = p["imageinfo"][0]
if "--solo-comprobar" in sys.argv:
    sys.exit()
from PIL import Image
for k, ii in info.items():
    m = ii.get("extmetadata", {})
    lic = limpia(m.get("LicenseShortName", {}).get("value"))
    if not re.search(r"public domain|dominio|cc0|cc by", lic, re.I):
        print("LICENCIA NO VÁLIDA", k, lic); continue
    url = ii["thumburl"].split("?")[0].replace("thumb.wikimedia.org", "upload.wikimedia.org")
    try:
        data = get(url, binary=True)
    except RuntimeError as ex:
        print("NO DESCARGA", k, url); continue
    im = Image.open(io.BytesIO(data)).convert("RGB")
    if im.width > 960:
        im = im.resize((960, round(im.height * 960 / im.width)), Image.LANCZOS)
    im.save(DEST / f"{k}.jpg", "JPEG", quality=82, optimize=True, progressive=True)
    cred[k] = {"autor": limpia(m.get("Artist", {}).get("value"))[:140] or "Desconocido",
               "licencia": lic, "url": ii["descriptionurl"], "w": im.width, "h": im.height}
    CRED.write_text(json.dumps(cred, ensure_ascii=False, indent=1))
    print("ok", k, im.size, lic)
    time.sleep(1.5)
