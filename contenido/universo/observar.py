from universo import F

SLUG = ("observar-el-cielo", "stargazing")
TITULO = ("Observar el cielo", "Stargazing")
RESUMEN = ("Guía práctica para mirar el cielo a simple vista, con prismáticos o con telescopio: constelaciones, eclipses, lluvias de estrellas y el calendario de los próximos meses.",
           "A practical guide to looking at the sky with the naked eye, binoculars or a telescope: constellations, eclipses, meteor showers and the calendar for the coming months.")
CLAVES = ("observar el cielo, astronomía para principiantes, constelaciones, eclipses, eclipse en España, lluvias de estrellas, Perseidas, telescopio para principiantes, cielos oscuros, contaminación lumínica, calendario astronómico 2027",
          "stargazing, astronomy for beginners, constellations, eclipses, eclipse in Spain, meteor showers, Perseids, beginner telescope, dark skies, light pollution, astronomy calendar 2027")
FOTO = "via_lactea_cielo"
INTRO = ("""
No hace falta ningún aparato para empezar: basta con salir de noche, dejar que los ojos se acostumbren a la oscuridad y saber dónde mirar. Esta sección reúne lo esencial para disfrutar del cielo desde cualquier lugar, con especial atención a lo que se puede ver desde España.
""", """
You need no equipment to start: just go out at night, let your eyes adjust to the dark and know where to look. This section gathers the essentials for enjoying the sky from anywhere, with special attention to what can be seen from Spain.
""")

EMPEZAR = F(
    ("empezar-a-observar", "getting-started"),
    ("Cómo empezar a observar", "How to start stargazing"),
    ("Consejos prácticos para tu primera noche bajo las estrellas: dónde ir, cuándo salir, qué llevar y qué buscar.",
     "Practical tips for your first night under the stars: where to go, when to go out, what to take and what to look for."),
    ("cómo observar las estrellas, astronomía para principiantes, adaptación a la oscuridad, luz roja, Stellarium, cielos oscuros, reservas Starlight, contaminación lumínica, escala de Bortle, ver la Vía Láctea, ver la Estación Espacial",
     "how to stargaze, astronomy for beginners, dark adaptation, red light, Stellarium, dark skies, Starlight reserves, light pollution, Bortle scale, seeing the Milky Way, spotting the Space Station"),
    "via_lactea_cielo",
    """
La astronomía es una de las pocas ciencias en las que cualquier persona puede disfrutar y hasta hacer aportaciones reales sin apenas equipo. Estos son los pasos para empezar con buen pie.

## Paso a paso

- **Busca oscuridad**: aléjate de las farolas y, si puedes, de la ciudad. Incluso un parque oscuro o una azotea sin luces directas mejoran mucho las cosas.
- **Elige bien la noche**: lo ideal es una noche despejada y sin Luna, o con la Luna aún sin salir. Unos días alrededor de la luna nueva son los mejores para ver estrellas débiles.
- **Deja que tus ojos se adapten**: la pupila se abre en pocos minutos, pero la sensibilidad completa tarda entre **20 y 30 minutos**. Una sola mirada al móvil con el brillo alto la arruina.
- **Usa luz roja**: una linterna roja, o un trozo de celofán rojo sobre una normal, permite ver un mapa sin perder la adaptación.
- **Abrígate**: incluso en verano, de noche y quieto, se pasa frío.
- **Lleva un mapa**: aplicaciones gratuitas como **Stellarium** muestran qué hay en cada parte del cielo con solo apuntar el móvil. Actívales el modo nocturno rojo.

## Qué buscar la primera noche

1. **La Luna**, sobre todo cuando no está llena: en el borde entre la luz y la sombra los cráteres se ven en relieve, incluso con prismáticos.
2. **Los planetas brillantes**: Venus, Júpiter, Saturno y Marte parecen estrellas muy brillantes que **no titilan**. Cambian de posición a lo largo de los meses.
3. **Una constelación fácil**, como [Orión](@constelaciones) en invierno o el Carro de la Osa Mayor todo el año.
4. **La Estación Espacial**: un punto muy brillante que cruza el cielo en unos minutos sin parpadear. La NASA y varias webs y apps avisan de sus pasos.
5. **La Vía Láctea**: en verano, desde un lugar oscuro, se ve como una nube blanquecina que cruza el cielo. Es el disco de [nuestra galaxia](@via-lactea) visto desde dentro.

## La luz que nos roba las estrellas

Según un estudio de 2016, **más de un tercio de la humanidad** no puede ver la Vía Láctea desde su casa; en Europa, el 60 %. La **contaminación lumínica**, el exceso de luz artificial mal dirigida, no solo borra las estrellas: también desorienta a aves e insectos y altera el sueño. Se mide con la **escala de Bortle**, de 1 (cielo prístino) a 9 (centro de una gran ciudad).

!foto contaminacion | La contaminación lumínica tiñe el cielo nocturno de naranja sobre las ciudades y apaga las estrellas.

## Cielos oscuros en España

España tiene algunos de los mejores cielos de Europa. La Fundación Starlight ha certificado decenas de destinos y reservas, y las **Canarias** tienen leyes que protegen el cielo de La Palma y Tenerife, donde están los observatorios del Roque de los Muchachos y del Teide, de los más importantes del mundo. Otros lugares conocidos: el Montsec (Lleida), Gúdar-Javalambre (Teruel), la Sierra Sur de Jaén, Sierra Morena, Monfragüe (Cáceres) o el Parque Nacional de Picos de Europa.

> Las estrellas parecen titilar porque su luz atraviesa capas de aire en movimiento. Los planetas, que vemos como pequeños discos y no como puntos, apenas titilan. Es el truco más rápido para distinguirlos.
""",
    """
Astronomy is one of the few sciences anyone can enjoy, and even contribute to, with barely any equipment. Here is how to get off to a good start.

## Step by step

- **Find darkness**: get away from street lights and, if you can, from the city. Even a dark park or a rooftop with no direct lights makes a big difference.
- **Pick the right night**: ideally clear and moonless, or before the Moon rises. The days around new moon are best for faint stars.
- **Let your eyes adjust**: your pupils open within minutes, but full sensitivity takes **20 to 30 minutes**. A single glance at a bright phone screen ruins it.
- **Use red light**: a red torch, or red cellophane over a normal one, lets you read a chart without losing your dark adaptation.
- **Wrap up warm**: even in summer, standing still at night gets cold.
- **Take a map**: free apps such as **Stellarium** show what is in each part of the sky when you point your phone. Turn on their red night mode.

## What to look for on your first night

1. **The Moon**, especially when it is not full: along the line between light and shadow, craters stand out in relief, even through binoculars.
2. **The bright planets**: Venus, Jupiter, Saturn and Mars look like very bright stars that **do not twinkle**. They shift position over the months.
3. **An easy constellation**, such as [Orion](@constelaciones) in winter or the Big Dipper all year round.
4. **The Space Station**: a very bright dot that crosses the sky in a few minutes without blinking. NASA and several websites and apps announce its passes.
5. **The Milky Way**: in summer, from a dark site, it looks like a pale cloud stretching across the sky. It is the disc of [our galaxy](@via-lactea) seen from inside.

## The light that steals our stars

According to a 2016 study, **more than a third of humanity** cannot see the Milky Way from home; in Europe, 60%. **Light pollution**, excess artificial light pointing the wrong way, does not only erase the stars: it also disorients birds and insects and disrupts sleep. It is measured on the **Bortle scale**, from 1 (pristine sky) to 9 (big-city centre).

!foto contaminacion | Light pollution turns the night sky orange over cities and drowns out the stars.

## Dark skies in Spain

Spain has some of the best skies in Europe. The Starlight Foundation has certified dozens of destinations and reserves, and the **Canary Islands** have laws protecting the skies of La Palma and Tenerife, home to the Roque de los Muchachos and Teide observatories, among the most important in the world. Other well-known spots: Montsec (Lleida), Gúdar-Javalambre (Teruel), Sierra Sur de Jaén, Sierra Morena, Monfragüe (Cáceres) and the Picos de Europa National Park.

> Stars seem to twinkle because their light passes through moving layers of air. Planets, which we see as tiny discs rather than points, hardly twinkle at all. It is the quickest trick for telling them apart.
""",
    datos=[("Adaptación a la oscuridad", "Dark adaptation", "20 a 30 minutos", "20 to 30 minutes"),
           ("Mejor momento", "Best time", "Cerca de la luna nueva", "Around new moon"),
           ("App recomendada", "Recommended app", "Stellarium (gratuita)", "Stellarium (free)"),
           ("Sin ver la Vía Láctea", "Can't see the Milky Way", "1 de cada 3 personas; 60 % en Europa", "1 in 3 people; 60% in Europe"),
           ("Escala de oscuridad", "Darkness scale", "Bortle, de 1 a 9", "Bortle, 1 to 9")],
    pie=("La Vía Láctea sobre un paisaje oscuro. Desde un lugar sin contaminación lumínica se ven miles de estrellas a simple vista.",
         "The Milky Way over a dark landscape. From a site free of light pollution, thousands of stars are visible to the naked eye."),
)

