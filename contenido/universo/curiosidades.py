from universo import F

SLUG = ("curiosidades", "curiosities")
TITULO = ("Curiosidades y cifras", "Curiosities and numbers")
RESUMEN = ("Simuladores, récords, distancias, anécdotas, descubrimientos sorprendentes y falsos mitos sobre el universo.",
           "Simulators, records, distances, anecdotes, surprising discoveries and myths about the universe.")
CLAVES = ("curiosidades del universo, datos curiosos del espacio, cifras del universo, récords del universo, simuladores, distancias en el universo, anécdotas de astronomía, mitos del espacio",
          "universe curiosities, fun space facts, universe numbers, cosmic records, simulators, distances in the universe, astronomy anecdotes, space myths")
FOTO = "campo_hubble"
INTRO = ("""
El universo está lleno de cifras que marean y de historias que parecen inventadas. Aquí las hemos reunido: simuladores para calcular tu peso en Júpiter o tu edad en Marte, los récords del cosmos, cómo se miden las distancias, las mejores anécdotas de la historia de la astronomía y los descubrimientos que más han sorprendido a los científicos.
""", """
The universe is full of dizzying numbers and stories that sound made up. We have gathered them here: simulators to work out your weight on Jupiter or your age on Mars, the records of the cosmos, how distances are measured, the best anecdotes in the history of astronomy and the discoveries that have most surprised scientists.
""")

SIMULADORES = F(
    ("simuladores", "simulators"),
    ("Simuladores del universo", "Universe simulators"),
    ("Calcula tu peso en otros mundos, tu edad en cada planeta, cuánto tardarías en llegar a las estrellas y la escala real del sistema solar.",
     "Work out your weight on other worlds, your age on each planet, how long it would take to reach the stars and the true scale of the solar system."),
    ("simulador sistema solar, peso en otros planetas, cuánto pesaría en la Luna, edad en otros planetas, cuánto se tarda en llegar a Marte, sistema solar a escala, tamaño de los planetas, calculadora espacial",
     "solar system simulator, weight on other planets, how much would I weigh on the Moon, age on other planets, how long to get to Mars, solar system to scale, planet sizes, space calculator"),
    "punto_azul",
    """
Las cifras del universo son tan grandes que cuesta imaginarlas. Estos simuladores te ayudan a ponerlas a escala humana. Todos funcionan directamente en tu navegador.

## Tu peso en otros mundos

Lo que marca una báscula depende de la gravedad del lugar donde estás. Tu masa, la cantidad de materia que tienes, es la misma en todas partes; lo que cambia es la fuerza con la que cada mundo te atrae.

!sim peso

En la Luna podrías saltar seis veces más alto. En Júpiter, en cambio, te costaría incluso ponerte en pie. Y en la superficie del Sol, si pudieras estar allí, pesarías casi 28 veces más que en casa.

## Tu edad en cada planeta

Un año es el tiempo que un planeta tarda en dar una vuelta completa al Sol. Cuanto más lejos está, más largo es su año. En Mercurio celebrarías cuatro cumpleaños por cada uno terrestre; en Neptuno, probablemente ninguno en toda tu vida.

!sim edad

## ¿Cuánto se tarda en llegar?

Las distancias en el espacio son tan grandes que incluso la luz, lo más rápido que existe, tarda años en recorrerlas. Compara cuánto se tardaría con distintos medios de transporte.

!sim viaje

## El sistema solar a escala

Casi todos los dibujos del sistema solar engañan: ponen los planetas muy juntos y muy grandes para que quepan en la página. A escala real, el sistema solar es sobre todo espacio vacío.

!sim escala

## Los tamaños comparados

!sim tamanos

## Las órbitas en movimiento

!sim orbitas

> Si la Tierra fuera del tamaño de una canica, el Sol sería una pelota de playa a unos 140 metros, y la estrella más cercana, otra pelota situada a unos 38.000 kilómetros.
""",
    """
The numbers of the universe are so large they are hard to imagine. These simulators help you bring them down to a human scale. They all work right in your browser.

## Your weight on other worlds

What a scale shows depends on the gravity where you stand. Your mass, the amount of matter you are made of, is the same everywhere; what changes is how strongly each world pulls on you.

!sim peso

On the Moon you could jump six times higher. On Jupiter, by contrast, you would struggle even to stand up. And on the surface of the Sun, if you could be there, you would weigh almost 28 times more than at home.

## Your age on each planet

A year is the time a planet takes to travel once around the Sun. The farther away it is, the longer its year. On Mercury you would celebrate four birthdays for every one on Earth; on Neptune, probably none in your whole life.

!sim edad

## How long would it take?

Distances in space are so vast that even light, the fastest thing there is, takes years to cross them. Compare how long the trip would take with different kinds of transport.

!sim viaje

## The solar system to scale

Almost every drawing of the solar system is misleading: it shows the planets close together and very large so they fit on the page. At true scale, the solar system is mostly empty space.

!sim escala

## Sizes compared

!sim tamanos

## Orbits in motion

!sim orbitas

> If Earth were the size of a marble, the Sun would be a beach ball about 140 metres away, and the nearest star another beach ball some 38,000 kilometres away.
""",
    pie=("La Tierra vista por la Voyager 1 desde 6.000 millones de km: el punto azul dentro del rayo de luz.",
         "Earth seen by Voyager 1 from 6 billion km away: the blue dot inside the ray of light."),
)

