from universo import F

SLUG = ("geografia-del-mundo", "world-geography")
TITULO = ("Geografía del mundo", "World geography")
RESUMEN = ("Continentes, montañas, desiertos, islas y polos: los grandes paisajes del planeta y la asombrosa variedad de España.",
           "Continents, mountains, deserts, islands and poles: the planet's great landscapes and the astonishing variety of Spain.")
CLAVES = ("geografía, geografía del mundo, continentes, países, montañas más altas, Everest, desiertos, Sahara, islas, polos, Antártida, Ártico, geografía de España, relieve de España",
          "geography, world geography, continents, countries, highest mountains, Everest, deserts, Sahara, islands, poles, Antarctica, Arctic, geography of Spain")
FOTO = "himalaya"
INTRO = ("""
La superficie de la Tierra es un mosaico de paisajes: cordilleras que crecen todavía, desiertos donde no ha llovido en siglos, miles de islas y dos polos cubiertos de hielo. Esta sección recorre los grandes rasgos de su geografía, con una parada especial en España.
""", """
The Earth's surface is a mosaic of landscapes: mountain ranges that are still rising, deserts where it has not rained for centuries, thousands of islands and two ice-covered poles. This section explores the main features of its geography, with a special stop in Spain.
""")

CONTINENTES = F(
    ("continentes-y-paises", "continents-and-countries"),
    ("Continentes y países", "Continents and countries"),
    ("¿Cinco, seis o siete continentes? Superficie, población y curiosidades de cada uno, y los países más grandes, más pequeños y más poblados.",
     "Five, six or seven continents? Area, population and curiosities of each, and the largest, smallest and most populous countries."),
    ("continentes, cuántos continentes hay, Asia, África, América, Europa, Oceanía, Antártida, países del mundo, cuántos países hay, país más grande, país más pequeño, Rusia, Vaticano, India, China, población mundial, fronteras",
     "continents, how many continents, Asia, Africa, America, Europe, Oceania, Antarctica, countries of the world, how many countries, largest country, smallest country, Russia, Vatican, India, China, world population, borders"),
    "tierra_noche",
    """
Las tierras emergidas ocupan solo el **29 %** de la superficie de la Tierra, unos 149 millones de km². El resto es [océano](@oceanos). Esas tierras se agrupan en grandes masas llamadas **continentes**, que llevan cientos de millones de años moviéndose por la [tectónica de placas](@tectonica-de-placas).

## ¿Cuántos continentes hay?

Depende de dónde se haya ido a la escuela. En España e Hispanoamérica se suele enseñar que hay **cinco o seis** (América como un solo continente), mientras que en el mundo anglosajón se cuentan **siete**, separando América del Norte y del Sur. Los cinco aros olímpicos representan los cinco continentes habitados.

| Continente | Superficie (millones de km²) | Población (millones, aprox.) |
|---|---|---|
| Asia | 44,6 | 4.800 |
| América | 42,5 | 1.050 |
| África | 30,4 | 1.500 |
| Antártida | 14,2 | 0 (unos 1.000-5.000 científicos) |
| Europa | 10,2 | 745 |
| Oceanía | 8,5 | 46 |

**Asia** es el más grande y poblado: en él vive casi el 60 % de la humanidad. **África** es el que más crece: a mediados de siglo tendrá una de cada cuatro personas del mundo. Y **Oceanía**, con Australia a la cabeza, es el menos poblado si no contamos la Antártida.

## ¿Cuántos países hay?

La ONU tiene **193 Estados miembros** y dos observadores (el Vaticano y Palestina). Según cómo se cuenten territorios como Taiwán o Kosovo, el número de países del mundo está entre 195 y 200.

- **El más grande**: Rusia, con 17,1 millones de km², casi el doble que Canadá, el segundo. Tiene 11 husos horarios.
- **El más pequeño**: el Vaticano, de 0,44 km², menos de la mitad que el parque del Retiro de Madrid.
- **El más poblado**: India, que superó a China en 2023 y tiene más de 1.450 millones de habitantes.
- **El más densamente poblado**: Mónaco, con unas 19.000 personas por km².
- **El que más fronteras tiene**: China y Rusia, con 14 vecinos cada uno.

## La Tierra de noche

!foto tierra_noche | Las luces de las ciudades vistas desde el espacio dibujan dónde vive la humanidad.

Las imágenes nocturnas tomadas desde satélites muestran dónde se concentra la gente: las costas, los grandes ríos como el Nilo y el Ganges, y las regiones más ricas. España se distingue con claridad: una gran mancha brillante en Madrid rodeada de una meseta oscura, y la costa iluminada como un collar.

> Hay lugares donde coinciden las fronteras de tres países, llamados trifinios. En el río Mosela, junto al pueblo luxemburgués de Schengen, se tocan Luxemburgo, Alemania y Francia: allí se firmó en 1985 el acuerdo que eliminó los controles fronterizos en buena parte de Europa.
""",
    """
Land makes up only **29%** of the Earth's surface, about 149 million km². The rest is [ocean](@oceanos). That land is grouped into large masses called **continents**, which have been moving for hundreds of millions of years through [plate tectonics](@tectonica-de-placas).

## How many continents are there?

It depends on where you went to school. In Spain and Latin America, children are usually taught there are **five or six** (with the Americas as a single continent), whereas in the English-speaking world **seven** are counted, separating North and South America. The five Olympic rings represent the five inhabited continents.

| Continent | Area (million km²) | Population (millions, approx.) |
|---|---|---|
| Asia | 44.6 | 4,800 |
| Americas | 42.5 | 1,050 |
| Africa | 30.4 | 1,500 |
| Antarctica | 14.2 | 0 (about 1,000–5,000 scientists) |
| Europe | 10.2 | 745 |
| Oceania | 8.5 | 46 |

**Asia** is the largest and most populous: almost 60% of humanity lives there. **Africa** is growing fastest: by mid-century it will be home to one in four people on Earth. And **Oceania**, led by Australia, is the least populated if we leave out Antarctica.

## How many countries are there?

The UN has **193 member states** and two observers (the Vatican and Palestine). Depending on how territories such as Taiwan or Kosovo are counted, the number of countries in the world is between 195 and 200.

- **Largest**: Russia, at 17.1 million km², almost twice the size of Canada, the second. It spans 11 time zones.
- **Smallest**: Vatican City, at 0.44 km², smaller than many city parks.
- **Most populous**: India, which overtook China in 2023 and has more than 1.45 billion people.
- **Most densely populated**: Monaco, with about 19,000 people per km².
- **Most neighbours**: China and Russia, with 14 each.

## The Earth at night

!foto tierra_noche | City lights seen from space trace where humanity lives.

Night-time satellite images show where people are concentrated: coastlines, great rivers such as the Nile and the Ganges, and the wealthiest regions. Spain stands out clearly: a big bright patch at Madrid surrounded by a dark plateau, and its coast lit up like a necklace.

> There are places where the borders of three countries meet, called tripoints. On the Moselle river, by the Luxembourg village of Schengen, Luxembourg, Germany and France touch: it was there, in 1985, that the agreement abolishing border checks across much of Europe was signed.
""",
    datos=[("Tierras emergidas", "Land", "29 % de la superficie, ≈ 149 millones de km²", "29% of the surface, ≈ 149 million km²"),
           ("Continente mayor", "Largest continent", "Asia, 44,6 millones de km²", "Asia, 44.6 million km²"),
           ("Estados de la ONU", "UN member states", "193", "193"),
           ("País más grande", "Largest country", "Rusia, 17,1 millones de km²", "Russia, 17.1 million km²"),
           ("País más pequeño", "Smallest country", "Vaticano, 0,44 km²", "Vatican City, 0.44 km²"),
           ("País más poblado", "Most populous country", "India", "India")],
    pie=("La Tierra de noche: las luces de las ciudades vistas por satélite.",
         "The Earth at night: city lights seen by satellite."),
)

