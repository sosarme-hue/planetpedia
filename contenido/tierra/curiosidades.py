from universo import F

SLUG = ("curiosidades-de-la-tierra", "earth-curiosities")
TITULO = ("Curiosidades de la Tierra", "Earth curiosities")
RESUMEN = ("Simuladores, récords del planeta, los lugares más extremos, fenómenos asombrosos y falsos mitos sobre la Tierra.",
           "Simulators, planet records, the most extreme places, astonishing phenomena and myths about the Earth.")
CLAVES = ("curiosidades de la Tierra, datos curiosos del planeta, récords de la Tierra, lugares extremos, fenómenos naturales asombrosos, mitos sobre la Tierra, simuladores, viaje al centro de la Tierra",
          "Earth curiosities, fun facts about the planet, Earth records, extreme places, amazing natural phenomena, myths about the Earth, simulators, journey to the centre of the Earth")
FOTO = "dallol"
INTRO = ("""
Nuestro planeta guarda récords que parecen inventados, lugares donde no se podría vivir más de unas horas y fenómenos que durante siglos se tomaron por magia. Aquí los reunimos, junto con simuladores para viajar al centro de la Tierra o comprimir toda su historia en un año, y los mitos que conviene desterrar.
""", """
Our planet holds records that sound made up, places where you could not survive more than a few hours and phenomena that for centuries were taken for magic. Here we gather them, together with simulators to travel to the centre of the Earth or squeeze its whole history into a year, and the myths worth putting to rest.
""")

SIMULADORES = F(
    ("simuladores-de-la-tierra", "earth-simulators"),
    ("Simuladores de la Tierra", "Earth simulators"),
    ("Viaja al centro de la Tierra, compara la energía de los grandes terremotos y descubre en qué día del año aparecerían los dinosaurios si la historia del planeta durara doce meses.",
     "Travel to the centre of the Earth, compare the energy of great earthquakes and find out on what day the dinosaurs would appear if the planet's history lasted twelve months."),
    ("simulador viaje al centro de la Tierra, simulador de terremotos, escala de magnitud, energía de un terremoto, calendario de la historia de la Tierra, año cósmico de la Tierra, capas de la Tierra interactivo",
     "journey to the centre of the Earth simulator, earthquake simulator, magnitude scale, earthquake energy, Earth history calendar, Earth history in a year, interactive Earth layers"),
    "capas",
    """
Las cifras de la Tierra, como las del universo, son difíciles de imaginar: miles de kilómetros de roca, miles de millones de años, energías equivalentes a miles de bombas. Estos simuladores las ponen a escala humana. Todos funcionan en tu navegador.

## Viaje al centro de la Tierra

Mueve el control para bajar desde la superficie hasta el centro del planeta, a 6.371 km. Verás en qué [capa](@estructura-de-la-tierra) estás, la temperatura y la presión aproximadas, y cuánto tardarías en llegar andando.

!sim centro

El agujero más profundo que hemos hecho, el **pozo de Kola**, en Rusia, llegó a 12,3 km: apenas un 0,2 % del camino. Todo lo que sabemos del interior lo hemos deducido estudiando cómo viajan las ondas de los [terremotos](@terremotos-y-tsunamis).

## La energía de un terremoto

La escala de magnitud es **logarítmica**: cada punto más significa unas 32 veces más energía. Elige una magnitud y compárala con terremotos famosos.

!sim magnitud

## La historia de la Tierra en un año

Si comprimimos los 4.540 millones de años de la Tierra en un solo año del calendario, la vida aparece pronto, pero los animales grandes llegan tarde, y nosotros, en el último suspiro.

!sim reloj

> En ese calendario, toda la historia escrita de la humanidad, desde las primeras escrituras de Mesopotamia hasta hoy, ocupa los últimos 40 segundos del 31 de diciembre.
""",
    """
The Earth's numbers, like those of the universe, are hard to picture: thousands of kilometres of rock, billions of years, energies equal to thousands of bombs. These simulators bring them down to human scale. They all run in your browser.

## Journey to the centre of the Earth

Move the slider to descend from the surface to the centre of the planet, 6,371 km down. You will see which [layer](@estructura-de-la-tierra) you are in, the approximate temperature and pressure, and how long it would take to walk there.

!sim centro

The deepest hole we have ever made, the **Kola borehole** in Russia, reached 12.3 km: barely 0.2% of the way. Everything we know about the interior we have worked out by studying how waves from [earthquakes](@terremotos-y-tsunamis) travel through it.

## The energy of an earthquake

The magnitude scale is **logarithmic**: each extra point means about 32 times more energy. Pick a magnitude and compare it with famous earthquakes.

!sim magnitud

## The history of the Earth in one year

If we squeeze the Earth's 4.54 billion years into a single calendar year, life appears early, but large animals arrive late, and we turn up at the very last moment.

!sim reloj

> On that calendar, the whole of written human history, from the first writing in Mesopotamia to today, fills the last 40 seconds of 31 December.
""",
    datos=[("Radio de la Tierra", "Earth's radius", "6.371 km", "6,371 km"),
           ("Agujero más profundo", "Deepest hole", "Pozo de Kola, 12,3 km", "Kola borehole, 12.3 km"),
           ("Temperatura del centro", "Temperature at the centre", "≈ 5.200-5.400 °C", "≈ 5,200–5,400 °C"),
           ("Un punto más de magnitud", "One more magnitude point", "≈ 32 veces más energía", "≈ 32 times more energy"),
           ("Edad de la Tierra", "Age of the Earth", "4.540 millones de años", "4.54 billion years")],
    pie=("Las capas de la Tierra, de la corteza al núcleo interno.",
         "The Earth's layers, from the crust to the inner core."),
)