CONSTELACIONES = F(
    ("constelaciones", "constellations"),
    ("Las constelaciones", "The constellations"),
    ("Las 88 figuras oficiales del cielo, sus leyendas y cómo encontrar las más fáciles: Orión, la Osa Mayor, Casiopea o el triángulo de verano.",
     "The sky's 88 official figures, their legends and how to find the easiest: Orion, the Great Bear, Cassiopeia and the Summer Triangle."),
    ("constelaciones, Orión, Osa Mayor, el Carro, Osa Menor, estrella Polar, Casiopea, triángulo de verano, Vega, Altair, Deneb, zodiaco, Ofiuco, asterismos, Cruz del Sur, constelaciones de invierno, constelaciones de verano",
     "constellations, Orion, Great Bear, Ursa Major, Big Dipper, Little Bear, Polaris, North Star, Cassiopeia, Summer Triangle, Vega, Altair, Deneb, zodiac, Ophiuchus, asterisms, Southern Cross, winter constellations, summer constellations"),
    "orion_constelacion",
    """
Desde hace miles de años, todas las culturas han unido las estrellas brillantes con líneas imaginarias para formar figuras: animales, héroes, objetos. Servían para contar historias, pero también para orientarse en el mar y saber cuándo sembrar.

## 88 constelaciones oficiales

En 1922 la Unión Astronómica Internacional fijó **88 constelaciones** que cubren todo el cielo, como las provincias de un mapa. Unas 48 vienen del astrónomo griego **Ptolomeo** (siglo II), que recogió tradiciones babilónicas y griegas; las del cielo austral se añadieron en los siglos XVI a XVIII, cuando los navegantes europeos viajaron al hemisferio sur, y por eso tienen nombres como el Telescopio, la Bomba Neumática o el Microscopio.

Las estrellas de una constelación no suelen estar cerca entre sí: solo parecen juntas vistas desde la Tierra. Una puede estar a 50 años luz y su vecina en el cielo, a 2.000.

## Las más fáciles de encontrar

- **Orión** (invierno): el cazador, con las tres estrellas alineadas de su cinturón, las Tres Marías. Arriba a la izquierda brilla la roja **Betelgeuse**, una supergigante que explotará algún día; abajo a la derecha, la azulada **Rigel**. Bajo el cinturón se distingue la [nebulosa de Orión](@nebulosas) como una manchita borrosa.
- **La Osa Mayor** (todo el año): sus siete estrellas más brillantes forman **el Carro** o el Cazo. Si prolongas unas cinco veces la línea que une las dos estrellas del extremo del cazo, llegas a la **estrella Polar**.
- **La Osa Menor**: la Polar es la punta de su cola. Siempre marca el norte y apenas se mueve, porque está casi exactamente sobre el eje de rotación de la Tierra. Su altura sobre el horizonte es igual a tu latitud.
- **Casiopea** (todo el año): una «W» o «M» al otro lado de la Polar respecto al Carro.
- **El triángulo de verano**: tres estrellas muy brillantes, **Vega** (en la Lira), **Deneb** (en el Cisne) y **Altair** (en el Águila), que dominan las noches de julio y agosto, con la Vía Láctea pasando por en medio.
- **Escorpio** (verano, bajo en el sur): con su corazón rojo, **Antares**, y su cola curvada.

!foto osa_mayor | La Osa Mayor y su asterismo más famoso, el Carro, que ayuda a encontrar la estrella Polar.

## El zodiaco tiene 13

El zodiaco son las constelaciones por las que pasa el Sol a lo largo del año vista desde la Tierra. Los astrónomos cuentan **13**, porque el Sol también cruza **Ofiuco**, el portador de la serpiente, entre el 29 de noviembre y el 17 de diciembre. Además, por un lento bamboleo del eje de la Tierra llamado **precesión**, las fechas ya no coinciden con las de los horóscopos, que se fijaron hace unos 2.000 años. La astrología no tiene base científica; la astronomía, sí.

## El cielo del sur

Desde las Canarias se ven estrellas que no asoman en la península, y desde el hemisferio sur se ven la **Cruz del Sur**, las **Nubes de Magallanes** (dos [galaxias vecinas](@galaxias-vecinas)) y el centro de la Vía Láctea en lo alto del cielo.

> Hace unos 12.000 años, la estrella Polar no era la Polar: era Vega. Dentro de otros 12.000 años, por la precesión, Vega volverá a marcar el norte.
""",
    """
For thousands of years, every culture has joined the bright stars with imaginary lines to make figures: animals, heroes, objects. They were used to tell stories, but also to navigate at sea and know when to sow.

## 88 official constellations

In 1922 the International Astronomical Union set **88 constellations** covering the whole sky, like the provinces on a map. About 48 come from the Greek astronomer **Ptolemy** (2nd century), who gathered Babylonian and Greek traditions; those in the southern sky were added from the 16th to the 18th centuries, when European navigators sailed south, which is why they have names like the Telescope, the Air Pump and the Microscope.

The stars of a constellation are not usually close together: they only look that way from Earth. One may be 50 light years away and its neighbour in the sky 2,000.

## The easiest to find

- **Orion** (winter): the hunter, with the three aligned stars of his belt. At top left shines red **Betelgeuse**, a supergiant that will explode one day; at bottom right, bluish **Rigel**. Below the belt the [Orion Nebula](@nebulosas) appears as a small fuzzy patch.
- **The Great Bear** (all year): its seven brightest stars form the **Big Dipper** or Plough. Extend the line joining the two stars at the end of the bowl about five times and you reach **Polaris**, the North Star.
- **The Little Bear**: Polaris is the tip of its tail. It always marks north and barely moves, because it lies almost exactly above Earth's axis of rotation. Its height above the horizon equals your latitude.
- **Cassiopeia** (all year): a "W" or "M" on the opposite side of Polaris from the Big Dipper.
- **The Summer Triangle**: three very bright stars, **Vega** (in Lyra), **Deneb** (in Cygnus) and **Altair** (in Aquila), dominating July and August nights, with the Milky Way running between them.
- **Scorpius** (summer, low in the south): with its red heart, **Antares**, and its curved tail.

!foto osa_mayor | The Great Bear and its most famous asterism, the Big Dipper, which helps you find Polaris.

## The zodiac has 13

The zodiac is the set of constellations the Sun passes through over the year as seen from Earth. Astronomers count **13**, because the Sun also crosses **Ophiuchus**, the serpent bearer, between 29 November and 17 December. On top of that, because of a slow wobble of Earth's axis called **precession**, the dates no longer match those of horoscopes, which were set about 2,000 years ago. Astrology has no scientific basis; astronomy does.

## The southern sky

From the Canary Islands you can see stars that never rise over mainland Spain, and from the southern hemisphere you can see the **Southern Cross**, the **Magellanic Clouds** (two [neighbouring galaxies](@galaxias-vecinas)) and the centre of the Milky Way high overhead.

> About 12,000 years ago the North Star was not Polaris: it was Vega. In another 12,000 years, thanks to precession, Vega will mark north again.
""",
    datos=[("Constelaciones oficiales", "Official constellations", "88 (desde 1922)", "88 (since 1922)"),
           ("La más grande", "Largest", "Hidra", "Hydra"),
           ("La más pequeña", "Smallest", "Cruz del Sur", "Southern Cross"),
           ("Estrella más brillante", "Brightest star", "Sirio, en el Can Mayor", "Sirius, in Canis Major"),
           ("Constelaciones del zodiaco", "Zodiac constellations", "13, con Ofiuco", "13, including Ophiuchus")],
    pie=("La constelación de Orión, con las tres estrellas de su cinturón, la roja Betelgeuse y la azulada Rigel.",
         "The constellation of Orion, with the three stars of its belt, red Betelgeuse and bluish Rigel."),
)