MONTANAS = F(
    ("montanas-y-cordilleras", "mountains-and-ranges"),
    ("Montañas y cordilleras", "Mountains and mountain ranges"),
    ("Del Everest a los Andes: cómo nacen las montañas, las cumbres más altas de cada continente y por qué el Himalaya sigue creciendo.",
     "From Everest to the Andes: how mountains form, the highest peaks on each continent and why the Himalayas are still rising."),
    ("montañas, cordilleras, Everest, montaña más alta del mundo, Himalaya, ochomiles, K2, Andes, Aconcagua, Alpes, Mont Blanc, Kilimanjaro, Mauna Kea, siete cumbres, Pirineos, Mulhacén, Teide, Edmund Hillary, Tenzing Norgay",
     "mountains, mountain ranges, Everest, highest mountain in the world, Himalayas, eight-thousanders, K2, Andes, Aconcagua, Alps, Mont Blanc, Kilimanjaro, Mauna Kea, Seven Summits, Pyrenees, Mulhacén, Teide, Edmund Hillary, Tenzing Norgay"),
    "everest",
    """
Las grandes cordilleras nacen del choque de las [placas tectónicas](@tectonica-de-placas). Cuando dos placas se empujan, la corteza se arruga y se levanta como una alfombra que se arrastra contra la pared. Los volcanes forman otras montañas, como el [Teide](@volcanes) o el Kilimanjaro.

## El techo del mundo

El **Everest** (Chomolungma en tibetano, Sagarmatha en nepalí) mide **8.849 metros**, según la medición conjunta de China y Nepal de 2020. Está en el **Himalaya**, la cordillera que se formó al chocar la India contra Asia hace unos 50 millones de años. La India sigue empujando unos 4-5 cm al año, y el Himalaya crece alrededor de **medio centímetro anual**, aunque la erosión lo desgasta.

En la cima hay rocas calizas con fósiles de animales marinos: hace 450 millones de años, aquella roca era el fondo de un mar.

El Everest fue escalado por primera vez el **29 de mayo de 1953** por el neozelandés **Edmund Hillary** y el sherpa **Tenzing Norgay**. Hoy lo han coronado más de 6.000 personas, y en las temporadas buenas se forman colas cerca de la cumbre.

## Los catorce ochomiles

Solo hay **14 montañas de más de 8.000 metros**, todas en el Himalaya y el Karakórum. La segunda es el **K2** (8.611 m), mucho más difícil y peligrosa que el Everest. El primero en subir los catorce fue el italiano Reinhold Messner, en 1986; el primer español, Juanito Oiarzabal, en 1999, y la primera mujer reconocida sin discusión, la española **Edurne Pasaban**, en 2010.

!foto himalaya | El Himalaya visto desde un avión: una muralla de cumbres de más de 2.400 km.

## Las cumbres de cada continente

| Continente | Montaña | Altura |
|---|---|---|
| Asia | Everest | 8.849 m |
| América | Aconcagua (Argentina) | 6.961 m |
| África | Kilimanjaro (Tanzania) | 5.895 m |
| Europa | Elbrús (Rusia) / Mont Blanc | 5.642 m / 4.806 m |
| Antártida | Macizo Vinson | 4.892 m |
| Oceanía | Puncak Jaya (Nueva Guinea) | 4.884 m |

Escalarlas todas es el reto de las **siete cumbres**.

## Récords que dependen de cómo se midan

- La montaña más alta **desde su base** es el **Mauna Kea**, en Hawái: mide unos 10.200 metros desde el fondo del océano, aunque solo asoma 4.207 sobre el agua.
- El punto más **alejado del centro de la Tierra** es la cima del **Chimborazo**, en Ecuador, porque la Tierra está achatada y abultada en el ecuador.
- La cordillera más **larga** es la de los **Andes**: unos 7.000 km a lo largo de Sudamérica. Pero la cordillera mayor de todas está bajo el mar: la **dorsal oceánica**, de 65.000 km.

## Las montañas de España

España es el segundo país más montañoso de Europa, después de Suiza.

- El pico más alto es el **Teide** (3.715 m), en Tenerife: un volcán que, medido desde el fondo del mar, supera los 7.500 metros.
- En la península, el **Mulhacén** (3.479 m), en Sierra Nevada, seguido del **Aneto** (3.404 m), el techo de los Pirineos.
- Los **Picos de Europa** forman el primer parque nacional de España, creado en 1918 (entonces, de la montaña de Covadonga).

> El aire en la cima del Everest tiene solo un tercio del oxígeno que hay al nivel del mar. Por encima de los 8.000 metros empieza la «zona de la muerte», donde el cuerpo humano no puede aclimatarse y se deteriora con cada hora que pasa.
""",
    """
The great mountain ranges are born from collisions between [tectonic plates](@tectonica-de-placas). When two plates push against each other, the crust crumples and rises like a rug shoved against a wall. Volcanoes form other mountains, such as [Teide](@volcanes) or Kilimanjaro.

## The roof of the world

**Everest** (Chomolungma in Tibetan, Sagarmatha in Nepali) stands **8,849 metres** tall, according to the joint Chinese–Nepali measurement of 2020. It lies in the **Himalayas**, the range that formed when India collided with Asia some 50 million years ago. India is still pushing at 4–5 cm a year, and the Himalayas rise by about **half a centimetre a year**, although erosion wears them down.

At the summit there are limestone rocks containing fossils of sea creatures: 450 million years ago, that rock was the floor of a sea.

Everest was first climbed on **29 May 1953** by the New Zealander **Edmund Hillary** and the Sherpa **Tenzing Norgay**. Today more than 6,000 people have reached the top, and in good seasons queues form near the summit.

## The fourteen eight-thousanders

There are only **14 mountains over 8,000 metres**, all in the Himalayas and Karakoram. The second highest is **K2** (8,611 m), much harder and more dangerous than Everest. The first person to climb all fourteen was the Italian Reinhold Messner, in 1986; the first Spaniard, Juanito Oiarzabal, in 1999; and the first woman to do so without dispute was Spain's **Edurne Pasaban**, in 2010.

!foto himalaya | The Himalayas from a plane: a wall of peaks more than 2,400 km long.

## The highest peak on each continent

| Continent | Mountain | Height |
|---|---|---|
| Asia | Everest | 8,849 m |
| Americas | Aconcagua (Argentina) | 6,961 m |
| Africa | Kilimanjaro (Tanzania) | 5,895 m |
| Europe | Elbrus (Russia) / Mont Blanc | 5,642 m / 4,806 m |
| Antarctica | Vinson Massif | 4,892 m |
| Oceania | Puncak Jaya (New Guinea) | 4,884 m |

Climbing them all is the **Seven Summits** challenge.

## Records that depend on how you measure

- The tallest mountain **from base to summit** is **Mauna Kea** in Hawaii: about 10,200 metres from the ocean floor, though only 4,207 m rises above the water.
- The point **farthest from the Earth's centre** is the summit of **Chimborazo** in Ecuador, because the Earth bulges at the equator.
- The **longest** range is the **Andes**: about 7,000 km along South America. But the greatest range of all is underwater: the **mid-ocean ridge**, 65,000 km long.

## The mountains of Spain

Spain is the second most mountainous country in Europe, after Switzerland.

- Its highest peak is **Teide** (3,715 m) on Tenerife: a volcano that, measured from the seabed, exceeds 7,500 metres.
- On the mainland, **Mulhacén** (3,479 m) in the Sierra Nevada, followed by **Aneto** (3,404 m), the roof of the Pyrenees.
- The **Picos de Europa** form Spain's first national park, created in 1918.

> The air at the top of Everest holds only a third of the oxygen found at sea level. Above 8,000 metres lies the "death zone", where the human body cannot acclimatise and deteriorates with every hour.
""",
    datos=[("Montaña más alta", "Highest mountain", "Everest, 8.849 m", "Everest, 8,849 m"),
           ("Primera ascensión", "First ascent", "Hillary y Tenzing, 1953", "Hillary and Tenzing, 1953"),
           ("Ochomiles", "Eight-thousanders", "14", "14"),
           ("Cordillera más larga", "Longest range", "Andes, ≈ 7.000 km", "Andes, ≈ 7,000 km"),
           ("Mayor desde su base", "Tallest from base", "Mauna Kea, ≈ 10.200 m", "Mauna Kea, ≈ 10,200 m"),
           ("Pico más alto de España", "Highest peak in Spain", "Teide, 3.715 m", "Teide, 3,715 m")],
    pie=("La cara norte del Everest desde el Tíbet.",
         "The north face of Everest from Tibet."),
)