RECORDS = F(
    ("records-de-la-tierra", "earth-records"),
    ("Récords del planeta", "Planet records"),
    ("El punto más alto y el más profundo, el río más largo, el lago más hondo, la cascada más alta, el lugar más lluvioso y otros récords de la Tierra.",
     "The highest and deepest points, the longest river, the deepest lake, the tallest waterfall, the wettest place and other Earth records."),
    ("récords de la Tierra, lugar más alto, lugar más profundo, río más largo del mundo, Nilo, Amazonas, lago más profundo, Baikal, cascada más alta, Salto Ángel, lugar más lluvioso, temperatura más alta, temperatura más baja, mar Muerto, punto más bajo",
     "Earth records, highest place, deepest place, longest river in the world, Nile, Amazon, deepest lake, Baikal, tallest waterfall, Angel Falls, wettest place, highest temperature, lowest temperature, Dead Sea, lowest point"),
    "nilo",
    """
Una colección de los récords naturales más asombrosos del planeta. Algunos se discuten todavía, porque dependen de cómo se mida; lo indicamos cuando es así.

## Alturas y profundidades

| Récord | Dónde | Cifra |
|---|---|---|
| Punto más alto | [Everest](@montanas-y-cordilleras) | 8.849 m |
| Punto más profundo | Abismo Challenger, [fosa de las Marianas](@vida-en-las-profundidades) | ≈ 10.935 m bajo el mar |
| Punto más bajo en tierra firme | Orilla del **mar Muerto** | ≈ 430 m bajo el nivel del mar, y bajando |
| Cañón más profundo | Cañón del Yarlung Tsangpo (Tíbet) | ≈ 5.000 m |
| Cueva más profunda | Cueva Veryovkina (Georgia) | 2.212 m |

La diferencia entre la cima del Everest y el fondo de las Marianas es de casi 20 km. Parece mucho, pero si la Tierra fuera del tamaño de una bola de billar, sería más lisa que una bola de billar real.

## Agua

| Récord | Dónde | Cifra |
|---|---|---|
| Río más largo | **Nilo** o **Amazonas** (en discusión) | ≈ 6.650 / 6.400-7.000 km |
| Río más caudaloso | [Amazonas](@rios-y-lagos) | ≈ 209.000 m³/s |
| Lago más profundo | [Baikal](@rios-y-lagos) (Rusia) | 1.642 m |
| Lago más grande | Mar Caspio | ≈ 371.000 km² |
| Cascada más alta | **Salto Ángel** (Venezuela) | 979 m |
| Cascada con más caudal | Cataratas del Congo (Inga) | ≈ 25.000 m³/s |
| Mar más salado | Mar Muerto | ≈ 34 % de sal, diez veces el océano |

El **mar Muerto** es tan salado que en él se flota sin esfuerzo y apenas hay vida. Su nivel baja más de un metro al año porque se desvía el agua del río Jordán.

!foto mar_muerto | Formaciones de sal en la orilla del mar Muerto, el lugar más bajo de la superficie terrestre.

## Clima

| Récord | Dónde | Cifra |
|---|---|---|
| Temperatura más alta fiable | Valle de la Muerte (EE. UU.) | 54,4 °C |
| Temperatura más baja | Base Vostok ([Antártida](@polos)) | −89,2 °C |
| Lugar más lluvioso | Mawsynram (India) | ≈ 11.800 mm al año |
| Lugar más seco | [Desierto de Atacama](@desiertos) (Chile) | < 1 mm al año en algunas zonas |
| Viento más fuerte medido | Isla Barrow (Australia), ciclón Olivia, 1996 | 408 km/h |
| Granizo más grande | Vivian (EE. UU.), 2010 | 20 cm de diámetro |
| Récord en España | La Rambla (Córdoba), 2021 | 47,4 °C |

## Seres vivos

- **El ser vivo más grande**: un hongo *Armillaria* de Oregón que ocupa casi 10 km² bajo tierra.
- **El árbol más alto**: *Hyperion*, una secuoya de 116 m (ver [bosques](@bosques-y-selvas)).
- **El animal más grande**: la ballena azul, hasta 30 m.
- **El animal más rápido**: el halcón peregrino, a más de 320 km/h en picado.
- **El ser vivo más longevo**: quizá la [posidonia](@arrecifes-y-vida-marina) de Ibiza y Formentera, de hasta 100.000 años.

> El monte Everest no es el lugar más cercano a las estrellas: por el abultamiento del ecuador, la cima del volcán Chimborazo, en Ecuador, está unos 2 km más lejos del centro de la Tierra.
""",
    """
A collection of the planet's most astonishing natural records. Some are still debated because they depend on how things are measured; we say so when that is the case.

## Heights and depths

| Record | Where | Figure |
|---|---|---|
| Highest point | [Everest](@montanas-y-cordilleras) | 8,849 m |
| Deepest point | Challenger Deep, [Mariana Trench](@vida-en-las-profundidades) | ≈ 10,935 m below sea level |
| Lowest point on dry land | Shore of the **Dead Sea** | ≈ 430 m below sea level, and falling |
| Deepest canyon | Yarlung Tsangpo Grand Canyon (Tibet) | ≈ 5,000 m |
| Deepest cave | Veryovkina Cave (Georgia) | 2,212 m |

The difference between the top of Everest and the bottom of the Mariana Trench is almost 20 km. It sounds like a lot, but if the Earth were the size of a billiard ball, it would be smoother than a real billiard ball.

## Water

| Record | Where | Figure |
|---|---|---|
| Longest river | **Nile** or **Amazon** (disputed) | ≈ 6,650 / 6,400–7,000 km |
| Greatest river flow | [Amazon](@rios-y-lagos) | ≈ 209,000 m³/s |
| Deepest lake | [Baikal](@rios-y-lagos) (Russia) | 1,642 m |
| Largest lake | Caspian Sea | ≈ 371,000 km² |
| Tallest waterfall | **Angel Falls** (Venezuela) | 979 m |
| Waterfall with greatest flow | Congo (Inga) Falls | ≈ 25,000 m³/s |
| Saltiest sea | Dead Sea | ≈ 34% salt, ten times the ocean |

The **Dead Sea** is so salty that you float effortlessly and almost nothing lives in it. Its level is dropping by more than a metre a year because the Jordan River's water is diverted.

!foto mar_muerto | Salt formations on the shore of the Dead Sea, the lowest place on the Earth's land surface.

## Climate

| Record | Where | Figure |
|---|---|---|
| Highest reliable temperature | Death Valley (USA) | 54.4 °C |
| Lowest temperature | Vostok Station ([Antarctica](@polos)) | −89.2 °C |
| Wettest place | Mawsynram (India) | ≈ 11,800 mm a year |
| Driest place | [Atacama Desert](@desiertos) (Chile) | < 1 mm a year in some areas |
| Strongest wind measured | Barrow Island (Australia), Cyclone Olivia, 1996 | 408 km/h |
| Largest hailstone | Vivian (USA), 2010 | 20 cm across |
| Spain's record | La Rambla (Córdoba), 2021 | 47.4 °C |

## Living things

- **Largest living thing**: an *Armillaria* fungus in Oregon covering almost 10 km² underground.
- **Tallest tree**: *Hyperion*, a 116 m redwood (see [forests](@bosques-y-selvas)).
- **Largest animal**: the blue whale, up to 30 m.
- **Fastest animal**: the peregrine falcon, over 320 km/h in a dive.
- **Oldest living thing**: perhaps the [posidonia](@arrecifes-y-vida-marina) meadow off Ibiza and Formentera, up to 100,000 years old.

> Mount Everest is not the place closest to the stars: because of the bulge at the equator, the summit of the Chimborazo volcano in Ecuador is about 2 km farther from the Earth's centre.
""",
    datos=[("Punto más alto", "Highest point", "Everest, 8.849 m", "Everest, 8,849 m"),
           ("Punto más profundo", "Deepest point", "Abismo Challenger, ≈ 10.935 m", "Challenger Deep, ≈ 10,935 m"),
           ("Cascada más alta", "Tallest waterfall", "Salto Ángel, 979 m", "Angel Falls, 979 m"),
           ("Lago más profundo", "Deepest lake", "Baikal, 1.642 m", "Baikal, 1,642 m"),
           ("Lugar más lluvioso", "Wettest place", "Mawsynram, ≈ 11.800 mm/año", "Mawsynram, ≈ 11,800 mm/year"),
           ("Récord de calor en España", "Spain's heat record", "47,4 °C (2021)", "47.4 °C (2021)")],
    pie=("El Nilo, uno de los dos ríos más largos del mundo, visto desde el espacio.",
         "The Nile, one of the two longest rivers in the world, seen from space."),
)

