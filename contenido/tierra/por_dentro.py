from universo import F

SLUG = ("tierra-por-dentro", "inside-the-earth")
TITULO = ("La Tierra por dentro", "Inside the Earth")
RESUMEN = ("Capas del planeta, placas tectónicas, volcanes, terremotos, rocas y minerales, y los 4.540 millones de años de historia que guardan.",
           "The planet's layers, tectonic plates, volcanoes, earthquakes, rocks and minerals, and the 4.54 billion years of history they hold.")
CLAVES = ("geología, capas de la Tierra, núcleo, manto, corteza, tectónica de placas, volcanes, terremotos, tsunamis, rocas, minerales, historia de la Tierra, eras geológicas, fósiles",
          "geology, Earth's layers, core, mantle, crust, plate tectonics, volcanoes, earthquakes, tsunamis, rocks, minerals, history of the Earth, geological eras, fossils")
FOTO = "volcan"
INTRO = ("""
Bajo nuestros pies hay un planeta vivo: un núcleo tan caliente como la superficie del Sol, un manto que fluye muy despacio y una corteza rota en placas que se mueven, chocan y se separan. De ese movimiento nacen las montañas, los volcanes y los terremotos.
""", """
Beneath our feet lies a living planet: a core as hot as the surface of the Sun, a mantle that flows very slowly and a crust broken into plates that move, collide and pull apart. That movement gives rise to mountains, volcanoes and earthquakes.
""")

ESTRUCTURA = F(
    ("estructura-de-la-tierra", "structure-of-the-earth"),
    ("Las capas de la Tierra", "The Earth's layers"),
    ("Corteza, manto y núcleo: un viaje de 6.371 km hasta el centro del planeta, donde hace tanto calor como en la superficie del Sol.",
     "Crust, mantle and core: a 6,371 km journey to the centre of the planet, where it is as hot as the surface of the Sun."),
    ("capas de la Tierra, estructura interna, corteza terrestre, manto, núcleo externo, núcleo interno, litosfera, astenosfera, discontinuidad de Mohorovičić, Inge Lehmann, campo magnético, pozo de Kola, centro de la Tierra",
     "layers of the Earth, internal structure, Earth's crust, mantle, outer core, inner core, lithosphere, asthenosphere, Moho, Inge Lehmann, magnetic field, Kola Superdeep Borehole, centre of the Earth"),
    "capas",
    """
Nadie ha viajado nunca al centro de la Tierra. El agujero más profundo jamás perforado, el **pozo superprofundo de Kola**, en Rusia, llegó en 1989 a 12.262 metros: apenas un 0,2 % del camino. Aun así, sabemos con bastante precisión cómo es el interior del planeta gracias a los **terremotos**: sus ondas atraviesan la Tierra, se aceleran, se frenan, se desvían o desaparecen según el material que cruzan, como una ecografía gigante.

## Un planeta en capas

| Capa | Profundidad | Cómo es |
|---|---|---|
| **Corteza** | 0 a 5-70 km | Roca sólida. Fina bajo los océanos (5-10 km) y gruesa bajo los continentes (30-70 km) |
| **Manto superior** | Hasta 660 km | Roca muy caliente que, a lo largo de millones de años, fluye como plastilina |
| **Manto inferior** | 660 a 2.900 km | Roca sólida sometida a presiones enormes |
| **Núcleo externo** | 2.900 a 5.150 km | Hierro y níquel **líquidos**, a unos 4.000-5.000 °C |
| **Núcleo interno** | 5.150 a 6.371 km | Una bola **sólida** de hierro y níquel a unos 5.200 °C |

La corteza y la parte más rígida del manto forman la **litosfera**, la capa que está rota en [placas tectónicas](@tectonica-de-placas). Debajo, la **astenosfera** es más blanda y permite que las placas se deslicen.

## Un núcleo tan caliente como el Sol

El centro de la Tierra está a unos **5.200 °C**, casi tanto como la superficie del Sol. Ese calor viene en parte de la formación del planeta y en parte de la desintegración de elementos radiactivos como el uranio y el torio. A pesar de la temperatura, el núcleo interno es sólido porque la presión, más de 3,5 millones de veces la de la superficie, impide que el hierro se funda.

En 1936 la sismóloga danesa **Inge Lehmann** descubrió, estudiando ondas de terremotos que aparecían donde no debían, que dentro del núcleo líquido había otro núcleo sólido. Lo publicó en un artículo cuyo título era una sola letra: *P'*.

## El escudo magnético

El hierro líquido del núcleo externo se mueve en corrientes que, junto con la rotación de la Tierra, generan el **campo magnético** del planeta. Es lo que orienta las brújulas y, sobre todo, lo que nos protege del viento solar y de la radiación cósmica. Sin él, la atmósfera se habría ido erosionando, como le ocurrió a [Marte](@marte). Las partículas que se cuelan cerca de los polos producen las [auroras](@auroras-y-fenomenos-opticos).

El campo magnético no es fijo: el polo norte magnético se desplaza decenas de kilómetros al año y, cada cierto tiempo, el campo se invierte por completo. La última inversión fue hace unos 780.000 años.

## La Tierra no es una esfera perfecta

Por la rotación, la Tierra está algo achatada: el diámetro entre los polos es unos 43 km menor que en el ecuador. Por eso el punto más alejado del centro de la Tierra no es la cima del Everest, sino la del volcán **Chimborazo**, en Ecuador, muy cerca del ecuador.

> Si la Tierra fuera del tamaño de una manzana, toda la corteza sobre la que vivimos sería más fina que su piel.
""",
    """
No one has ever travelled to the centre of the Earth. The deepest hole ever drilled, the **Kola Superdeep Borehole** in Russia, reached 12,262 metres in 1989: barely 0.2% of the way. Even so, we know fairly precisely what the planet's interior is like thanks to **earthquakes**: their waves cross the Earth, speeding up, slowing down, bending or vanishing depending on the material they pass through, like a giant ultrasound scan.

## A layered planet

| Layer | Depth | What it is like |
|---|---|---|
| **Crust** | 0 to 5–70 km | Solid rock. Thin under the oceans (5–10 km) and thick under the continents (30–70 km) |
| **Upper mantle** | Down to 660 km | Very hot rock that flows like modelling clay over millions of years |
| **Lower mantle** | 660 to 2,900 km | Solid rock under enormous pressure |
| **Outer core** | 2,900 to 5,150 km | **Liquid** iron and nickel at about 4,000–5,000 °C |
| **Inner core** | 5,150 to 6,371 km | A **solid** ball of iron and nickel at about 5,200 °C |

The crust and the most rigid part of the mantle form the **lithosphere**, the layer broken into [tectonic plates](@tectonica-de-placas). Below it, the softer **asthenosphere** lets the plates slide.

## A core as hot as the Sun

The centre of the Earth is at about **5,200 °C**, nearly as hot as the surface of the Sun. That heat comes partly from the planet's formation and partly from the decay of radioactive elements such as uranium and thorium. Despite the temperature, the inner core is solid because the pressure, more than 3.5 million times that at the surface, stops the iron from melting.

In 1936 the Danish seismologist **Inge Lehmann** discovered, by studying earthquake waves that turned up where they should not, that inside the liquid core there was another, solid core. She published it in a paper whose title was a single letter: *P'*.

## The magnetic shield

Liquid iron in the outer core moves in currents that, together with the Earth's rotation, generate the planet's **magnetic field**. It is what points compass needles and, above all, what shields us from the solar wind and cosmic radiation. Without it, the atmosphere would have been gradually stripped away, as happened on [Mars](@marte). Particles that slip in near the poles produce the [auroras](@auroras-y-fenomenos-opticos).

The magnetic field is not fixed: the magnetic north pole moves tens of kilometres a year and, every so often, the field flips completely. The last reversal was about 780,000 years ago.

## The Earth is not a perfect sphere

Because it spins, the Earth is slightly flattened: the diameter between the poles is about 43 km shorter than at the equator. That is why the point farthest from the centre of the Earth is not the summit of Everest but that of **Chimborazo** volcano in Ecuador, very close to the equator.

> If the Earth were the size of an apple, the entire crust we live on would be thinner than its skin.
""",
    datos=[("Radio medio", "Mean radius", "6.371 km", "6,371 km"),
           ("Grosor de la corteza", "Crust thickness", "5 a 70 km", "5 to 70 km"),
           ("Temperatura del centro", "Temperature at the centre", "≈ 5.200 °C", "≈ 5,200 °C"),
           ("Perforación más profunda", "Deepest borehole", "12.262 m (Kola, 1989)", "12,262 m (Kola, 1989)"),
           ("Núcleo interno descubierto", "Inner core discovered", "Inge Lehmann, 1936", "Inge Lehmann, 1936"),
           ("Edad de la Tierra", "Age of the Earth", "4.540 millones de años", "4.54 billion years")],
    pie=("Esquema de las capas de la Tierra: corteza, manto, núcleo externo líquido y núcleo interno sólido.",
         "Diagram of the Earth's layers: crust, mantle, liquid outer core and solid inner core."),
)