DESIERTOS = F(
    ("desiertos", "deserts"),
    ("Desiertos", "Deserts"),
    ("Arena, sal y hielo: el Sahara, el Atacama, el salar de Uyuni y por qué la Antártida es el mayor desierto del planeta.",
     "Sand, salt and ice: the Sahara, the Atacama, the Uyuni salt flat and why Antarctica is the largest desert on the planet."),
    ("desiertos, desierto más grande del mundo, Sahara, Atacama, desierto más seco, salar de Uyuni, dunas, oasis, Antártida desierto, Tabernas, Bardenas Reales, desertificación, Sahara verde, Valle de la Muerte",
     "deserts, largest desert in the world, Sahara, Atacama, driest desert, Uyuni salt flat, dunes, oasis, Antarctic desert, Tabernas, Bardenas Reales, desertification, Green Sahara, Death Valley"),
    "sahara",
    """
Un **desierto** no se define por el calor ni por la arena, sino por la falta de lluvia: es un lugar donde caen **menos de 250 mm de precipitación al año** y se evapora más agua de la que llega. Los desiertos cubren alrededor de **un tercio de las tierras** del planeta.

## El mayor desierto es de hielo

Con esa definición, el desierto más grande del mundo es la **Antártida** (14 millones de km²), seguida del **Ártico**. El mayor desierto cálido es el **Sahara**, con unos 9,2 millones de km², casi tan grande como Estados Unidos o China.

Solo alrededor de una cuarta parte del Sahara es arena; el resto son llanuras de piedra, montañas y mesetas. Sus dunas pueden superar los 150 metros de altura y moverse varios metros al año.

## El Sahara fue verde

Hace entre 11.000 y 5.000 años, un cambio en la órbita de la Tierra desplazó los monzones hacia el norte y el Sahara se llenó de lagos, sabanas, hipopótamos, jirafas y cocodrilos. En sus rocas hay pinturas de pastores con ganado y de gente nadando. Hoy, el polvo del Sahara viaja cada año a la Amazonia, a la que abona con fósforo, y a menudo cubre de barro los coches de España cuando llega la «calima».

## El lugar más seco del mundo

El **desierto de Atacama**, en Chile, es el desierto no polar más seco del mundo. Hay estaciones meteorológicas que nunca han registrado lluvia, y algunas zonas podrían llevar siglos sin una precipitación apreciable. Su suelo es tan parecido al de [Marte](@marte) que la NASA prueba allí sus robots. Y su cielo limpísimo hace que albergue algunos de los mayores [telescopios](@telescopios-para-aficionados) del mundo.

Cuando por fin llueve, el Atacama se cubre de flores en pocas semanas: es el fenómeno del **desierto florido**.

!foto atacama | El desierto de Atacama, en Chile, uno de los lugares más secos del planeta.

## El espejo más grande del mundo

El **salar de Uyuni**, en Bolivia, es el mayor desierto de sal del mundo: más de 10.000 km² de costra blanca y casi perfectamente plana, restos de un antiguo lago evaporado. En la estación de lluvias se cubre de una fina capa de agua y se convierte en un espejo gigante que refleja el cielo. Bajo la sal se esconde una de las mayores reservas de **litio** del planeta, clave para las baterías.

!foto uyuni | El salar de Uyuni (Bolivia), un desierto de sal de más de 10.000 km².

## Desiertos de España

España tiene el único desierto de Europa según algunas definiciones: el **desierto de Tabernas**, en Almería, donde se rodaron decenas de películas del Oeste y escenas de *Indiana Jones* o *Juego de tronos*. Otros paisajes semidesérticos son las **Bardenas Reales** en Navarra y el **cabo de Gata**.

El gran riesgo es la **desertificación**: la degradación de tierras secas por el mal uso del agua y del suelo y por el [cambio climático](@cambio-climatico). Alrededor de tres cuartas partes del territorio español son susceptibles de sufrirla.

## Vivir sin agua

- El **camello** puede beber más de 100 litros en pocos minutos y aguantar una semana o más sin beber.
- El **escarabajo de niebla** del desierto del Namib bebe las gotas de niebla que se condensan sobre su espalda.
- La ***Welwitschia mirabilis***, también del Namib, tiene solo dos hojas que crecen sin parar durante más de mil años.

> El Valle de la Muerte, en California, tiene el récord de la temperatura del aire más alta medida de forma fiable: 54,4 °C en 2020 y 2021. El récord oficial de 56,7 °C de 1913 es muy discutido.
""",
    """
A **desert** is defined not by heat or sand, but by lack of rain: it is a place that receives **less than 250 mm of precipitation a year** and loses more water to evaporation than arrives. Deserts cover about **a third of the planet's land**.

## The largest desert is made of ice

By that definition, the largest desert in the world is **Antarctica** (14 million km²), followed by the **Arctic**. The largest hot desert is the **Sahara**, at about 9.2 million km², almost as big as the United States or China.

Only about a quarter of the Sahara is sand; the rest is stony plains, mountains and plateaus. Its dunes can exceed 150 metres in height and move several metres a year.

## The Sahara was once green

Between 11,000 and 5,000 years ago, a shift in Earth's orbit pushed the monsoons north and the Sahara filled with lakes, savanna, hippos, giraffes and crocodiles. Its rocks bear paintings of herders with cattle and of people swimming. Today, Saharan dust travels every year to the Amazon, which it fertilises with phosphorus, and it often coats cars in Spain with mud when the "calima" arrives.

## The driest place on Earth

The **Atacama Desert** in Chile is the driest non-polar desert in the world. Some weather stations there have never recorded rain, and some areas may have gone centuries without significant rainfall. Its soil is so similar to that of [Mars](@marte) that NASA tests its robots there. And its crystal-clear skies make it home to some of the world's largest [telescopes](@telescopios-para-aficionados).

When it finally rains, the Atacama is covered in flowers within weeks: the phenomenon of the **flowering desert**.

!foto atacama | The Atacama Desert in Chile, one of the driest places on the planet.

## The world's largest mirror

The **Salar de Uyuni** in Bolivia is the largest salt flat in the world: more than 10,000 km² of white crust, almost perfectly flat, the remains of an ancient evaporated lake. In the rainy season it is covered by a thin film of water and becomes a giant mirror reflecting the sky. Beneath the salt lies one of the planet's largest reserves of **lithium**, key to batteries.

!foto uyuni | The Salar de Uyuni (Bolivia), a salt desert of more than 10,000 km².

## Deserts of Spain

By some definitions Spain has the only desert in Europe: the **Tabernas Desert** in Almería, where dozens of westerns and scenes from *Indiana Jones* and *Game of Thrones* were filmed. Other semi-desert landscapes include the **Bardenas Reales** in Navarre and **Cabo de Gata**.

The great risk is **desertification**: the degradation of drylands through poor use of water and soil and through [climate change](@cambio-climatico). About three quarters of Spain's territory is susceptible to it.

## Living without water

- The **camel** can drink more than 100 litres in a few minutes and go a week or more without drinking.
- The Namib Desert's **fog-basking beetle** drinks the droplets of fog that condense on its back.
- ***Welwitschia mirabilis***, also from the Namib, has just two leaves that keep growing for more than a thousand years.

> Death Valley in California holds the record for the highest reliably measured air temperature: 54.4 °C in 2020 and 2021. The official 56.7 °C record from 1913 is widely disputed.
""",
    datos=[("Definición", "Definition", "< 250 mm de lluvia al año", "< 250 mm of rain a year"),
           ("Mayor desierto", "Largest desert", "Antártida, 14 millones de km²", "Antarctica, 14 million km²"),
           ("Mayor desierto cálido", "Largest hot desert", "Sahara, ≈ 9,2 millones de km²", "Sahara, ≈ 9.2 million km²"),
           ("Desierto más seco", "Driest desert", "Atacama (Chile)", "Atacama (Chile)"),
           ("Mayor salar", "Largest salt flat", "Uyuni, > 10.000 km²", "Uyuni, > 10,000 km²"),
           ("Temperatura récord fiable", "Reliable record temperature", "54,4 °C, Valle de la Muerte", "54.4 °C, Death Valley")],
    pie=("Dunas del Sahara, el mayor desierto cálido del mundo.",
         "Dunes in the Sahara, the largest hot desert in the world."),
)

