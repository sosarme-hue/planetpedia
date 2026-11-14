from universo import F

NEPTUNO = F(
    ("neptuno", "neptune"),
    ("Neptuno", "Neptune"),
    ("El planeta más lejano: un mundo azul intenso con los vientos más rápidos del sistema solar, descubierto gracias a las matemáticas.",
     "The farthest planet: a deep blue world with the fastest winds in the solar system, discovered thanks to mathematics."),
    ("Neptuno, gigante de hielo, planeta más lejano, Urbain Le Verrier, Johann Galle, Tritón, vientos de Neptuno, Gran Mancha Oscura, Voyager 2, lluvia de diamantes",
     "Neptune, ice giant, farthest planet, Urbain Le Verrier, Johann Galle, Triton, Neptune winds, Great Dark Spot, Voyager 2, diamond rain"),
    "neptuno",
    """
Neptuno es el octavo y último planeta del sistema solar, a unos 4.500 millones de kilómetros del Sol: treinta veces más lejos que la Tierra. Desde allí, el Sol se ve como una estrella muy brillante, y su luz tarda más de **cuatro horas** en llegar.

## Descubierto con lápiz y papel

Neptuno es el único planeta que se encontró antes por cálculo que por observación. Los astrónomos notaban que [Urano](@urano) se desviaba de su órbita prevista, como si algo invisible tirara de él. El francés **Urbain Le Verrier** calculó dónde debía estar ese planeta desconocido y envió su predicción a Berlín. La noche del **23 de septiembre de 1846**, Johann Galle lo encontró a menos de un grado del punto indicado.

> Galileo ya había visto Neptuno en 1612 y 1613, pero lo tomó por una estrella. Lo dibujó en sus cuadernos sin saber que tenía delante un planeta.

## Los vientos más rápidos

Aunque recibe muy poca energía del Sol, Neptuno tiene la atmósfera más agitada del sistema solar. Sus vientos alcanzan **2.100 km/h**, más rápidos que la velocidad del sonido en la Tierra. En 1989 la Voyager 2 fotografió la **Gran Mancha Oscura**, una tormenta del tamaño de la Tierra que pocos años después había desaparecido.

Su intenso color azul se debe al metano, como en Urano, aunque las imágenes clásicas de la Voyager exageraron el tono. Reprocesadas en 2024, muestran que los dos gigantes de hielo tienen colores más parecidos de lo que se creía.

## ¿Lluvia de diamantes?

En el interior de Urano y Neptuno, la presión y la temperatura son tan altas que el metano podría descomponerse y el carbono convertirse en **diamante**, que caería lentamente hacia el centro como una lluvia. Se ha reproducido algo parecido en laboratorio con láseres muy potentes.

## Tritón, una luna al revés

Neptuno tiene **16 lunas conocidas**. La mayor, **Tritón**, gira alrededor del planeta en sentido contrario a su rotación, algo que ninguna otra gran luna hace. Eso indica que es un objeto del cinturón de Kuiper, parecido a [Plutón](@planetas-enanos), que Neptuno capturó. Tritón tiene géiseres de nitrógeno que lanzan columnas oscuras a 8 km de altura y una superficie de las más frías conocidas, a −235 °C.

!foto triton | Tritón, la gran luna de Neptuno, en un mosaico de la Voyager 2 (1989).

## Un año larguísimo

Neptuno tarda **165 años** en dar una vuelta al Sol. Desde que se descubrió en 1846 solo ha completado una órbita, que cumplió en julio de 2011. Como Urano, también tiene anillos, finos y oscuros, y uno de ellos tiene unos curiosos «arcos» más brillantes.

> Una única nave ha visitado Neptuno: la Voyager 2, en agosto de 1989, doce años después de su lanzamiento.
""",
    """
Neptune is the eighth and last planet of the solar system, some 4.5 billion kilometres from the Sun: thirty times farther than Earth. From there the Sun looks like a very bright star, and its light takes more than **four hours** to arrive.

## Discovered with pen and paper

Neptune is the only planet found by calculation before it was seen. Astronomers noticed that [Uranus](@urano) was drifting from its predicted orbit, as if something invisible were pulling on it. The Frenchman **Urbain Le Verrier** worked out where that unknown planet should be and sent his prediction to Berlin. On the night of **23 September 1846**, Johann Galle found it less than one degree from the predicted spot.

> Galileo had already seen Neptune in 1612 and 1613, but took it for a star. He sketched it in his notebooks without realising he was looking at a planet.

## The fastest winds

Although it receives very little energy from the Sun, Neptune has the most turbulent atmosphere in the solar system. Its winds reach **2,100 km/h**, faster than the speed of sound on Earth. In 1989 Voyager 2 photographed the **Great Dark Spot**, an Earth-sized storm that had vanished a few years later.

Its deep blue colour comes from methane, as on Uranus, although the classic Voyager images exaggerated the tone. Reprocessed in 2024, they show that the two ice giants are more alike in colour than once thought.

## Diamond rain?

Inside Uranus and Neptune, pressures and temperatures are so high that methane could break down and its carbon turn into **diamond**, slowly sinking towards the centre like rain. Something similar has been reproduced in the laboratory with very powerful lasers.

## Triton, a backwards moon

Neptune has **16 known moons**. The largest, **Triton**, orbits the planet in the opposite direction to its rotation, something no other large moon does. That suggests it is a Kuiper belt object, similar to [Pluto](@planetas-enanos), captured by Neptune. Triton has nitrogen geysers that throw dark plumes 8 km high, and one of the coldest surfaces known, at −235 °C.

!foto triton | Triton, Neptune's large moon, in a Voyager 2 mosaic (1989).

## A very long year

Neptune takes **165 years** to orbit the Sun. Since its discovery in 1846 it has completed just one orbit, which it finished in July 2011. Like Uranus, it also has thin, dark rings, one of which has curious brighter "arcs".

> Only one spacecraft has visited Neptune: Voyager 2, in August 1989, twelve years after its launch.
""",
    datos=[("Diámetro", "Diameter", "49.244 km (3,9 Tierras)", "49,244 km (3.9 Earths)"),
           ("Distancia media al Sol", "Average distance from the Sun", "4.495 millones de km (30 UA)", "4,495 million km (30 AU)"),
           ("Año", "Year", "164,8 años", "164.8 years"),
           ("Día", "Day", "16 h 6 min", "16 h 6 min"),
           ("Vientos máximos", "Top wind speed", "2.100 km/h", "2,100 km/h"),
           ("Temperatura de las nubes", "Cloud-top temperature", "−214 °C", "−214 °C"),
           ("Lunas conocidas", "Known moons", "16", "16"),
           ("Descubrimiento", "Discovery", "Le Verrier y Galle, 1846", "Le Verrier and Galle, 1846")],
    pie=("Neptuno fotografiado por la Voyager 2 en 1989.", "Neptune photographed by Voyager 2 in 1989."),
)

