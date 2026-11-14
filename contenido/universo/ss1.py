from universo import F

GENERAL = F(
    ("vision-general", "overview"),
    ("El sistema solar", "The solar system"),
    ("Una estrella, ocho planetas, cientos de lunas y millones de cuerpos menores que giran juntos desde hace 4.600 millones de años.",
     "One star, eight planets, hundreds of moons and millions of smaller bodies that have travelled together for 4.6 billion years."),
    ("sistema solar, planetas, orden de los planetas, Sol, órbitas, formación del sistema solar, planetas rocosos, gigantes gaseosos, gigantes de hielo, cinturón de asteroides, cinturón de Kuiper, nube de Oort, heliosfera",
     "solar system, planets, order of the planets, Sun, orbits, formation of the solar system, rocky planets, gas giants, ice giants, asteroid belt, Kuiper belt, Oort cloud, heliosphere"),
    "punto_azul",
    """
El sistema solar es nuestro barrio cósmico: el Sol y todo lo que su gravedad mantiene atado. Incluye ocho planetas, al menos cinco planetas enanos reconocidos, cerca de 300 lunas confirmadas, más de un millón de asteroides catalogados y un número enorme de cometas. El Sol concentra el **99,86 % de toda la masa**: los planetas, sumados, son casi un detalle.

## Cómo se formó

Hace unos 4.600 millones de años, una nube de gas y polvo de la Vía Láctea empezó a contraerse, probablemente empujada por la onda de choque de una supernova cercana. Al encogerse, giró cada vez más rápido y se aplanó en un disco. En el centro, la presión y la temperatura encendieron las reacciones nucleares: había nacido el Sol.

En el disco, los granos de polvo se pegaron unos a otros y formaron planetesimales, rocas de kilómetros que chocaban y crecían. Cerca del Sol solo resistían los metales y la roca, y así nacieron los **planetas rocosos**. Más lejos, más allá de la llamada *línea de hielo*, el agua y otros compuestos se congelaban, los embriones crecieron mucho más deprisa y atraparon enormes envolturas de hidrógeno y helio: los **gigantes gaseosos**.

## Los ocho planetas, en orden

Una frase clásica para recordarlos es «**Mi Viejo Tío Me Jura Solemnemente Un Nombre**»: [Mercurio](@mercurio), [Venus](@venus), [Tierra](@tierra), [Marte](@marte), [Júpiter](@jupiter), [Saturno](@saturno), [Urano](@urano) y [Neptuno](@neptuno).

| Planeta | Distancia media al Sol | Diámetro | Lunas conocidas | Un año dura |
|---|---|---|---|---|
| Mercurio | 58 millones de km | 4.879 km | 0 | 88 días |
| Venus | 108 millones de km | 12.104 km | 0 | 225 días |
| Tierra | 150 millones de km | 12.742 km | 1 | 365,25 días |
| Marte | 228 millones de km | 6.779 km | 2 | 687 días |
| Júpiter | 778 millones de km | 139.820 km | 97 | 11,9 años |
| Saturno | 1.434 millones de km | 116.460 km | 274 | 29,5 años |
| Urano | 2.871 millones de km | 50.724 km | 29 | 84 años |
| Neptuno | 4.495 millones de km | 49.244 km | 16 | 165 años |

!sim tamanos

## Tres familias de mundos

Los **planetas rocosos o terrestres** (Mercurio, Venus, la Tierra y Marte) son pequeños y densos, con superficie sólida y pocas o ninguna luna. Los **gigantes gaseosos** (Júpiter y Saturno) están hechos sobre todo de hidrógeno y helio; no tienen una superficie donde posarse. Los **gigantes de hielo** (Urano y Neptuno) contienen mucha agua, amoníaco y metano en estado de fluidos calientes y densos bajo sus atmósferas.

## Más allá de los planetas

Entre Marte y Júpiter se extiende el [cinturón de asteroides](@asteroides-y-cometas). Más allá de Neptuno, el **cinturón de Kuiper** alberga a [Plutón](@planetas-enanos) y a miles de mundos helados. Y mucho más lejos, quizá a un año luz, se supone que existe la **nube de Oort**, una esfera de billones de núcleos de cometas que marca el límite real del dominio del Sol.

!sim orbitas

## Un sistema casi plano

Todos los planetas giran alrededor del Sol en el mismo sentido y casi en el mismo plano, herencia del disco en el que se formaron. Por eso, desde la Tierra, los planetas siempre aparecen cerca de una misma franja del cielo, la eclíptica, por donde también pasan el Sol y la Luna.

> La famosa foto del «Pálido punto azul» la tomó la sonda Voyager 1 en 1990, a 6.000 millones de kilómetros. La Tierra ocupa menos de un píxel. Carl Sagan, que pidió que se hiciera, escribió: «Mira ese punto. Eso es aquí. Eso es nuestro hogar».

!foto salida_tierra | La Tierra asomando sobre el horizonte lunar, fotografiada por la tripulación del Apolo 8 en la Nochebuena de 1968.
""",
    """
The solar system is our cosmic neighbourhood: the Sun and everything its gravity holds on to. It includes eight planets, at least five recognised dwarf planets, around 300 confirmed moons, more than a million catalogued asteroids and a vast number of comets. The Sun holds **99.86% of all the mass**: the planets, added together, are almost a footnote.

## How it formed

About 4.6 billion years ago, a cloud of gas and dust in the Milky Way began to collapse, probably nudged by the shock wave of a nearby supernova. As it shrank, it spun faster and flattened into a disc. At the centre, pressure and temperature ignited nuclear reactions: the Sun was born.

In the disc, dust grains stuck together and built planetesimals, kilometre-sized rocks that collided and grew. Close to the Sun only metals and rock survived the heat, which gave rise to the **rocky planets**. Farther out, beyond the so-called *frost line*, water and other compounds froze, embryos grew much faster and captured huge envelopes of hydrogen and helium: the **gas giants**.

## The eight planets, in order

A classic way to remember them is "**My Very Educated Mother Just Served Us Noodles**": [Mercury](@mercurio), [Venus](@venus), [Earth](@tierra), [Mars](@marte), [Jupiter](@jupiter), [Saturn](@saturno), [Uranus](@urano) and [Neptune](@neptuno).

| Planet | Average distance from the Sun | Diameter | Known moons | One year lasts |
|---|---|---|---|---|
| Mercury | 58 million km | 4,879 km | 0 | 88 days |
| Venus | 108 million km | 12,104 km | 0 | 225 days |
| Earth | 150 million km | 12,742 km | 1 | 365.25 days |
| Mars | 228 million km | 6,779 km | 2 | 687 days |
| Jupiter | 778 million km | 139,820 km | 97 | 11.9 years |
| Saturn | 1,434 million km | 116,460 km | 274 | 29.5 years |
| Uranus | 2,871 million km | 50,724 km | 29 | 84 years |
| Neptune | 4,495 million km | 49,244 km | 16 | 165 years |

!sim tamanos

## Three families of worlds

The **rocky or terrestrial planets** (Mercury, Venus, Earth and Mars) are small and dense, with solid surfaces and few or no moons. The **gas giants** (Jupiter and Saturn) are made mostly of hydrogen and helium and have no surface to stand on. The **ice giants** (Uranus and Neptune) contain a lot of water, ammonia and methane as hot, dense fluids beneath their atmospheres.

## Beyond the planets

Between Mars and Jupiter lies the [asteroid belt](@asteroides-y-cometas). Beyond Neptune, the **Kuiper belt** is home to [Pluto](@planetas-enanos) and thousands of icy worlds. And much farther away, perhaps a light year out, the **Oort cloud** is thought to exist: a sphere of trillions of comet nuclei that marks the true edge of the Sun's domain.

!sim orbitas

## An almost flat system

All the planets travel around the Sun in the same direction and almost in the same plane, a legacy of the disc they formed in. That is why, from Earth, the planets always appear near the same strip of sky, the ecliptic, along which the Sun and the Moon also move.

> The famous "Pale Blue Dot" photo was taken by Voyager 1 in 1990, from 6 billion kilometres away. Earth fills less than a pixel. Carl Sagan, who asked for the picture, wrote: "Look again at that dot. That's here. That's home."

!foto salida_tierra | Earth rising above the lunar horizon, photographed by the Apollo 8 crew on Christmas Eve 1968.
""",
    datos=[("Edad", "Age", "4.600 millones de años", "4.6 billion years"),
           ("Planetas", "Planets", "8", "8"),
           ("Planetas enanos reconocidos", "Recognised dwarf planets", "5", "5"),
           ("Masa en el Sol", "Mass in the Sun", "99,86 %", "99.86%"),
           ("Diámetro de la heliosfera", "Heliosphere diameter", "≈ 240 UA", "≈ 240 AU"),
           ("Posición en la galaxia", "Position in the galaxy", "Brazo de Orión, a 26.000 años luz del centro", "Orion Arm, 26,000 light years from the centre")],
    pie=("El «Pálido punto azul»: la Tierra vista por la Voyager 1 desde 6.000 millones de km (1990).",
         "The \"Pale Blue Dot\": Earth seen by Voyager 1 from 6 billion km away (1990)."),
)