ISLAS = F(
    ("islas-y-costas", "islands-and-coasts"),
    ("Islas y costas", "Islands and coasts"),
    ("Groenlandia, las Galápagos, las Maldivas y las Canarias: cómo nacen las islas, las más grandes y las más raras del planeta.",
     "Greenland, the Galápagos, the Maldives and the Canary Islands: how islands form, and the largest and strangest on the planet."),
    ("islas, isla más grande del mundo, Groenlandia, islas volcánicas, atolones, Maldivas, Galápagos, Socotra, Canarias, Baleares, Lanzarote, Calzada del Gigante, costas, acantilados, playas, isla más remota",
     "islands, largest island in the world, Greenland, volcanic islands, atolls, Maldives, Galápagos, Socotra, Canary Islands, Balearic Islands, Lanzarote, Giant's Causeway, coasts, cliffs, beaches, most remote island"),
    "maldivas",
    """
En la Tierra hay cientos de miles de islas: solo Suecia tiene más de 260.000. Las hay del tamaño de un país y del tamaño de una roca, heladas y tropicales, recién nacidas y muy antiguas. Por su aislamiento, son laboratorios de la [evolución](@evolucion) y albergan especies que no existen en ningún otro lugar.

## Cómo nacen las islas

- **Continentales**: trozos de continente separados por el mar, como Gran Bretaña, Madagascar o las Baleares.
- **Volcánicas**: levantadas por erupciones desde el fondo del océano, como Hawái, Islandia o las **Canarias**. Algunas son recientes: Surtsey, frente a Islandia, nació entre 1963 y 1967.
- **Coralinas**: los **atolones** son anillos de arrecife que rodean una laguna. Se forman sobre volcanes que se van hundiendo mientras el coral sigue creciendo hacia la luz, como explicó Darwin.

## Islas de récord

- La **más grande**: **Groenlandia**, de 2,17 millones de km², más de cuatro veces España. Australia es mayor, pero se considera un continente. El 80 % de Groenlandia está cubierto de [hielo](@glaciares-y-hielo).
- La **más poblada**: **Java**, en Indonesia, con unos 150 millones de habitantes.
- La **más remota** habitada: **Tristán de Acuña**, en el Atlántico Sur, a unos 2.400 km de la costa más cercana, con unas 250 personas.
- **Indonesia** es el país con más islas habitadas: tiene más de 17.000 en total.

## Islas que son un mundo aparte

- Las **Galápagos** (Ecuador), donde Darwin observó sus pinzones, tienen tortugas gigantes, iguanas marinas que bucean para comer algas y cormoranes que perdieron la capacidad de volar.
- **Socotra** (Yemen) tiene árboles con forma de paraguas, los dragos de sangre de dragón, y un tercio de sus plantas no existe en ningún otro sitio.
- **Madagascar** se separó de África hace 160 millones de años: el 90 % de su fauna es endémica, incluidos todos los lémures del mundo.

!foto galapagos | Una tortuga gigante de las Galápagos. Estos animales pueden vivir más de 150 años.

## Las Maldivas, en peligro

Las **Maldivas** son el país más bajo del mundo: su punto más alto apenas supera los 2 metros sobre el mar y la altura media es de 1,5 metros. La [subida del nivel del mar](@cambio-climatico) amenaza su existencia. En 2009 su Gobierno celebró una reunión bajo el agua, con trajes de buceo, para llamar la atención del mundo.

## Las islas de España

España tiene dos grandes archipiélagos de origen muy distinto:

- Las **Baleares** son continentales: la continuación submarina de las cordilleras béticas.
- Las **Canarias** son volcánicas y siguen activas: la última erupción, la del [Tajogaite](@volcanes) en La Palma, fue en 2021. **Lanzarote** tiene paisajes de lava de las erupciones de Timanfaya de 1730-1736, que duraron seis años, y toda la isla es Reserva de la Biosfera. **El Hierro** vio nacer un volcán submarino en 2011.

## Costas asombrosas

La costa es la frontera más cambiante del planeta. Las olas excavan **acantilados**, cuevas y arcos de roca, y los ríos y las corrientes construyen **playas**, flechas de arena y deltas. La **Calzada del Gigante**, en Irlanda del Norte, está formada por unas 40.000 columnas hexagonales de basalto que se formaron al enfriarse lentamente una colada de lava. En España, la **playa de las Catedrales** (Lugo) muestra arcos de roca de hasta 30 metros que solo se pueden recorrer con la marea baja.

> La costa de Noruega mide unos 2.650 km en línea recta, pero si se cuentan todos los fiordos y las islas supera los 100.000 km, más de dos vueltas a la Tierra. Cuanto más pequeña es la regla con la que se mide una costa, más larga sale: es la «paradoja de la línea de costa».
""",
    """
There are hundreds of thousands of islands on Earth: Sweden alone has more than 260,000. Some are the size of a country and others the size of a rock; some are icy and others tropical, some newborn and some very old. Because of their isolation, they are laboratories of [evolution](@evolucion) and are home to species found nowhere else.

## How islands form

- **Continental**: pieces of continent cut off by the sea, such as Great Britain, Madagascar or the Balearic Islands.
- **Volcanic**: raised by eruptions from the ocean floor, such as Hawaii, Iceland or the **Canary Islands**. Some are very young: Surtsey, off Iceland, was born between 1963 and 1967.
- **Coral**: **atolls** are rings of reef surrounding a lagoon. They form on top of volcanoes that slowly sink while the coral keeps growing towards the light, as Darwin explained.

## Record-breaking islands

- **Largest**: **Greenland**, at 2.17 million km², more than four times the size of Spain. Australia is bigger but counts as a continent. 80% of Greenland is covered in [ice](@glaciares-y-hielo).
- **Most populous**: **Java**, in Indonesia, with some 150 million people.
- **Most remote** inhabited island: **Tristan da Cunha**, in the South Atlantic, about 2,400 km from the nearest coast, with around 250 residents.
- **Indonesia** is the country with the most inhabited islands: it has more than 17,000 in total.

## Islands that are worlds apart

- The **Galápagos** (Ecuador), where Darwin studied his finches, have giant tortoises, marine iguanas that dive to eat seaweed and cormorants that have lost the ability to fly.
- **Socotra** (Yemen) has umbrella-shaped dragon's blood trees, and a third of its plants exist nowhere else.
- **Madagascar** split from Africa 160 million years ago: 90% of its wildlife is endemic, including all the world's lemurs.

!foto galapagos | A Galápagos giant tortoise. These animals can live more than 150 years.

## The Maldives in danger

The **Maldives** is the lowest-lying country in the world: its highest point barely exceeds 2 metres above sea level and the average height is 1.5 metres. [Rising seas](@cambio-climatico) threaten its very existence. In 2009 its government held a cabinet meeting underwater, in scuba gear, to draw the world's attention.

## The islands of Spain

Spain has two major archipelagos of very different origin:

- The **Balearic Islands** are continental: the underwater continuation of the Betic mountain ranges.
- The **Canary Islands** are volcanic and still active: the last eruption, [Tajogaite](@volcanes) on La Palma, was in 2021. **Lanzarote** has lava landscapes from the Timanfaya eruptions of 1730–1736, which lasted six years, and the whole island is a Biosphere Reserve. **El Hierro** saw an underwater volcano born in 2011.

## Astonishing coasts

The coast is the planet's most changeable frontier. Waves carve **cliffs**, caves and rock arches, while rivers and currents build **beaches**, sand spits and deltas. The **Giant's Causeway** in Northern Ireland is made of some 40,000 hexagonal basalt columns formed as a lava flow cooled slowly. In Spain, **As Catedrais beach** (Lugo) has rock arches up to 30 metres high that can only be explored at low tide.

> Norway's coast is about 2,650 km long in a straight line, but counting all the fjords and islands it exceeds 100,000 km, more than twice around the Earth. The smaller the ruler you use to measure a coastline, the longer it comes out: this is the "coastline paradox".
""",
    datos=[("Isla más grande", "Largest island", "Groenlandia, 2,17 millones de km²", "Greenland, 2.17 million km²"),
           ("Isla más poblada", "Most populous island", "Java, ≈ 150 millones", "Java, ≈ 150 million"),
           ("Isla habitada más remota", "Most remote inhabited island", "Tristán de Acuña", "Tristan da Cunha"),
           ("País más bajo", "Lowest country", "Maldivas, altura media 1,5 m", "Maldives, average height 1.5 m"),
           ("Última erupción en España", "Latest eruption in Spain", "Tajogaite, La Palma, 2021", "Tajogaite, La Palma, 2021")],
    pie=("Atolones de las Maldivas, el país más bajo del mundo.",
         "Atolls in the Maldives, the lowest-lying country in the world."),
)