EXTREMOS = F(
    ("lugares-extremos", "extreme-places"),
    ("Lugares extremos", "Extreme places"),
    ("Dallol, el lago Natron, la Cueva de los Cristales, la puerta del infierno y otros lugares de la Tierra que parecen de otro planeta.",
     "Dallol, Lake Natron, the Cave of the Crystals, the Door to Hell and other places on Earth that look like another planet."),
    ("lugares extremos, lugares más raros del mundo, Dallol, lago Natron, Cueva de los Cristales, Naica, puerta del infierno, Darvaza, Valle de la Muerte, piedras que se mueven, Oymyakón, lugar más frío habitado, Danakil",
     "extreme places, strangest places in the world, Dallol, Lake Natron, Cave of the Crystals, Naica, Door to Hell, Darvaza, Death Valley, sailing stones, Oymyakon, coldest inhabited place, Danakil"),
    "dallol",
    """
Hay rincones del planeta tan calientes, tan ácidos o tan extraños que parecen escenarios de otro mundo. Muchos de ellos interesan a los científicos que buscan vida en [Marte](@marte) o en las [lunas](@lunas) heladas del sistema solar.

## Dallol (Etiopía)

En la **depresión de Danakil**, a más de 100 metros bajo el nivel del mar, el área volcánica de **Dallol** es uno de los lugares más calientes e inhóspitos del planeta: la temperatura media anual ronda los 35 °C. Sus charcas son de colores amarillo, verde y naranja intenso por el azufre, el hierro y las sales, y algunas son más ácidas que el ácido de las baterías. Durante años se discutió si podía existir vida allí: algunos estudios han encontrado microbios en sus bordes, pero las charcas más extremas parecen estériles.

## La Cueva de los Cristales (México)

En 2000, unos mineros de **Naica**, en Chihuahua, encontraron a 300 metros de profundidad una cueva llena de **cristales de yeso gigantes**, de hasta 12 metros de largo y 55 toneladas, los mayores conocidos. Se formaron durante unos 500.000 años en agua caliente rica en minerales. Dentro se alcanzan unos 50 °C con casi el 100 % de humedad: una persona sin protección no aguanta más de diez minutos. Hoy está de nuevo inundada.

!foto cueva_cristales | Los cristales gigantes de yeso de la cueva de Naica, en México.

## El lago Natron (Tanzania)

Es un lago tan alcalino, con un pH de hasta 10,5, y caliente que puede quemar la piel. Los animales que mueren en él quedan cubiertos de sales y parecen convertidos en piedra. Sin embargo, es el principal lugar de cría del **flamenco enano**: más de dos millones nacen allí, a salvo de los depredadores que no se atreven a entrar.

## La puerta del infierno (Turkmenistán)

En el desierto de Karakum, el cráter de **Darvaza** lleva ardiendo desde hace más de 50 años. Se cree que se formó al hundirse el terreno durante una prospección de gas soviética, y se le prendió fuego para que el metano no se extendiera. Nunca se ha apagado, aunque las llamas han disminuido en los últimos años.

## El pueblo más frío del mundo

**Oymyakón**, en Siberia, con unos 500 habitantes, registró −67,7 °C en 1933. En invierno, las temperaturas de −50 °C son normales. Los coches se dejan arrancados todo el día porque, si se apagan, no vuelven a encender, y las tumbas se excavan derritiendo el suelo helado con hogueras.

## Las piedras que caminan

En el **Racetrack Playa**, un lago seco del Valle de la Muerte, hay rocas de hasta 300 kilos que dejan largos surcos en el suelo, como si se arrastraran solas. El misterio duró décadas hasta que en 2014 se grabó la explicación: en invierno se forma una fina capa de hielo que, al romperse en placas, empujada por un viento suave, desplaza las piedras unos pocos metros por minuto.

## Extremos en España

- La **sima del Trave**, en los Picos de Europa, supera los 1.400 metros de profundidad.
- **Los Monegros** y el **Desierto de Tabernas** registran algunos de los paisajes más áridos de Europa.
- El **Río Tinto** es uno de los ríos más ácidos del mundo, y uno de los modelos de vida extraterrestre que estudia la NASA (ver [el origen de la vida](@origen-de-la-vida)).

> La isla de Bouvet, en el Atlántico Sur, es la más remota del mundo: el lugar con tierra más cercano es la Antártida, a 1.600 km. Está casi totalmente cubierta de hielo y no tiene habitantes.
""",
    """
Some corners of the planet are so hot, so acidic or so strange that they look like scenes from another world. Many of them interest scientists searching for life on [Mars](@marte) or the icy [moons](@lunas) of the solar system.

## Dallol (Ethiopia)

In the **Danakil Depression**, more than 100 metres below sea level, the **Dallol** volcanic area is one of the hottest and most hostile places on the planet: the average annual temperature is around 35 °C. Its pools glow yellow, green and bright orange from sulphur, iron and salts, and some are more acidic than battery acid. For years scientists debated whether life could exist there: some studies have found microbes around their edges, but the most extreme pools appear to be sterile.

## The Cave of the Crystals (Mexico)

In 2000, miners at **Naica** in Chihuahua found, 300 metres underground, a cave full of **giant gypsum crystals** up to 12 metres long and 55 tonnes, the largest known. They grew over about 500,000 years in hot, mineral-rich water. Inside, temperatures reach about 50 °C with nearly 100% humidity: an unprotected person cannot last more than ten minutes. Today it is flooded again.

!foto cueva_cristales | The giant gypsum crystals of the Naica cave in Mexico.

## Lake Natron (Tanzania)

This lake is so alkaline, with a pH up to 10.5, and so hot that it can burn skin. Animals that die in it become coated in salts and look as if they have turned to stone. Yet it is the main breeding site of the **lesser flamingo**: more than two million are born there, safe from predators that dare not wade in.

## The Door to Hell (Turkmenistan)

In the Karakum Desert, the **Darvaza** crater has been burning for more than 50 years. It is thought to have formed when the ground collapsed during a Soviet gas survey, and it was set alight to stop the methane spreading. It has never gone out, although the flames have died down in recent years.

## The coldest village in the world

**Oymyakon** in Siberia, with about 500 residents, recorded −67.7 °C in 1933. In winter, temperatures of −50 °C are normal. Cars are left running all day because, if switched off, they will not start again, and graves are dug by thawing the frozen ground with bonfires.

## The walking stones

At **Racetrack Playa**, a dry lake in Death Valley, rocks weighing up to 300 kilos leave long trails in the ground, as if they moved by themselves. The mystery lasted for decades until in 2014 the explanation was filmed: in winter a thin sheet of ice forms which, breaking into panels pushed by a gentle wind, moves the stones a few metres a minute.

## Extremes in Spain

- The **Sima del Trave** in the Picos de Europa is more than 1,400 metres deep.
- **Los Monegros** and the **Tabernas Desert** have some of the most arid landscapes in Europe.
- The **Río Tinto** is one of the most acidic rivers in the world, and one of the models for alien life studied by NASA (see [the origin of life](@origen-de-la-vida)).

> Bouvet Island in the South Atlantic is the most remote island in the world: the nearest land is Antarctica, 1,600 km away. It is almost entirely covered in ice and has no inhabitants.
""",
    datos=[("Temperatura media de Dallol", "Average temperature at Dallol", "≈ 35 °C", "≈ 35 °C"),
           ("Mayores cristales", "Largest crystals", "Naica, hasta 12 m", "Naica, up to 12 m"),
           ("pH del lago Natron", "pH of Lake Natron", "Hasta 10,5", "Up to 10.5"),
           ("Pueblo más frío", "Coldest village", "Oymyakón, −67,7 °C", "Oymyakon, −67.7 °C"),
           ("Isla más remota", "Most remote island", "Bouvet, a 1.600 km de tierra", "Bouvet, 1,600 km from land")],
    pie=("Las charcas de colores de Dallol, en Etiopía, uno de los lugares más extremos del planeta.",
         "The coloured pools of Dallol, in Ethiopia, one of the most extreme places on the planet."),
)