SOL = F(
    ("sol", "sun"),
    ("El Sol", "The Sun"),
    ("Una estrella corriente que, a 150 millones de kilómetros, nos da luz, calor y la energía de casi toda la vida en la Tierra.",
     "An ordinary star that, 150 million kilometres away, gives us light, warmth and the energy behind almost all life on Earth."),
    ("Sol, estrella, enana amarilla, fusión nuclear, manchas solares, fulguraciones, eyección de masa coronal, viento solar, corona solar, ciclo solar, temperatura del Sol, auroras",
     "Sun, star, yellow dwarf, nuclear fusion, sunspots, solar flares, coronal mass ejection, solar wind, solar corona, solar cycle, temperature of the Sun, auroras"),
    "sol",
    """
El Sol es una estrella de tipo G, lo que los astrónomos llaman una *enana amarilla*, aunque en realidad su luz es blanca: la atmósfera terrestre la tiñe de amarillo. Es una esfera de plasma de 1,39 millones de kilómetros de diámetro, tan grande que dentro cabrían **1,3 millones de Tierras**.

## Un reactor nuclear natural

En su núcleo, a unos 15 millones de grados, el hidrógeno se fusiona para formar helio. Cada segundo el Sol convierte unos **600 millones de toneladas de hidrógeno** en helio, y unos 4 millones de toneladas de esa masa se transforman en energía, tal como predice la famosa fórmula de Einstein, E = mc².

Esa energía tarda muchísimo en salir. Los fotones rebotan dentro de la *zona radiativa* durante decenas de miles de años, quizá más de 100.000, antes de llegar a la *zona convectiva*, donde el gas caliente sube y baja como el agua hirviendo. Desde la superficie, la luz solo necesita **8 minutos y 20 segundos** para alcanzar la Tierra.

## Las capas del Sol

- **Núcleo**: donde se produce la fusión, a 15 millones de °C.
- **Zona radiativa**: la energía avanza a base de absorberse y reemitirse.
- **Zona convectiva**: corrientes de gas que transportan el calor hacia fuera.
- **Fotosfera**: la «superficie» visible, a unos 5.500 °C.
- **Cromosfera**: una capa rojiza que solo se ve bien en los eclipses.
- **Corona**: la atmósfera exterior, que inexplicablemente está a más de un millón de grados.

!foto sol_mancha | Manchas solares vistas de cerca: zonas más frías donde los campos magnéticos frenan la convección.

## Manchas, fulguraciones y tormentas

La actividad del Sol sigue un **ciclo de unos 11 años**. En el máximo aparecen muchas *manchas solares*, regiones más frías y oscuras atravesadas por campos magnéticos intensos. Cuando esos campos se reorganizan de golpe liberan fulguraciones y **eyecciones de masa coronal**: nubes de miles de millones de toneladas de plasma lanzadas al espacio.

Si una de esas nubes alcanza la Tierra, provoca tormentas geomagnéticas y auroras espectaculares, pero también puede dañar satélites y redes eléctricas. En 1859, el *evento Carrington* hizo saltar chispas en los telégrafos y se vieron auroras casi en el trópico. En mayo de 2024 hubo auroras visibles desde España.

!foto sol_eyeccion | Una eyección de masa coronal del 31 de agosto de 2012, vista por el observatorio SDO de la NASA.

## Los eclipses de Sol

Por una casualidad cósmica, el Sol es unas 400 veces más grande que la Luna, pero está unas 400 veces más lejos. Por eso, desde la Tierra, ambos se ven casi del mismo tamaño y la Luna puede taparlo por completo. España vivirá un **eclipse total el 12 de agosto de 2026** y otro el 2 de agosto de 2027.

!foto sol_eclipse | La corona solar, solo visible a simple vista durante un eclipse total (Francia, 1999).

## El futuro del Sol

El Sol lleva 4.600 millones de años brillando y le quedan unos 5.000 millones más. Al agotar el hidrógeno del núcleo se hinchará hasta convertirse en una **gigante roja** que engullirá a Mercurio y a Venus, y quizá a la Tierra. Después expulsará sus capas exteriores y quedará una [enana blanca](@vida-de-las-estrellas) del tamaño de la Tierra que se irá enfriando durante miles de millones de años.

> El Sol no «quema» como un fuego: si fuera una hoguera de carbón del mismo tamaño, se habría apagado en unos pocos miles de años.
""",
    """
The Sun is a G-type star, what astronomers call a *yellow dwarf*, although its light is actually white: Earth's atmosphere tints it yellow. It is a sphere of plasma 1.39 million kilometres across, so large that **1.3 million Earths** would fit inside.

## A natural nuclear reactor

In its core, at around 15 million degrees, hydrogen fuses into helium. Every second the Sun converts some **600 million tonnes of hydrogen** into helium, and about 4 million tonnes of that mass turn into energy, exactly as Einstein's famous formula, E = mc², predicts.

That energy takes a very long time to get out. Photons bounce around inside the *radiative zone* for tens of thousands of years, perhaps more than 100,000, before reaching the *convective zone*, where hot gas rises and sinks like boiling water. From the surface, light needs only **8 minutes and 20 seconds** to reach Earth.

## The layers of the Sun

- **Core**: where fusion happens, at 15 million °C.
- **Radiative zone**: energy moves outwards by being absorbed and re-emitted.
- **Convective zone**: currents of gas carry heat towards the surface.
- **Photosphere**: the visible "surface", at about 5,500 °C.
- **Chromosphere**: a reddish layer best seen during eclipses.
- **Corona**: the outer atmosphere, which puzzlingly reaches more than a million degrees.

!foto sol_mancha | Sunspots up close: cooler regions where magnetic fields hold back convection.

## Spots, flares and storms

Solar activity follows a **cycle of about 11 years**. At maximum, many *sunspots* appear: cooler, darker regions threaded by intense magnetic fields. When those fields suddenly reconnect they release flares and **coronal mass ejections**, clouds of billions of tonnes of plasma flung into space.

If one of those clouds reaches Earth it triggers geomagnetic storms and spectacular auroras, but it can also damage satellites and power grids. In 1859 the *Carrington event* made telegraph lines spark, and auroras were seen almost in the tropics. In May 2024, auroras were visible as far south as Spain.

!foto sol_eyeccion | A coronal mass ejection on 31 August 2012, seen by NASA's Solar Dynamics Observatory.

## Solar eclipses

By a cosmic coincidence, the Sun is about 400 times larger than the Moon but also about 400 times farther away. So from Earth they look almost the same size, and the Moon can cover it completely. Spain will see a **total eclipse on 12 August 2026** and another on 2 August 2027.

!foto sol_eclipse | The solar corona, only visible to the naked eye during a total eclipse (France, 1999).

## The Sun's future

The Sun has been shining for 4.6 billion years and has about 5 billion left. When the hydrogen in its core runs out it will swell into a **red giant**, swallowing Mercury and Venus and perhaps Earth. Then it will shed its outer layers, leaving a Earth-sized [white dwarf](@vida-de-las-estrellas) that will cool for billions of years.

> The Sun does not "burn" like a fire: if it were a coal fire of the same size, it would have gone out within a few thousand years.
""",
    datos=[("Tipo", "Type", "Estrella G2V (enana amarilla)", "G2V star (yellow dwarf)"),
           ("Diámetro", "Diameter", "1.392.700 km (109 Tierras)", "1,392,700 km (109 Earths)"),
           ("Masa", "Mass", "333.000 Tierras", "333,000 Earths"),
           ("Temperatura de la superficie", "Surface temperature", "≈ 5.500 °C", "≈ 5,500 °C"),
           ("Temperatura del núcleo", "Core temperature", "≈ 15 millones de °C", "≈ 15 million °C"),
           ("Distancia a la Tierra", "Distance from Earth", "149,6 millones de km (1 UA)", "149.6 million km (1 AU)"),
           ("Rotación", "Rotation", "25 días (ecuador) a 35 (polos)", "25 days (equator) to 35 (poles)"),
           ("Edad", "Age", "4.600 millones de años", "4.6 billion years")],
    pie=("El Sol en luz ultravioleta extrema, captado por el Solar Dynamics Observatory de la NASA.",
         "The Sun in extreme ultraviolet light, captured by NASA's Solar Dynamics Observatory."),
)