RECORDS = F(
    ("cifras-y-records", "numbers-and-records"),
    ("Cifras y récords del universo", "Numbers and records of the universe"),
    ("Lo más grande, lo más caliente, lo más rápido y lo más lejano: los récords del cosmos en una sola página.",
     "The biggest, the hottest, the fastest and the farthest: the records of the cosmos on a single page."),
    ("récords del universo, estrella más grande, planeta más grande, lugar más frío del universo, objeto más lejano, galaxia más lejana, agujero negro más grande, cifras astronómicas, cuántas estrellas hay",
     "universe records, biggest star, largest planet, coldest place in the universe, most distant object, most distant galaxy, biggest black hole, astronomical numbers, how many stars are there"),
    "agujero_m87",
    """
El universo bate récords que desafían la imaginación. Estos son algunos de los más asombrosos que conocemos hoy, aunque muchos cambian cada pocos años gracias a nuevos telescopios.

## En el sistema solar

| Récord | Quién lo tiene | Cifra |
|---|---|---|
| Planeta más grande | [Júpiter](@jupiter) | 139.820 km de diámetro |
| Planeta más caliente | [Venus](@venus) | 465 °C de media |
| Planeta más frío | [Urano](@urano) | −224 °C |
| Día más corto | Júpiter | 9 h 56 min |
| Día más largo | Venus | 243 días terrestres |
| Vientos más rápidos | [Neptuno](@neptuno) | 2.100 km/h |
| Volcán más alto | Olympus Mons ([Marte](@marte)) | ≈ 22 km |
| Luna más grande | Ganímedes | 5.268 km |
| Planeta con más lunas | [Saturno](@saturno) | 274 |
| Objeto visitado más lejano | Arrokoth | 6.600 millones de km |

## Estrellas y agujeros negros

- **Estrella más grande conocida**: candidatas como **UY Scuti** o **Stephenson 2-18**, con un radio de 1.700 a 2.150 veces el del Sol. Si se pusiera una en el lugar del Sol, su superficie llegaría más allá de la órbita de Júpiter o incluso de Saturno.
- **Estrella más masiva**: **R136a1**, en la Gran Nube de Magallanes, con unas 200 masas solares.
- **Estrella más cercana**: [Próxima Centauri](@vida-de-las-estrellas), a 4,24 años luz.
- **Estrella más brillante del cielo nocturno**: Sirio, a 8,6 años luz.
- **Agujero negro más grande**: los de algunos cuásares, como **TON 618**, se estiman en decenas de miles de millones de masas solares.
- **Objeto más denso que no es agujero negro**: las estrellas de neutrones. Una cucharadita de su materia pesaría unos 1.000 millones de toneladas.

## Galaxias y universo

- **Galaxia más lejana confirmada**: el telescopio James Webb ha confirmado galaxias como **MoM-z14**, cuya luz salió cuando el universo tenía unos 280 millones de años.
- **Galaxia grande más cercana**: [Andrómeda](@galaxias-vecinas), a 2,5 millones de años luz. Se ve a simple vista desde lugares oscuros.
- **Estructura más grande**: supercúmulos y «murallas» de galaxias de más de mil millones de años luz, como la Gran Muralla Hércules-Corona Boreal.
- **Lugar natural más frío conocido**: la **nebulosa del Bumerán**, a −272 °C, solo un grado por encima del cero absoluto y más fría que el propio fondo cósmico.
- **Temperatura más alta**: en los primeros instantes del Big Bang se alcanzaron billones de grados.

## Cifras que dan vértigo

- En el universo observable hay, según las estimaciones, unos **2 billones de galaxias** y más estrellas que granos de arena en todas las playas de la Tierra.
- La Vía Láctea tiene entre **100.000 y 400.000 millones de estrellas**.
- El universo observable mide unos **93.000 millones de años luz** de diámetro.
- Cada segundo, la Tierra recorre **30 kilómetros** en su órbita, y el Sol arrastra todo el sistema solar a **230 km/s** alrededor del centro de la galaxia.

!foto bala | El cúmulo Bala: dos cúmulos de galaxias que chocaron. En azul, la masa calculada; en rosa, el gas caliente. Es una de las pruebas de la materia oscura.

> El récord humano de distancia lo tiene la tripulación del Apolo 13, que en 1970 llegó a 400.171 km de la Tierra al rodear la Luna en su accidentado viaje.
""",
    """
The universe breaks records that defy the imagination. These are some of the most astonishing we know today, although many change every few years thanks to new telescopes.

## In the solar system

| Record | Holder | Figure |
|---|---|---|
| Largest planet | [Jupiter](@jupiter) | 139,820 km across |
| Hottest planet | [Venus](@venus) | 465 °C on average |
| Coldest planet | [Uranus](@urano) | −224 °C |
| Shortest day | Jupiter | 9 h 56 min |
| Longest day | Venus | 243 Earth days |
| Fastest winds | [Neptune](@neptuno) | 2,100 km/h |
| Highest volcano | Olympus Mons ([Mars](@marte)) | ≈ 22 km |
| Largest moon | Ganymede | 5,268 km |
| Planet with most moons | [Saturn](@saturno) | 274 |
| Most distant object visited | Arrokoth | 6.6 billion km |

## Stars and black holes

- **Largest known star**: candidates such as **UY Scuti** or **Stephenson 2-18**, with a radius 1,700 to 2,150 times the Sun's. Placed where the Sun is, its surface would extend beyond the orbit of Jupiter or even Saturn.
- **Most massive star**: **R136a1**, in the Large Magellanic Cloud, at about 200 solar masses.
- **Nearest star**: [Proxima Centauri](@vida-de-las-estrellas), 4.24 light years away.
- **Brightest star in the night sky**: Sirius, 8.6 light years away.
- **Largest black hole**: those powering some quasars, such as **TON 618**, are estimated at tens of billions of solar masses.
- **Densest object that is not a black hole**: neutron stars. A teaspoon of their matter would weigh about a billion tonnes.

## Galaxies and the universe

- **Most distant confirmed galaxy**: the James Webb telescope has confirmed galaxies such as **MoM-z14**, whose light set out when the universe was about 280 million years old.
- **Nearest large galaxy**: [Andromeda](@galaxias-vecinas), 2.5 million light years away. It can be seen with the naked eye from dark sites.
- **Largest structure**: superclusters and "walls" of galaxies more than a billion light years long, like the Hercules–Corona Borealis Great Wall.
- **Coldest known natural place**: the **Boomerang Nebula**, at −272 °C, just one degree above absolute zero and colder than the cosmic background itself.
- **Highest temperature**: in the first instants of the Big Bang, trillions of degrees were reached.

## Dizzying numbers

- The observable universe is estimated to contain about **2 trillion galaxies** and more stars than grains of sand on all of Earth's beaches.
- The Milky Way holds between **100 and 400 billion stars**.
- The observable universe is about **93 billion light years** across.
- Every second, Earth travels **30 kilometres** along its orbit, and the Sun carries the whole solar system at **230 km/s** around the centre of the galaxy.

!foto bala | The Bullet Cluster: two clusters of galaxies that collided. In blue, the calculated mass; in pink, the hot gas. It is one of the pieces of evidence for dark matter.

> The human distance record belongs to the crew of Apollo 13, who in 1970 reached 400,171 km from Earth while looping around the Moon on their troubled journey.
""",
    pie=("La primera imagen de un agujero negro, en el centro de la galaxia M87, obtenida por el Event Horizon Telescope en 2019.",
         "The first image of a black hole, at the centre of galaxy M87, obtained by the Event Horizon Telescope in 2019."),
)