LUNAS = F(
    ("lunas", "moons"),
    ("Las lunas del sistema solar", "Moons of the solar system"),
    ("Volcanes de azufre, océanos ocultos bajo el hielo y lagos de metano: las lunas son algunos de los mundos más asombrosos que conocemos.",
     "Sulphur volcanoes, oceans hidden under ice and methane lakes: moons are some of the most astonishing worlds we know."),
    ("lunas, satélites naturales, Ío, Europa, Ganímedes, Calisto, Titán, Encélado, Tritón, Miranda, océanos subterráneos, vida extraterrestre, lunas de Júpiter, lunas de Saturno",
     "moons, natural satellites, Io, Europa, Ganymede, Callisto, Titan, Enceladus, Triton, Miranda, subsurface oceans, extraterrestrial life, moons of Jupiter, moons of Saturn"),
    "europa",
    """
En el sistema solar se conocen cerca de **300 lunas** que giran alrededor de planetas, y cientos más alrededor de planetas enanos y asteroides. Algunas son simples rocas capturadas de pocos kilómetros; otras son mundos más grandes que Mercurio, con atmósfera, volcanes u océanos. Hoy muchos científicos creen que el mejor lugar para encontrar vida fuera de la Tierra no es un planeta, sino una luna.

## Recuento por planetas

| Planeta | Lunas confirmadas | La mayor |
|---|---|---|
| Mercurio y Venus | 0 | — |
| Tierra | 1 | [La Luna](@luna) |
| Marte | 2 | Fobos |
| Júpiter | 97 | Ganímedes |
| Saturno | 274 | Titán |
| Urano | 29 | Titania |
| Neptuno | 16 | Tritón |

## Ío: el mundo de los volcanes

Ío, una de las lunas de [Júpiter](@jupiter), es el lugar con más actividad volcánica del sistema solar: tiene unos **400 volcanes activos**. La gravedad de Júpiter y de sus lunas vecinas la estira y la comprime sin parar, y ese roce calienta su interior. Algunas de sus erupciones lanzan azufre a 500 km de altura. Su superficie, de amarillos, rojos y blancos, se renueva tan deprisa que no tiene cráteres.

!foto io | Ío en color real, con su superficie cubierta de azufre y lava.

## Europa: un océano bajo el hielo

Europa es un poco más pequeña que nuestra Luna y está cubierta por una corteza de hielo surcada de grietas. Debajo, a unos 15 o 25 km de profundidad, hay un **océano de agua salada** que podría contener el doble de agua que todos los océanos de la Tierra. Agua, energía y química: Europa tiene los ingredientes básicos para la vida. La sonda **Europa Clipper** llegará en 2030 para estudiarla.

## Ganímedes y Calisto

**Ganímedes** es la luna más grande del sistema solar, con 5.268 km de diámetro, más que el planeta Mercurio. Es la única luna con su propio campo magnético, y también esconde un océano. La misión europea **JUICE** se pondrá en órbita a su alrededor en 2034. **Calisto**, su vecina, tiene una de las superficies más antiguas y con más cráteres del sistema solar.

## Titán: una Tierra helada

La mayor luna de [Saturno](@saturno) tiene una atmósfera más densa que la terrestre, formada sobre todo por nitrógeno. En su superficie llueve metano, que forma ríos, lagos y mares, como el mar Kraken, mayor que el Caspio. En 2005 la sonda europea **Huygens** se posó en ella. La NASA prepara **Dragonfly**, un dron que volará de un lugar a otro de Titán a partir de 2034.

!foto encelado | Encélado, la pequeña luna helada de Saturno que lanza chorros de agua al espacio.

## Encélado: géiseres de agua

Con solo 500 km de diámetro, Encélado es una de las superficies más blancas del sistema solar. Cerca de su polo sur, unas grietas llamadas «rayas de tigre» expulsan chorros de vapor y hielo que alimentan uno de los anillos de Saturno. La sonda Cassini voló a través de ellos y encontró **sal, sílice y moléculas orgánicas**, señales de un océano en contacto con roca caliente.

## Tritón y otras rarezas

**Tritón**, la gran luna de [Neptuno](@neptuno), gira al revés y tiene géiseres de nitrógeno. **Miranda**, de Urano, parece montada con piezas que no encajan. **Hiperión**, de Saturno, parece una esponja gigante. Y **Jápeto** tiene una cara blanca y otra negra como el carbón, además de una cordillera que recorre su ecuador como la costura de una nuez.

> Ganímedes es más grande que Mercurio, pero tiene menos de la mitad de su masa: es una mezcla de roca y hielo, mientras que Mercurio es casi todo metal y roca.
""",
    """
Around **300 moons** are known to orbit the planets of the solar system, and hundreds more orbit dwarf planets and asteroids. Some are mere captured rocks a few kilometres across; others are worlds larger than Mercury, with atmospheres, volcanoes or oceans. Many scientists now think the best place to find life beyond Earth is not a planet but a moon.

## Count by planet

| Planet | Confirmed moons | Largest |
|---|---|---|
| Mercury and Venus | 0 | — |
| Earth | 1 | [The Moon](@luna) |
| Mars | 2 | Phobos |
| Jupiter | 97 | Ganymede |
| Saturn | 274 | Titan |
| Uranus | 29 | Titania |
| Neptune | 16 | Triton |

## Io: the volcano world

Io, one of [Jupiter's](@jupiter) moons, is the most volcanically active place in the solar system, with about **400 active volcanoes**. The gravity of Jupiter and its neighbouring moons stretches and squeezes it constantly, and that friction heats its interior. Some eruptions hurl sulphur 500 km high. Its yellow, red and white surface is renewed so quickly that it has no craters.

!foto io | Io in true colour, its surface covered in sulphur and lava.

## Europa: an ocean under the ice

Europa is a little smaller than our Moon and covered by a crust of ice criss-crossed with cracks. Beneath it, some 15 to 25 km down, lies an **ocean of salt water** that could hold twice as much water as all of Earth's oceans. Water, energy and chemistry: Europa has the basic ingredients for life. The **Europa Clipper** probe arrives in 2030 to study it.

## Ganymede and Callisto

**Ganymede** is the largest moon in the solar system, 5,268 km across, bigger than the planet Mercury. It is the only moon with its own magnetic field, and it also hides an ocean. Europe's **JUICE** mission will enter orbit around it in 2034. **Callisto**, its neighbour, has one of the oldest and most cratered surfaces in the solar system.

## Titan: a frozen Earth

[Saturn's](@saturno) largest moon has an atmosphere thicker than Earth's, made mostly of nitrogen. Methane rains on its surface, forming rivers, lakes and seas such as Kraken Mare, larger than the Caspian. In 2005 Europe's **Huygens** probe landed there. NASA is preparing **Dragonfly**, a drone that will hop around Titan from 2034.

!foto encelado | Enceladus, Saturn's small icy moon that sprays jets of water into space.

## Enceladus: water geysers

Only 500 km across, Enceladus has one of the whitest surfaces in the solar system. Near its south pole, cracks called "tiger stripes" eject jets of vapour and ice that feed one of Saturn's rings. The Cassini probe flew through them and found **salt, silica and organic molecules**, signs of an ocean in contact with hot rock.

## Triton and other oddities

**Triton**, [Neptune's](@neptuno) large moon, orbits backwards and has nitrogen geysers. Uranus's **Miranda** looks assembled from pieces that do not fit. Saturn's **Hyperion** looks like a giant sponge. And **Iapetus** has one white face and one as black as coal, plus a ridge running around its equator like the seam of a walnut.

> Ganymede is larger than Mercury but has less than half its mass: it is a mix of rock and ice, while Mercury is almost all metal and rock.
""",
    datos=[("Lunas de planetas conocidas", "Known planetary moons", "≈ 420", "≈ 420"),
           ("La más grande", "Largest", "Ganímedes, 5.268 km", "Ganymede, 5,268 km"),
           ("La más volcánica", "Most volcanic", "Ío", "Io"),
           ("Con atmósfera densa", "With a thick atmosphere", "Titán", "Titan"),
           ("Con océanos probables", "Likely oceans", "Europa, Ganímedes, Calisto, Encélado, Titán", "Europa, Ganymede, Callisto, Enceladus, Titan"),
           ("Planeta con más lunas", "Planet with most moons", "Saturno (274)", "Saturn (274)")],
    pie=("Europa, la luna helada de Júpiter, en una imagen de la sonda Galileo.", "Europa, Jupiter's icy moon, in an image from the Galileo probe."),
)