FENOMENOS = F(
    ("fenomenos-asombrosos", "amazing-phenomena"),
    ("Fenómenos asombrosos", "Amazing phenomena"),
    ("Arcoíris, copos de nieve únicos, géiseres, tornados de fuego, lluvia de peces y el olor a tierra mojada: la ciencia detrás de las maravillas cotidianas.",
     "Rainbows, unique snowflakes, geysers, fire tornadoes, raining fish and the smell of rain: the science behind everyday wonders."),
    ("fenómenos naturales, arcoíris, copos de nieve, géiseres, tornados, olor a lluvia, petricor, bioluminiscencia, lluvia de animales, rayo globular, relámpago del Catatumbo, mar de nubes, fenómenos curiosos",
     "natural phenomena, rainbow, snowflakes, geysers, tornadoes, smell of rain, petrichor, bioluminescence, raining animals, ball lightning, Catatumbo lightning, sea of clouds, curious phenomena"),
    "arcoiris",
    """
La naturaleza tiene trucos que parecen magia. Casi todos tienen una explicación científica igual de asombrosa.

## El arcoíris

Un arcoíris aparece cuando tenemos el Sol a la espalda y lluvia delante. Cada gota actúa como un pequeño prisma: la luz entra, se refleja en el fondo de la gota y sale separada en colores, siempre con un ángulo de unos 42°. Por eso el arcoíris es en realidad un **círculo completo**: desde un avión se puede ver entero. Y cada persona ve su propio arcoíris, formado por gotas distintas. A veces aparece un **arcoíris doble**, con los colores invertidos (más en [fenómenos ópticos](@auroras-y-fenomenos-opticos)).

## No hay dos copos de nieve iguales

Un copo de nieve está formado por hasta un trillón de moléculas de agua que se ordenan en una forma de **seis brazos**. Mientras cae, cada copo pasa por zonas con distinta temperatura y humedad que modifican su crecimiento. Como el camino de cada uno es único, es prácticamente imposible que dos copos sean idénticos. El primero en fotografiarlos, en 1885, fue un granjero estadounidense, Wilson Bentley, que retrató más de 5.000.

!foto copo | Un copo de nieve fotografiado al microscopio: siempre tiene simetría de seis.

## Géiseres

Un **géiser** es una fuente termal que lanza chorros de agua hirviendo y vapor. El agua se calienta en el subsuelo por el magma hasta que la presión la hace estallar. La palabra viene del **Geysir** de Islandia. El cercano **Strokkur** entra en erupción cada pocos minutos, y el **Old Faithful** de Yellowstone lo hace cada hora y media, más o menos.

## El olor de la lluvia

Ese olor a tierra mojada se llama **petricor**. Lo producen sobre todo unas bacterias del suelo que fabrican una sustancia, la **geosmina**, y las gotas de lluvia la lanzan al aire en forma de pequeños aerosoles. Nuestro olfato es extraordinariamente sensible a ella: podemos detectarla en concentraciones de unas pocas partes por billón, más que un tiburón detecta la sangre.

## Lluvia de peces y ranas

Hay registros históricos de **lluvias de peces, ranas y gusanos**. La explicación más aceptada son las **trombas marinas**: tornados sobre el agua que aspiran animales pequeños y los sueltan kilómetros más allá. En Yoro (Honduras) se celebra un festival de la «lluvia de peces», que ocurre, según los vecinos, casi todos los años.

## El relámpago del Catatumbo

Sobre la desembocadura del río Catatumbo en el lago de Maracaibo (Venezuela) se producen tormentas eléctricas casi 300 noches al año, con decenas de rayos por minuto. Es el lugar con más [rayos](@tormentas-y-huracanes) del mundo. Los marineros lo usaban como faro natural.

## Bioluminiscencia

En algunas playas, al mover el agua de noche, esta se ilumina de azul. Son algas microscópicas, los **dinoflagelados**, que emiten luz al ser agitadas. Muchos animales de las [profundidades](@vida-en-las-profundidades) también fabrican su propia luz, al igual que las luciérnagas y algunos hongos.

## Mar de nubes

Cuando una capa de nubes bajas queda atrapada bajo aire más cálido, las montañas sobresalen como islas en un océano blanco. En **Canarias**, el mar de nubes que traen los vientos alisios es tan habitual que alimenta de humedad los bosques de [laurisilva](@bosques-y-selvas).

> El rayo globular, una bola de luz que flota durante segundos durante las tormentas, fue considerado un mito durante siglos. En 2012, unos científicos chinos lo grabaron por casualidad con un espectrómetro, aunque todavía no se sabe con certeza cómo se forma.
""",
    """
Nature has tricks that look like magic. Almost all of them have a scientific explanation that is just as amazing.

## The rainbow

A rainbow appears when the Sun is behind us and rain is in front. Each drop acts like a tiny prism: light enters, reflects off the back of the drop and leaves split into colours, always at an angle of about 42°. That is why a rainbow is really a **full circle**: from a plane you can see all of it. And each person sees their own rainbow, made by different drops. Sometimes a **double rainbow** appears, with its colours reversed (more in [optical phenomena](@auroras-y-fenomenos-opticos)).

## No two snowflakes are alike

A snowflake is made of up to a quintillion water molecules arranged in a **six-armed** shape. As it falls, each flake passes through zones of different temperature and humidity that change how it grows. Because each one's journey is unique, it is practically impossible for two flakes to be identical. The first person to photograph them, in 1885, was an American farmer, Wilson Bentley, who captured more than 5,000.

!foto copo | A snowflake photographed under a microscope: it always has six-fold symmetry.

## Geysers

A **geyser** is a hot spring that shoots out jets of boiling water and steam. The water is heated underground by magma until the pressure makes it burst out. The word comes from **Geysir** in Iceland. Nearby **Strokkur** erupts every few minutes, and Yellowstone's **Old Faithful** roughly every hour and a half.

## The smell of rain

That smell of wet earth is called **petrichor**. It comes mainly from soil bacteria that make a substance called **geosmin**, and raindrops fling it into the air as tiny aerosols. Our sense of smell is extraordinarily sensitive to it: we can detect it at a few parts per trillion, better than a shark detects blood.

## Raining fish and frogs

There are historical records of **showers of fish, frogs and worms**. The most accepted explanation is **waterspouts**: tornadoes over water that suck up small animals and drop them kilometres away. In Yoro, Honduras, a "rain of fish" festival is held, as locals say it happens almost every year.

## Catatumbo lightning

Over the mouth of the Catatumbo River at Lake Maracaibo (Venezuela), thunderstorms occur nearly 300 nights a year, with dozens of flashes a minute. It is the place with the most [lightning](@tormentas-y-huracanes) in the world. Sailors used it as a natural lighthouse.

## Bioluminescence

On some beaches, stirring the water at night makes it glow blue. It is microscopic algae, **dinoflagellates**, that give off light when disturbed. Many [deep-sea](@vida-en-las-profundidades) animals also make their own light, as do fireflies and some fungi.

## Sea of clouds

When a layer of low cloud is trapped beneath warmer air, mountains poke out like islands in a white ocean. In the **Canary Islands**, the sea of clouds brought by the trade winds is so common that it feeds moisture to the [laurel forests](@bosques-y-selvas).

> Ball lightning, a ball of light that floats for seconds during storms, was considered a myth for centuries. In 2012 Chinese scientists happened to record one with a spectrometer, although how it forms is still not known for certain.
""",
    datos=[("Ángulo del arcoíris", "Rainbow angle", "≈ 42°", "≈ 42°"),
           ("Brazos de un copo", "Arms of a snowflake", "6", "6"),
           ("Sustancia del olor a lluvia", "Smell-of-rain compound", "Geosmina", "Geosmin"),
           ("Lugar con más rayos", "Place with most lightning", "Lago de Maracaibo (Catatumbo)", "Lake Maracaibo (Catatumbo)"),
           ("Strokkur (Islandia)", "Strokkur (Iceland)", "Erupción cada pocos minutos", "Erupts every few minutes")],
    pie=("Un arcoíris doble: en el segundo arco los colores aparecen invertidos.",
         "A double rainbow: in the second arc the colours are reversed."),
)