PLACAS = F(
    ("tectonica-de-placas", "plate-tectonics"),
    ("Tectónica de placas", "Plate tectonics"),
    ("La superficie de la Tierra es un puzle de placas que se mueven unos centímetros al año. Así se abren océanos y se levantan cordilleras.",
     "The Earth's surface is a jigsaw of plates moving a few centimetres a year. That is how oceans open and mountain ranges rise."),
    ("tectónica de placas, deriva continental, Alfred Wegener, Pangea, placas litosféricas, dorsal oceánica, subducción, Anillo de Fuego, placa ibérica, supercontinente, movimiento de los continentes",
     "plate tectonics, continental drift, Alfred Wegener, Pangaea, lithospheric plates, mid-ocean ridge, subduction, Ring of Fire, Iberian plate, supercontinent, moving continents"),
    "placas",
    """
Si miras un mapa, la costa de Sudamérica y la de África encajan como dos piezas de un puzle. No es casualidad: hace unos 180 millones de años estaban unidas. La **tectónica de placas** explica por qué los continentes se mueven, y es a la geología lo que la evolución es a la biología: la idea que lo explica casi todo.

## Wegener, el meteorólogo al que nadie creyó

En 1912 el alemán **Alfred Wegener** propuso que los continentes habían estado unidos en un supercontinente al que llamó **Pangea** y que se habían ido separando. Sus pruebas eran sólidas: las costas encajaban, había fósiles idénticos de reptiles y helechos a ambos lados del Atlántico y huellas de antiguos glaciares en zonas hoy tropicales. Pero no podía explicar qué fuerza movía los continentes, y la mayoría de los geólogos se burló de él. Murió en 1930 en una expedición por Groenlandia.

Su idea solo se aceptó en los años sesenta, cuando el estudio de los fondos marinos reveló cordilleras submarinas donde se fabrica corteza nueva y rocas con franjas magnéticas simétricas a ambos lados. La geóloga y cartógrafa **Marie Tharp** dibujó el primer mapa del fondo del Atlántico y descubrió la gran grieta central.

!foto pangea | Pangea, el supercontinente que reunía casi todas las tierras emergidas hace unos 300 a 180 millones de años.

## Un puzle en movimiento

La litosfera está dividida en unas **15 placas grandes** y decenas de pequeñas. Flotan sobre el manto y se mueven entre **2 y 15 centímetros al año**, más o menos lo que crecen las uñas. Lo que las mueve es el calor del interior de la Tierra y, sobre todo, el peso de las placas que se hunden en el manto, que tiran del resto.

## Tres tipos de bordes

- **Divergentes**: las placas se separan y el magma sube a rellenar el hueco. Pasa en las **dorsales oceánicas**, como la del Atlántico, que se abre unos 2,5 cm al año, y en tierra en Islandia o en el **Rift de África Oriental**, que algún día partirá África en dos.
- **Convergentes**: las placas chocan. Si una es oceánica, se hunde bajo la otra en una **zona de subducción**, que crea fosas profundísimas y cadenas de volcanes, como los Andes o Japón. Si chocan dos continentes, la corteza se arruga y se levantan cordilleras: así nació el **Himalaya**, cuando la India chocó con Asia.
- **Transformantes**: las placas se deslizan una junto a la otra, como la **falla de San Andrés** en California, fuente de grandes terremotos.

## El Anillo de Fuego

Alrededor del océano Pacífico, las zonas de subducción forman el **Anillo de Fuego**, un arco de 40.000 km que concentra unas tres cuartas partes de los volcanes activos del mundo y la mayoría de los grandes terremotos.

## La península ibérica

La península está en la **placa euroasiática**, cerca del límite con la africana, que la empuja hacia el norte unos milímetros al año. Ese empuje levantó los Pirineos y las cordilleras Béticas y explica los terremotos del sur y el sureste. Las Canarias, en cambio, son islas volcánicas en el interior de la placa africana.

## El futuro supercontinente

Los continentes se han reunido y separado varias veces. Dentro de unos 200 a 250 millones de años probablemente volverán a juntarse en un nuevo supercontinente, que algunos geólogos llaman **Pangea Última**.

> El Everest todavía crece unos milímetros al año porque la India sigue empujando contra Asia. En su cumbre hay calizas con fósiles marinos: rocas que se formaron en el fondo de un océano.
""",
    """
Look at a map and the coasts of South America and Africa fit together like two jigsaw pieces. It is no coincidence: about 180 million years ago they were joined. **Plate tectonics** explains why continents move, and it is to geology what evolution is to biology: the idea that explains almost everything.

## Wegener, the meteorologist nobody believed

In 1912 the German **Alfred Wegener** proposed that the continents had once been joined in a supercontinent he called **Pangaea** and had drifted apart. His evidence was strong: the coastlines matched, identical fossils of reptiles and ferns turned up on both sides of the Atlantic, and there were traces of ancient glaciers in places that are now tropical. But he could not explain what force moved the continents, and most geologists mocked him. He died in 1930 on an expedition across Greenland.

His idea was only accepted in the 1960s, when the study of the seafloor revealed underwater mountain ranges where new crust is made, and rocks with symmetrical magnetic stripes on either side. The geologist and cartographer **Marie Tharp** drew the first map of the Atlantic seafloor and discovered the great central rift.

!foto pangea | Pangaea, the supercontinent that held almost all the land on Earth from about 300 to 180 million years ago.

## A moving jigsaw

The lithosphere is divided into about **15 large plates** and dozens of small ones. They float on the mantle and move **2 to 15 centimetres a year**, about as fast as fingernails grow. What drives them is the heat from inside the Earth and, above all, the weight of plates sinking into the mantle, which pull the rest along.

## Three kinds of boundary

- **Divergent**: plates pull apart and magma rises to fill the gap. This happens at **mid-ocean ridges**, such as the Atlantic one, which opens about 2.5 cm a year, and on land in Iceland and the **East African Rift**, which will one day split Africa in two.
- **Convergent**: plates collide. If one is oceanic it sinks beneath the other in a **subduction zone**, creating extremely deep trenches and chains of volcanoes, such as the Andes or Japan. If two continents collide, the crust crumples and mountain ranges rise: that is how the **Himalayas** were born, when India crashed into Asia.
- **Transform**: plates slide past each other, like the **San Andreas Fault** in California, a source of major earthquakes.

## The Ring of Fire

Around the Pacific Ocean, subduction zones form the **Ring of Fire**, a 40,000 km arc that holds about three quarters of the world's active volcanoes and most of its great earthquakes.

## The Iberian Peninsula

The peninsula sits on the **Eurasian plate**, close to its boundary with the African plate, which pushes it north a few millimetres a year. That push raised the Pyrenees and the Betic ranges and explains the earthquakes of southern and south-eastern Spain. The Canary Islands, by contrast, are volcanic islands in the interior of the African plate.

## The next supercontinent

The continents have come together and split apart several times. In about 200 to 250 million years they will probably join again in a new supercontinent, which some geologists call **Pangaea Ultima**.

> Everest is still growing a few millimetres a year because India keeps pushing into Asia. Its summit has limestone with marine fossils: rocks that formed at the bottom of an ocean.
""",
    datos=[("Placas principales", "Major plates", "≈ 15", "≈ 15"),
           ("Velocidad", "Speed", "2 a 15 cm al año", "2 to 15 cm a year"),
           ("Deriva continental", "Continental drift", "Alfred Wegener, 1912", "Alfred Wegener, 1912"),
           ("Último supercontinente", "Last supercontinent", "Pangea (hace 300-180 millones de años)", "Pangaea (300–180 million years ago)"),
           ("Anillo de Fuego", "Ring of Fire", "≈ 75 % de los volcanes activos", "≈ 75% of active volcanoes")],
    pie=("Mapa de las principales placas tectónicas de la Tierra y sus límites.",
         "Map of the Earth's main tectonic plates and their boundaries."),
)