ENANOS = F(
    ("planetas-enanos", "dwarf-planets"),
    ("Plutón y los planetas enanos", "Pluto and the dwarf planets"),
    ("Plutón, Ceres, Eris, Haumea y Makemake: mundos redondos que no llegan a planetas, y el cinturón de Kuiper donde viven casi todos.",
     "Pluto, Ceres, Eris, Haumea and Makemake: round worlds that fall short of being planets, and the Kuiper belt where most of them live."),
    ("planetas enanos, Plutón, Ceres, Eris, Haumea, Makemake, cinturón de Kuiper, New Horizons, Dawn, Caronte, Arrokoth, por qué Plutón no es un planeta, Unión Astronómica Internacional",
     "dwarf planets, Pluto, Ceres, Eris, Haumea, Makemake, Kuiper belt, New Horizons, Dawn, Charon, Arrokoth, why Pluto is not a planet, International Astronomical Union"),
    "pluton",
    """
Durante 76 años, Plutón fue el noveno planeta. En 2006 la **Unión Astronómica Internacional** definió por primera vez qué es un planeta, y Plutón quedó fuera. Desde entonces es un **planeta enano**, una categoría que comparte con al menos otros cuatro mundos.

## ¿Por qué Plutón ya no es un planeta?

Según la definición de 2006, un planeta debe cumplir tres condiciones:

- Girar alrededor del Sol.
- Tener masa suficiente para que su gravedad lo haga casi redondo.
- Haber «limpiado» su órbita de otros objetos de tamaño parecido.

Plutón cumple las dos primeras, pero no la tercera: comparte su zona con miles de cuerpos del **cinturón de Kuiper**. El detonante fue el descubrimiento de **Eris** en 2005, un mundo de tamaño casi idéntico. O se aceptaba un décimo planeta, y probablemente muchos más, o había que crear una nueva categoría.

## Plutón, de cerca

Cuando la sonda **New Horizons** pasó junto a Plutón el 14 de julio de 2015, después de nueve años de viaje, descubrió un mundo mucho más vivo de lo esperado. Su rasgo más famoso es un enorme **corazón** blanco, la región Tombaugh, cuya mitad izquierda es un glaciar de nitrógeno helado llamado Sputnik Planitia. También tiene montañas de hielo de agua de 3.500 metros, una atmósfera fina con capas de neblina azul y quizá un océano bajo la superficie.

Su luna **Caronte** es tan grande, la mitad de Plutón, que ambos giran alrededor de un punto situado entre los dos. Siempre se muestran la misma cara mutuamente.

## Los cinco reconocidos

| Planeta enano | Dónde está | Diámetro | Descubierto |
|---|---|---|---|
| Ceres | Cinturón de asteroides | 940 km | 1801 |
| Plutón | Cinturón de Kuiper | 2.377 km | 1930 |
| Haumea | Cinturón de Kuiper | ≈ 1.600 km (alargado) | 2004 |
| Makemake | Cinturón de Kuiper | ≈ 1.430 km | 2005 |
| Eris | Disco disperso | 2.326 km | 2005 |

!foto ceres | Ceres, el planeta enano del cinturón de asteroides, fotografiado por la sonda Dawn. Las manchas brillantes son depósitos de sal.

## Ceres, el más cercano

**Ceres** fue el primer objeto descubierto en el cinturón de asteroides, por el italiano Giuseppe Piazzi el 1 de enero de 1801. Durante medio siglo se le consideró un planeta. La sonda **Dawn** lo orbitó entre 2015 y 2018 y encontró manchas brillantes de sal en el cráter Occator, restos de agua salada que subió desde el interior.

## El cinturón de Kuiper

Más allá de Neptuno, entre 30 y 50 veces la distancia de la Tierra al Sol, se extiende un anillo de cuerpos helados restos de la formación del sistema solar. Además de los planetas enanos, allí está **Arrokoth**, el objeto más lejano visitado por una nave: New Horizons pasó junto a él el 1 de enero de 2019. Es una especie de muñeco de nieve formado por dos bolas que se unieron suavemente.

!foto arrokoth | Arrokoth, a 6.600 millones de km del Sol, el objeto más lejano fotografiado de cerca.

> Plutón fue descubierto en 1930 por Clyde Tombaugh, un joven de 24 años sin título universitario. Parte de sus cenizas viaja a bordo de New Horizons, la nave que por fin le hizo una foto de cerca.

> El nombre de Plutón lo propuso una niña inglesa de 11 años, Venetia Burney, mientras desayunaba con su abuelo.
""",
    """
For 76 years Pluto was the ninth planet. In 2006 the **International Astronomical Union** defined what a planet is for the first time, and Pluto was left out. Since then it has been a **dwarf planet**, a category it shares with at least four other worlds.

## Why is Pluto no longer a planet?

Under the 2006 definition, a planet must meet three conditions:

- Orbit the Sun.
- Have enough mass for its gravity to make it nearly round.
- Have "cleared" its orbit of other objects of similar size.

Pluto meets the first two but not the third: it shares its zone with thousands of bodies in the **Kuiper belt**. The trigger was the discovery of **Eris** in 2005, a world of almost identical size. Either a tenth planet was accepted, and probably many more, or a new category was needed.

## Pluto up close

When the **New Horizons** probe flew past Pluto on 14 July 2015, after a nine-year journey, it found a far livelier world than expected. Its most famous feature is a huge white **heart**, Tombaugh Regio, whose left half is a glacier of frozen nitrogen called Sputnik Planitia. It also has water-ice mountains 3,500 metres high, a thin atmosphere with layers of blue haze and perhaps an ocean beneath its surface.

Its moon **Charon** is so large, half Pluto's size, that the two orbit a point between them. They always show each other the same face.

## The five recognised

| Dwarf planet | Where it is | Diameter | Discovered |
|---|---|---|---|
| Ceres | Asteroid belt | 940 km | 1801 |
| Pluto | Kuiper belt | 2,377 km | 1930 |
| Haumea | Kuiper belt | ≈ 1,600 km (elongated) | 2004 |
| Makemake | Kuiper belt | ≈ 1,430 km | 2005 |
| Eris | Scattered disc | 2,326 km | 2005 |

!foto ceres | Ceres, the dwarf planet in the asteroid belt, photographed by the Dawn probe. The bright spots are salt deposits.

## Ceres, the closest

**Ceres** was the first object discovered in the asteroid belt, by the Italian Giuseppe Piazzi on 1 January 1801. For half a century it was considered a planet. The **Dawn** probe orbited it from 2015 to 2018 and found bright patches of salt in Occator crater, the remains of brine that rose from the interior.

## The Kuiper belt

Beyond Neptune, between 30 and 50 times the Earth–Sun distance, lies a ring of icy bodies left over from the formation of the solar system. Besides the dwarf planets, it is home to **Arrokoth**, the most distant object ever visited by a spacecraft: New Horizons flew past it on 1 January 2019. It looks like a snowman made of two balls that gently stuck together.

!foto arrokoth | Arrokoth, 6.6 billion km from the Sun, the most distant object ever photographed up close.

> Pluto was discovered in 1930 by Clyde Tombaugh, a 24-year-old with no university degree. Some of his ashes are travelling aboard New Horizons, the spacecraft that finally photographed it up close.

> Pluto's name was suggested by an 11-year-old English girl, Venetia Burney, over breakfast with her grandfather.
""",
    datos=[("Plutón: diámetro", "Pluto: diameter", "2.377 km", "2,377 km"),
           ("Plutón: año", "Pluto: year", "248 años", "248 years"),
           ("Plutón: temperatura", "Pluto: temperature", "≈ −230 °C", "≈ −230 °C"),
           ("Plutón: lunas", "Pluto: moons", "5 (Caronte, Nix, Hidra, Cerbero, Estigia)", "5 (Charon, Nix, Hydra, Kerberos, Styx)"),
           ("Reclasificado", "Reclassified", "24 de agosto de 2006", "24 August 2006"),
           ("Visita de New Horizons", "New Horizons flyby", "14 de julio de 2015", "14 July 2015")],
    pie=("Plutón en color real, fotografiado por New Horizons en 2015. Se ve su famoso «corazón».",
         "Pluto in true colour, photographed by New Horizons in 2015, showing its famous \"heart\"."),
)