DISTANCIAS = F(
    ("distancias", "distances"),
    ("Distancias y escalas del universo", "Distances and scales of the universe"),
    ("Unidad astronómica, año luz y pársec: cómo se miden las distancias imposibles y cómo hacerse una idea de ellas.",
     "Astronomical unit, light year and parsec: how impossible distances are measured and how to picture them."),
    ("distancias en el universo, año luz, qué es un año luz, unidad astronómica, pársec, paralaje, escala del universo, distancia a las estrellas, distancia a la Luna, tamaño del universo observable",
     "distances in the universe, light year, what is a light year, astronomical unit, parsec, parallax, scale of the universe, distance to the stars, distance to the Moon, size of the observable universe"),
    "via_lactea",
    """
En el espacio, los kilómetros se quedan pequeños enseguida. Para hablar de distancias astronómicas se usan unidades especiales, y para entenderlas lo mejor es compararlas con cosas conocidas.

## Las unidades del cosmos

- **Unidad astronómica (UA)**: la distancia media entre la Tierra y el Sol, **149.597.870,7 km**. Se usa dentro del sistema solar: Júpiter está a 5,2 UA y Neptuno a 30 UA.
- **Año luz**: la distancia que recorre la luz en un año, unos **9,46 billones de kilómetros**. Es una medida de distancia, no de tiempo.
- **Pársec**: 3,26 años luz. Es la unidad que prefieren los astrónomos, porque nace de su forma de medir las estrellas cercanas.

## Mirar lejos es mirar atrás

Como la luz tarda en llegar, todo lo que vemos en el cielo lo vemos como era en el pasado. La Luna, como era hace 1,3 segundos; el Sol, hace 8 minutos; la estrella Polar, hace unos 430 años. La galaxia de Andrómeda la vemos como era hace 2,5 millones de años, cuando aún no existía nuestra especie. Los telescopios más potentes son, en realidad, máquinas del tiempo.

| Objeto | Distancia | La luz tarda |
|---|---|---|
| La Luna | 384.400 km | 1,3 segundos |
| El Sol | 150 millones de km | 8 min 20 s |
| Neptuno | 4.500 millones de km | 4 horas |
| Voyager 1 (2026) | 25.400 millones de km | 23,5 horas |
| Próxima Centauri | 40 billones de km | 4,24 años |
| Centro de la Vía Láctea | 26.000 años luz | 26.000 años |
| Galaxia de Andrómeda | 2,5 millones de años luz | 2,5 millones de años |
| Límite del universo observable | 46.500 millones de años luz | — |

## ¿Cómo se miden?

- **Radar y láser**: para la Luna y los planetas cercanos, se envía una señal y se mide cuánto tarda en volver. Así se conoce la distancia a la Luna con precisión de milímetros.
- **Paralaje**: para las estrellas cercanas. Al mirarlas desde dos puntos opuestos de la órbita terrestre, parecen moverse un poco contra el fondo, como un dedo delante de los ojos cuando cierras uno y luego el otro. El satélite europeo **Gaia** ha medido así la posición de casi 2.000 millones de estrellas.
- **Candelas estándar**: para las galaxias lejanas se usan objetos de brillo conocido, como las estrellas cefeidas o ciertas supernovas. Comparando lo brillantes que son de verdad con lo brillantes que se ven, se calcula su distancia.
- **Desplazamiento al rojo**: cuanto más lejos está una galaxia, más deprisa se aleja por la [expansión del universo](@big-bang) y más se estira su luz hacia el rojo.

!sim viaje

## Una escala para entenderlo

Imagina que la distancia entre la Tierra y el Sol se redujera a **un centímetro**. Entonces, Neptuno estaría a 30 centímetros, la nube de Oort se extendería unos cientos de metros, Próxima Centauri estaría a 2,7 kilómetros y el centro de la Vía Láctea, a unos 16.000 kilómetros, más que la distancia de Madrid a Sídney.

> La Voyager 1, el objeto humano más lejano, viaja a 61.000 km/h. Aun así, tardaría unos 75.000 años en recorrer la distancia hasta Próxima Centauri.
""",
    """
In space, kilometres soon fall short. Special units are used to talk about astronomical distances, and the best way to understand them is to compare them with familiar things.

## The units of the cosmos

- **Astronomical unit (AU)**: the average distance between Earth and the Sun, **149,597,870.7 km**. It is used within the solar system: Jupiter is 5.2 AU away and Neptune 30 AU.
- **Light year**: the distance light travels in a year, about **9.46 trillion kilometres**. It is a measure of distance, not time.
- **Parsec**: 3.26 light years. It is the unit astronomers prefer, because it comes from the way they measure nearby stars.

## Looking far is looking back

Because light takes time to arrive, everything we see in the sky we see as it was in the past. The Moon as it was 1.3 seconds ago; the Sun, 8 minutes ago; the Pole Star, about 430 years ago. We see the Andromeda galaxy as it was 2.5 million years ago, before our species existed. The most powerful telescopes are really time machines.

| Object | Distance | Light takes |
|---|---|---|
| The Moon | 384,400 km | 1.3 seconds |
| The Sun | 150 million km | 8 min 20 s |
| Neptune | 4.5 billion km | 4 hours |
| Voyager 1 (2026) | 25.4 billion km | 23.5 hours |
| Proxima Centauri | 40 trillion km | 4.24 years |
| Centre of the Milky Way | 26,000 light years | 26,000 years |
| Andromeda galaxy | 2.5 million light years | 2.5 million years |
| Edge of the observable universe | 46.5 billion light years | — |

## How are they measured?

- **Radar and laser**: for the Moon and nearby planets, a signal is sent and the time it takes to come back is measured. That is how we know the distance to the Moon to within millimetres.
- **Parallax**: for nearby stars. Seen from two opposite points of Earth's orbit, they seem to shift slightly against the background, like a finger held in front of your eyes when you close one eye and then the other. Europe's **Gaia** satellite has measured the positions of almost 2 billion stars this way.
- **Standard candles**: for distant galaxies, objects of known brightness are used, such as Cepheid stars or certain supernovae. Comparing how bright they really are with how bright they look gives their distance.
- **Redshift**: the farther away a galaxy is, the faster it recedes because of the [expansion of the universe](@big-bang) and the more its light is stretched towards red.

!sim viaje

## A scale to make sense of it

Imagine the distance between Earth and the Sun shrunk to **one centimetre**. Then Neptune would be 30 centimetres away, the Oort cloud would stretch a few hundred metres, Proxima Centauri would be 2.7 kilometres away and the centre of the Milky Way about 16,000 kilometres away, farther than from Madrid to Sydney.

> Voyager 1, the most distant human-made object, travels at 61,000 km/h. Even so, it would take about 75,000 years to cover the distance to Proxima Centauri.
""",
    datos=[("1 unidad astronómica", "1 astronomical unit", "149,6 millones de km", "149.6 million km"),
           ("1 año luz", "1 light year", "9,46 billones de km", "9.46 trillion km"),
           ("1 pársec", "1 parsec", "3,26 años luz", "3.26 light years"),
           ("Velocidad de la luz", "Speed of light", "299.792,458 km/s", "299,792.458 km/s"),
           ("Universo observable", "Observable universe", "≈ 93.000 millones de años luz de diámetro", "≈ 93 billion light years across")],
    pie=("La Vía Láctea sobre el observatorio Paranal (Chile), con el láser de un telescopio apuntando a su centro.",
         "The Milky Way over the Paranal observatory (Chile), with a telescope's laser pointing at its centre."),
)