MITOS = F(
    ("mitos-de-la-tierra", "earth-myths"),
    ("Falsos mitos sobre la Tierra", "Myths about the Earth"),
    ("La Gran Muralla vista desde el espacio, los rayos que no caen dos veces, el agua que gira al revés en el otro hemisferio y otros mitos sobre la Tierra.",
     "The Great Wall seen from space, lightning never striking twice, water swirling the other way in the other hemisphere and other myths about the Earth."),
    ("mitos sobre la Tierra, falsos mitos, Gran Muralla vista desde el espacio, rayo dos veces mismo sitio, efecto Coriolis lavabo, estaciones distancia al Sol, Colón Tierra plana, Tierra plana, Sahara caliente, diamantes carbón, mitos de geografía",
     "myths about the Earth, misconceptions, Great Wall visible from space, lightning strikes twice, Coriolis effect sink, seasons distance from the Sun, Columbus flat Earth, flat Earth, diamonds from coal, geography myths"),
    "calzada",
    """
Algunas ideas sobre la Tierra se repiten tanto que parecen ciertas. Estas son algunas de las más extendidas, y lo que dice la ciencia.

## «La Gran Muralla china se ve desde el espacio»

**Falso.** La muralla es muy larga pero estrecha, de unos 6 metros, y del mismo color que el terreno. Desde la Estación Espacial, a 400 km, los astronautas no la distinguen a simple vista. Se ven mejor las autopistas, los aeropuertos, los invernaderos de **Almería** (que forman un enorme mar de plástico blanco) o las luces de las ciudades de noche.

## «Hace calor en verano porque estamos más cerca del Sol»

**Falso.** La Tierra está más cerca del Sol a principios de **enero**, en pleno invierno del hemisferio norte. Las estaciones se deben a la **inclinación del eje** de la Tierra (unos 23,4°): en verano, los rayos del Sol nos llegan más directos y los días son más largos. Por eso, cuando en España es verano, en Argentina es invierno (más en [la Tierra](@tierra)).

## «Un rayo nunca cae dos veces en el mismo sitio»

**Falso.** Los [rayos](@tormentas-y-huracanes) caen una y otra vez en los lugares altos y conductores. El Empire State Building recibe unos 20-25 rayos al año. Y el guardabosques estadounidense Roy Sullivan sobrevivió a siete rayos a lo largo de su vida.

## «En el hemisferio sur el agua del lavabo gira al revés»

**Falso**, al menos en un lavabo. El **efecto Coriolis**, causado por la rotación de la Tierra, sí hace que los [huracanes](@tormentas-y-huracanes) giren en sentidos contrarios en cada hemisferio. Pero en algo tan pequeño como un lavabo es muchísimo más débil que la forma del recipiente o el movimiento del agua al llenarlo.

## «En la Edad Media se creía que la Tierra era plana»

**Falso.** Los sabios griegos ya sabían que la Tierra es redonda, y hacia el 240 a. C. **Eratóstenes** midió su tamaño con bastante precisión usando sombras. En la Edad Media, las personas cultas lo daban por hecho. Los expertos que se oponían al viaje de **Colón** no pensaban que se caería por un borde: sabían que la Tierra era mucho más grande de lo que él calculaba, y tenían razón. Colón sobrevivió porque, sin saberlo, encontró un continente en medio.

## «Los diamantes se forman a partir del carbón»

**Falso.** Los diamantes se forman a unos 150 km de profundidad, en el [manto](@estructura-de-la-tierra), a partir de carbono sometido a presiones y temperaturas enormes, y la mayoría tienen más de mil millones de años: son anteriores a las plantas terrestres de las que procede el carbón. Llegan a la superficie en erupciones volcánicas muy profundas y rápidas.

## «El Sahara siempre ha sido un desierto»

**Falso.** Hace solo 6.000 años era una sabana verde con lagos y animales (ver [desiertos](@desiertos)).

## «Los camellos guardan agua en la joroba»

**Falso.** La joroba es una reserva de **grasa**, que el animal puede convertir en energía cuando no encuentra comida. Su resistencia a la sed se debe a otras adaptaciones: pierden muy poca agua al orinar y sudar, y sus glóbulos rojos aguantan cambios bruscos de hidratación.

> El monte más alto del sistema solar no está en la Tierra: es el Olympus Mons, en [Marte](@marte), de unos 22 km de altura, casi tres Everest.
""",
    """
Some ideas about the Earth are repeated so often that they seem true. Here are some of the most widespread, and what science says.

## "The Great Wall of China can be seen from space"

**False.** The wall is very long but narrow, about 6 metres, and the same colour as the land around it. From the Space Station, 400 km up, astronauts cannot pick it out with the naked eye. Motorways, airports, the greenhouses of **Almería** (a vast sea of white plastic) and city lights at night are far easier to see.

## "It's hot in summer because we are closer to the Sun"

**False.** The Earth is closest to the Sun in early **January**, in the depths of the northern hemisphere's winter. The seasons are caused by the **tilt of the Earth's axis** (about 23.4°): in summer, sunlight strikes us more directly and days are longer. That is why when it is summer in Spain, it is winter in Argentina (more on [the Earth](@tierra)).

## "Lightning never strikes the same place twice"

**False.** [Lightning](@tormentas-y-huracanes) strikes tall, conductive places again and again. The Empire State Building is hit about 20–25 times a year. And US park ranger Roy Sullivan survived seven lightning strikes during his life.

## "Water drains the other way in the southern hemisphere"

**False**, at least in a sink. The **Coriolis effect**, caused by the Earth's rotation, does make [hurricanes](@tormentas-y-huracanes) spin in opposite directions in each hemisphere. But in something as small as a sink it is far weaker than the shape of the basin or the motion of the water as it filled.

## "In the Middle Ages people thought the Earth was flat"

**False.** Greek scholars already knew the Earth was round, and around 240 BC **Eratosthenes** measured its size quite accurately using shadows. In the Middle Ages, educated people took it for granted. The experts who opposed **Columbus**'s voyage did not think he would fall off an edge: they knew the Earth was much bigger than he calculated, and they were right. Columbus survived because, without knowing it, he found a continent in the way.

## "Diamonds form from coal"

**False.** Diamonds form about 150 km down, in the [mantle](@estructura-de-la-tierra), from carbon under enormous pressure and heat, and most are more than a billion years old: older than the land plants that coal comes from. They reach the surface in very deep, fast volcanic eruptions.

## "The Sahara has always been a desert"

**False.** Just 6,000 years ago it was a green savanna with lakes and animals (see [deserts](@desiertos)).

## "Camels store water in their humps"

**False.** The hump is a store of **fat**, which the animal can turn into energy when food is scarce. Its resistance to thirst comes from other adaptations: camels lose very little water in urine and sweat, and their red blood cells cope with sudden changes in hydration.

> The tallest mountain in the solar system is not on Earth: it is Olympus Mons on [Mars](@marte), about 22 km high, almost three Everests.
""",
    datos=[("Anchura de la Gran Muralla", "Width of the Great Wall", "≈ 6 m", "≈ 6 m"),
           ("Perihelio (más cerca del Sol)", "Perihelion (closest to the Sun)", "Principios de enero", "Early January"),
           ("Inclinación del eje", "Axial tilt", "≈ 23,4°", "≈ 23.4°"),
           ("Rayos al año en el Empire State", "Lightning strikes a year on the Empire State", "≈ 20-25", "≈ 20–25"),
           ("Profundidad de formación del diamante", "Depth where diamonds form", "≈ 150 km", "≈ 150 km")],
    pie=("La Calzada del Gigante (Irlanda del Norte): una leyenda dice que la construyó un gigante; en realidad son columnas de lava enfriada.",
         "The Giant's Causeway (Northern Ireland): legend says a giant built it; in fact the columns are cooled lava."),
)

FICHAS = [SIMULADORES, RECORDS, EXTREMOS, FENOMENOS, MITOS]