ECLIPSES = F(
    ("eclipses", "eclipses"),
    ("Eclipses", "Eclipses"),
    ("Por qué ocurren, cómo verlos sin riesgo y los grandes eclipses de España: el de agosto de 2026 y el de agosto de 2027.",
     "Why they happen, how to watch them safely and Spain's great eclipses: August 2026 and August 2027."),
    ("eclipse solar, eclipse lunar, eclipse total, eclipse anular, eclipse en España, eclipse 12 de agosto de 2026, eclipse 2 de agosto de 2027, eclipse 2028, gafas de eclipse, corona solar, luna de sangre, Saros",
     "solar eclipse, lunar eclipse, total eclipse, annular eclipse, eclipse in Spain, 12 August 2026 eclipse, 2 August 2027 eclipse, 2028 eclipse, eclipse glasses, solar corona, blood moon, Saros"),
    "sol_eclipse",
    """
Un **eclipse** ocurre cuando el Sol, la Tierra y la Luna se alinean. Es una coincidencia asombrosa: el Sol es unas 400 veces más grande que la Luna, pero también está unas 400 veces más lejos, así que en el cielo los dos parecen del mismo tamaño.

## Eclipses de Sol

La Luna se interpone entre el Sol y la Tierra y su sombra cae sobre una franja de nuestro planeta. Solo pueden ocurrir en **luna nueva**.

- **Total**: la Luna tapa el Sol por completo. Durante unos minutos se hace casi de noche, baja la temperatura, aparecen estrellas y planetas y se ve la **corona solar**, la atmósfera exterior del Sol, como un halo plateado. Solo se ve dentro de una franja estrecha, de unos 100 a 250 km de ancho.
- **Anular**: la Luna está algo más lejos y no llega a tapar todo el Sol; queda un «anillo de fuego».
- **Parcial**: la Luna tapa solo una parte del Sol. Se ve en una zona mucho más amplia.

## Eclipses de Luna

La Tierra se interpone entre el Sol y la Luna, y la Luna entra en nuestra sombra. Solo ocurren en **luna llena** y se ven desde toda la mitad de la Tierra donde es de noche. En un eclipse total la Luna no desaparece: se vuelve **rojiza**, porque la atmósfera terrestre desvía hacia ella la luz roja de todos los amaneceres y atardeceres del mundo. Por eso se habla de «luna de sangre». Se pueden mirar sin ninguna protección.

!foto eclipse_lunar | Eclipse total de Luna: la luz rojiza es la de todos los amaneceres y atardeceres de la Tierra a la vez.

## Cómo mirar un eclipse de Sol sin dañarte la vista

- Usa **gafas de eclipse homologadas** con la norma **ISO 12312-2**, sin rayas ni agujeros.
- **No sirven** las gafas de sol, los cristales ahumados, las radiografías ni los CD.
- Nunca mires con prismáticos, telescopio o cámara sin un **filtro solar** delante del objetivo: concentran la luz y causan lesiones en segundos.
- Un método seguro y sencillo: un **proyector estenopeico**, un agujero pequeño en un cartón que proyecta la imagen del Sol sobre el suelo. Los huecos entre las hojas de un árbol hacen lo mismo y llenan el suelo de pequeños soles mordidos.
- Solo durante la totalidad, cuando el Sol está completamente tapado, se puede mirar sin gafas. En cuanto reaparece el primer destello, hay que volver a ponérselas.

## Los grandes eclipses de España

Después de más de un siglo sin un eclipse total en la península (el último fue en 1905), España vive una racha extraordinaria:

| Fecha | Tipo | Dónde se ve |
|---|---|---|
| 12 de agosto de 2026 | **Total** | Franja del norte y el este peninsular, de Galicia y Asturias a Aragón, la Comunidad Valenciana y Baleares, al atardecer |
| 2 de agosto de 2027 | **Total** | Sur de la península: Cádiz y Málaga, por el estrecho de Gibraltar. Hasta unos 4,5 minutos de totalidad en Tarifa |
| 26 de enero de 2028 | **Anular** | Franja del sur y el oeste peninsular, al atardecer |

El eclipse del **12 de agosto de 2026** ya ha pasado a la historia como el primero total visible en la península en 121 años: se produjo con el Sol muy bajo, poco antes de ponerse, y coincidió con el máximo de las [Perseidas](@lluvias-de-estrellas). El del **2 de agosto de 2027** será uno de los más largos del siglo: en Luxor (Egipto) durará más de seis minutos.

## El ciclo de Saros

Los eclipses se repiten en ciclos de **18 años, 11 días y 8 horas**, el llamado ciclo de Saros, conocido ya por los astrónomos babilonios. Por eso se pueden predecir con siglos de antelación y al segundo.

> En el año 585 a. C., un eclipse total interrumpió una batalla entre lidios y medos, en la actual Turquía. Ambos ejércitos lo tomaron como una señal de los dioses y firmaron la paz. Según Heródoto, el filósofo Tales de Mileto lo había predicho.
""",
    """
An **eclipse** happens when the Sun, Earth and Moon line up. It is an astonishing coincidence: the Sun is about 400 times bigger than the Moon, but also about 400 times farther away, so in the sky the two look the same size.

## Solar eclipses

The Moon passes between the Sun and Earth and its shadow falls on a strip of our planet. They can only happen at **new moon**.

- **Total**: the Moon covers the Sun completely. For a few minutes it gets almost dark, the temperature drops, stars and planets appear and you can see the **solar corona**, the Sun's outer atmosphere, as a silvery halo. It is visible only within a narrow strip about 100 to 250 km wide.
- **Annular**: the Moon is a little farther away and does not cover the whole Sun; a "ring of fire" remains.
- **Partial**: the Moon covers only part of the Sun. It is visible over a much wider area.

## Lunar eclipses

Earth passes between the Sun and the Moon, and the Moon moves into our shadow. They only happen at **full moon** and can be seen from the whole night side of Earth. In a total eclipse the Moon does not disappear: it turns **reddish**, because Earth's atmosphere bends towards it the red light of every sunrise and sunset on the planet. That is why people speak of a "blood moon". They are safe to look at with no protection.

!foto eclipse_lunar | Total lunar eclipse: the reddish light comes from all of Earth's sunrises and sunsets at once.

## How to watch a solar eclipse safely

- Use **certified eclipse glasses** meeting the **ISO 12312-2** standard, with no scratches or holes.
- Sunglasses, smoked glass, X-ray film and CDs **are not safe**.
- Never look through binoculars, a telescope or a camera without a **solar filter** over the front: they concentrate the light and cause injury within seconds.
- A safe, simple method: a **pinhole projector**, a small hole in a piece of card that projects the Sun's image onto the ground. Gaps between the leaves of a tree do the same and fill the ground with little bitten suns.
- Only during totality, when the Sun is completely covered, can you look without glasses. As soon as the first flash reappears, put them back on.

## Spain's great eclipses

After more than a century without a total eclipse on the Spanish mainland (the last was in 1905), Spain is enjoying an extraordinary run:

| Date | Type | Where it is visible |
|---|---|---|
| 12 August 2026 | **Total** | A band across northern and eastern Spain, from Galicia and Asturias to Aragon, Valencia and the Balearics, at sunset |
| 2 August 2027 | **Total** | Southern Spain: Cádiz and Málaga, across the Strait of Gibraltar. Up to about 4.5 minutes of totality in Tarifa |
| 26 January 2028 | **Annular** | A band across southern and western Spain, at sunset |

The eclipse of **12 August 2026** has already gone down in history as the first total eclipse visible from mainland Spain in 121 years: it happened with the Sun very low, shortly before sunset, and coincided with the peak of the [Perseids](@lluvias-de-estrellas). The one on **2 August 2027** will be one of the longest of the century: in Luxor (Egypt) it will last more than six minutes.

## The Saros cycle

Eclipses repeat in cycles of **18 years, 11 days and 8 hours**, the so-called Saros cycle, already known to Babylonian astronomers. That is why they can be predicted centuries ahead, to the second.

> In 585 BC a total eclipse interrupted a battle between the Lydians and the Medes, in what is now Turkey. Both armies took it as a sign from the gods and made peace. According to Herodotus, the philosopher Thales of Miletus had predicted it.
""",
    datos=[("Eclipse solar", "Solar eclipse", "Solo en luna nueva", "Only at new moon"),
           ("Eclipse lunar", "Lunar eclipse", "Solo en luna llena", "Only at full moon"),
           ("Totalidad máxima posible", "Longest possible totality", "≈ 7 min 30 s", "≈ 7 min 30 s"),
           ("Gafas seguras", "Safe glasses", "Norma ISO 12312-2", "ISO 12312-2 standard"),
           ("Próximo total en España", "Next total in Spain", "2 de agosto de 2027", "2 August 2027"),
           ("Ciclo de Saros", "Saros cycle", "18 años, 11 días, 8 horas", "18 years, 11 days, 8 hours")],
    pie=("Eclipse total de Sol: durante la totalidad se ve la corona solar, invisible el resto del tiempo.",
         "Total solar eclipse: during totality the solar corona becomes visible, hidden the rest of the time."),
)