MENORES = F(
    ("asteroides-y-cometas", "asteroids-and-comets"),
    ("Asteroides, cometas y meteoritos", "Asteroids, comets and meteorites"),
    ("Las piezas sobrantes del sistema solar: rocas, bolas de hielo sucio y las estrellas fugaces que caen cada noche.",
     "The leftover pieces of the solar system: rocks, dirty snowballs and the shooting stars that fall every night."),
    ("asteroides, cometas, meteoritos, meteoros, estrellas fugaces, cinturón de asteroides, Vesta, Bennu, Apophis, DART, Rosetta, cometa Halley, Hale-Bopp, nube de Oort, impacto de asteroide, dinosaurios, Tunguska, Cheliábinsk",
     "asteroids, comets, meteorites, meteors, shooting stars, asteroid belt, Vesta, Bennu, Apophis, DART, Rosetta, Halley's comet, Hale-Bopp, Oort cloud, asteroid impact, dinosaurs, Tunguska, Chelyabinsk"),
    "cometa_67p",
    """
Además del Sol, los planetas y sus lunas, el sistema solar está lleno de cuerpos pequeños: restos de los ladrillos con los que se construyeron los planetas. Estudiarlos es como abrir una cápsula del tiempo de hace 4.600 millones de años.

## Asteroides

Los asteroides son cuerpos rocosos o metálicos, desde pocos metros hasta cientos de kilómetros. Se han catalogado **más de 1,4 millones**. La mayoría se concentra en el **cinturón de asteroides**, entre Marte y Júpiter, donde la gravedad del gigante impidió que llegaran a formar un planeta. Aun así, están muy separados: si viajaras por el cinturón, probablemente no verías ninguno a simple vista.

El mayor es [Ceres](@planetas-enanos), considerado planeta enano. Le siguen **Vesta**, con una montaña de 22 km en su polo sur, y Palas. Algunos asteroides tienen sus propias lunas, como Ida, que tiene a la pequeña Dáctilo.

!foto vesta | Vesta, el segundo cuerpo más grande del cinturón de asteroides, fotografiado por la sonda Dawn.

## Muestras traídas a la Tierra

Japón trajo polvo del asteroide Itokawa (2010) y de Ryugu (2020) con sus sondas **Hayabusa**. La NASA trajo en 2023 unos 120 gramos del asteroide **Bennu** con la sonda OSIRIS-REx. En ellos se han encontrado aminoácidos y sales formadas en agua: algunos ingredientes de la vida pudieron llegar a la Tierra a bordo de asteroides.

## Cometas

Los cometas son bolas de hielo sucio, polvo y roca de pocos kilómetros. Vienen de las regiones más lejanas del sistema solar, el cinturón de Kuiper y la nube de Oort. Cuando uno se acerca al Sol, el hielo se convierte en gas y forma una **coma** brillante y dos **colas** que pueden medir millones de kilómetros: una de polvo, curvada, y otra de gas, siempre apuntando en sentido contrario al Sol.

- El **cometa Halley** vuelve cada 76 años. Su última visita fue en 1986 y la próxima será en **2061**.
- El **Hale-Bopp** fue visible a simple vista durante 18 meses en 1996 y 1997.
- En 2014 la sonda europea **Rosetta** se puso en órbita alrededor del cometa 67P y dejó caer sobre él el módulo **Philae**, el primer aterrizaje en un cometa.

!foto hale_bopp | El cometa Hale-Bopp en 1997, con su cola de polvo blanca y la de gas, azulada.

## Meteoros y meteoritos

Cuando un pequeño fragmento de roca entra en la atmósfera a decenas de kilómetros por segundo, se calienta y deja una estela luminosa: un **meteoro** o estrella fugaz. Si algún trozo sobrevive y llega al suelo se llama **meteorito**. Las **lluvias de estrellas**, como las Perseidas de agosto, ocurren cuando la Tierra cruza la estela de polvo que dejó un cometa.

## Cuando caen del cielo

- Hace **66 millones de años**, un asteroide de unos 10 km cayó en la península de Yucatán (México), formó el cráter de Chicxulub y provocó la extinción de los dinosaurios no avianos.
- En **1908**, la explosión de un objeto sobre **Tunguska** (Siberia) arrasó 2.000 km² de bosque.
- En **2013**, un meteoro de 20 metros estalló sobre **Cheliábinsk** (Rusia); la onda expansiva rompió miles de ventanas.

## Defensa planetaria

En septiembre de 2022, la misión **DART** de la NASA chocó a propósito contra el pequeño asteroide Dimorphos y logró cambiar su órbita: fue la primera vez que la humanidad desvió un cuerpo celeste. La misión europea **Hera** llega en 2026 para estudiar el resultado. El asteroide **Apophis**, de 340 metros, pasará el 13 de abril de 2029 a solo 32.000 km de la Tierra, más cerca que algunos satélites, sin peligro de choque.

> Se calcula que cada día caen sobre la Tierra decenas de toneladas de material del espacio, casi todo en forma de polvo. Parte del polvo que hay en tu casa podría venir del espacio.
""",
    """
Besides the Sun, the planets and their moons, the solar system is full of small bodies: leftovers of the building blocks the planets were made from. Studying them is like opening a time capsule from 4.6 billion years ago.

## Asteroids

Asteroids are rocky or metallic bodies, from a few metres to hundreds of kilometres across. **More than 1.4 million** have been catalogued. Most are found in the **asteroid belt**, between Mars and Jupiter, where the giant's gravity stopped them from forming a planet. Even so, they are far apart: if you travelled through the belt, you probably would not see a single one with the naked eye.

The largest is [Ceres](@planetas-enanos), classed as a dwarf planet. Next come **Vesta**, with a 22 km mountain at its south pole, and Pallas. Some asteroids have moons of their own, like Ida with little Dactyl.

!foto vesta | Vesta, the second-largest body in the asteroid belt, photographed by the Dawn probe.

## Samples brought to Earth

Japan brought back dust from asteroid Itokawa (2010) and from Ryugu (2020) with its **Hayabusa** probes. In 2023 NASA returned about 120 grams of asteroid **Bennu** with the OSIRIS-REx probe. Amino acids and salts formed in water have been found in them: some of the ingredients of life may have reached Earth aboard asteroids.

## Comets

Comets are dirty snowballs of ice, dust and rock a few kilometres across. They come from the most distant regions of the solar system, the Kuiper belt and the Oort cloud. When one approaches the Sun, its ice turns to gas and forms a bright **coma** and two **tails** that can stretch for millions of kilometres: a curved dust tail and a gas tail that always points away from the Sun.

- **Halley's comet** returns every 76 years. Its last visit was in 1986 and the next will be in **2061**.
- **Hale–Bopp** was visible to the naked eye for 18 months in 1996 and 1997.
- In 2014 Europe's **Rosetta** probe went into orbit around comet 67P and dropped the **Philae** lander onto it, the first landing on a comet.

!foto hale_bopp | Comet Hale–Bopp in 1997, with its white dust tail and its bluish gas tail.

## Meteors and meteorites

When a small fragment of rock enters the atmosphere at tens of kilometres per second, it heats up and leaves a glowing trail: a **meteor** or shooting star. If a piece survives and reaches the ground it is called a **meteorite**. **Meteor showers**, like the Perseids in August, happen when Earth crosses the trail of dust left by a comet.

## When they fall from the sky

- **66 million years ago**, an asteroid about 10 km wide struck the Yucatán peninsula (Mexico), formed the Chicxulub crater and caused the extinction of the non-avian dinosaurs.
- In **1908**, an object exploded over **Tunguska** (Siberia) and flattened 2,000 km² of forest.
- In **2013**, a 20-metre meteor burst over **Chelyabinsk** (Russia); the shock wave shattered thousands of windows.

## Planetary defence

In September 2022, NASA's **DART** mission deliberately crashed into the small asteroid Dimorphos and changed its orbit: the first time humanity moved a celestial body. Europe's **Hera** mission arrives in 2026 to study the result. Asteroid **Apophis**, 340 metres wide, will pass just 32,000 km from Earth on 13 April 2029, closer than some satellites, with no risk of impact.

> Tens of tonnes of material from space are estimated to fall on Earth every day, almost all of it as dust. Some of the dust in your home could have come from space.
""",
    datos=[("Asteroides catalogados", "Catalogued asteroids", "Más de 1,4 millones", "More than 1.4 million"),
           ("Asteroide mayor", "Largest asteroid", "Ceres, 940 km", "Ceres, 940 km"),
           ("Cometas conocidos", "Known comets", "Más de 4.000", "More than 4,000"),
           ("Próximo paso del Halley", "Halley's next return", "2061", "2061"),
           ("Primera desviación de un asteroide", "First asteroid deflection", "DART, 2022", "DART, 2022"),
           ("Paso de Apophis", "Apophis flyby", "13 de abril de 2029", "13 April 2029")],
    pie=("El cometa 67P/Churiumov-Guerasimenko, fotografiado por la sonda Rosetta en 2014.",
         "Comet 67P/Churyumov–Gerasimenko, photographed by the Rosetta probe in 2014."),
)

FICHAS = [NEPTUNO, LUNAS, ENANOS, MENORES]