ANECDOTAS = F(
    ("anecdotas", "anecdotes"),
    ("Anécdotas de la astronomía y del espacio", "Anecdotes from astronomy and space"),
    ("Del astrónomo que perdió la nariz en un duelo al bocadillo que viajó de contrabando al espacio: las historias más curiosas.",
     "From the astronomer who lost his nose in a duel to the sandwich smuggled into space: the most curious stories."),
    ("anécdotas de astronomía, historias del espacio, Tycho Brahe, Galileo, Apolo 11, Laika, Yuri Gagarin, curiosidades de astronautas, historia de la astronomía",
     "astronomy anecdotes, space stories, Tycho Brahe, Galileo, Apollo 11, Laika, Yuri Gagarin, astronaut trivia, history of astronomy"),
    "aldrin",
    """
La historia de la astronomía y de la exploración espacial está llena de personajes geniales, errores afortunados y momentos que parecen sacados de una novela. Estas son algunas de nuestras favoritas.

## La nariz de metal de Tycho Brahe

El gran astrónomo danés Tycho Brahe perdió parte de la nariz en un duelo a espada en 1566, discutiendo con un primo sobre una fórmula matemática. Durante el resto de su vida llevó una prótesis de latón. Tenía además un alce domesticado que, según se cuenta, murió tras beber demasiada cerveza y caerse por una escalera.

## Galileo y sus «orejas» de Saturno

Cuando Galileo apuntó su telescopio a Saturno en 1610, vio dos bultos a los lados y pensó que eran lunas o «asas». Para asegurarse la prioridad del descubrimiento sin revelarlo, envió a otros astrónomos un anagrama en latín. Dos años después, los bultos desaparecieron: los anillos se veían de canto. No entendió lo que había visto.

## El ruido que resultó ser el Big Bang

En 1964, los ingenieros Arno Penzias y Robert Wilson no lograban eliminar un molesto zumbido de su antena. Llegaron a limpiar los excrementos de las palomas que anidaban en ella. El ruido seguía: era el **fondo cósmico de microondas**, el eco del Big Bang. Ganaron el Premio Nobel de Física en 1978.

## Laika, Belka y Strelka

La perra **Laika** fue el primer ser vivo en orbitar la Tierra, a bordo del Sputnik 2 en 1957. No sobrevivió al viaje. En 1960, **Belka y Strelka** pasaron un día en órbita y volvieron sanas; un cachorro de Strelka fue regalado por Jruschov a la hija del presidente Kennedy.

## «Poyejali!»

Antes de despegar el 12 de abril de 1961 y convertirse en el primer ser humano en el espacio, **Yuri Gagarin** dijo «¡Vámonos!» (*Poyejali!*). Tras el aterrizaje se eyectó de la cápsula y bajó en paracaídas en un campo, donde una campesina y su nieta lo vieron llegar con su traje naranja.

## El bocadillo de contrabando

En 1965, el astronauta John Young sacó en plena misión **Gemini 3** un bocadillo de carne en conserva que había metido a escondidas en su traje. Las migas, flotando en la cabina, preocuparon tanto a la NASA que el asunto acabó en el Congreso de Estados Unidos.

## Una alarma a punto de cancelar el alunizaje

Durante el descenso del Apolo 11, el ordenador de a bordo lanzó varias alarmas, la «1202» y la «1201». Un joven controlador de 26 años, Steve Bales, decidió en segundos que se podía seguir. Armstrong posó el módulo con apenas unos **25 segundos de combustible** de margen antes de tener que abortar.

## El software de Margaret Hamilton

El programa de vuelo del Apolo lo dirigió **Margaret Hamilton**, que acuñó el término *ingeniería de software*. Una famosa foto la muestra junto a una pila de listados de código tan alta como ella.

## Unas zapatillas y un palo de golf

En 1971, el astronauta Alan Shepard golpeó **dos pelotas de golf** en la Luna con un palo improvisado. Una de ellas recorrió unos 40 metros, no los «kilómetros y kilómetros» que él bromeó.

!foto huella | La huella de una bota en el polvo lunar, tomada por Buzz Aldrin para estudiar el suelo.

## El error que cegó al Hubble

Cuando el telescopio Hubble se lanzó en 1990, sus primeras imágenes salieron borrosas: su espejo principal tenía un defecto de **2 micrómetros**, una cincuentava parte del grosor de un cabello. En 1993, unos astronautas le instalaron unas «gafas» correctoras en una de las misiones de reparación más famosas de la historia.

> El primer mensaje enviado por correo electrónico desde el espacio fue en 1991, desde el transbordador Atlantis: «Hola, Tierra, saludos de la tripulación del STS-43».
""",
    """
The history of astronomy and space exploration is full of brilliant characters, lucky mistakes and moments that seem lifted from a novel. Here are some of our favourites.

## Tycho Brahe's metal nose

The great Danish astronomer Tycho Brahe lost part of his nose in a sword duel in 1566, arguing with a cousin over a mathematical formula. For the rest of his life he wore a brass prosthesis. He also kept a tame elk which, the story goes, died after drinking too much beer and falling down a staircase.

## Galileo and Saturn's "ears"

When Galileo pointed his telescope at Saturn in 1610, he saw two bulges at its sides and thought they were moons or "handles". To secure credit for the discovery without revealing it, he sent other astronomers an anagram in Latin. Two years later the bulges disappeared: the rings were edge-on. He never understood what he had seen.

## The noise that turned out to be the Big Bang

In 1964, engineers Arno Penzias and Robert Wilson could not get rid of an annoying hiss in their antenna. They even cleaned out the droppings of pigeons nesting in it. The noise remained: it was the **cosmic microwave background**, the echo of the Big Bang. They won the Nobel Prize in Physics in 1978.

## Laika, Belka and Strelka

The dog **Laika** was the first living creature to orbit Earth, aboard Sputnik 2 in 1957. She did not survive the trip. In 1960 **Belka and Strelka** spent a day in orbit and came back safely; one of Strelka's puppies was given by Khrushchev to President Kennedy's daughter.

## "Poyekhali!"

Before lifting off on 12 April 1961 to become the first human in space, **Yuri Gagarin** said "Let's go!" (*Poyekhali!*). After re-entry he ejected from the capsule and parachuted into a field, where a farmer and her granddaughter watched him arrive in his orange suit.

## The smuggled sandwich

In 1965, astronaut John Young produced a corned beef sandwich in the middle of the **Gemini 3** mission, having sneaked it aboard in his suit. The crumbs floating around the cabin worried NASA so much that the matter reached the US Congress.

## An alarm that nearly cancelled the landing

During Apollo 11's descent, the onboard computer threw several alarms, "1202" and "1201". A 26-year-old controller, Steve Bales, decided in seconds that it was safe to continue. Armstrong set the lander down with only about **25 seconds of fuel** to spare before having to abort.

## Margaret Hamilton's software

Apollo's flight software was led by **Margaret Hamilton**, who coined the term *software engineering*. A famous photo shows her next to a stack of code listings as tall as she was.

## A golf club on the Moon

In 1971, astronaut Alan Shepard hit **two golf balls** on the Moon with an improvised club. One of them travelled about 40 metres, not the "miles and miles" he joked about.

!foto huella | A bootprint in the lunar dust, taken by Buzz Aldrin to study the soil.

## The flaw that blinded Hubble

When the Hubble telescope was launched in 1990, its first images were blurry: its main mirror had a flaw of **2 micrometres**, a fiftieth of the width of a human hair. In 1993, astronauts fitted it with corrective "glasses" in one of the most famous repair missions in history.

> The first email sent from space was in 1991, from the space shuttle Atlantis: "Hello Earth! Greetings from the STS-43 crew."
""",
    pie=("Buzz Aldrin en la Luna, fotografiado por Neil Armstrong. En su visor se refleja el fotógrafo.",
         "Buzz Aldrin on the Moon, photographed by Neil Armstrong, who is reflected in his visor."),
)