MERCURIO = F(
    ("mercurio", "mercury"),
    ("Mercurio", "Mercury"),
    ("El planeta más pequeño y el más cercano al Sol: un mundo de cráteres con días abrasadores y noches heladas.",
     "The smallest planet and the closest to the Sun: a cratered world of scorching days and freezing nights."),
    ("Mercurio, planeta Mercurio, planeta más cercano al Sol, MESSENGER, BepiColombo, cráteres, cuenca Caloris, día en Mercurio, temperatura de Mercurio, hielo en Mercurio",
     "Mercury, planet Mercury, closest planet to the Sun, MESSENGER, BepiColombo, craters, Caloris basin, day on Mercury, temperature of Mercury, ice on Mercury"),
    "mercurio",
    """
Mercurio es el planeta más pequeño del sistema solar, apenas algo mayor que nuestra Luna, y el más cercano al Sol. Da una vuelta completa en solo **88 días**, a casi 48 kilómetros por segundo, y por eso los romanos le pusieron el nombre del veloz mensajero de los dioses.

## Un día más largo que un año

Mercurio gira muy despacio sobre sí mismo: tarda 59 días terrestres en dar una vuelta. Pero, como a la vez avanza tan deprisa en su órbita, desde su superficie un **día solar completo, de amanecer a amanecer, dura 176 días terrestres**: el doble que su año.

Sin apenas atmósfera que retenga el calor, las temperaturas son extremas. A mediodía el suelo alcanza **430 °C**, suficiente para fundir el plomo, y por la noche cae hasta **−180 °C**. Es la mayor diferencia entre el día y la noche de todos los planetas.

## Hielo junto al Sol

Aunque parezca imposible, Mercurio tiene hielo. En el fondo de los cráteres de sus polos hay zonas que nunca reciben la luz del Sol, porque el eje del planeta está casi derecho. La sonda MESSENGER confirmó en 2012 que esas trampas frías guardan **agua helada**, probablemente traída por cometas.

!foto mercurio_color | Mercurio en colores realzados por la sonda MESSENGER: cada tono revela una composición distinta del suelo.

## Un planeta encogido

Mercurio tiene un núcleo de hierro enorme, que ocupa alrededor del **85 % de su radio**. Al enfriarse, el núcleo se contrajo y la corteza se arrugó como la piel de una manzana seca, formando escarpes de cientos de kilómetros de largo y hasta tres de altura. Se calcula que el planeta ha encogido unos 7 kilómetros de radio.

Su accidente más famoso es la **cuenca Caloris**, un cráter de 1.550 km de diámetro excavado por un impacto gigantesco. La sacudida fue tan fuerte que en el lado opuesto del planeta dejó un terreno caótico de colinas.

## Las sondas que lo visitaron

- **Mariner 10** (NASA, 1974–1975) sobrevoló Mercurio tres veces y fotografió casi la mitad del planeta.
- **MESSENGER** (NASA, 2011–2015) fue la primera en orbitarlo y lo cartografió entero antes de estrellarse a propósito contra su superficie.
- **BepiColombo** (ESA y Japón) llegará a su órbita en noviembre de 2026 con dos naves que lo estudiarán a la vez.

## Cómo verlo

Mercurio nunca se aleja mucho del Sol en el cielo, así que solo se ve un rato al anochecer o al amanecer, muy bajo sobre el horizonte. Se dice que el propio Copérnico nunca llegó a verlo.

> La órbita de Mercurio avanza un poco en cada vuelta de una forma que la física de Newton no lograba explicar. La teoría de la relatividad de Einstein lo resolvió en 1915, y fue una de sus primeras grandes pruebas.
""",
    """
Mercury is the smallest planet in the solar system, only slightly larger than our Moon, and the closest to the Sun. It completes an orbit in just **88 days**, at almost 48 kilometres per second, which is why the Romans named it after the swift messenger of the gods.

## A day longer than a year

Mercury spins very slowly: it takes 59 Earth days to turn once on its axis. But because it moves so quickly along its orbit, from its surface a **full solar day, sunrise to sunrise, lasts 176 Earth days**: twice its year.

With almost no atmosphere to hold heat, temperatures are extreme. At noon the ground reaches **430 °C**, hot enough to melt lead, and at night it drops to **−180 °C**. It is the largest day–night difference of any planet.

## Ice next to the Sun

Unlikely as it sounds, Mercury has ice. At the bottom of craters near its poles there are places the Sun never reaches, because the planet's axis is almost upright. The MESSENGER probe confirmed in 2012 that these cold traps hold **water ice**, probably delivered by comets.

!foto mercurio_color | Mercury in enhanced colour from the MESSENGER probe: each shade reveals a different soil composition.

## A shrinking planet

Mercury has a huge iron core taking up about **85% of its radius**. As the core cooled it contracted, and the crust wrinkled like the skin of a drying apple, forming cliffs hundreds of kilometres long and up to three kilometres high. The planet is thought to have shrunk by about 7 kilometres in radius.

Its most famous feature is the **Caloris basin**, a crater 1,550 km across dug out by a gigantic impact. The shock was so strong that it left a chaotic, hilly terrain on the opposite side of the planet.

## The probes that visited it

- **Mariner 10** (NASA, 1974–1975) flew past Mercury three times and photographed almost half of the planet.
- **MESSENGER** (NASA, 2011–2015) was the first to orbit it and mapped it completely before being deliberately crashed into its surface.
- **BepiColombo** (ESA and Japan) reaches orbit in November 2026 with two spacecraft that will study it at the same time.

## How to see it

Mercury never strays far from the Sun in the sky, so it can only be seen briefly at dusk or dawn, very low on the horizon. Copernicus himself is said never to have seen it.

> Mercury's orbit shifts slightly with each lap in a way Newton's physics could not explain. Einstein's theory of relativity solved it in 1915, one of its first great tests.
""",
    datos=[("Diámetro", "Diameter", "4.879 km", "4,879 km"),
           ("Distancia media al Sol", "Average distance from the Sun", "57,9 millones de km", "57.9 million km"),
           ("Año", "Year", "88 días", "88 days"),
           ("Día solar", "Solar day", "176 días terrestres", "176 Earth days"),
           ("Temperatura", "Temperature", "−180 °C a 430 °C", "−180 °C to 430 °C"),
           ("Gravedad", "Gravity", "0,38 g", "0.38 g"),
           ("Lunas", "Moons", "Ninguna", "None")],
    pie=("Mercurio en color real, en un mosaico de la sonda MESSENGER.", "Mercury in true colour, in a mosaic from the MESSENGER probe."),
)