VOLCANES = F(
    ("volcanes", "volcanoes"),
    ("Volcanes", "Volcanoes"),
    ("Ventanas al interior de la Tierra: cómo funcionan, las grandes erupciones de la historia y los volcanes de España, del Teide a La Palma y Olot.",
     "Windows into the Earth's interior: how they work, history's great eruptions and Spain's volcanoes, from Teide to La Palma and Olot."),
    ("volcanes, erupción volcánica, magma, lava, Teide, volcán de La Palma, Tajogaite, Cumbre Vieja, Olot, Garrotxa, Vesubio, Pompeya, Krakatoa, Tambora, supervolcán, Yellowstone, Mauna Kea, tipos de volcanes",
     "volcanoes, volcanic eruption, magma, lava, Teide, La Palma volcano, Tajogaite, Cumbre Vieja, Olot, Garrotxa, Vesuvius, Pompeii, Krakatoa, Tambora, supervolcano, Yellowstone, Mauna Kea, types of volcanoes"),
    "volcan",
    """
Un volcán es una abertura en la corteza por la que sale **magma**, roca fundida del interior de la Tierra. Cuando llega a la superficie se llama **lava**. Hay unos **1.350 volcanes potencialmente activos** en tierra firme, y cada año entran en erupción entre 50 y 70. Muchos más están ocultos bajo el mar.

## Por qué hay volcanes

Casi todos se forman en los bordes de las [placas tectónicas](@tectonica-de-placas): donde se separan, como en Islandia, o donde una se hunde bajo otra, como en los Andes, Japón o Indonesia. Otros nacen sobre **puntos calientes**, columnas de material caliente que suben desde el manto profundo y atraviesan la placa como un soplete. Así se formaron Hawái y, probablemente, las Canarias.

## Explosivos o tranquilos

El carácter de un volcán depende de su magma. Si es **fluido y pobre en gases**, como en Hawái, la lava sale en ríos y fuentes y forma volcanes anchos y suaves llamados **en escudo**. Si es **espeso y rico en gases**, la presión se acumula como en una botella de cava agitada y el volcán explota, lanzando cenizas a decenas de kilómetros de altura. Lo más peligroso son las **nubes ardientes** o flujos piroclásticos: avalanchas de gas y ceniza a cientos de grados que bajan a más de 100 km/h.

!foto lava | Río de lava en Hawái. El magma pobre en sílice es muy fluido y puede recorrer kilómetros.

## Erupciones que cambiaron la historia

| Volcán | Año | Qué pasó |
|---|---|---|
| Vesubio (Italia) | 79 | Sepultó **Pompeya** y Herculano bajo la ceniza |
| Tambora (Indonesia) | 1815 | La mayor erupción de la historia escrita; 1816 fue «el año sin verano» en Europa |
| Krakatoa (Indonesia) | 1883 | La explosión se oyó a 4.800 km; tsunamis con más de 36.000 muertos |
| Monte Santa Helena (EE. UU.) | 1980 | El volcán perdió 400 metros de altura en una explosión lateral |
| Pinatubo (Filipinas) | 1991 | Enfrió el clima de todo el planeta medio grado durante un año |
| Hunga Tonga (Tonga) | 2022 | La explosión submarina lanzó vapor de agua hasta la mesosfera |

## Los volcanes de España

- **El Teide** (Tenerife), con 3.715 metros, es la montaña más alta de España. Medido desde el fondo del océano supera los 7.000 metros, lo que lo convierte en uno de los volcanes más grandes del mundo. Su parque nacional es Patrimonio de la Humanidad.
- **La Palma**: el 19 de septiembre de 2021 comenzó la erupción del volcán de la **Cumbre Vieja**, bautizado como **Tajogaite**. Duró 85 días, la lava cubrió más de 1.200 hectáreas, sepultó barrios enteros y miles de edificaciones y ganó terreno al mar. Fue la erupción más estudiada de la historia de España.
- **Lanzarote**: entre 1730 y 1736 las erupciones de **Timanfaya** cubrieron una cuarta parte de la isla.
- **La Garrotxa** (Girona): alrededor de **Olot** hay unos 40 conos volcánicos, como el Croscat o el Santa Margarida, con un cráter que alberga una ermita. La última erupción fue hace unos 13.000 años.
- **Campo de Calatrava** (Ciudad Real) y **Cabo de Gata** (Almería) son otras zonas volcánicas, hoy dormidas.

!foto tajogaite | La erupción del volcán Tajogaite, en La Palma, en el otoño de 2021.

## Supervolcanes

Algunos volcanes pueden expulsar más de 1.000 km³ de material en una sola erupción. **Yellowstone**, en Estados Unidos, lo ha hecho tres veces en los últimos 2,1 millones de años. Bajo su parque, famoso por sus géiseres, hay una gran cámara de magma, aunque los científicos no ven señales de una erupción próxima.

> Las tierras volcánicas son de las más fértiles del mundo. En Lanzarote, los viticultores plantan cada cepa en un hoyo excavado en la ceniza volcánica y protegido por un muro de piedra semicircular: el paisaje de La Geria.
""",
    """
A volcano is an opening in the crust through which **magma**, molten rock from inside the Earth, escapes. Once it reaches the surface it is called **lava**. There are about **1,350 potentially active volcanoes** on land, and 50 to 70 of them erupt each year. Many more are hidden under the sea.

## Why there are volcanoes

Almost all form along the edges of [tectonic plates](@tectonica-de-placas): where they pull apart, as in Iceland, or where one sinks beneath another, as in the Andes, Japan or Indonesia. Others arise above **hotspots**, columns of hot material rising from the deep mantle that burn through the plate like a blowtorch. That is how Hawaii and, probably, the Canary Islands formed.

## Explosive or gentle

A volcano's temperament depends on its magma. If it is **runny and low in gas**, as in Hawaii, lava pours out in rivers and fountains and builds broad, gentle **shield volcanoes**. If it is **thick and gas-rich**, pressure builds like in a shaken bottle of fizz and the volcano explodes, hurling ash tens of kilometres high. The deadliest danger is **pyroclastic flows**: avalanches of gas and ash at hundreds of degrees racing downhill at over 100 km/h.

!foto lava | A river of lava in Hawaii. Low-silica magma is very runny and can travel for kilometres.

## Eruptions that changed history

| Volcano | Year | What happened |
|---|---|---|
| Vesuvius (Italy) | 79 | Buried **Pompeii** and Herculaneum under ash |
| Tambora (Indonesia) | 1815 | The largest eruption in written history; 1816 was "the year without a summer" in Europe |
| Krakatoa (Indonesia) | 1883 | The blast was heard 4,800 km away; tsunamis killed over 36,000 people |
| Mount St Helens (US) | 1980 | The volcano lost 400 metres of height in a sideways blast |
| Pinatubo (Philippines) | 1991 | Cooled the whole planet's climate by half a degree for a year |
| Hunga Tonga (Tonga) | 2022 | The underwater explosion blasted water vapour into the mesosphere |

## Spain's volcanoes

- **Teide** (Tenerife), at 3,715 metres, is Spain's highest mountain. Measured from the ocean floor it exceeds 7,000 metres, making it one of the largest volcanoes in the world. Its national park is a World Heritage Site.
- **La Palma**: on 19 September 2021 the **Cumbre Vieja** volcano began erupting, at a vent later named **Tajogaite**. The eruption lasted 85 days; lava covered more than 1,200 hectares, buried whole neighbourhoods and thousands of buildings, and added new land to the island. It was the most studied eruption in Spain's history.
- **Lanzarote**: between 1730 and 1736 the eruptions of **Timanfaya** covered a quarter of the island.
- **La Garrotxa** (Girona): around **Olot** there are some 40 volcanic cones, such as Croscat and Santa Margarida, whose crater holds a chapel. The last eruption was about 13,000 years ago.
- **Campo de Calatrava** (Ciudad Real) and **Cabo de Gata** (Almería) are other volcanic areas, now dormant.

!foto tajogaite | The eruption of the Tajogaite volcano on La Palma in autumn 2021.

## Supervolcanoes

Some volcanoes can eject more than 1,000 km³ of material in a single eruption. **Yellowstone** in the United States has done so three times in the last 2.1 million years. Beneath its park, famous for its geysers, lies a large magma chamber, although scientists see no sign of an imminent eruption.

> Volcanic soils are among the most fertile in the world. On Lanzarote, winegrowers plant each vine in a hollow dug into volcanic ash and shielded by a semicircular stone wall: the landscape of La Geria.
""",
    datos=[("Volcanes activos en tierra", "Active volcanoes on land", "≈ 1.350", "≈ 1,350"),
           ("Erupciones al año", "Eruptions per year", "50 a 70", "50 to 70"),
           ("Volcán más alto de España", "Spain's highest volcano", "Teide, 3.715 m", "Teide, 3,715 m"),
           ("Última erupción en España", "Latest eruption in Spain", "Tajogaite, La Palma, 2021 (85 días)", "Tajogaite, La Palma, 2021 (85 days)"),
           ("Mayor erupción histórica", "Largest historical eruption", "Tambora, 1815", "Tambora, 1815")],
    pie=("Erupción nocturna del Stromboli, en Italia, uno de los volcanes más activos del mundo, conocido como «el faro del Mediterráneo».",
         "Night eruption of Stromboli in Italy, one of the world's most active volcanoes, known as \"the lighthouse of the Mediterranean\"."),
)