NOTICIAS = F(
    ("descubrimientos-sorprendentes", "surprising-discoveries"),
    ("Descubrimientos sorprendentes", "Surprising discoveries"),
    ("Visitantes de otras estrellas, galaxias demasiado tempranas, ondas que estiran el espacio y la foto de un agujero negro: las noticias que asombraron a la ciencia.",
     "Visitors from other stars, galaxies that came too early, waves that stretch space and a photo of a black hole: the news that astonished science."),
    ("descubrimientos astronómicos, noticias del espacio, ondas gravitacionales, Oumuamua, objeto interestelar, 3I/ATLAS, James Webb, foto agujero negro, exoplanetas, Betelgeuse, TRAPPIST-1, K2-18b",
     "astronomical discoveries, space news, gravitational waves, Oumuamua, interstellar object, 3I/ATLAS, James Webb, black hole photo, exoplanets, Betelgeuse, TRAPPIST-1, K2-18b"),
    "campo_webb",
    """
La astronomía avanza a toda velocidad. En las últimas décadas, los nuevos telescopios y sondas han traído noticias que habrían parecido ciencia ficción hace poco. Estas son algunas de las que más han sorprendido.

## La primera foto de un agujero negro (2019)

El 10 de abril de 2019, el **Event Horizon Telescope**, una red de radiotelescopios repartidos por todo el planeta que funcionan como uno solo del tamaño de la Tierra, presentó la primera imagen de un agujero negro: el de la galaxia M87, con 6.500 millones de masas solares. En 2022 llegó la foto de **Sagitario A\\***, el agujero negro del centro de nuestra galaxia.

!foto agujero_m87 | El agujero negro de la galaxia M87: el anillo es gas a enorme temperatura que gira a su alrededor.

## Ondas en el tejido del espacio (2015)

Einstein predijo que las masas aceleradas producen **ondas gravitacionales**, arrugas en el propio espacio-tiempo, pero creía que nunca se podrían detectar. El 14 de septiembre de 2015, los detectores **LIGO** registraron la señal de dos agujeros negros que chocaron hace 1.300 millones de años. La deformación medida fue una milésima del tamaño de un protón. Premio Nobel en 2017.

## Visitantes de otras estrellas

En 2017 se detectó **ʻOumuamua**, el primer objeto que llegaba al sistema solar desde otra estrella: alargado, rojizo y con una aceleración que aún se discute. En 2019 llegó el cometa **Borisov**, y en julio de 2025 se descubrió **3I/ATLAS**, el tercer visitante interestelar, un cometa que podría ser más antiguo que el propio sistema solar.

## Galaxias demasiado pronto

Desde 2022, el telescopio **James Webb** ha encontrado galaxias grandes y brillantes cuando el universo tenía solo unos cientos de millones de años, antes de lo que preveían muchos modelos. Ha obligado a revisar cómo se formaron las primeras estrellas y agujeros negros.

## Miles de planetas en otras estrellas

En 1995, Michel Mayor y Didier Queloz descubrieron **51 Pegasi b**, el primer planeta alrededor de una estrella como el Sol. Hoy se conocen **más de 6.000 exoplanetas**. El sistema **TRAPPIST-1** tiene siete planetas del tamaño de la Tierra, tres en la zona habitable. En el planeta **K2-18b**, el Webb ha detectado metano y dióxido de carbono, y se investiga si podría tener un océano.

## Betelgeuse se apagó (pero no explotó)

A finales de 2019, la estrella gigante roja Betelgeuse, el hombro de Orión, perdió dos tercios de su brillo. Muchos se preguntaron si estaba a punto de estallar como supernova. Resultó ser una gran nube de polvo que la propia estrella había expulsado. Algún día explotará, pero quizá dentro de 100.000 años.

## Agua por todas partes

Se ha encontrado hielo en los cráteres polares de Mercurio y de la Luna, océanos bajo el hielo de varias lunas de Júpiter y Saturno, y en 2023 el Webb detectó vapor de agua en el disco donde se forman planetas alrededor de otra estrella.

## Encélado y los ingredientes de la vida

En 2023 se anunció que los chorros de **Encélado** contienen fósforo, el último de los seis elementos esenciales para la vida que faltaba por encontrar en su océano. Encélado tiene así todos los ingredientes químicos básicos.

> La sonda Voyager 1 dejó de enviar datos comprensibles en noviembre de 2023 por un chip dañado. Desde 24.000 millones de kilómetros, los ingenieros reescribieron su software, que data de los años setenta, y en 2024 la nave volvió a «hablar».
""",
    """
Astronomy is moving at full speed. In recent decades, new telescopes and probes have brought news that would have sounded like science fiction not long ago. These are some of the discoveries that caused the greatest surprise.

## The first photo of a black hole (2019)

On 10 April 2019, the **Event Horizon Telescope**, a network of radio telescopes spread across the planet working as one dish the size of Earth, unveiled the first image of a black hole: the one in galaxy M87, with 6.5 billion solar masses. In 2022 came the photo of **Sagittarius A\\***, the black hole at the centre of our galaxy.

!foto agujero_m87 | The black hole in galaxy M87: the ring is extremely hot gas swirling around it.

## Ripples in the fabric of space (2015)

Einstein predicted that accelerating masses produce **gravitational waves**, wrinkles in space-time itself, but he thought they could never be detected. On 14 September 2015, the **LIGO** detectors recorded the signal from two black holes that had collided 1.3 billion years earlier. The distortion measured was a thousandth of the size of a proton. Nobel Prize in 2017.

## Visitors from other stars

In 2017 astronomers detected **ʻOumuamua**, the first object known to enter the solar system from another star: elongated, reddish and with an acceleration still debated. In 2019 came comet **Borisov**, and in July 2025 **3I/ATLAS** was discovered, the third interstellar visitor, a comet that may be older than the solar system itself.

## Galaxies too soon

Since 2022 the **James Webb** telescope has found large, bright galaxies when the universe was only a few hundred million years old, earlier than many models predicted. It has forced a rethink of how the first stars and black holes formed.

## Thousands of planets around other stars

In 1995 Michel Mayor and Didier Queloz discovered **51 Pegasi b**, the first planet orbiting a Sun-like star. Today **more than 6,000 exoplanets** are known. The **TRAPPIST-1** system has seven Earth-sized planets, three in the habitable zone. On the planet **K2-18b**, Webb has detected methane and carbon dioxide, and scientists are investigating whether it could have an ocean.

## Betelgeuse dimmed (but did not explode)

At the end of 2019 the red supergiant Betelgeuse, Orion's shoulder, lost two thirds of its brightness. Many wondered whether it was about to go supernova. It turned out to be a huge cloud of dust the star itself had thrown out. It will explode one day, but perhaps not for another 100,000 years.

## Water everywhere

Ice has been found in the polar craters of Mercury and the Moon, oceans under the ice of several moons of Jupiter and Saturn, and in 2023 Webb detected water vapour in the planet-forming disc around another star.

## Enceladus and the ingredients of life

In 2023 scientists announced that the jets of **Enceladus** contain phosphorus, the last of the six elements essential for life that had not yet been found in its ocean. Enceladus therefore has all the basic chemical ingredients.

> Voyager 1 stopped sending readable data in November 2023 because of a damaged chip. From 24 billion kilometres away, engineers rewrote its 1970s software, and in 2024 the spacecraft "spoke" again.
""",
    pie=("El primer campo profundo del telescopio James Webb (2022): miles de galaxias en un trozo de cielo del tamaño de un grano de arena sostenido con el brazo extendido.",
         "The James Webb telescope's first deep field (2022): thousands of galaxies in a patch of sky the size of a grain of sand held at arm's length."),
)