LLUVIAS = F(
    ("lluvias-de-estrellas", "meteor-showers"),
    ("Lluvias de estrellas", "Meteor showers"),
    ("Perseidas, Gemínidas, Cuadrántidas y demás: qué son las estrellas fugaces, cuándo verlas y cómo sacarles partido.",
     "Perseids, Geminids, Quadrantids and more: what shooting stars are, when to see them and how to make the most of them."),
    ("lluvia de estrellas, estrellas fugaces, Perseidas, lágrimas de San Lorenzo, Gemínidas, Cuadrántidas, Leónidas, Oriónidas, Líridas, meteoros, meteoritos, bólidos, radiante, tasa horaria cenital",
     "meteor shower, shooting stars, Perseids, tears of St Lawrence, Geminids, Quadrantids, Leonids, Orionids, Lyrids, meteors, meteorites, fireballs, radiant, zenithal hourly rate"),
    "perseidas",
    """
Las **estrellas fugaces** no son estrellas. Son granitos de polvo, la mayoría más pequeños que un grano de arena, que entran en la atmósfera a entre 11 y 72 km por segundo y se ponen incandescentes a unos 100 km de altura. Lo que vemos es la estela de aire brillante que dejan.

## Por qué hay lluvias

Los cometas, al acercarse al Sol, van soltando polvo a lo largo de su órbita. Cuando la Tierra cruza cada año esa estela, muchos granos entran en la atmósfera a la vez: es una **lluvia de meteoros**. Como todos llegan en paralelo, por perspectiva parecen salir de un mismo punto del cielo, el **radiante**, que da nombre a la lluvia (las Perseidas parecen venir de Perseo; las Gemínidas, de Géminis).

## Las principales del año

| Lluvia | Máximo | Meteoros por hora* | Origen |
|---|---|---|---|
| Cuadrántidas | 3-4 de enero | Hasta 120 | Asteroide 2003 EH1 |
| Líridas | 22-23 de abril | ≈ 18 | Cometa Thatcher |
| Eta Acuáridas | 5-6 de mayo | ≈ 50 (mejor en el sur) | Cometa Halley |
| **Perseidas** | 12-13 de agosto | ≈ 100 | Cometa Swift-Tuttle |
| Oriónidas | 21-22 de octubre | ≈ 20 | Cometa Halley |
| Leónidas | 17-18 de noviembre | ≈ 15 | Cometa Tempel-Tuttle |
| **Gemínidas** | 13-14 de diciembre | ≈ 150 | Asteroide Faetón |

*Cifras en condiciones ideales, con el radiante en lo alto y un cielo muy oscuro. En la práctica se ven menos.

## Las lágrimas de San Lorenzo

Las **Perseidas** son las más populares porque llegan en las noches cálidas de agosto. En España se llaman tradicionalmente las «lágrimas de San Lorenzo», porque el santo se celebra el 10 de agosto, justo antes del máximo. Proceden del cometa **Swift-Tuttle**, de 26 km de diámetro, que pasa cerca del Sol cada 133 años.

Las **Gemínidas** de diciembre son en realidad las más abundantes, y son raras: vienen de un asteroide rocoso, 3200 Faetón, y no de un cometa.

## Consejos para verlas

- Las mejores horas son **de madrugada**, de 2 a 5 de la mañana, cuando nuestro lado de la Tierra mira hacia adelante en su órbita y «choca» de frente con el polvo.
- **No hace falta telescopio ni prismáticos**: abarcan muy poco cielo. Lo mejor es tumbarse en una hamaca o una esterilla y mirar hacia arriba, sin fijarse solo en el radiante.
- Ten paciencia: los meteoros llegan a rachas. Dedica al menos una hora.
- Fíjate en la **fase lunar**: con luna llena, solo se ven los más brillantes.

## Bólidos y meteoritos

A veces entra un fragmento mayor y produce un **bólido**, un meteoro más brillante que Venus que puede iluminar el paisaje y, en ocasiones, explotar. Si un trozo sobrevive y llega al suelo, se llama **meteorito**. Cada año caen a la Tierra unas 17.000 rocas de este tipo, casi todas en el mar o en zonas deshabitadas. Redes de cámaras como la española SPMN vigilan el cielo toda la noche para calcular dónde caen.

> En 1833, las Leónidas produjeron una tormenta de decenas de miles de meteoros por hora sobre Norteamérica. Muchos testigos creyeron que había llegado el fin del mundo. Aquel espectáculo impulsó el estudio científico de los meteoros.
""",
    """
**Shooting stars** are not stars. They are specks of dust, most smaller than a grain of sand, that enter the atmosphere at 11 to 72 km per second and glow white-hot about 100 km up. What we see is the trail of glowing air they leave behind.

## Why showers happen

As comets approach the Sun they shed dust along their orbit. When Earth crosses that trail each year, many grains enter the atmosphere at once: a **meteor shower**. Since they all arrive in parallel, perspective makes them appear to come from one point in the sky, the **radiant**, which names the shower (the Perseids seem to come from Perseus; the Geminids, from Gemini).

## The main showers of the year

| Shower | Peak | Meteors per hour* | Source |
|---|---|---|---|
| Quadrantids | 3–4 January | Up to 120 | Asteroid 2003 EH1 |
| Lyrids | 22–23 April | ≈ 18 | Comet Thatcher |
| Eta Aquariids | 5–6 May | ≈ 50 (better in the south) | Halley's Comet |
| **Perseids** | 12–13 August | ≈ 100 | Comet Swift–Tuttle |
| Orionids | 21–22 October | ≈ 20 | Halley's Comet |
| Leonids | 17–18 November | ≈ 15 | Comet Tempel–Tuttle |
| **Geminids** | 13–14 December | ≈ 150 | Asteroid Phaethon |

*Figures for ideal conditions, with the radiant high and a very dark sky. In practice you see fewer.

## The tears of St Lawrence

The **Perseids** are the most popular because they come on warm August nights. In Spain they are traditionally called the "tears of St Lawrence", because his feast day is 10 August, just before the peak. They come from comet **Swift–Tuttle**, 26 km across, which passes close to the Sun every 133 years.

December's **Geminids** are actually the richest, and they are unusual: they come from a rocky asteroid, 3200 Phaethon, rather than a comet.

## Tips for watching

- The best hours are **before dawn**, from 2 to 5 a.m., when our side of Earth faces forward in its orbit and ploughs head-on into the dust.
- **You do not need a telescope or binoculars**: they cover too little sky. Lie back on a lounger or mat and look up, without staring only at the radiant.
- Be patient: meteors come in bursts. Give it at least an hour.
- Check the **Moon phase**: with a full moon, only the brightest show up.

## Fireballs and meteorites

Sometimes a bigger fragment comes in and produces a **fireball**, a meteor brighter than Venus that can light up the landscape and sometimes explode. If a piece survives and reaches the ground, it is called a **meteorite**. Around 17,000 such rocks fall to Earth each year, nearly all into the sea or uninhabited areas. Camera networks like Spain's SPMN watch the sky all night to work out where they land.

> In 1833 the Leonids produced a storm of tens of thousands of meteors per hour over North America. Many witnesses believed the end of the world had come. The spectacle kick-started the scientific study of meteors.
""",
    datos=[("Altura a la que brillan", "Height where they glow", "≈ 100 km", "≈ 100 km"),
           ("Velocidad", "Speed", "11 a 72 km/s", "11 to 72 km/s"),
           ("Lluvia más abundante", "Richest shower", "Gemínidas (diciembre)", "Geminids (December)"),
           ("Lluvia más popular", "Most popular shower", "Perseidas (agosto)", "Perseids (August)"),
           ("Mejor hora", "Best time", "De 2 a 5 de la madrugada", "2 to 5 a.m.")],
    pie=("Perseidas cruzando el cielo de agosto. Todas parecen salir del mismo punto, el radiante, en la constelación de Perseo.",
         "Perseids streaking across the August sky. They all seem to come from the same point, the radiant, in the constellation Perseus."),
)