TERREMOTOS = F(
    ("terremotos-y-tsunamis", "earthquakes-and-tsunamis"),
    ("Terremotos y tsunamis", "Earthquakes and tsunamis"),
    ("Por qué tiembla la Tierra, cómo se miden los terremotos, los más destructivos de la historia y los que han sacudido España.",
     "Why the Earth shakes, how earthquakes are measured, the most destructive in history and those that have struck Spain."),
    ("terremoto, sismo, seísmo, escala de Richter, magnitud de momento, epicentro, hipocentro, tsunami, maremoto, terremoto de Lisboa 1755, terremoto de Lorca, terremoto de Chile 1960, sismógrafo, riesgo sísmico en España",
     "earthquake, seismic, Richter scale, moment magnitude, epicentre, hypocentre, tsunami, 1755 Lisbon earthquake, Lorca earthquake, 1960 Chile earthquake, seismograph, seismic risk in Spain"),
    "terremoto",
    """
Las [placas tectónicas](@tectonica-de-placas) no se deslizan con suavidad: sus bordes se atascan y la tensión se acumula durante años o siglos, como en un muelle comprimido. Cuando la roca no aguanta más, se rompe de golpe y libera la energía en forma de **ondas sísmicas**. Eso es un terremoto.

El punto bajo tierra donde empieza la ruptura es el **hipocentro**; el punto de la superficie justo encima, el **epicentro**. Cada año se registran unos **500.000 terremotos**; unos 100.000 se notan y alrededor de un centenar causan daños.

## Cómo se miden

En 1935 **Charles Richter** creó una escala para comparar terremotos en California. Hoy los sismólogos usan la **magnitud de momento**, que funciona de forma parecida pero sirve para los terremotos más grandes. Es una escala logarítmica: **cada punto más supone unas 32 veces más energía**. Un terremoto de magnitud 7 libera unas 1.000 veces más energía que uno de 5.

La **intensidad**, en cambio, mide los efectos en un lugar concreto (de I, apenas perceptible, a XII, destrucción total). Un mismo terremoto tiene una sola magnitud pero distintas intensidades según la distancia.

!sim magnitud

## Los más fuertes y los más mortíferos

| Terremoto | Año | Magnitud | Consecuencias |
|---|---|---|---|
| Lisboa (Portugal) | 1755 | ≈ 8,5 | Terremoto, incendio y tsunami; arrasó Lisboa y golpeó Cádiz y Huelva |
| Valdivia (Chile) | 1960 | **9,5** | El más fuerte jamás registrado |
| Tangshan (China) | 1976 | 7,6 | Uno de los más mortíferos del siglo XX |
| Océano Índico | 2004 | 9,1 | Tsunami con más de 220.000 víctimas en 14 países |
| Tohoku (Japón) | 2011 | 9,0 | Tsunami de hasta 40 m y accidente nuclear de Fukushima |
| Turquía y Siria | 2023 | 7,8 | Más de 50.000 víctimas |

## Tsunamis

Cuando un terremoto mueve el fondo del mar, desplaza toda la columna de agua y genera un **tsunami**. En mar abierto la ola apenas mide un metro, pero viaja a unos **800 km/h**, la velocidad de un avión. Al llegar a aguas poco profundas se frena y crece hasta convertirse en una pared de agua. Una señal de alarma es que el mar se retire de forma repentina: hay que alejarse de la costa hacia zonas altas de inmediato.

## España, un país con terremotos moderados

España tiene una actividad sísmica **moderada**, concentrada en el sur y el sureste (Granada, Murcia, Almería, Málaga), los Pirineos y Galicia. El **Instituto Geográfico Nacional** registra miles de pequeños terremotos al año, casi ninguno perceptible.

- **Torrevieja** (Alicante), 1829: destruyó la ciudad.
- **Arenas del Rey** (Granada), 1884: el «terremoto de Andalucía», con unos 900 muertos.
- **Lorca** (Murcia), 2011: magnitud 5,1, muy superficial; nueve víctimas y graves daños en el casco histórico.
- **Granada**, 2021: un enjambre de cientos de pequeños terremotos alarmó durante semanas a los vecinos de Santa Fe y Atarfe.

## ¿Se pueden predecir?

Todavía no. Los sismólogos saben **dónde** es probable que ocurran grandes terremotos, pero no **cuándo**. Lo que sí funciona son los **sistemas de alerta temprana**, como el de Japón o México, que detectan las primeras ondas y avisan unos segundos antes de que lleguen las más destructivas: tiempo para parar trenes, abrir puertas de parques de bomberos o ponerse a cubierto. Y, sobre todo, construir edificios preparados para resistirlos.

> El terremoto de Japón de 2011 desplazó la isla principal del país unos 2,4 metros hacia el este y acortó la duración del día en 1,8 microsegundos al cambiar la distribución de la masa de la Tierra.
""",
    """
[Tectonic plates](@tectonica-de-placas) do not slide smoothly: their edges get stuck and stress builds up for years or centuries, like a compressed spring. When the rock can take no more, it breaks suddenly and releases the energy as **seismic waves**. That is an earthquake.

The underground point where the rupture starts is the **hypocentre**; the point on the surface directly above it is the **epicentre**. Around **500,000 earthquakes** are recorded each year; about 100,000 are felt and around a hundred cause damage.

## How they are measured

In 1935 **Charles Richter** created a scale to compare earthquakes in California. Today seismologists use the **moment magnitude**, which works in a similar way but copes with the largest quakes. It is a logarithmic scale: **each extra point means about 32 times more energy**. A magnitude 7 earthquake releases about 1,000 times more energy than a magnitude 5.

**Intensity**, by contrast, measures the effects at a particular place (from I, barely felt, to XII, total destruction). A single earthquake has one magnitude but different intensities depending on distance.

!sim magnitud

## The strongest and the deadliest

| Earthquake | Year | Magnitude | Consequences |
|---|---|---|---|
| Lisbon (Portugal) | 1755 | ≈ 8.5 | Quake, fire and tsunami; flattened Lisbon and struck Cádiz and Huelva |
| Valdivia (Chile) | 1960 | **9.5** | The strongest ever recorded |
| Tangshan (China) | 1976 | 7.6 | One of the deadliest of the 20th century |
| Indian Ocean | 2004 | 9.1 | Tsunami killing more than 220,000 people in 14 countries |
| Tōhoku (Japan) | 2011 | 9.0 | Tsunami up to 40 m high and the Fukushima nuclear accident |
| Turkey and Syria | 2023 | 7.8 | More than 50,000 deaths |

## Tsunamis

When an earthquake moves the seafloor, it shifts the whole column of water above it and creates a **tsunami**. In the open ocean the wave is barely a metre high, but it travels at about **800 km/h**, the speed of a jet. On reaching shallow water it slows and grows into a wall of water. One warning sign is the sea suddenly drawing back: move away from the coast to high ground immediately.

## Spain, a country with moderate earthquakes

Spain has **moderate** seismic activity, concentrated in the south and south-east (Granada, Murcia, Almería, Málaga), the Pyrenees and Galicia. The **National Geographic Institute** records thousands of small earthquakes a year, almost none of them felt.

- **Torrevieja** (Alicante), 1829: destroyed the town.
- **Arenas del Rey** (Granada), 1884: the "Andalusian earthquake", with about 900 deaths.
- **Lorca** (Murcia), 2011: magnitude 5.1, very shallow; nine deaths and severe damage to the historic centre.
- **Granada**, 2021: a swarm of hundreds of small quakes alarmed residents of Santa Fe and Atarfe for weeks.

## Can they be predicted?

Not yet. Seismologists know **where** large earthquakes are likely, but not **when**. What does work is **early warning systems**, like those in Japan and Mexico, which detect the first waves and give a few seconds' notice before the most destructive ones arrive: time to stop trains, open fire-station doors or take cover. And, above all, constructing buildings designed to withstand them.

> Japan's 2011 earthquake shifted the country's main island about 2.4 metres east and shortened the length of the day by 1.8 microseconds by changing how the Earth's mass is distributed.
""",
    datos=[("Terremotos registrados al año", "Earthquakes recorded per year", "≈ 500.000", "≈ 500,000"),
           ("Más fuerte registrado", "Strongest recorded", "Valdivia (Chile), 1960, magnitud 9,5", "Valdivia (Chile), 1960, magnitude 9.5"),
           ("Un punto más de magnitud", "One extra magnitude point", "≈ 32 veces más energía", "≈ 32 times more energy"),
           ("Velocidad de un tsunami", "Tsunami speed", "≈ 800 km/h en mar abierto", "≈ 800 km/h in open ocean"),
           ("Zonas sísmicas en España", "Seismic areas in Spain", "Sur, sureste, Pirineos y Galicia", "South, south-east, Pyrenees and Galicia")],
    pie=("Edificio derrumbado tras un terremoto. La mayoría de las víctimas de los seísmos se deben al colapso de construcciones.",
         "A building collapsed by an earthquake. Most earthquake deaths are caused by buildings falling down."),
)

