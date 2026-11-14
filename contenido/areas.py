# Áreas temáticas de Planetpedia que genera build_universo.py.
# Cada área: paquete de contenido, orden de secciones, carpetas (es, en), foto de portada,
# cifras de la portada y textos propios.

CIFRAS_UNIVERSO = [
    ("13.800 millones de años", "13.8 billion years", "edad del universo", "age of the universe"),
    ("2 billones", "2 trillion", "galaxias en el universo observable (estimación)", "galaxies in the observable universe (estimate)"),
    ("8 min 20 s", "8 min 20 s", "tarda la luz del Sol en llegar a la Tierra", "for sunlight to reach Earth"),
    ("299.792 km/s", "299,792 km/s", "velocidad de la luz en el vacío", "speed of light in a vacuum"),
    ("4,24 años luz", "4.24 light years", "hasta Próxima Centauri, la estrella más cercana", "to Proxima Centauri, the nearest star"),
    ("−270 °C", "−270 °C", "temperatura del fondo cósmico", "temperature of the cosmic background"),
]


CIFRAS_TIERRA = [
    ("4.540 millones de años", "4.54 billion years", "edad de la Tierra", "age of the Earth"),
    ("71 %", "71%", "de la superficie cubierta por océanos", "of the surface covered by oceans"),
    ("8.849 m", "8,849 m", "altura del Everest, el punto más alto", "height of Everest, the highest point"),
    ("10.935 m", "10,935 m", "profundidad de la fosa de las Marianas", "depth of the Mariana Trench"),
    ("8,7 millones", "8.7 million", "especies estimadas en el planeta", "estimated species on the planet"),
    ("5.400 °C", "5,400 °C", "temperatura del núcleo interno", "temperature of the inner core"),
]


AREAS = {
    "universo": dict(
        pkg="universo",
        orden=["sistema_solar", "estrellas", "galaxias", "cosmologia", "exploracion", "observar", "curiosidades"],
        base=("universo", "en/universe"),
        foto="campo_webb",
        cifras=CIFRAS_UNIVERSO,
        txt={
            "es": dict(uni="Universo", h1="Universo", eyebrow="Enciclopedia del cosmos",
                       buscar="Busca en el Universo: Saturno, agujero negro, eclipse…", buscar_lbl="Buscar en Universo",
                       lede="Una enciclopedia del cosmos: del Sol a las galaxias más lejanas, con fotos reales de telescopios y sondas, cifras, curiosidades y simuladores.",
                       creditos="Fotografías de Wikimedia Commons (NASA, ESA, ESO y otros autores), con su licencia en cada imagen.",
                       videos_lede="Una selección de los mejores vídeos divulgativos de YouTube para cada ficha, de canales como QuantumFracture, Astrum Español, En Pocas Palabras (Kurzgesagt), Date un Vlog o NASA en Español."),
            "en": dict(uni="Universe", h1="Universe", eyebrow="Encyclopedia of the cosmos",
                       buscar="Search the Universe: Saturn, black hole, eclipse…", buscar_lbl="Search the Universe",
                       lede="An encyclopedia of the cosmos: from the Sun to the most distant galaxies, with real images from telescopes and probes, figures, curiosities and simulators.",
                       creditos="Photographs from Wikimedia Commons (NASA, ESA, ESO and other authors), with each image's licence.",
                       videos_lede="A selection of the best explainer videos on YouTube for each article, from channels such as Kurzgesagt, PBS Space Time, TED-Ed, National Geographic, NASA and ESA."),
        },
    ),
    "tierra": dict(
        pkg="tierra",
        orden=["por_dentro", "oceanos", "atmosfera", "vida", "geografia", "impacto", "curiosidades"],
        base=("tierra", "en/earth"),
        foto="tierra",
        cifras=CIFRAS_TIERRA,
        txt={
            "es": dict(uni="Planeta Tierra", h1="Planeta Tierra", eyebrow="Enciclopedia de nuestro planeta",
                       buscar="Busca en Planeta Tierra: volcanes, Everest, tsunami…", buscar_lbl="Buscar en Planeta Tierra",
                       lede="Una enciclopedia de nuestro planeta: su interior, los océanos, el clima, la vida, los paisajes del mundo y nuestro impacto, con fotos, cifras, récords y simuladores.",
                       creditos="Fotografías de Wikimedia Commons (NASA, NOAA y otros autores), con su licencia en cada imagen.",
                       videos_lede="Una selección de los mejores vídeos divulgativos de YouTube para cada ficha, de canales como National Geographic, En Pocas Palabras (Kurzgesagt), CuriosaMente, BBC Mundo o DW Documental."),
            "en": dict(uni="Planet Earth", h1="Planet Earth", eyebrow="Encyclopedia of our planet",
                       buscar="Search Planet Earth: volcanoes, Everest, tsunami…", buscar_lbl="Search Planet Earth",
                       lede="An encyclopedia of our planet: its interior, the oceans, climate, life, the world's landscapes and our impact, with photos, figures, records and simulators.",
                       creditos="Photographs from Wikimedia Commons (NASA, NOAA and other authors), with each image's licence.",
                       videos_lede="A selection of the best explainer videos on YouTube for each article, from channels such as National Geographic, Kurzgesagt, TED-Ed, BBC Earth and PBS Terra."),
        },
    ),
}