TELESCOPIOS_AF = F(
    ("telescopios-para-aficionados", "telescopes-for-beginners"),
    ("Prismáticos y telescopios", "Binoculars and telescopes"),
    ("Qué comprar para empezar, qué se puede ver con cada aparato y los errores más comunes al elegir un telescopio.",
     "What to buy to get started, what you can see with each instrument and the most common mistakes when choosing a telescope."),
    ("telescopio para principiantes, qué telescopio comprar, prismáticos para astronomía, refractor, reflector, dobsoniano, apertura, aumentos, montura ecuatorial, astrofotografía, qué se ve con un telescopio",
     "beginner telescope, which telescope to buy, astronomy binoculars, refractor, reflector, Dobsonian, aperture, magnification, equatorial mount, astrophotography, what you can see through a telescope"),
    "pleyades",
    """
Es tentador empezar comprando un telescopio, pero muchos acaban guardados en un armario tras dos noches frustrantes. El mejor consejo de los astrónomos aficionados es empezar por conocer el cielo a simple vista y con **prismáticos**.

## Los prismáticos: el mejor primer instrumento

Unos prismáticos de **10×50** o **7×50** (el primer número son los aumentos; el segundo, el diámetro de cada lente en milímetros) son baratos, fáciles de usar y muestran muchísimo:

- Los cráteres y mares de la **Luna**.
- Las cuatro **lunas de Júpiter**, como puntitos alineados que cambian cada noche.
- Cúmulos de estrellas como las **Pléyades** o el Pesebre, que con ellos se convierten en un joyero.
- La **galaxia de Andrómeda** como una mancha alargada, a 2,5 millones de años luz.
- Miles de estrellas en la Vía Láctea que a simple vista no se ven.

Apoyarlos en un trípode o en una valla mejora mucho la imagen.

## Lo que importa en un telescopio: la apertura

El dato clave de un telescopio es su **apertura**, el diámetro de la lente o el espejo principal: cuanto mayor, más luz recoge y más detalle muestra. Los **aumentos** importan mucho menos. Como regla, el aumento útil máximo es aproximadamente **el doble de la apertura en milímetros**: un telescopio de 70 mm no da imágenes nítidas a más de 140 aumentos. Desconfía de las cajas que anuncian «¡525 aumentos!» en telescopios pequeños.

## Tipos de telescopio

| Tipo | Cómo funciona | Ventajas | Inconvenientes |
|---|---|---|---|
| Refractor | Lente en la parte delantera | Imagen nítida, sin mantenimiento | Caro por centímetro de apertura |
| Reflector newtoniano | Espejo cóncavo al fondo | Mucha apertura por poco dinero | Hay que alinear los espejos de vez en cuando |
| Dobsoniano | Newtoniano sobre una base giratoria sencilla | El más recomendado para empezar: sencillo y potente | Voluminoso |
| Catadióptrico | Combina espejos y lentes | Compacto, bueno para planetas | Más caro |

Para quien empieza, un **dobsoniano de 150 a 200 mm** suele ser la mejor compra: muestra los anillos de Saturno, las bandas de Júpiter, cientos de cúmulos y nebulosas y muchas galaxias. Las monturas **ecuatoriales** permiten seguir las estrellas, pero son más difíciles de montar; las computerizadas (*GoTo*) apuntan solas a miles de objetos.

## Qué esperar

En un telescopio, las nebulosas y galaxias se ven grises y tenues, no como en las fotos del Hubble, que acumulan luz durante horas. Pero ver con tus propios ojos los anillos de Saturno o la luz que salió de Andrómeda hace 2,5 millones de años tiene una emoción que ninguna foto iguala.

## Astrofotografía

Hoy, con un móvil sobre un trípode y el modo nocturno, se pueden fotografiar la Luna, las constelaciones e incluso la Vía Láctea. Los telescopios «inteligentes», que combinan cámara y montura automática y se manejan desde el móvil, han hecho la astrofotografía más accesible que nunca. Muchos aficionados contribuyen a la ciencia descubriendo supernovas, cometas y asteroides.

## Nunca apuntes al Sol

Mirar el Sol con prismáticos o telescopio sin un **filtro solar certificado** colocado delante causa ceguera permanente en un instante. Nunca uses los filtros que se enroscan en el ocular: pueden romperse con el calor.

> Galileo hizo sus descubrimientos de 1609 y 1610, las lunas de Júpiter, las fases de Venus, los cráteres de la Luna, con telescopios de unos 20 aumentos y peor calidad que los prismáticos más baratos de hoy.
""",
    """
It is tempting to start by buying a telescope, but many end up in a cupboard after two frustrating nights. The best advice from amateur astronomers is to start by getting to know the sky with the naked eye and **binoculars**.

## Binoculars: the best first instrument

A pair of **10×50** or **7×50** binoculars (the first number is the magnification; the second, the diameter of each lens in millimetres) is cheap, easy to use and shows a great deal:

- The **Moon**'s craters and seas.
- Jupiter's four big **moons**, as little aligned dots that change every night.
- Star clusters such as the **Pleiades** or the Beehive, which turn into a jewellery box.
- The **Andromeda Galaxy** as an elongated smudge, 2.5 million light years away.
- Thousands of Milky Way stars invisible to the naked eye.

Resting them on a tripod or a fence greatly improves the view.

## What matters in a telescope: aperture

A telescope's key figure is its **aperture**, the diameter of the main lens or mirror: the larger it is, the more light it collects and the more detail it shows. **Magnification** matters much less. As a rule, the maximum useful magnification is about **twice the aperture in millimetres**: a 70 mm telescope does not give sharp images beyond 140×. Be wary of boxes promising "525× power!" on small telescopes.

## Types of telescope

| Type | How it works | Pros | Cons |
|---|---|---|---|
| Refractor | Lens at the front | Sharp image, no maintenance | Expensive per centimetre of aperture |
| Newtonian reflector | Concave mirror at the back | Lots of aperture for little money | Mirrors need aligning now and then |
| Dobsonian | Newtonian on a simple swivel base | Most recommended for beginners: simple and powerful | Bulky |
| Catadioptric | Combines mirrors and lenses | Compact, good for planets | More expensive |

For beginners, a **150 to 200 mm Dobsonian** is usually the best buy: it shows Saturn's rings, Jupiter's belts, hundreds of clusters and nebulae, and many galaxies. **Equatorial** mounts can track the stars but are harder to set up; computerised (*GoTo*) mounts point by themselves to thousands of objects.

## What to expect

Through a telescope, nebulae and galaxies look grey and faint, not like Hubble photos, which gather light for hours. But seeing Saturn's rings with your own eyes, or light that left Andromeda 2.5 million years ago, has a thrill no photo can match.

## Astrophotography

Today, with a phone on a tripod and night mode, you can photograph the Moon, the constellations and even the Milky Way. "Smart" telescopes, which combine a camera and automatic mount and are controlled from a phone, have made astrophotography more accessible than ever. Many amateurs contribute to science by discovering supernovae, comets and asteroids.

## Never point at the Sun

Looking at the Sun through binoculars or a telescope without a **certified solar filter** over the front causes permanent blindness in an instant. Never use filters that screw into the eyepiece: they can crack from the heat.

> Galileo made his 1609–1610 discoveries, Jupiter's moons, the phases of Venus, the Moon's craters, with telescopes of about 20× and poorer quality than today's cheapest binoculars.
""",
    datos=[("Primer instrumento", "First instrument", "Prismáticos 10×50 o 7×50", "10×50 or 7×50 binoculars"),
           ("Dato clave", "Key figure", "La apertura (mm)", "Aperture (mm)"),
           ("Aumento útil máximo", "Max useful magnification", "≈ 2 × apertura en mm", "≈ 2 × aperture in mm"),
           ("Recomendado para empezar", "Recommended for beginners", "Dobsoniano de 150-200 mm", "150–200 mm Dobsonian"),
           ("Sol", "Sun", "Solo con filtro solar certificado delante", "Only with a certified front solar filter")],
    pie=("Las Pléyades, uno de los objetos más bonitos para ver con prismáticos, a unos 440 años luz.",
         "The Pleiades, one of the loveliest sights through binoculars, about 440 light years away."),
)