ROCAS = F(
    ("rocas-y-minerales", "rocks-and-minerals"),
    ("Rocas y minerales", "Rocks and minerals"),
    ("Los ladrillos de la Tierra: cómo se forman las rocas, qué son los minerales y dónde están los cristales más asombrosos, de Naica a la geoda de Pulpí.",
     "The Earth's building blocks: how rocks form, what minerals are and where to find the most astonishing crystals, from Naica to the Pulpí geode."),
    ("rocas, minerales, ciclo de las rocas, rocas ígneas, rocas sedimentarias, rocas metamórficas, granito, mármol, cuarzo, escala de Mohs, diamante, cristales, cueva de Naica, geoda de Pulpí, gemas",
     "rocks, minerals, rock cycle, igneous rocks, sedimentary rocks, metamorphic rocks, granite, marble, quartz, Mohs scale, diamond, crystals, Cave of the Crystals, Naica, Pulpí geode, gems"),
    "geoda",
    """
Un **mineral** es una sustancia natural sólida con una composición química concreta y una estructura ordenada de átomos, es decir, un cristal. Una **roca** es una mezcla de uno o varios minerales. El granito, por ejemplo, está hecho de cuarzo, feldespato y mica: los granitos blancos, rosados y negros que se ven en las encimeras.

Se conocen **más de 6.000 minerales**, pero solo unas decenas forman casi todas las rocas. Los más abundantes en la corteza son los **feldespatos** y el **cuarzo**.

## Tres familias de rocas

- **Ígneas**: nacen del enfriamiento del magma. Si se enfría despacio en el interior, forma cristales grandes, como el **granito**. Si se enfría deprisa en la superficie, cristales diminutos, como el **basalto** de las coladas volcánicas.
- **Sedimentarias**: se forman cuando la arena, el barro o los restos de seres vivos se acumulan en capas y se compactan. Son la **arenisca**, la **arcilla** o la **caliza**, a menudo llena de fósiles. Cubren el 75 % de la superficie de los continentes.
- **Metamórficas**: son rocas transformadas por el calor y la presión sin llegar a fundirse. La caliza se convierte en **mármol**, la arcilla en **pizarra**.

## El ciclo de las rocas

Ninguna roca es eterna. Las montañas se erosionan y sus granos acaban en el fondo del mar, donde se convierten en roca sedimentaria; esta puede hundirse con las placas, transformarse con el calor, fundirse y volver a subir como magma. Es el **ciclo de las rocas**, que recicla la corteza una y otra vez a lo largo de cientos de millones de años.

## La escala de dureza de Mohs

En 1812 el mineralogista alemán Friedrich Mohs ordenó los minerales según cuál raya a cuál:

| Dureza | Mineral | Referencia |
|---|---|---|
| 1 | Talco | Se raya con la uña |
| 2 | Yeso | Se raya con la uña |
| 3 | Calcita | Se raya con una moneda de cobre |
| 4 | Fluorita | Se raya con un cuchillo |
| 5 | Apatito | Se raya con un cuchillo con esfuerzo |
| 6 | Ortoclasa | Raya el vidrio con dificultad |
| 7 | Cuarzo | Raya el vidrio |
| 8 | Topacio | |
| 9 | Corindón (rubí, zafiro) | |
| 10 | **Diamante** | El mineral natural más duro |

El diamante y el grafito de los lápices son el mismo elemento, carbono; solo cambia cómo se ordenan sus átomos. Los diamantes se forman a más de 150 km de profundidad y suben a la superficie en erupciones volcánicas muy rápidas.

## Cristales gigantes

!foto cueva_cristales | La cueva de los Cristales de Naica, en México, con cristales de yeso de más de 10 metros.

En 2000, unos mineros descubrieron en **Naica** (México), a 300 metros de profundidad, una cueva llena de cristales de yeso de hasta **12 metros** de largo, los mayores conocidos. Crecieron durante cientos de miles de años en agua caliente rica en minerales. La cueva está a unos 50 °C y casi el 100 % de humedad: sin un traje refrigerado, una persona solo aguanta allí unos minutos.

En España está la **geoda de Pulpí** (Almería), descubierta en 1999 en una antigua mina de plata. Es una cavidad de unos 8 metros de largo tapizada de cristales transparentes de yeso, la mayor geoda visitable del mundo. Se puede visitar desde 2019.

> Los minerales más antiguos de la Tierra son unos diminutos cristales de circón de Jack Hills, en Australia, de **4.400 millones de años**. Demuestran que poco después de formarse el planeta ya había corteza y probablemente agua líquida.
""",
    """
A **mineral** is a natural solid substance with a specific chemical composition and an ordered arrangement of atoms, in other words a crystal. A **rock** is a mixture of one or more minerals. Granite, for example, is made of quartz, feldspar and mica: the white, pink and black granites you see on kitchen worktops.

More than **6,000 minerals** are known, but just a few dozen make up almost all rocks. The most abundant in the crust are **feldspars** and **quartz**.

## Three families of rock

- **Igneous**: born from cooling magma. If it cools slowly underground it forms large crystals, like **granite**. If it cools quickly at the surface, tiny crystals, like the **basalt** of lava flows.
- **Sedimentary**: formed when sand, mud or the remains of living things pile up in layers and are compacted. They include **sandstone**, **clay** and **limestone**, often full of fossils. They cover 75% of the continents' surface.
- **Metamorphic**: rocks transformed by heat and pressure without melting. Limestone becomes **marble**; clay becomes **slate**.

## The rock cycle

No rock lasts forever. Mountains erode and their grains end up on the seabed, where they turn into sedimentary rock; this can be dragged down with the plates, transformed by heat, melted and rise again as magma. This is the **rock cycle**, which recycles the crust again and again over hundreds of millions of years.

## The Mohs hardness scale

In 1812 the German mineralogist Friedrich Mohs ranked minerals by which one scratches which:

| Hardness | Mineral | Reference |
|---|---|---|
| 1 | Talc | Scratched by a fingernail |
| 2 | Gypsum | Scratched by a fingernail |
| 3 | Calcite | Scratched by a copper coin |
| 4 | Fluorite | Scratched by a knife |
| 5 | Apatite | Scratched by a knife with effort |
| 6 | Orthoclase | Scratches glass with difficulty |
| 7 | Quartz | Scratches glass |
| 8 | Topaz | |
| 9 | Corundum (ruby, sapphire) | |
| 10 | **Diamond** | The hardest natural mineral |

Diamond and the graphite in pencils are the same element, carbon; only the arrangement of the atoms differs. Diamonds form more than 150 km down and reach the surface in very fast volcanic eruptions.

## Giant crystals

!foto cueva_cristales | The Cave of the Crystals at Naica, Mexico, with gypsum crystals more than 10 metres long.

In 2000 miners at **Naica** (Mexico) broke into a cave 300 metres underground filled with gypsum crystals up to **12 metres** long, the largest known. They grew for hundreds of thousands of years in hot, mineral-rich water. The cave is at about 50 °C and nearly 100% humidity: without a cooling suit, a person can last only a few minutes.

Spain has the **Pulpí geode** (Almería), discovered in 1999 in an old silver mine. It is a cavity about 8 metres long lined with transparent gypsum crystals, the largest geode in the world that can be visited. It has been open to the public since 2019.

> The oldest minerals on Earth are tiny zircon crystals from Jack Hills, Australia, **4.4 billion years** old. They show that soon after the planet formed there was already crust and probably liquid water.
""",
    datos=[("Minerales conocidos", "Known minerals", "Más de 6.000", "More than 6,000"),
           ("Familias de rocas", "Rock families", "Ígneas, sedimentarias y metamórficas", "Igneous, sedimentary and metamorphic"),
           ("Mineral más duro", "Hardest mineral", "Diamante (10 en la escala de Mohs)", "Diamond (10 on the Mohs scale)"),
           ("Mayores cristales", "Largest crystals", "Naica (México), hasta 12 m", "Naica (Mexico), up to 12 m"),
           ("Mineral más antiguo", "Oldest mineral", "Circones de Jack Hills, 4.400 millones de años", "Jack Hills zircons, 4.4 billion years")],
    pie=("Geoda de amatista: una cavidad en la roca tapizada de cristales de cuarzo violeta.",
         "Amethyst geode: a cavity in rock lined with violet quartz crystals."),
)