VENUS = F(
    ("venus", "venus"),
    ("Venus", "Venus"),
    ("El gemelo infernal de la Tierra: un planeta de nubes ácidas y 465 °C donde el Sol sale por el oeste.",
     "Earth's hellish twin: a planet of acid clouds and 465 °C where the Sun rises in the west."),
    ("Venus, planeta Venus, lucero del alba, efecto invernadero, temperatura de Venus, nubes de ácido sulfúrico, rotación retrógrada, Venera, Magellan, volcanes de Venus",
     "Venus, planet Venus, morning star, evening star, greenhouse effect, temperature of Venus, sulphuric acid clouds, retrograde rotation, Venera, Magellan, volcanoes on Venus"),
    "venus",
    """
Venus es casi del mismo tamaño que la Tierra y está hecho de los mismos materiales, por eso se le llama nuestro planeta gemelo. Pero es un gemelo infernal. Es el objeto más brillante del cielo nocturno después de la Luna, el «lucero del alba» o «de la tarde», y su brillo se debe a una capa de nubes que refleja el 75 % de la luz del Sol.

## El planeta más caliente

Aunque Mercurio está más cerca del Sol, Venus es el planeta más caliente: su superficie está a **465 °C** día y noche, en los polos y en el ecuador. La culpa es de su atmósfera, formada en un 96 % por dióxido de carbono, que atrapa el calor en un **efecto invernadero desbocado**.

Esa atmósfera es tan densa que la presión en el suelo es **92 veces la de la Tierra**, como estar a 900 metros bajo el mar. Las nubes, a unos 50 km de altura, están hechas de gotas de **ácido sulfúrico**.

## Un día más largo que su año

Venus gira sobre sí mismo al revés que casi todos los planetas, y lo hace con una lentitud asombrosa: tarda **243 días terrestres** en dar una vuelta, más que los 225 que tarda en rodear al Sol. Desde su superficie, el Sol saldría por el oeste y se pondría por el este. En cambio, la parte alta de la atmósfera da la vuelta al planeta en solo cuatro días, con vientos de 360 km/h.

!foto venus_radar | Venus sin nubes: un mapa de radar de la sonda Magellan muestra un mundo de volcanes y llanuras de lava.

## Un mundo de volcanes

Bajo las nubes, el radar de la sonda Magellan (1990–1994) reveló más de **1.600 volcanes grandes** y cientos de miles de pequeños, llanuras de lava y estructuras únicas llamadas *coronas*. Casi no hay cráteres viejos, lo que indica que la superficie se renovó por completo hace unos 500 millones de años. En 2023 se confirmó en imágenes antiguas que un volcán había cambiado de forma: Venus sigue activo.

!foto venus_relieve | Vista en relieve de la corona Latona y el cañón Dali Chasma, a partir de datos de radar de Magellan.

## Las sondas que llegaron al infierno

La Unión Soviética envió las sondas **Venera**. La Venera 7 fue en 1970 la primera nave que funcionó en la superficie de otro planeta, y la Venera 13 envió en 1982 las primeras fotos en color del suelo venusiano antes de quedar destruida por el calor tras 127 minutos. Para la próxima década hay preparadas tres misiones: DAVINCI y VERITAS, de la NASA, y EnVision, de la ESA.

## ¿Vida en las nubes?

A 50 km de altura, la temperatura y la presión de Venus son parecidas a las de la Tierra. En 2020 se anunció la posible detección de fosfina, un gas que en nuestro planeta producen seres vivos. El hallazgo sigue siendo muy discutido, pero reavivó la idea de buscar vida microscópica en sus nubes.

> Venus no tiene lunas y es el único planeta con nombre de mujer. Casi todos sus accidentes geográficos llevan nombres de mujeres reales o mitológicas.
""",
    """
Venus is almost the same size as Earth and made of the same materials, which is why it is called our twin planet. But it is a hellish twin. It is the brightest object in the night sky after the Moon, the "morning star" or "evening star", and its brilliance comes from a cloud layer that reflects 75% of the sunlight.

## The hottest planet

Although Mercury is closer to the Sun, Venus is the hottest planet: its surface sits at **465 °C** day and night, at the poles and at the equator. The culprit is its atmosphere, 96% carbon dioxide, which traps heat in a **runaway greenhouse effect**.

The atmosphere is so dense that the pressure at the ground is **92 times Earth's**, like being 900 metres under the sea. The clouds, about 50 km up, are made of droplets of **sulphuric acid**.

## A day longer than its year

Venus spins backwards compared with almost every other planet, and astonishingly slowly: it takes **243 Earth days** to turn once, longer than the 225 it takes to orbit the Sun. From its surface, the Sun would rise in the west and set in the east. Its upper atmosphere, however, circles the planet in just four days, with winds of 360 km/h.

!foto venus_radar | Venus without clouds: a radar map from the Magellan probe shows a world of volcanoes and lava plains.

## A world of volcanoes

Beneath the clouds, the radar of the Magellan probe (1990–1994) revealed more than **1,600 large volcanoes** and hundreds of thousands of small ones, lava plains and unique structures called *coronae*. There are almost no old craters, which suggests the whole surface was renewed some 500 million years ago. In 2023, old images confirmed that a volcanic vent had changed shape: Venus is still active.

!foto venus_relieve | A relief view of Latona Corona and Dali Chasma, built from Magellan radar data.

## The probes that reached hell

The Soviet Union sent the **Venera** probes. In 1970, Venera 7 became the first spacecraft to work on the surface of another planet, and in 1982 Venera 13 sent back the first colour photos of the Venusian ground before the heat destroyed it after 127 minutes. Three missions are planned for the coming decade: NASA's DAVINCI and VERITAS, and ESA's EnVision.

## Life in the clouds?

About 50 km up, Venus has temperatures and pressures similar to Earth's. In 2020 scientists announced a possible detection of phosphine, a gas produced on our planet by living things. The finding is still hotly debated, but it revived the idea of looking for microscopic life in its clouds.

> Venus has no moons and is the only planet named after a woman. Almost all of its surface features are named after real or mythological women.
""",
    datos=[("Diámetro", "Diameter", "12.104 km", "12,104 km"),
           ("Distancia media al Sol", "Average distance from the Sun", "108,2 millones de km", "108.2 million km"),
           ("Año", "Year", "225 días", "225 days"),
           ("Rotación", "Rotation", "243 días (retrógrada)", "243 days (retrograde)"),
           ("Temperatura media", "Average temperature", "465 °C", "465 °C"),
           ("Presión en la superficie", "Surface pressure", "92 veces la terrestre", "92 times Earth's"),
           ("Gravedad", "Gravity", "0,90 g", "0.90 g"),
           ("Lunas", "Moons", "Ninguna", "None")],
    pie=("Venus fotografiado por la sonda Mariner 10 en 1974, en color natural y con el contraste realzado.",
         "Venus photographed by Mariner 10 in 1974, in natural colour and with enhanced contrast."),
)