CALENDARIO = F(
    ("calendario-astronomico", "astronomy-calendar"),
    ("Calendario astronómico 2026-2028", "Astronomy calendar 2026–2028"),
    ("Las citas del cielo de los próximos meses vistas desde España: lluvias de estrellas, eclipses, planetas y estaciones.",
     "The sky's upcoming events as seen from Spain: meteor showers, eclipses, planets and seasons."),
    ("calendario astronómico, efemérides, eventos astronómicos 2027, cielo de diciembre, oposición de Marte 2027, oposición de Júpiter, oposición de Saturno, eclipse 2027, solsticio, equinoccio, lluvias de estrellas 2027",
     "astronomy calendar, sky events, astronomical events 2027, December sky, Mars opposition 2027, Jupiter opposition, Saturn opposition, 2027 eclipse, solstice, equinox, meteor showers 2027"),
    "luna",
    """
Este calendario recoge los acontecimientos más destacados visibles desde España hasta principios de 2028. Las fechas de las lluvias de estrellas indican la noche del máximo; conviene mirar también una o dos noches antes y después.

## Finales de 2026

| Fecha | Acontecimiento |
|---|---|
| 17-18 de noviembre | Máximo de las **Leónidas** |
| 13-14 de diciembre | Máximo de las **Gemínidas**, la lluvia más abundante del año |
| 21 de diciembre | **Solsticio de invierno**: la noche más larga del año |

## 2027

| Fecha | Acontecimiento |
|---|---|
| 3-4 de enero | Máximo de las **Cuadrántidas** |
| Febrero | **Júpiter en oposición**: toda la noche visible y en su máximo brillo |
| 19 de febrero | **Marte en oposición**: el mejor momento para verlo en dos años, aunque algo pequeño |
| 20 de marzo | **Equinoccio de primavera** |
| 22-23 de abril | Máximo de las **Líridas** |
| 5-6 de mayo | Máximo de las **Eta Acuáridas** |
| 21 de junio | **Solsticio de verano**: el día más largo |
| Julio y agosto | Mejores meses para ver la **Vía Láctea** de madrugada y al anochecer |
| **2 de agosto** | **Eclipse total de Sol** en el sur de España (Cádiz y Málaga); parcial en el resto |
| 12-13 de agosto | Máximo de las **Perseidas** |
| 23 de septiembre | **Equinoccio de otoño** |
| Octubre | **Saturno en oposición**: los anillos de nuevo bien abiertos tras verse de canto en 2025 |
| 21-22 de octubre | Máximo de las **Oriónidas** |
| 17-18 de noviembre | Máximo de las **Leónidas** |
| 13-14 de diciembre | Máximo de las **Gemínidas** |
| 22 de diciembre | **Solsticio de invierno** |

## Principios de 2028

| Fecha | Acontecimiento |
|---|---|
| 3-4 de enero | Máximo de las **Cuadrántidas** |
| **26 de enero** | **Eclipse anular de Sol** al atardecer en el sur y el oeste de la península |

## Qué es una oposición

Un planeta exterior está **en oposición** cuando la Tierra pasa entre él y el Sol. Entonces sale al anochecer, se pone al amanecer, está más cerca de nosotros y brilla más que en ningún otro momento del año. Es la mejor época para observarlo con telescopio. Las oposiciones de Júpiter se repiten cada 13 meses; las de Saturno, cada algo más de un año; las de Marte, solo cada 26 meses.

## Fenómenos de cada mes

Además de estas fechas, cada mes hay una **luna llena**, una **luna nueva** (la mejor para observar estrellas débiles) y pasos visibles de la [Estación Espacial](@estacion-espacial). Venus brilla como «lucero del alba» o «lucero de la tarde» según la época, y siempre se puede usar una app como Stellarium para ver qué hay en el cielo esa misma noche.

> Las fechas del calendario son aproximadas para la hora peninsular. Los eclipses y las ocultaciones se calculan al segundo, pero lo que se ve desde cada sitio depende del horizonte, la meteorología y la contaminación lumínica.
""",
    """
This calendar lists the highlights visible from Spain through early 2028. Meteor shower dates give the night of the peak; it is worth looking one or two nights either side as well.

## Late 2026

| Date | Event |
|---|---|
| 17–18 November | Peak of the **Leonids** |
| 13–14 December | Peak of the **Geminids**, the richest shower of the year |
| 21 December | **Winter solstice**: the longest night of the year |

## 2027

| Date | Event |
|---|---|
| 3–4 January | Peak of the **Quadrantids** |
| February | **Jupiter at opposition**: visible all night and at its brightest |
| 19 February | **Mars at opposition**: the best time to see it in two years, though it looks rather small |
| 20 March | **Spring equinox** |
| 22–23 April | Peak of the **Lyrids** |
| 5–6 May | Peak of the **Eta Aquariids** |
| 21 June | **Summer solstice**: the longest day |
| July and August | Best months to see the **Milky Way** in the early hours and after dusk |
| **2 August** | **Total solar eclipse** in southern Spain (Cádiz and Málaga); partial elsewhere |
| 12–13 August | Peak of the **Perseids** |
| 23 September | **Autumn equinox** |
| October | **Saturn at opposition**: rings opening up again after being edge-on in 2025 |
| 21–22 October | Peak of the **Orionids** |
| 17–18 November | Peak of the **Leonids** |
| 13–14 December | Peak of the **Geminids** |
| 22 December | **Winter solstice** |

## Early 2028

| Date | Event |
|---|---|
| 3–4 January | Peak of the **Quadrantids** |
| **26 January** | **Annular solar eclipse** at sunset over southern and western Spain |

## What an opposition is

An outer planet is **at opposition** when Earth passes between it and the Sun. It then rises at dusk, sets at dawn, is closest to us and shines brighter than at any other time of year. It is the best time to observe it through a telescope. Jupiter's oppositions recur every 13 months; Saturn's, every little over a year; Mars's, only every 26 months.

## Every month

Besides these dates, each month brings a **full moon**, a **new moon** (best for faint stars) and visible passes of the [Space Station](@estacion-espacial). Venus shines as the "morning star" or "evening star" depending on the season, and you can always use an app like Stellarium to see what is in the sky that very night.

> Calendar dates are approximate for mainland Spanish time. Eclipses and occultations are calculated to the second, but what you see from each place depends on the horizon, the weather and light pollution.
""",
    datos=[("Próxima lluvia destacada", "Next major shower", "Gemínidas, 13-14 dic. 2026", "Geminids, 13–14 Dec 2026"),
           ("Oposición de Marte", "Mars opposition", "19 de febrero de 2027", "19 February 2027"),
           ("Eclipse total", "Total eclipse", "2 de agosto de 2027", "2 August 2027"),
           ("Eclipse anular", "Annular eclipse", "26 de enero de 2028", "26 January 2028")],
    pie=("La Luna, la compañera de todas las noches de observación: cada mes cambia de fase y de posición entre las estrellas.",
         "The Moon, companion to every night of stargazing: each month it changes phase and position among the stars."),
)

FICHAS = [EMPEZAR, CONSTELACIONES, ECLIPSES, LLUVIAS, TELESCOPIOS_AF, CALENDARIO]