HISTORIA = F(
    ("historia-de-la-tierra", "history-of-the-earth"),
    ("La historia de la Tierra", "The history of the Earth"),
    ("De una bola de roca fundida a un planeta azul lleno de vida: los 4.540 millones de años de la Tierra, contados en eras.",
     "From a ball of molten rock to a blue planet full of life: the Earth's 4.54 billion years, told era by era."),
    ("historia de la Tierra, eras geológicas, escala de tiempo geológico, Hádico, Arcaico, Proterozoico, Paleozoico, Mesozoico, Cenozoico, origen de la Luna, Tierra bola de nieve, explosión cámbrica, fósiles, Gran Cañón, edad de la Tierra",
     "history of the Earth, geological eras, geological time scale, Hadean, Archean, Proterozoic, Paleozoic, Mesozoic, Cenozoic, origin of the Moon, Snowball Earth, Cambrian explosion, fossils, Grand Canyon, age of the Earth"),
    "gran_canon",
    """
La Tierra se formó hace unos **4.540 millones de años** a partir del polvo y las rocas que giraban alrededor del joven Sol. Los geólogos dividen su historia en **eones, eras y periodos**, y la leen en las capas de roca y en los fósiles, como si fueran las páginas de un libro. En el **Gran Cañón** del Colorado, el río ha dejado al descubierto casi 2.000 millones de años de historia en una pared de 1,8 km.

## Las grandes etapas

| Etapa | Hace (millones de años) | Qué ocurrió |
|---|---|---|
| **Hádico** | 4.540 a 4.000 | Planeta de magma; un choque gigante forma la [Luna](@luna); aparecen los primeros océanos |
| **Arcaico** | 4.000 a 2.500 | Primeros continentes y primera vida: bacterias y [estromatolitos](@origen-de-la-vida) |
| **Proterozoico** | 2.500 a 539 | Las bacterias llenan de oxígeno la atmósfera; células complejas; la Tierra se congela casi entera |
| **Paleozoico** | 539 a 252 | Explosión de vida animal; plantas y animales conquistan la tierra; se forma Pangea |
| **Mesozoico** | 252 a 66 | La era de los dinosaurios; aparecen mamíferos, aves y flores |
| **Cenozoico** | 66 a hoy | La era de los mamíferos; glaciaciones; aparece el ser humano |

## Un infierno sin oxígeno

Al principio la Tierra era una bola de roca fundida bombardeada por asteroides. Uno de esos choques, con un planeta del tamaño de Marte al que llaman **Tea**, arrancó el material que formó la Luna. Cuando la superficie se enfrió, el vapor de agua se condensó en lluvias que duraron millones de años y llenaron los océanos. La atmósfera era de dióxido de carbono y nitrógeno: no había oxígeno libre.

## La gran oxidación

Hace unos 2.400 millones de años, unas bacterias llamadas **cianobacterias**, que hacían la fotosíntesis, habían liberado tanto oxígeno que la atmósfera cambió para siempre. Fue la **Gran Oxidación**. Para muchos microbios de entonces el oxígeno era un veneno, y fue quizá la primera gran extinción. Para nosotros, la condición para existir. El hierro de los océanos se oxidó y se depositó en el fondo, formando los grandes yacimientos de hierro que hoy se explotan.

## La Tierra bola de nieve

Entre hace 720 y 635 millones de años, la Tierra se congeló probablemente casi por completo, con hielo hasta cerca del ecuador. Se salió de ella gracias a los volcanes, que siguieron expulsando dióxido de carbono hasta calentar el planeta.

## La explosión de la vida

Hace unos 539 millones de años, en el **Cámbrico**, aparecieron en un tiempo geológicamente breve casi todos los grandes grupos de animales: con caparazones, ojos, patas. Los **trilobites** fueron sus estrellas. Después llegarían los peces, las plantas terrestres, los anfibios, los reptiles y los [dinosaurios](@evolucion), interrumpidos por varias [grandes extinciones](@extinciones).

!foto amonite | Fósil de amonite, un pariente de los calamares con concha en espiral que llenó los mares durante 340 millones de años y se extinguió junto a los dinosaurios.

## La historia en un año

Para hacerse una idea de las proporciones, imagina la historia de la Tierra comprimida en un solo año:

!sim reloj

> Si toda la historia de la Tierra fuera un día de 24 horas, nuestra especie aparecería en los últimos seis segundos antes de la medianoche, y toda la historia escrita cabría en la última décima de segundo.
""",
    """
The Earth formed about **4.54 billion years** ago from the dust and rocks orbiting the young Sun. Geologists divide its history into **eons, eras and periods**, and read it in rock layers and fossils as if they were the pages of a book. In the **Grand Canyon** of the Colorado, the river has exposed nearly 2 billion years of history in a 1.8 km wall.

## The great stages

| Stage | Million years ago | What happened |
|---|---|---|
| **Hadean** | 4,540 to 4,000 | A magma planet; a giant impact forms the [Moon](@luna); the first oceans appear |
| **Archean** | 4,000 to 2,500 | First continents and first life: bacteria and [stromatolites](@origen-de-la-vida) |
| **Proterozoic** | 2,500 to 539 | Bacteria fill the atmosphere with oxygen; complex cells; the Earth freezes almost entirely |
| **Paleozoic** | 539 to 252 | Explosion of animal life; plants and animals conquer land; Pangaea forms |
| **Mesozoic** | 252 to 66 | The age of the dinosaurs; mammals, birds and flowers appear |
| **Cenozoic** | 66 to today | The age of mammals; ice ages; humans appear |

## An oxygen-free hell

At first the Earth was a ball of molten rock pounded by asteroids. One of those collisions, with a Mars-sized planet called **Theia**, blasted off the material that formed the Moon. When the surface cooled, water vapour condensed into rains that lasted millions of years and filled the oceans. The atmosphere was carbon dioxide and nitrogen: there was no free oxygen.

## The Great Oxidation

About 2.4 billion years ago, bacteria called **cyanobacteria**, which carried out photosynthesis, had released so much oxygen that the atmosphere changed forever. This was the **Great Oxidation Event**. For many microbes of the time oxygen was poison, and it was perhaps the first great extinction. For us, it was the condition for existing. Iron in the oceans rusted and settled on the seabed, forming the great iron deposits that are mined today.

## Snowball Earth

Between 720 and 635 million years ago the Earth probably froze almost completely, with ice reaching close to the equator. It escaped thanks to volcanoes, which kept pouring out carbon dioxide until the planet warmed up.

## The explosion of life

About 539 million years ago, in the **Cambrian**, almost all the major groups of animals appeared in a geologically short time: with shells, eyes and legs. **Trilobites** were its stars. Then came fish, land plants, amphibians, reptiles and [dinosaurs](@evolucion), interrupted by several [mass extinctions](@extinciones).

!foto amonite | An ammonite fossil, a relative of squid with a spiral shell that filled the seas for 340 million years and died out with the dinosaurs.

## History in a year

To get a sense of proportion, imagine the Earth's history squeezed into a single year:

!sim reloj

> If the whole history of the Earth were a 24-hour day, our species would appear in the last six seconds before midnight, and all of written history would fit into the last tenth of a second.
""",
    datos=[("Edad de la Tierra", "Age of the Earth", "4.540 millones de años", "4.54 billion years"),
           ("Primera vida", "First life", "Hace más de 3.500 millones de años", "Over 3.5 billion years ago"),
           ("Gran Oxidación", "Great Oxidation", "Hace ≈ 2.400 millones de años", "≈ 2.4 billion years ago"),
           ("Explosión cámbrica", "Cambrian explosion", "Hace ≈ 539 millones de años", "≈ 539 million years ago"),
           ("Fin de los dinosaurios", "End of the dinosaurs", "Hace 66 millones de años", "66 million years ago"),
           ("Homo sapiens", "Homo sapiens", "Hace ≈ 300.000 años", "≈ 300,000 years ago")],
    pie=("El Gran Cañón del Colorado: sus paredes muestran capas de roca de casi 2.000 millones de años de historia.",
         "The Grand Canyon of the Colorado: its walls show rock layers spanning nearly 2 billion years of history."),
)

FICHAS = [ESTRUCTURA, PLACAS, VOLCANES, TERREMOTOS, ROCAS, HISTORIA]