MITOS = F(
    ("falsos-mitos", "myths"),
    ("Falsos mitos sobre el espacio", "Space myths"),
    ("¿Se ve la Gran Muralla desde el espacio? ¿Explotarías sin traje? ¿Hace más calor en verano porque estamos más cerca del Sol? Lo que es cierto y lo que no.",
     "Can you see the Great Wall from space? Would you explode without a suit? Is summer hotter because we are closer to the Sun? What is true and what is not."),
    ("mitos del espacio, falsos mitos astronomía, Gran Muralla desde el espacio, cara oculta de la Luna, gravedad cero, estaciones del año, por qué hace calor en verano, preguntas sobre el espacio",
     "space myths, astronomy misconceptions, Great Wall from space, dark side of the Moon, zero gravity, seasons, why is summer hot, questions about space"),
    "iss",
    """
Algunas ideas sobre el espacio están tan extendidas que casi todo el mundo las da por ciertas. Estas son algunas de las más comunes, y lo que dice la ciencia.

## «La Gran Muralla china se ve desde el espacio»

**Falso.** La muralla es muy larga, pero tiene solo unos 6 metros de ancho y un color parecido al del terreno. Desde la Estación Espacial, a 400 km, no se distingue a simple vista. El primer astronauta chino, Yang Liwei, confirmó en 2003 que no la había visto. En cambio, sí se ven ciudades de noche, aeropuertos y grandes presas.

## «En verano hace calor porque la Tierra está más cerca del Sol»

**Falso.** La Tierra está más cerca del Sol a principios de enero. Las estaciones se deben a la **inclinación del eje terrestre**: en verano, los rayos del Sol llegan más de frente y los días son más largos. Por eso, cuando es verano en España, es invierno en Argentina. Lo explicamos en la ficha de la [Tierra](@tierra).

## «La cara oculta de la Luna está siempre a oscuras»

**Falso.** La cara oculta recibe tanta luz del Sol como la visible. Se llama así porque nunca la vemos desde la Tierra. Cuando hay luna nueva, de hecho, es la cara oculta la que está completamente iluminada.

## «En el espacio no hay gravedad»

**Falso.** A 400 km de altura, donde orbita la Estación Espacial, la gravedad es casi el **90 % de la que sentimos en el suelo**. Los astronautas flotan porque están en **caída libre** continua: caen hacia la Tierra, pero avanzan tan deprisa, a 28.000 km/h, que nunca llegan a tocarla.

## «Sin traje espacial, explotarías»

**Falso.** El cuerpo no explota en el vacío. Una persona perdería el conocimiento en unos **15 segundos** por falta de oxígeno y sufriría hinchazón y daños, pero si se la recuperara en uno o dos minutos podría sobrevivir. Tampoco se congelaría al instante: el vacío es un buen aislante.

## «El Sol es amarillo»

**Falso.** El Sol emite luz de todos los colores, y en conjunto es **blanco**. Desde el espacio se ve blanco. Lo vemos amarillento, o rojo al atardecer, porque la atmósfera dispersa la luz azul, la misma razón por la que el cielo es azul.

## «Mercurio es el planeta más caliente»

**Falso.** Aunque es el más cercano al Sol, el planeta más caliente es [Venus](@venus), por su densa atmósfera de dióxido de carbono.

## «La Estrella Polar es la más brillante del cielo»

**Falso.** Es útil porque marca el norte, pero está en el puesto 48 de brillo, más o menos. La más brillante del cielo nocturno es **Sirio**.

## «Los agujeros negros se lo tragan todo como aspiradoras»

**Falso.** A una distancia razonable, un agujero negro atrae como cualquier otro objeto de su masa. Si el Sol se convirtiera de repente en un agujero negro de la misma masa, la Tierra seguiría girando en la misma órbita, aunque eso sí, a oscuras.

## «Los meteoritos llegan al suelo ardiendo»

**Falso en general.** Brillan al atravesar la atmósfera, pero solo se calienta su capa exterior durante unos segundos. Su interior conserva el frío del espacio, y la mayoría llegan al suelo a temperatura ambiente o fríos.

> Tampoco es verdad que en el espacio no se pueda llorar: las lágrimas salen, pero sin gravedad no caen, sino que se acumulan en una bola de agua sobre el ojo.
""",
    """
Some ideas about space are so widespread that almost everyone takes them as true. These are some of the most common, and what science says.

## "You can see the Great Wall of China from space"

**False.** The wall is very long, but only about 6 metres wide and similar in colour to the ground around it. From the Space Station, 400 km up, it cannot be made out with the naked eye. China's first astronaut, Yang Liwei, confirmed in 2003 that he had not seen it. Cities at night, airports and large dams, however, are visible.

## "Summer is hot because Earth is closer to the Sun"

**False.** Earth is closest to the Sun in early January. The seasons are caused by the **tilt of Earth's axis**: in summer the Sun's rays arrive more directly and days are longer. That is why, when it is summer in Spain, it is winter in Argentina. We explain it in the article on [Earth](@tierra).

## "The far side of the Moon is always dark"

**False.** The far side gets as much sunlight as the near side. It is called that because we never see it from Earth. At new moon, in fact, it is the far side that is fully lit.

## "There is no gravity in space"

**False.** At 400 km up, where the Space Station orbits, gravity is almost **90% of what we feel on the ground**. Astronauts float because they are in continuous **free fall**: they fall towards Earth but move so fast, 28,000 km/h, that they never reach it.

## "Without a spacesuit, you would explode"

**False.** The body does not explode in a vacuum. A person would lose consciousness in about **15 seconds** for lack of oxygen and suffer swelling and injuries, but if rescued within a minute or two they could survive. Nor would they freeze instantly: a vacuum is a good insulator.

## "The Sun is yellow"

**False.** The Sun gives off light of every colour, and together it is **white**. From space it looks white. We see it yellowish, or red at sunset, because the atmosphere scatters blue light, the same reason the sky is blue.

## "Mercury is the hottest planet"

**False.** Although it is closest to the Sun, the hottest planet is [Venus](@venus), because of its thick carbon dioxide atmosphere.

## "The Pole Star is the brightest star in the sky"

**False.** It is useful because it marks north, but it ranks only around 48th in brightness. The brightest star in the night sky is **Sirius**.

## "Black holes suck everything in like vacuum cleaners"

**False.** At a reasonable distance, a black hole pulls like any other object of the same mass. If the Sun suddenly became a black hole of the same mass, Earth would keep orbiting just as before, though in the dark.

## "Meteorites land burning hot"

**Mostly false.** They glow as they pass through the atmosphere, but only their outer layer heats up for a few seconds. Their interior keeps the cold of space, and most land at room temperature or cold.

> Nor is it true that you cannot cry in space: tears do form, but without gravity they do not fall; they collect in a ball of water over the eye.
""",
    pie=("La Estación Espacial Internacional, a 400 km de altura, donde los astronautas flotan aunque la gravedad es casi la de la Tierra.",
         "The International Space Station, 400 km up, where astronauts float even though gravity is almost as strong as on Earth."),
)

FICHAS = [SIMULADORES, RECORDS, DISTANCIAS, ANECDOTAS, NOTICIAS, MITOS]