POLOS = F(
    ("polos", "poles"),
    ("Los polos", "The poles"),
    ("La Antártida y el Ártico: el continente helado, la carrera al Polo Sur, el sol de medianoche y un hielo que se está derritiendo.",
     "Antarctica and the Arctic: the frozen continent, the race to the South Pole, the midnight sun and ice that is melting."),
    ("polos, Polo Norte, Polo Sur, Antártida, Ártico, Amundsen, Scott, carrera al Polo Sur, temperatura más baja, base Vostok, sol de medianoche, noche polar, Tratado Antártico, base Juan Carlos I, hielo marino",
     "poles, North Pole, South Pole, Antarctica, Arctic, Amundsen, Scott, race to the South Pole, lowest temperature, Vostok Station, midnight sun, polar night, Antarctic Treaty, Juan Carlos I base, sea ice"),
    "iceberg",
    """
Los polos son los extremos del eje sobre el que gira la Tierra. Son los lugares más fríos del planeta porque los rayos del Sol les llegan muy inclinados, y viven seis meses de día y seis de noche. Pero son muy distintos entre sí: **el Ártico es un océano rodeado de continentes; la Antártida es un continente rodeado de océano.**

## La Antártida

La **Antártida** es el continente más frío, seco, ventoso y alto (de media) de la Tierra. Su capa de hielo tiene un espesor medio de unos **1.900 metros**, y en algunos puntos casi 5.000. Contiene alrededor del **70 % del agua dulce** del planeta: si se derritiera entera, el nivel del mar subiría unos 58 metros.

En la base rusa **Vostok** se midió en 1983 la temperatura del aire más baja registrada en una estación: **−89,2 °C**. Satélites han detectado en algunas hondonadas de la meseta antártica temperaturas de la superficie de unos −98 °C.

Bajo el hielo se esconden más de 400 **lagos subglaciales** de agua líquida, como el lago Vostok, aislado del exterior desde hace millones de años.

## La carrera al Polo Sur

En 1911, dos expediciones compitieron por ser las primeras en llegar al Polo Sur. El noruego **Roald Amundsen**, con perros de trineo y esquís, llegó el **14 de diciembre de 1911**. El británico **Robert Falcon Scott** llegó 34 días después y encontró la bandera noruega. Scott y sus cuatro compañeros murieron de frío y hambre en el camino de vuelta.

## Un continente para la ciencia

El **Tratado Antártico** de 1959 convirtió la Antártida en una reserva dedicada a la paz y la ciencia: prohíbe las actividades militares, las pruebas nucleares y la minería. Unas 30 naciones tienen bases allí. España tiene dos: **Juan Carlos I**, en la isla Livingston, y **Gabriel de Castilla**, en la isla Decepción, un volcán activo.

!foto iceberg | Un iceberg tabular en la Antártida, desprendido de una plataforma de hielo.

## El Ártico

El **Ártico** es un océano helado rodeado por Canadá, Groenlandia, Rusia, Noruega y Alaska. En el **Polo Norte** no hay tierra: solo una capa de hielo marino de unos pocos metros que flota sobre un océano de más de 4.000 metros de profundidad. En 2007, un submarino ruso dejó una bandera de titanio en el fondo marino bajo el polo.

A diferencia de la Antártida, el Ártico tiene habitantes desde hace miles de años, como los **inuit** de Canadá y Groenlandia y los **sami** de Escandinavia.

## El hielo se está derritiendo

El Ártico se calienta unas **cuatro veces más rápido** que el resto del planeta. La superficie de hielo marino al final del verano se ha reducido alrededor de un 40 % desde 1979, y los científicos creen que hacia mediados de siglo podría haber veranos sin hielo en el Ártico. En la Antártida, las grandes plataformas de hielo también se están debilitando, y en 2023 el hielo marino antártico marcó mínimos históricos.

## Sol de medianoche y noche polar

Por la inclinación del eje terrestre, en los polos el Sol no se pone durante seis meses y no sale durante otros seis. Más allá del círculo polar, hay al menos un día al año de **sol de medianoche** y uno de **noche polar**. Son también los mejores lugares para ver [auroras](@auroras-y-fenomenos-opticos).

> En el Polo Sur, todas las direcciones apuntan al norte. Y como allí se juntan todos los meridianos, en la base Amundsen-Scott se puede dar la vuelta al mundo en unos segundos, caminando alrededor del poste que marca el polo.
""",
    """
The poles are the ends of the axis on which the Earth spins. They are the coldest places on the planet because sunlight strikes them at a low angle, and they have six months of day and six of night. But they are very different from each other: **the Arctic is an ocean surrounded by continents; Antarctica is a continent surrounded by ocean.**

## Antarctica

**Antarctica** is the coldest, driest, windiest and (on average) highest continent on Earth. Its ice sheet averages about **1,900 metres** thick, and in places almost 5,000. It holds around **70% of the planet's fresh water**: if it all melted, sea level would rise by about 58 metres.

At Russia's **Vostok** base the lowest air temperature ever recorded at a station was measured in 1983: **−89.2 °C**. Satellites have detected surface temperatures of about −98 °C in some hollows on the Antarctic plateau.

Beneath the ice lie more than 400 **subglacial lakes** of liquid water, such as Lake Vostok, sealed off from the outside world for millions of years.

## The race to the South Pole

In 1911, two expeditions raced to be first to the South Pole. The Norwegian **Roald Amundsen**, with sled dogs and skis, arrived on **14 December 1911**. The Briton **Robert Falcon Scott** arrived 34 days later and found the Norwegian flag. Scott and his four companions died of cold and hunger on the way back.

## A continent for science

The 1959 **Antarctic Treaty** made Antarctica a reserve devoted to peace and science: it bans military activity, nuclear testing and mining. About 30 nations have bases there. Spain has two: **Juan Carlos I** on Livingston Island and **Gabriel de Castilla** on Deception Island, an active volcano.

!foto iceberg | A tabular iceberg in Antarctica, broken off from an ice shelf.

## The Arctic

The **Arctic** is a frozen ocean surrounded by Canada, Greenland, Russia, Norway and Alaska. At the **North Pole** there is no land: just a layer of sea ice a few metres thick floating on an ocean more than 4,000 metres deep. In 2007 a Russian submarine planted a titanium flag on the seabed beneath the pole.

Unlike Antarctica, the Arctic has been inhabited for thousands of years, by peoples such as the **Inuit** of Canada and Greenland and the **Sámi** of Scandinavia.

## The ice is melting

The Arctic is warming about **four times faster** than the rest of the planet. The area of sea ice at the end of summer has shrunk by around 40% since 1979, and scientists think there could be ice-free Arctic summers by mid-century. In Antarctica the great ice shelves are also weakening, and in 2023 Antarctic sea ice hit record lows.

## Midnight sun and polar night

Because of the tilt of the Earth's axis, at the poles the Sun does not set for six months and does not rise for another six. Beyond the polar circles there is at least one day a year of **midnight sun** and one of **polar night**. They are also the best places to see [auroras](@auroras-y-fenomenos-opticos).

> At the South Pole, every direction is north. And since all the meridians meet there, at the Amundsen–Scott base you can walk around the world in a few seconds by circling the post that marks the pole.
""",
    datos=[("Espesor medio del hielo antártico", "Average Antarctic ice thickness", "≈ 1.900 m", "≈ 1,900 m"),
           ("Agua dulce del planeta", "Planet's fresh water", "≈ 70 % en la Antártida", "≈ 70% in Antarctica"),
           ("Temperatura más baja medida", "Lowest temperature measured", "−89,2 °C, Vostok, 1983", "−89.2 °C, Vostok, 1983"),
           ("Primero en el Polo Sur", "First at the South Pole", "Amundsen, 14-12-1911", "Amundsen, 14 Dec 1911"),
           ("Bases españolas", "Spanish bases", "Juan Carlos I y Gabriel de Castilla", "Juan Carlos I and Gabriel de Castilla"),
           ("Calentamiento del Ártico", "Arctic warming", "≈ 4 veces más rápido que la media", "≈ 4 times faster than average")],
    pie=("Un iceberg en aguas de la Antártida.",
         "An iceberg in Antarctic waters."),
)