TIERRA = F(
    ("tierra", "earth"),
    ("La Tierra", "Earth"),
    ("El único planeta conocido con vida y con agua líquida en su superficie: nuestro hogar, visto como un planeta más.",
     "The only known planet with life and liquid water on its surface: our home, seen as just another planet."),
    ("Tierra, planeta Tierra, canica azul, agua líquida, atmósfera, campo magnético, estaciones, inclinación del eje, zona habitable, placas tectónicas, vida en la Tierra",
     "Earth, planet Earth, Blue Marble, liquid water, atmosphere, magnetic field, seasons, axial tilt, habitable zone, plate tectonics, life on Earth"),
    "tierra",
    """
La Tierra es el tercer planeta desde el Sol, el mayor de los rocosos y, hasta donde sabemos, el único lugar del universo donde existe vida. Vista desde el espacio es una esfera azul y blanca: el **71 % de su superficie está cubierto de océanos**.

## La zona habitable

La Tierra está a la distancia justa del Sol para que el agua sea líquida en su superficie, en lo que se llama la *zona habitable*. Si estuviera un poco más cerca, los océanos se evaporarían, como probablemente ocurrió en [Venus](@venus); un poco más lejos, se congelarían, como en [Marte](@marte). Su atmósfera, de nitrógeno (78 %) y oxígeno (21 %), mantiene una temperatura media de unos 15 °C.

## Un escudo invisible

El núcleo de hierro de la Tierra, en parte líquido, genera un **campo magnético** que desvía la mayor parte del viento solar. Sin ese escudo, las partículas del Sol irían arrancando poco a poco la atmósfera. Cuando algunas consiguen entrar cerca de los polos, chocan con el aire y lo hacen brillar: son las **auroras**.

## Por qué hay estaciones

El eje de la Tierra está inclinado **23,4 grados**. Por eso, durante media órbita el hemisferio norte recibe la luz del Sol más de frente y los días son más largos (verano), y durante la otra media ocurre al revés. No tiene que ver con la distancia al Sol: de hecho, la Tierra está más cerca del Sol a principios de enero, en pleno invierno del norte.

!foto salida_tierra | «Salida de la Tierra», la foto que tomó William Anders desde la órbita lunar en 1968.

## Un planeta vivo por dentro

La superficie terrestre está dividida en **placas tectónicas** que se mueven unos centímetros al año, más o menos lo que crecen las uñas. Su movimiento levanta montañas, abre océanos, provoca terremotos y alimenta volcanes. Es el único planeta conocido con tectónica de placas activa, y este reciclaje de la corteza ayuda a regular el clima a lo largo de millones de años.

## Datos que asombran

- La Tierra gira a unos **1.670 km/h** en el ecuador y viaja alrededor del Sol a **107.000 km/h**.
- No es una esfera perfecta: está achatada por los polos. El diámetro ecuatorial supera al polar en 43 km.
- El punto más alejado del centro de la Tierra no es la cima del Everest, sino la del **Chimborazo**, en Ecuador, por estar cerca del ecuador.
- Cada día caen sobre la Tierra entre 50 y 100 toneladas de polvo y pequeños meteoritos.

## La Tierra vista desde lejos

La foto de la **Canica azul**, tomada por la tripulación del Apolo 17 en 1972, es una de las imágenes más reproducidas de la historia. La de la «Salida de la Tierra», de 1968, se considera el inicio del movimiento ecologista moderno: por primera vez vimos nuestro planeta pequeño y frágil en la inmensidad del espacio.

> Un día no dura exactamente 24 horas: la Tierra tarda 23 horas, 56 minutos y 4 segundos en girar respecto a las estrellas. Y los días se alargan unos 2 milisegundos por siglo porque la Luna frena la rotación terrestre con las mareas.

Para saber mucho más sobre nuestro planeta, visita la sección **Planeta Tierra** de Planetpedia.
""",
    """
Earth is the third planet from the Sun, the largest of the rocky ones and, as far as we know, the only place in the universe where life exists. Seen from space it is a blue and white sphere: **71% of its surface is covered by oceans**.

## The habitable zone

Earth sits at just the right distance from the Sun for water to be liquid on its surface, in what is called the *habitable zone*. A little closer and the oceans would boil away, as probably happened on [Venus](@venus); a little farther and they would freeze, as on [Mars](@marte). Its atmosphere of nitrogen (78%) and oxygen (21%) keeps the average temperature at around 15 °C.

## An invisible shield

Earth's iron core, partly liquid, generates a **magnetic field** that deflects most of the solar wind. Without that shield, particles from the Sun would slowly strip away the atmosphere. When some manage to get in near the poles, they collide with the air and make it glow: the **auroras**.

## Why there are seasons

Earth's axis is tilted **23.4 degrees**. So for half of the orbit the northern hemisphere receives sunlight more directly and days are longer (summer), and for the other half the reverse happens. It has nothing to do with distance from the Sun: in fact, Earth is closest to the Sun in early January, in the middle of the northern winter.

!foto salida_tierra | "Earthrise", the photo William Anders took from lunar orbit in 1968.

## A planet alive inside

Earth's surface is split into **tectonic plates** that move a few centimetres a year, about as fast as fingernails grow. Their motion raises mountains, opens oceans, triggers earthquakes and feeds volcanoes. It is the only planet known to have active plate tectonics, and this recycling of the crust helps regulate the climate over millions of years.

## Astonishing facts

- Earth spins at about **1,670 km/h** at the equator and travels around the Sun at **107,000 km/h**.
- It is not a perfect sphere: it is flattened at the poles. The equatorial diameter exceeds the polar one by 43 km.
- The point farthest from Earth's centre is not the summit of Everest but that of **Chimborazo**, in Ecuador, because it is close to the equator.
- Every day, between 50 and 100 tonnes of dust and small meteorites fall on Earth.

## Earth from afar

The **Blue Marble** photo, taken by the Apollo 17 crew in 1972, is one of the most reproduced images in history. "Earthrise", from 1968, is considered the start of the modern environmental movement: for the first time we saw our planet small and fragile in the vastness of space.

> A day is not exactly 24 hours: Earth takes 23 hours, 56 minutes and 4 seconds to turn relative to the stars. And days get about 2 milliseconds longer every century because the Moon slows Earth's rotation through the tides.

To learn much more about our planet, visit the **Planet Earth** section of Planetpedia.
""",
    datos=[("Diámetro", "Diameter", "12.742 km", "12,742 km"),
           ("Distancia media al Sol", "Average distance from the Sun", "149,6 millones de km", "149.6 million km"),
           ("Año", "Year", "365,25 días", "365.25 days"),
           ("Día sidéreo", "Sidereal day", "23 h 56 min 4 s", "23 h 56 min 4 s"),
           ("Inclinación del eje", "Axial tilt", "23,4°", "23.4°"),
           ("Temperatura media", "Average temperature", "15 °C", "15 °C"),
           ("Superficie de océanos", "Ocean surface", "71 %", "71%"),
           ("Lunas", "Moons", "1", "1"),
           ("Edad", "Age", "4.540 millones de años", "4.54 billion years")],
    pie=("La «Canica azul», fotografiada por la tripulación del Apolo 17 en 1972.", "The \"Blue Marble\", photographed by the Apollo 17 crew in 1972."),
)

FICHAS = [GENERAL, SOL, MERCURIO, VENUS, TIERRA]