ESPANA = F(
    ("geografia-de-espana", "geography-of-spain"),
    ("La geografía de España", "The geography of Spain"),
    ("Un país de montañas, mesetas, volcanes y dos mares: el relieve, los ríos, los climas y los paisajes más asombrosos de España.",
     "A country of mountains, plateaus, volcanoes and two seas: the relief, rivers, climates and most astonishing landscapes of Spain."),
    ("geografía de España, relieve de España, Meseta Central, ríos de España, Tajo, Ebro, Duero, Guadalquivir, parques nacionales, Picos de Europa, Doñana, Teide, Ordesa, climas de España, paisajes de España, Río Tinto",
     "geography of Spain, relief of Spain, Central Plateau, rivers of Spain, Tagus, Ebro, Douro, Guadalquivir, national parks, Picos de Europa, Doñana, Teide, Ordesa, climates of Spain, landscapes of Spain, Río Tinto"),
    "picos_europa",
    """
España ocupa unos **506.000 km²**, la mayor parte de la península ibérica, más los archipiélagos de Baleares y Canarias, Ceuta y Melilla. Es el cuarto país más grande de Europa y uno de los más variados: en pocas horas de viaje se pasa de bosques atlánticos a desiertos, de cumbres nevadas a volcanes.

## Una península alta

La gran protagonista es la **Meseta Central**, una llanura elevada de entre 600 y 1.000 metros de altitud que ocupa casi la mitad de la península. Madrid es la capital más alta de la Unión Europea, a unos 650 metros. La Meseta está dividida en dos por el **Sistema Central** y rodeada de cordilleras: la **cordillera Cantábrica**, el **Sistema Ibérico** y **Sierra Morena**. Fuera de ella se alzan los **Pirineos** y las **cordilleras Béticas**, donde está Sierra Nevada.

## Los ríos

| Río | Longitud | Desemboca en |
|---|---|---|
| Tajo | 1.007 km (el más largo de la península) | Atlántico, en Lisboa |
| Ebro | 930 km (el más caudaloso de España) | Mediterráneo, en un gran delta |
| Duero | 897 km | Atlántico, en Oporto |
| Guadiana | 744 km | Atlántico |
| Guadalquivir | 657 km (el único navegable hasta Sevilla) | Atlántico, en Doñana |

La mayoría de los grandes ríos van al Atlántico, porque la Meseta está inclinada hacia el oeste. El **delta del Ebro**, uno de los mayores humedales del Mediterráneo, está retrocediendo porque los embalses retienen los sedimentos que lo formaban.

## Los climas

España tiene una enorme variedad de [climas](@climas-del-mundo):

- **Oceánico** en el norte: suave y lluvioso, la «España verde».
- **Mediterráneo** en la mayor parte del país: veranos secos y calurosos.
- **Continental** en la Meseta: inviernos fríos y veranos muy calurosos.
- **De montaña** en las cordilleras.
- **Subtropical** en Canarias, con temperaturas suaves todo el año.
- **Semiárido** en el sureste: el **cabo de Gata** es uno de los lugares más secos de Europa.

## Los parques nacionales

España tiene **16 parques nacionales**. Algunos de los más famosos:

- **Picos de Europa**, el primero (1918).
- **Ordesa y Monte Perdido**, en el Pirineo de Huesca, con cañones de más de 1.000 metros.
- **Doñana**, uno de los humedales más importantes de Europa, parada de millones de aves migratorias y refugio del lince ibérico.
- **Teide**, el parque nacional más visitado de España y uno de los más visitados del mundo.
- **Sierra de las Nieves** (Málaga), el más reciente (2021), famoso por sus pinsapos.

!foto donana | Las marismas de Doñana, uno de los grandes humedales de Europa.

## Paisajes que parecen de otro planeta

- El **río Tinto** (Huelva), de aguas rojas y ácidas por el hierro, explotado por sus minas desde hace 5.000 años.
- La **Ciudad Encantada** de Cuenca, con rocas calizas esculpidas por el agua y el viento.
- **Las Médulas** (León), restos de una gigantesca mina de oro romana, Patrimonio de la Humanidad.
- El **Torcal de Antequera** (Málaga), un laberinto de rocas que fue fondo marino hace 150 millones de años.
- Los paisajes volcánicos de **Timanfaya** y el [Teide](@volcanes) en Canarias.

!foto rio_tinto | Las aguas rojas del río Tinto, en Huelva.

> España es uno de los países con más Reservas de la Biosfera del mundo: tiene más de 50, entre ellas islas enteras como Lanzarote, Menorca, La Palma, El Hierro y Fuerteventura.
""",
    """
Spain covers about **506,000 km²**, most of the Iberian Peninsula plus the Balearic and Canary archipelagos and the cities of Ceuta and Melilla. It is the fourth-largest country in Europe and one of the most varied: in a few hours you can travel from Atlantic forests to deserts, from snowy peaks to volcanoes.

## A high peninsula

The star feature is the **Meseta Central**, a raised plateau 600 to 1,000 metres high that covers almost half the peninsula. Madrid is the highest capital in the European Union, at about 650 metres. The Meseta is split in two by the **Sistema Central** and ringed by mountain ranges: the **Cantabrian Mountains**, the **Iberian System** and the **Sierra Morena**. Beyond it rise the **Pyrenees** and the **Betic ranges**, home to the Sierra Nevada.

## The rivers

| River | Length | Flows into |
|---|---|---|
| Tagus (Tajo) | 1,007 km (the longest in the peninsula) | Atlantic, at Lisbon |
| Ebro | 930 km (the largest flow in Spain) | Mediterranean, in a great delta |
| Douro (Duero) | 897 km | Atlantic, at Porto |
| Guadiana | 744 km | Atlantic |
| Guadalquivir | 657 km (the only one navigable up to Seville) | Atlantic, at Doñana |

Most of the big rivers flow into the Atlantic, because the Meseta tilts westwards. The **Ebro Delta**, one of the Mediterranean's largest wetlands, is shrinking because dams trap the sediment that built it.

## The climates

Spain has a huge variety of [climates](@climas-del-mundo):

- **Oceanic** in the north: mild and rainy, "Green Spain".
- **Mediterranean** across most of the country: dry, hot summers.
- **Continental** on the Meseta: cold winters and very hot summers.
- **Mountain** in the ranges.
- **Subtropical** in the Canaries, mild all year round.
- **Semi-arid** in the south-east: **Cabo de Gata** is one of the driest places in Europe.

## The national parks

Spain has **16 national parks**. Some of the best known:

- **Picos de Europa**, the first (1918).
- **Ordesa y Monte Perdido**, in the Huesca Pyrenees, with canyons more than 1,000 metres deep.
- **Doñana**, one of Europe's most important wetlands, a stopover for millions of migrating birds and a refuge for the Iberian lynx.
- **Teide**, Spain's most visited national park and one of the most visited in the world.
- **Sierra de las Nieves** (Málaga), the newest (2021), famous for its Spanish firs.

!foto donana | The Doñana marshes, one of Europe's great wetlands.

## Landscapes from another planet

- The **Río Tinto** (Huelva), with red, acidic, iron-laden water, mined for 5,000 years.
- The **Ciudad Encantada** ("Enchanted City") in Cuenca, with limestone rocks sculpted by water and wind.
- **Las Médulas** (León), the remains of a gigantic Roman gold mine, a World Heritage Site.
- **El Torcal de Antequera** (Málaga), a maze of rocks that was seabed 150 million years ago.
- The volcanic landscapes of **Timanfaya** and [Teide](@volcanes) in the Canary Islands.

!foto rio_tinto | The red waters of the Río Tinto in Huelva.

> Spain is one of the countries with the most Biosphere Reserves in the world: more than 50, including entire islands such as Lanzarote, Menorca, La Palma, El Hierro and Fuerteventura.
""",
    datos=[("Superficie", "Area", "≈ 506.000 km²", "≈ 506,000 km²"),
           ("Altitud de la Meseta", "Meseta altitude", "600-1.000 m", "600–1,000 m"),
           ("Río más largo", "Longest river", "Tajo, 1.007 km", "Tagus, 1,007 km"),
           ("Río más caudaloso", "River with the greatest flow", "Ebro", "Ebro"),
           ("Parques nacionales", "National parks", "16", "16"),
           ("Pico más alto", "Highest peak", "Teide, 3.715 m", "Teide, 3,715 m")],
    pie=("Los Picos de Europa, el primer parque nacional de España (1918).",
         "The Picos de Europa, Spain's first national park (1918)."),
)

FICHAS = [CONTINENTES, MONTANAS, DESIERTOS, ISLAS, POLOS, ESPANA]
