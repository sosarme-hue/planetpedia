from universo import F

SLUG = ("atmosfera-y-clima", "atmosphere-and-climate")
TITULO = ("Atmósfera y clima", "Atmosphere and climate")
RESUMEN = ("El aire que nos protege, las nubes y el tiempo, tormentas y huracanes, los climas del mundo, el cambio climático y los espectáculos de luz del cielo.",
           "The air that protects us, clouds and weather, storms and hurricanes, the world's climates, climate change and the sky's light shows.")
CLAVES = ("atmósfera, clima, tiempo atmosférico, meteorología, nubes, lluvia, tormentas, rayos, huracanes, tornados, dana, climas del mundo, cambio climático, calentamiento global, auroras, arcoíris",
          "atmosphere, climate, weather, meteorology, clouds, rain, storms, lightning, hurricanes, tornadoes, DANA, world climates, climate change, global warming, auroras, rainbow")
FOTO = "atmosfera_iss"
INTRO = ("""
Una capa de gas tan fina que, vista desde la Estación Espacial, parece un halo azul sobre el horizonte. Ella nos da el aire, filtra la radiación, reparte el calor y fabrica el tiempo de cada día. Esta sección explica cómo funciona y cómo la estamos cambiando.
""", """
A layer of gas so thin that, seen from the Space Station, it looks like a blue halo above the horizon. It gives us air, filters radiation, spreads heat around and makes each day's weather. This section explains how it works and how we are changing it.
""")

ATMOSFERA = F(
    ("la-atmosfera", "the-atmosphere"),
    ("La atmósfera", "The atmosphere"),
    ("De qué está hecho el aire, sus cinco capas, la capa de ozono y por qué el cielo es azul.",
     "What air is made of, its five layers, the ozone layer and why the sky is blue."),
    ("atmósfera terrestre, composición del aire, nitrógeno, oxígeno, dióxido de carbono, troposfera, estratosfera, mesosfera, termosfera, exosfera, capa de ozono, agujero de ozono, Protocolo de Montreal, línea de Kármán, por qué el cielo es azul, presión atmosférica",
     "Earth's atmosphere, composition of air, nitrogen, oxygen, carbon dioxide, troposphere, stratosphere, mesosphere, thermosphere, exosphere, ozone layer, ozone hole, Montreal Protocol, Kármán line, why the sky is blue, air pressure"),
    "atmosfera_iss",
    """
La **atmósfera** es la capa de gases que envuelve la Tierra, sujeta por la gravedad. Aunque se extiende cientos de kilómetros, la mitad de todo el aire está por debajo de los 5,5 km de altura, y tres cuartas partes en los primeros 12 km. Si la Tierra fuera un balón de fútbol, la parte de la atmósfera en la que hay tiempo meteorológico sería más fina que una hoja de papel.

## De qué está hecho el aire

| Gas | Proporción |
|---|---|
| Nitrógeno | 78 % |
| Oxígeno | 21 % |
| Argón | 0,93 % |
| Dióxido de carbono | ≈ 0,042 % (unas 425 partes por millón) |
| Vapor de agua | Variable, de casi 0 a 4 % |

El dióxido de carbono es una parte diminuta, pero tiene un papel enorme: es uno de los gases que retienen calor y mantienen la Tierra templada. Sin el **efecto invernadero** natural, la temperatura media sería de unos −18 °C en lugar de 15 °C. El problema actual es que lo estamos [reforzando](@cambio-climatico).

## Las capas

| Capa | Altura | Qué pasa allí |
|---|---|---|
| **Troposfera** | 0 a 8-17 km | Aquí está casi todo el vapor de agua y se forman las nubes y el tiempo. La temperatura baja unos 6,5 °C por kilómetro |
| **Estratosfera** | Hasta 50 km | Contiene la **capa de ozono**. Vuelan los aviones en su parte baja, por encima de las tormentas |
| **Mesosfera** | Hasta 85 km | La capa más fría, hasta −90 °C. Aquí se queman las [estrellas fugaces](@lluvias-de-estrellas) |
| **Termosfera** | Hasta 600 km | Se forman las [auroras](@auroras-y-fenomenos-opticos); orbita la Estación Espacial |
| **Exosfera** | Hasta unos 10.000 km | El aire se va diluyendo hasta mezclarse con el espacio |

Por convenio, el espacio empieza en la **línea de Kármán**, a 100 km de altura.

## La capa de ozono

Entre los 15 y 35 km de altura hay una zona rica en **ozono**, una molécula de tres átomos de oxígeno que absorbe la mayor parte de la radiación ultravioleta del Sol, peligrosa para la vida. En 1985, científicos británicos descubrieron que cada primavera austral se abría un **agujero** sobre la Antártida, causado por los CFC de los aerosoles y los frigoríficos.

La respuesta fue un éxito histórico: el **Protocolo de Montreal** de 1987, firmado por todos los países del mundo, prohibió esos gases. La capa se está recuperando y se espera que vuelva a su estado de 1980 hacia mediados de siglo. Los químicos Mario Molina, Sherwood Rowland y Paul Crutzen, que habían avisado del peligro, ganaron el Nobel en 1995.

## ¿Por qué el cielo es azul?

La luz del Sol contiene todos los colores. Al atravesar el aire, las moléculas de gas desvían mucho más la luz azul, de onda corta, que la roja: es la **dispersión de Rayleigh**. Por eso el azul nos llega desde todas las direcciones del cielo. Al atardecer, la luz cruza mucha más atmósfera, el azul se pierde por el camino y solo llegan los naranjas y rojos. En Marte, con una atmósfera muy distinta, los atardeceres son azules.

## El peso del aire

Aunque no lo notemos, el aire pesa: sobre cada centímetro cuadrado de nuestro cuerpo hay alrededor de **1 kg** de aire. En 1654, el alcalde de Magdeburgo, Otto von Guericke, unió dos semiesferas de cobre y extrajo el aire de su interior: ni dos tiros de ocho caballos lograron separarlas.

> En 2012, el austriaco Felix Baumgartner saltó en paracaídas desde un globo a 39 km de altura, en la estratosfera. Durante la caída libre superó la velocidad del sonido, sin ningún vehículo.
""",
    """
The **atmosphere** is the layer of gases wrapped around the Earth, held in place by gravity. Although it stretches hundreds of kilometres, half of all the air lies below 5.5 km, and three quarters in the first 12 km. If the Earth were a football, the part of the atmosphere where weather happens would be thinner than a sheet of paper.

## What air is made of

| Gas | Share |
|---|---|
| Nitrogen | 78% |
| Oxygen | 21% |
| Argon | 0.93% |
| Carbon dioxide | ≈ 0.042% (about 425 parts per million) |
| Water vapour | Variable, from almost 0 to 4% |

Carbon dioxide is a tiny share, but it plays a huge role: it is one of the gases that trap heat and keep the Earth mild. Without the natural **greenhouse effect**, the average temperature would be about −18 °C instead of 15 °C. Today's problem is that we are [strengthening](@cambio-climatico) it.

## The layers

| Layer | Height | What happens there |
|---|---|---|
| **Troposphere** | 0 to 8–17 km | Almost all the water vapour is here, and clouds and weather form. Temperature falls about 6.5 °C per kilometre |
| **Stratosphere** | Up to 50 km | Holds the **ozone layer**. Planes fly in its lower part, above the storms |
| **Mesosphere** | Up to 85 km | The coldest layer, down to −90 °C. [Shooting stars](@lluvias-de-estrellas) burn up here |
| **Thermosphere** | Up to 600 km | [Auroras](@auroras-y-fenomenos-opticos) form; the Space Station orbits |
| **Exosphere** | Up to about 10,000 km | The air thins out until it merges with space |

By convention, space begins at the **Kármán line**, 100 km up.

## The ozone layer

Between 15 and 35 km up there is a region rich in **ozone**, a molecule of three oxygen atoms that absorbs most of the Sun's ultraviolet radiation, which is harmful to life. In 1985 British scientists discovered that every southern spring a **hole** opened over Antarctica, caused by CFCs from aerosols and refrigerators.

The response was a historic success: the 1987 **Montreal Protocol**, signed by every country in the world, banned those gases. The layer is recovering and is expected to return to its 1980 state around the middle of the century. Chemists Mario Molina, Sherwood Rowland and Paul Crutzen, who had warned of the danger, won the 1995 Nobel Prize.

## Why is the sky blue?

Sunlight contains every colour. As it passes through the air, gas molecules scatter blue light, with its short wavelength, far more than red: this is **Rayleigh scattering**. So blue reaches us from every direction in the sky. At sunset, light crosses much more atmosphere, the blue is lost along the way and only oranges and reds get through. On Mars, with a very different atmosphere, sunsets are blue.

## The weight of air

Although we do not feel it, air has weight: about **1 kg** of it presses on every square centimetre of our body. In 1654 the mayor of Magdeburg, Otto von Guericke, joined two copper hemispheres and pumped the air out from inside: two teams of eight horses could not pull them apart.

> In 2012 the Austrian Felix Baumgartner parachuted from a balloon 39 km up, in the stratosphere. During his free fall he broke the speed of sound, without any vehicle.
""",
    datos=[("Nitrógeno y oxígeno", "Nitrogen and oxygen", "78 % y 21 %", "78% and 21%"),
           ("CO₂ (2025)", "CO₂ (2025)", "≈ 425 ppm", "≈ 425 ppm"),
           ("Mitad del aire", "Half of the air", "Por debajo de 5,5 km", "Below 5.5 km"),
           ("Capa de ozono", "Ozone layer", "15 a 35 km", "15 to 35 km"),
           ("Comienzo del espacio", "Where space begins", "Línea de Kármán, 100 km", "Kármán line, 100 km"),
           ("Temperatura sin efecto invernadero", "Temperature with no greenhouse effect", "≈ −18 °C", "≈ −18 °C")],
    pie=("La atmósfera vista de canto desde la Estación Espacial: una fina franja azul sobre la Tierra al anochecer.",
         "The atmosphere seen edge-on from the Space Station: a thin blue band above the Earth at dusk."),
)

TIEMPO = F(
    ("tiempo-y-nubes", "weather-and-clouds"),
    ("El tiempo y las nubes", "Weather and clouds"),
    ("Cómo se forman las nubes y la lluvia, cómo se predice el tiempo y los récords de calor y frío del planeta y de España.",
     "How clouds and rain form, how the weather is forecast, and heat and cold records for the planet and for Spain."),
    ("tiempo atmosférico, meteorología, nubes, tipos de nubes, cúmulos, cirros, estratos, cumulonimbos, niebla, lluvia, nieve, granizo, previsión del tiempo, AEMET, anticiclón, borrasca, récord de temperatura, ola de calor",
     "weather, meteorology, clouds, types of clouds, cumulus, cirrus, stratus, cumulonimbus, fog, rain, snow, hail, weather forecast, AEMET, anticyclone, low pressure, temperature record, heatwave"),
    "nubes",
    """
El **tiempo** es el estado de la atmósfera en un lugar y un momento concretos: si llueve, hace sol o sopla el viento hoy. El **clima** es el promedio del tiempo durante muchos años. Como dicen los meteorólogos: el clima es lo que esperas; el tiempo, lo que te toca.

## Altas y bajas presiones

El motor del tiempo es el Sol, que calienta la Tierra de forma desigual. El aire caliente sube y deja debajo una zona de **bajas presiones** (borrasca), donde el aire ascendente se enfría y forma nubes y lluvia. El aire frío baja y crea **altas presiones** (anticiclón), con cielos despejados. El viento es el aire que corre de las altas a las bajas presiones. En España, el **anticiclón de las Azores** decide buena parte de nuestros veranos secos.

## Cómo nacen las nubes

Una nube es un enorme conjunto de gotitas de agua o cristales de hielo tan pequeños que flotan. Se forman cuando el aire húmedo sube y se enfría hasta que su vapor se condensa alrededor de partículas de polvo, sal marina o polen. Un cúmulo mediano de buen tiempo puede pesar unas **500 toneladas**, lo mismo que un avión jumbo cargado; flota porque sus gotas son diminutas y están repartidas en kilómetros cúbicos de aire.

## Tipos de nubes

En 1802 el farmacéutico inglés **Luke Howard** les puso nombres latinos que aún usamos:

- **Cirros** («rizo»): nubes altas, finas y blancas, de cristales de hielo. Suelen anunciar un cambio de tiempo.
- **Cúmulos** («montón»): nubes de algodón con base plana. Las de buen tiempo son pequeñas.
- **Estratos** («capa»): mantos grises que cubren el cielo y dan llovizna. La **niebla** es un estrato a ras de suelo.
- **Cumulonimbos**: torres gigantes que pueden superar los 12 km de altura, con cima en forma de yunque. Son las nubes de [tormenta](@tormentas-y-huracanes), con rayos, granizo y chaparrones.

## Lluvia, nieve y granizo

Dentro de la nube, las gotitas chocan y se unen hasta que pesan demasiado y caen. Las gotas de lluvia no tienen forma de lágrima: las pequeñas son esferas y las grandes se aplastan como panecillos de hamburguesa. Si en la nube hace mucho frío, se forman cristales de hielo que caen como **nieve**; cada copo tiene seis brazos, pero no hay dos iguales. El **granizo** nace en las corrientes de los cumulonimbos, que suben y bajan las bolitas de hielo una y otra vez, añadiéndoles capas como a una cebolla.

## Predecir el tiempo

Hoy se predice con superordenadores que resuelven las ecuaciones de la atmósfera a partir de millones de datos de satélites, estaciones, globos sonda, barcos y aviones. Una previsión a 5 días es hoy tan fiable como lo era una a un día en los años ochenta. En España se encarga la **AEMET**, heredera del servicio meteorológico creado en 1887, y en Europa el Centro Europeo de Previsión a Plazo Medio, cuyo modelo es uno de los mejores del mundo.

## Récords de temperatura

| Récord | Valor | Lugar |
|---|---|---|
| Más calor del mundo | 56,7 °C | Valle de la Muerte (EE. UU.), 1913 |
| Más frío del mundo | −89,2 °C | Base Vostok (Antártida), 1983 |
| Más calor de España | 47,6 °C | La Rambla (Córdoba), 14 de agosto de 2021 |
| Más frío de España | −32 °C | Estany Gento (Lleida), 1956 |

> Los primeros partes del tiempo se publicaron en el periódico *The Times* en 1861. Su autor, el almirante Robert FitzRoy, el capitán del barco de Darwin, inventó la palabra *forecast* («pronóstico»). Las burlas cuando fallaba eran tantas que acabó muy amargado.
""",
    """
**Weather** is the state of the atmosphere at a particular place and time: whether it is raining, sunny or windy today. **Climate** is the average of the weather over many years. As meteorologists say: climate is what you expect; weather is what you get.

## Highs and lows

The weather's engine is the Sun, which heats the Earth unevenly. Warm air rises and leaves an area of **low pressure** below it, where the rising air cools and forms clouds and rain. Cold air sinks and creates **high pressure** (an anticyclone), with clear skies. Wind is air flowing from high to low pressure. In Spain the **Azores High** decides much of our dry summers.

## How clouds are born

A cloud is a huge collection of water droplets or ice crystals so small that they float. They form when moist air rises and cools until its vapour condenses around specks of dust, sea salt or pollen. An average fair-weather cumulus can weigh about **500 tonnes**, as much as a loaded jumbo jet; it floats because its droplets are tiny and spread through cubic kilometres of air.

## Types of cloud

In 1802 the English pharmacist **Luke Howard** gave them the Latin names we still use:

- **Cirrus** ("curl"): high, thin white clouds of ice crystals. They often herald a change in the weather.
- **Cumulus** ("heap"): cotton-wool clouds with flat bases. Fair-weather ones are small.
- **Stratus** ("layer"): grey blankets covering the sky and bringing drizzle. **Fog** is stratus at ground level.
- **Cumulonimbus**: giant towers that can top 12 km, with anvil-shaped summits. These are [storm](@tormentas-y-huracanes) clouds, with lightning, hail and downpours.

## Rain, snow and hail

Inside the cloud, droplets collide and merge until they are too heavy and fall. Raindrops are not tear-shaped: small ones are spheres and large ones flatten like hamburger buns. If the cloud is very cold, ice crystals form and fall as **snow**; every flake has six arms, but no two are alike. **Hail** is born in the updraughts of cumulonimbus clouds, which carry the ice pellets up and down again and again, adding layers like an onion.

## Forecasting the weather

Today forecasts are made by supercomputers that solve the equations of the atmosphere using millions of observations from satellites, weather stations, balloons, ships and aircraft. A 5-day forecast is now as reliable as a 1-day forecast was in the 1980s. In Spain the job falls to **AEMET**, heir to the weather service founded in 1887, and in Europe to the European Centre for Medium-Range Weather Forecasts, whose model is one of the best in the world.

## Temperature records

| Record | Value | Place |
|---|---|---|
| Hottest in the world | 56.7 °C | Death Valley (US), 1913 |
| Coldest in the world | −89.2 °C | Vostok Station (Antarctica), 1983 |
| Hottest in Spain | 47.6 °C | La Rambla (Córdoba), 14 August 2021 |
| Coldest in Spain | −32 °C | Estany Gento (Lleida), 1956 |

> The first weather forecasts were published in *The Times* in 1861. Their author, Admiral Robert FitzRoy, captain of Darwin's ship, coined the word *forecast*. The mockery whenever he got it wrong was so great that he became deeply embittered.
""",
    datos=[("Peso de un cúmulo", "Weight of a cumulus", "≈ 500 toneladas", "≈ 500 tonnes"),
           ("Altura de un cumulonimbo", "Height of a cumulonimbus", "Más de 12 km", "Over 12 km"),
           ("Nombres de las nubes", "Cloud names", "Luke Howard, 1802", "Luke Howard, 1802"),
           ("Récord de calor en España", "Spain's heat record", "47,6 °C (La Rambla, 2021)", "47.6 °C (La Rambla, 2021)"),
           ("Récord de frío mundial", "World cold record", "−89,2 °C (Vostok, 1983)", "−89.2 °C (Vostok, 1983)")],
    pie=("Un cumulonimbo, la nube de tormenta, con su característica cima en forma de yunque.",
         "A cumulonimbus, the thunderstorm cloud, with its characteristic anvil-shaped top."),
)

TORMENTAS = F(
    ("tormentas-y-huracanes", "storms-and-hurricanes"),
    ("Tormentas, huracanes y tornados", "Storms, hurricanes and tornadoes"),
    ("Rayos cinco veces más calientes que el Sol, huracanes del tamaño de un país y danas que descargan en horas la lluvia de un año.",
     "Lightning five times hotter than the Sun, hurricanes the size of a country and DANA storms that dump a year's rain in hours."),
    ("tormentas, rayos, relámpagos, truenos, huracanes, tifones, ciclones, escala Saffir-Simpson, tornados, escala Fujita, dana, gota fría, dana de Valencia 2024, granizo, medicanes, relámpago del Catatumbo",
     "storms, lightning, thunder, hurricanes, typhoons, cyclones, Saffir–Simpson scale, tornadoes, Fujita scale, DANA, cut-off low, 2024 Valencia floods, hail, medicanes, Catatumbo lightning"),
    "rayo",
    """
En cada momento hay unas **2.000 tormentas** activas en algún lugar de la Tierra. Son la forma que tiene la atmósfera de liberar energía: el calor y la humedad acumulados cerca del suelo suben con violencia y se descargan en forma de lluvia, viento y electricidad.

## Rayos y truenos

Dentro de un cumulonimbo, las corrientes de aire hacen chocar granizos y cristales de hielo, que se cargan eléctricamente como un globo frotado en el pelo. Cuando la diferencia de carga es enorme, salta una chispa gigante: el **rayo**. Calienta el aire a unos **30.000 °C**, cinco veces más que la superficie del Sol, y el aire se expande de golpe con un estallido: el **trueno**.

Como la luz llega casi al instante y el sonido viaja a unos 340 metros por segundo, si cuentas los segundos entre el relámpago y el trueno y los divides entre tres, sabrás a cuántos kilómetros está la tormenta.

En el mundo caen unos **44 rayos por segundo**. El lugar con más rayos es el **lago de Maracaibo**, en Venezuela: el «relámpago del Catatumbo» ilumina el cielo unas 260 noches al año. El guarda forestal estadounidense Roy Sullivan sobrevivió a **siete** rayos.

## Huracanes, tifones y ciclones

Son el mismo fenómeno con distintos nombres según el océano: **huracán** en el Atlántico y el Pacífico oriental, **tifón** en el Pacífico occidental y **ciclón** en el Índico. Nacen sobre mares tropicales con el agua a más de 26 °C, que les da energía. Pueden medir 500 km de diámetro y tienen en el centro un **ojo** en calma, rodeado por un muro de nubes con los vientos más fuertes.

!foto huracan | Un huracán fotografiado desde la Estación Espacial. Se ve el ojo en el centro de la espiral de nubes.

La **escala Saffir-Simpson** los clasifica de 1 a 5 según el viento: la categoría 5 supera los 252 km/h. El huracán Patricia (2015) alcanzó los 345 km/h, el viento sostenido más fuerte medido. Sus nombres, alternando masculinos y femeninos, se eligen de listas de la Organización Meteorológica Mundial; los de los más destructivos, como Katrina, se retiran para siempre.

En el Mediterráneo se forman a veces tormentas con aspecto de huracán pequeño, los **medicanes**.

## Tornados

Un tornado es una columna de aire que gira con violencia entre una nube de tormenta y el suelo. Mide de decenas a cientos de metros de ancho, pero sus vientos pueden superar los **400 km/h**. Se clasifican con la escala **Fujita mejorada**, de EF0 a EF5. Estados Unidos registra más de 1.000 al año, sobre todo en el llamado «Callejón de los Tornados». En España se producen unas decenas al año, casi siempre débiles, en el litoral mediterráneo, Andalucía occidental y las Baleares.

## Danas y gota fría

Una **dana** (depresión aislada en niveles altos) es una bolsa de aire muy frío en altura que se separa de la corriente general y se queda estancada. En otoño, cuando el Mediterráneo aún está muy caliente, puede provocar lluvias torrenciales: lo que popularmente se llamaba **gota fría**.

El **29 de octubre de 2024**, una dana descargó en pocas horas más de 700 litros por metro cuadrado en algunos puntos de Valencia. Las crecidas de los barrancos, como el del Poyo, arrasaron decenas de municipios de l'Horta Sud y causaron más de 220 víctimas: la mayor catástrofe meteorológica de la historia reciente de España.

## Granizo

Las piedras de granizo más grandes pueden superar los 20 cm y el kilo de peso. En España, en agosto de 2022, una granizada con piedras de más de 10 cm golpeó La Bisbal d'Empordà (Girona).

> Un solo rayo tiene energía suficiente para tostar unas 100.000 rebanadas de pan, pero dura tan poco, unas milésimas de segundo, que no se puede aprovechar para producir electricidad.
""",
    """
At any moment there are about **2,000 thunderstorms** active somewhere on Earth. They are how the atmosphere releases energy: heat and moisture built up near the ground rise violently and discharge as rain, wind and electricity.

## Lightning and thunder

Inside a cumulonimbus, air currents make hailstones and ice crystals collide, and they become electrically charged like a balloon rubbed on your hair. When the difference in charge becomes enormous, a giant spark jumps: **lightning**. It heats the air to about **30,000 °C**, five times hotter than the surface of the Sun, and the air expands suddenly with a bang: **thunder**.

Because light arrives almost instantly and sound travels at about 340 metres per second, if you count the seconds between flash and thunder and divide by three, you get the storm's distance in kilometres.

About **44 lightning flashes strike every second** worldwide. The place with the most lightning is **Lake Maracaibo** in Venezuela: the "Catatumbo lightning" lights up the sky some 260 nights a year. US park ranger Roy Sullivan survived **seven** lightning strikes.

## Hurricanes, typhoons and cyclones

They are the same phenomenon with different names depending on the ocean: **hurricane** in the Atlantic and eastern Pacific, **typhoon** in the western Pacific and **cyclone** in the Indian Ocean. They are born over tropical seas with water above 26 °C, which feeds them energy. They can be 500 km across and have a calm **eye** at the centre, surrounded by a wall of cloud with the strongest winds.

!foto huracan | A hurricane photographed from the Space Station. The eye is visible at the centre of the cloud spiral.

The **Saffir–Simpson scale** rates them from 1 to 5 by wind speed: category 5 exceeds 252 km/h. Hurricane Patricia (2015) reached 345 km/h, the strongest sustained wind ever measured. Their names, alternating male and female, come from World Meteorological Organization lists; those of the most destructive, such as Katrina, are retired for good.

The Mediterranean sometimes spawns storms that look like small hurricanes, called **medicanes**.

## Tornadoes

A tornado is a violently spinning column of air between a thundercloud and the ground. It is tens to hundreds of metres wide, but its winds can exceed **400 km/h**. They are rated on the **Enhanced Fujita scale**, from EF0 to EF5. The United States records more than 1,000 a year, especially in "Tornado Alley". Spain has a few dozen a year, almost always weak, on the Mediterranean coast, in western Andalusia and in the Balearics.

## DANA storms

A **DANA** (the Spanish acronym for an isolated upper-level low) is a pocket of very cold air high up that breaks away from the main airflow and stalls. In autumn, when the Mediterranean is still very warm, it can trigger torrential rain: what used to be popularly called **gota fría** ("cold drop").

On **29 October 2024**, a DANA dumped more than 700 litres per square metre in a few hours on parts of Valencia. Flash floods in ravines such as the Poyo swept through dozens of towns south of the city and killed more than 220 people: the worst weather disaster in Spain's recent history.

## Hail

The largest hailstones can exceed 20 cm and weigh more than a kilo. In Spain, in August 2022, a hailstorm with stones over 10 cm across struck La Bisbal d'Empordà (Girona).

> A single lightning bolt has enough energy to toast about 100,000 slices of bread, but it lasts so briefly, a few thousandths of a second, that it cannot be harnessed to produce electricity.
""",
    datos=[("Tormentas activas", "Active storms", "≈ 2.000 en cada momento", "≈ 2,000 at any time"),
           ("Rayos por segundo", "Lightning per second", "≈ 44", "≈ 44"),
           ("Temperatura de un rayo", "Lightning temperature", "≈ 30.000 °C", "≈ 30,000 °C"),
           ("Viento más fuerte medido", "Strongest wind measured", "345 km/h (huracán Patricia, 2015)", "345 km/h (Hurricane Patricia, 2015)"),
           ("Huracán: temperatura del mar", "Hurricane: sea temperature", "Más de 26 °C", "Above 26 °C"),
           ("Dana de Valencia", "Valencia DANA", "29 de octubre de 2024", "29 October 2024")],
    pie=("Un rayo cae durante una tormenta nocturna. Calienta el aire a unos 30.000 °C en una fracción de segundo.",
         "Lightning strikes during a night storm. It heats the air to about 30,000 °C in a fraction of a second."),
)

CLIMAS = F(
    ("climas-del-mundo", "world-climates"),
    ("Los climas del mundo", "The world's climates"),
    ("Por qué hay estaciones, los grandes tipos de clima de la Tierra, los lugares más lluviosos y secos y la enorme variedad climática de España.",
     "Why there are seasons, the Earth's main climate types, the wettest and driest places, and Spain's remarkable climatic variety."),
    ("climas del mundo, tipos de clima, clasificación de Köppen, clima tropical, clima desértico, clima mediterráneo, clima oceánico, clima continental, clima polar, estaciones del año, inclinación del eje, monzón, clima de España, desierto de Tabernas, lugar más lluvioso",
     "world climates, climate types, Köppen classification, tropical climate, desert climate, Mediterranean climate, oceanic climate, continental climate, polar climate, seasons, axial tilt, monsoon, climate of Spain, Tabernas desert, wettest place"),
    "sabana",
    """
El clima de un lugar depende sobre todo de su **latitud** (cuánta luz solar recibe), de su **altitud**, de la **distancia al mar** y de los **vientos y corrientes** dominantes. Por eso, a la misma distancia del ecuador, Lisboa es templada y Nueva York tiene inviernos helados.

## ¿Por qué hay estaciones?

No es porque la Tierra se acerque o se aleje del Sol: de hecho, estamos más cerca en enero. Las estaciones existen porque el eje de la Tierra está **inclinado 23,4 grados**. En junio, el hemisferio norte se inclina hacia el Sol: los rayos llegan más verticales, los días son más largos y hace calor. En diciembre ocurre al revés. Por eso, cuando en España es verano, en Argentina o Australia es invierno.

## Los grandes tipos de clima

En 1900 el climatólogo **Wladimir Köppen** clasificó los climas según la vegetación que permiten, con un sistema que aún se usa:

| Grupo | Cómo es | Ejemplos |
|---|---|---|
| **Tropical** | Calor todo el año; mucha lluvia o estación seca y húmeda | Amazonia, Congo, India |
| **Seco** | Llueve muy poco; desiertos y estepas | Sahara, Atacama, sureste de España |
| **Templado** | Inviernos suaves; incluye el mediterráneo y el oceánico | Barcelona, Londres, Buenos Aires |
| **Continental** | Inviernos muy fríos y veranos cálidos | Moscú, Chicago, Pekín |
| **Polar** | Frío todo el año; tundra y hielo | Groenlandia, Antártida |

El **clima mediterráneo**, con veranos secos y calurosos e inviernos suaves, solo se da en cinco regiones del mundo: la cuenca mediterránea, California, el centro de Chile, la región del Cabo en Sudáfrica y el suroeste de Australia. Todas tienen vinos y paisajes parecidos.

## El monzón

En el sur de Asia, el viento cambia de dirección según la estación. En verano sopla desde el océano Índico cargado de humedad y descarga lluvias torrenciales: es el **monzón**, del que depende la agricultura, y la comida, de más de mil millones de personas. **Mawsynram**, en el noreste de la India, recibe de media unos 11.800 litros por metro cuadrado al año, unas veinte veces más que Madrid.

## Lo más seco

En partes del **desierto de Atacama**, en Chile, hay estaciones meteorológicas que nunca han registrado lluvia. Sus suelos son tan parecidos a los de Marte que la NASA prueba allí sus vehículos. Y en los **valles secos** de la Antártida no ha llovido ni nevado en miles de años.

## España, un continente en miniatura

Pocas zonas de Europa tienen tanta variedad climática:

- **Oceánico** en Galicia, Asturias, Cantabria y el País Vasco: verde, lluvioso y templado.
- **Mediterráneo** en la costa este y el sur, con matices: más húmedo en Cataluña, más seco en Murcia y Almería.
- **Mediterráneo continentalizado** en las mesetas: inviernos fríos y veranos calurosos.
- **Semiárido** en el sureste: el **desierto de Tabernas** (Almería) es uno de los pocos desiertos de Europa, escenario de cientos de westerns.
- **De montaña** en los Pirineos, Sierra Nevada y otras cordilleras.
- **Subtropical** en las Canarias, con temperaturas suaves todo el año.

> El clima de una ciudad cambia incluso de un barrio a otro. Las ciudades son «islas de calor»: el asfalto y el hormigón acumulan calor de día y lo sueltan de noche, de modo que el centro de una gran ciudad puede estar varios grados más caliente que el campo que la rodea.
""",
    """
A place's climate depends mainly on its **latitude** (how much sunlight it gets), its **altitude**, its **distance from the sea** and the prevailing **winds and currents**. That is why, at the same distance from the equator, Lisbon is mild while New York has freezing winters.

## Why are there seasons?

It is not because the Earth moves closer to or farther from the Sun: in fact we are closest in January. Seasons exist because the Earth's axis is **tilted 23.4 degrees**. In June the northern hemisphere leans towards the Sun: the rays arrive more steeply, the days are longer and it is hot. In December the reverse happens. That is why, when it is summer in Spain, it is winter in Argentina or Australia.

## The main climate types

In 1900 the climatologist **Wladimir Köppen** classified climates by the vegetation they allow, with a system still in use:

| Group | What it is like | Examples |
|---|---|---|
| **Tropical** | Hot all year; lots of rain or a dry and a wet season | Amazonia, Congo, India |
| **Dry** | Very little rain; deserts and steppes | Sahara, Atacama, south-east Spain |
| **Temperate** | Mild winters; includes Mediterranean and oceanic | Barcelona, London, Buenos Aires |
| **Continental** | Very cold winters and warm summers | Moscow, Chicago, Beijing |
| **Polar** | Cold all year; tundra and ice | Greenland, Antarctica |

The **Mediterranean climate**, with hot, dry summers and mild winters, is found in only five regions of the world: the Mediterranean basin, California, central Chile, South Africa's Cape region and south-western Australia. All have similar wines and landscapes.

## The monsoon

In South Asia the wind changes direction with the seasons. In summer it blows in from the Indian Ocean laden with moisture and unleashes torrential rain: this is the **monsoon**, on which the farming, and the food, of more than a billion people depends. **Mawsynram**, in north-east India, receives an average of about 11,800 litres per square metre a year, some twenty times more than Madrid.

## The driest places

In parts of Chile's **Atacama Desert** there are weather stations that have never recorded rain. Its soils are so like those of Mars that NASA tests its rovers there. And in Antarctica's **dry valleys** it has not rained or snowed for thousands of years.

## Spain, a continent in miniature

Few parts of Europe have so much climatic variety:

- **Oceanic** in Galicia, Asturias, Cantabria and the Basque Country: green, rainy and mild.
- **Mediterranean** on the east and south coasts, with nuances: wetter in Catalonia, drier in Murcia and Almería.
- **Continental Mediterranean** on the central plateaus: cold winters and hot summers.
- **Semi-arid** in the south-east: the **Tabernas Desert** (Almería) is one of Europe's few deserts and the setting for hundreds of westerns.
- **Mountain** in the Pyrenees, Sierra Nevada and other ranges.
- **Subtropical** in the Canary Islands, mild all year round.

> Climate changes even from one neighbourhood to another. Cities are "heat islands": asphalt and concrete soak up heat by day and release it at night, so the centre of a big city can be several degrees warmer than the surrounding countryside.
""",
    datos=[("Inclinación del eje", "Axial tilt", "23,4°", "23.4°"),
           ("Grupos de Köppen", "Köppen groups", "Tropical, seco, templado, continental y polar", "Tropical, dry, temperate, continental and polar"),
           ("Regiones mediterráneas", "Mediterranean regions", "5 en todo el mundo", "5 worldwide"),
           ("Lugar más lluvioso", "Wettest place", "Mawsynram (India), ≈ 11.800 mm al año", "Mawsynram (India), ≈ 11,800 mm a year"),
           ("Desierto europeo", "European desert", "Tabernas (Almería)", "Tabernas (Almería)")],
    pie=("La sabana africana, típica del clima tropical con una estación seca y otra lluviosa.",
         "The African savanna, typical of a tropical climate with one dry and one rainy season."),
)

CAMBIO = F(
    ("cambio-climatico", "climate-change"),
    ("El cambio climático", "Climate change"),
    ("La Tierra se ha calentado más de 1,2 °C desde la era preindustrial por los gases que emitimos. Las pruebas, las consecuencias y las soluciones.",
     "The Earth has warmed by more than 1.2 °C since pre-industrial times because of the gases we emit. The evidence, the consequences and the solutions."),
    ("cambio climático, calentamiento global, efecto invernadero, dióxido de carbono, gases de efecto invernadero, curva de Keeling, IPCC, Acuerdo de París, 1,5 grados, subida del nivel del mar, olas de calor, cambio climático en España, energías renovables, Eunice Foote",
     "climate change, global warming, greenhouse effect, carbon dioxide, greenhouse gases, Keeling curve, IPCC, Paris Agreement, 1.5 degrees, sea-level rise, heatwaves, climate change in Spain, renewable energy, Eunice Foote"),
    "deshielo",
    """
El clima de la Tierra siempre ha cambiado, pero lo ha hecho a lo largo de miles o millones de años. Lo que ocurre ahora es distinto: la temperatura media del planeta ha subido **más de 1,2 °C** desde finales del siglo XIX, casi todo en los últimos 50 años, y la causa principal somos nosotros.

## Una idea con más de siglo y medio

- En 1856 la científica estadounidense **Eunice Foote** demostró con unos tubos de vidrio al sol que el aire con dióxido de carbono se calentaba más que el aire normal, y sugirió que más CO₂ calentaría el planeta.
- En 1859 el irlandés **John Tyndall** midió qué gases absorben el calor.
- En 1896 el sueco **Svante Arrhenius** calculó cuánto se calentaría la Tierra si se duplicara el CO₂ quemando carbón. Su resultado no está lejos de los cálculos actuales.
- Desde 1958, **Charles Keeling** mide el CO₂ del aire en el volcán Mauna Loa, en Hawái. Su gráfica, la **curva de Keeling**, sube año tras año: de unas 315 partes por millón entonces a unas **425** hoy. Antes de la Revolución Industrial eran unas 280.

## Cómo funciona

El Sol calienta la superficie de la Tierra, que devuelve parte de esa energía en forma de calor. Algunos gases de la [atmósfera](@la-atmosfera), como el **dióxido de carbono**, el **metano** y el vapor de agua, atrapan parte de ese calor, como el cristal de un invernadero. Al quemar carbón, petróleo y gas, talar bosques y criar enormes cantidades de ganado, hemos añadido más de esos gases y reforzado el efecto.

## Las pruebas

- **Temperatura**: los diez años más cálidos registrados son todos de la última década. **2024** fue el año más caluroso desde que hay mediciones y el primero en superar en todo el año 1,5 °C sobre el nivel preindustrial.
- **Hielo**: el Ártico ha perdido alrededor del 40 % de su hielo de verano desde 1979, y casi todos los glaciares de montaña retroceden, incluidos los de los [Pirineos](@glaciares-y-hielo).
- **Mar**: el nivel medio ha subido más de 20 cm desde 1900 y ahora sube unos 4 mm al año. Los océanos están más calientes y más ácidos.
- **Extremos**: las olas de calor son más frecuentes e intensas, y las lluvias torrenciales, más fuertes.

## Lo que dice la ciencia

El **IPCC**, el grupo de científicos de la ONU creado en 1988 que revisa miles de estudios, concluyó en 2021 que es «**inequívoco**» que la influencia humana ha calentado la atmósfera, los océanos y la tierra. En el **Acuerdo de París** de 2015, casi todos los países del mundo se comprometieron a limitar el calentamiento muy por debajo de 2 °C y, a ser posible, a 1,5 °C.

## España, en primera línea

España y el Mediterráneo se calientan más deprisa que la media mundial. Según la AEMET, el verano dura ahora unas cinco semanas más que a principios de los años ochenta, y las noches tropicales, en las que no se baja de 20 °C, se han multiplicado. Aumenta el riesgo de sequías, incendios y desertificación en el sur y el sureste, y el Mediterráneo bate récords de temperatura que alimentan danas más intensas.

## Soluciones

La clave es dejar de emitir gases de efecto invernadero: producir electricidad con **energías renovables**, electrificar el transporte y la calefacción, ahorrar energía, proteger y recuperar bosques y suelos y cambiar algunos hábitos de consumo. España es uno de los países donde la transición avanza más deprisa: en 2024 las renovables, sobre todo el viento y el sol, produjeron más de la mitad de su electricidad. Además, hay que [adaptarse](@cuidar-el-planeta) a los cambios que ya son inevitables.

> El agujero de la capa de ozono demostró que el mundo puede ponerse de acuerdo para resolver un problema ambiental global. El Protocolo de Montreal, además, ha evitado también una parte del calentamiento, porque los gases que prohibió eran potentes gases de efecto invernadero.
""",
    """
The Earth's climate has always changed, but over thousands or millions of years. What is happening now is different: the planet's average temperature has risen by **more than 1.2 °C** since the late 19th century, almost all of it in the last 50 years, and the main cause is us.

## An idea more than 150 years old

- In 1856 the American scientist **Eunice Foote** showed, with glass tubes in the sun, that air containing carbon dioxide warmed more than ordinary air, and suggested that more CO₂ would warm the planet.
- In 1859 the Irishman **John Tyndall** measured which gases absorb heat.
- In 1896 the Swede **Svante Arrhenius** calculated how much the Earth would warm if burning coal doubled the CO₂. His result is not far from today's estimates.
- Since 1958 **Charles Keeling** has measured CO₂ in the air on Mauna Loa volcano in Hawaii. His graph, the **Keeling curve**, rises year after year: from about 315 parts per million then to about **425** today. Before the Industrial Revolution it was about 280.

## How it works

The Sun warms the Earth's surface, which sends some of that energy back out as heat. Some gases in the [atmosphere](@la-atmosfera), such as **carbon dioxide**, **methane** and water vapour, trap part of that heat, like the glass of a greenhouse. By burning coal, oil and gas, clearing forests and raising vast numbers of livestock, we have added more of these gases and strengthened the effect.

## The evidence

- **Temperature**: the ten warmest years on record are all from the last decade. **2024** was the hottest year since measurements began and the first full year more than 1.5 °C above pre-industrial levels.
- **Ice**: the Arctic has lost around 40% of its summer ice since 1979, and almost all mountain glaciers are retreating, including those in the [Pyrenees](@glaciares-y-hielo).
- **Sea**: average sea level has risen more than 20 cm since 1900 and now rises about 4 mm a year. The oceans are warmer and more acidic.
- **Extremes**: heatwaves are more frequent and intense, and torrential downpours heavier.

## What science says

The **IPCC**, the UN group of scientists set up in 1988 to review thousands of studies, concluded in 2021 that it is "**unequivocal**" that human influence has warmed the atmosphere, oceans and land. In the 2015 **Paris Agreement**, almost every country in the world committed to limiting warming to well below 2 °C and, if possible, to 1.5 °C.

## Spain on the front line

Spain and the Mediterranean are warming faster than the global average. According to AEMET, summer now lasts about five weeks longer than in the early 1980s, and tropical nights, when the temperature stays above 20 °C, have multiplied. The risk of drought, wildfires and desertification is growing in the south and south-east, and record Mediterranean sea temperatures are fuelling more intense DANA storms.

## Solutions

The key is to stop emitting greenhouse gases: generate electricity from **renewable energy**, electrify transport and heating, save energy, protect and restore forests and soils, and change some consumer habits. Spain is one of the countries where the transition is moving fastest: in 2024 renewables, mainly wind and solar, produced more than half its electricity. We also need to [adapt](@cuidar-el-planeta) to changes that are already unavoidable.

> The ozone hole showed that the world can agree to solve a global environmental problem. The Montreal Protocol has also prevented some warming, because the gases it banned were powerful greenhouse gases.
""",
    datos=[("Calentamiento desde 1850-1900", "Warming since 1850–1900", "Más de 1,2 °C", "More than 1.2 °C"),
           ("Año más cálido", "Hottest year", "2024", "2024"),
           ("CO₂ preindustrial y actual", "CO₂ pre-industrial and now", "280 → 425 ppm", "280 → 425 ppm"),
           ("Subida del mar desde 1900", "Sea-level rise since 1900", "Más de 20 cm", "More than 20 cm"),
           ("Acuerdo de París", "Paris Agreement", "2015: muy por debajo de 2 °C", "2015: well below 2 °C"),
           ("Renovables en España (2024)", "Renewables in Spain (2024)", "Más de la mitad de la electricidad", "More than half of electricity")],
    pie=("Hielo desprendido de los glaciares de Groenlandia flotando en un fiordo. Groenlandia pierde cientos de miles de millones de toneladas de hielo al año.",
         "Ice broken off Greenland's glaciers floating in a fjord. Greenland loses hundreds of billions of tonnes of ice every year."),
)

LUCES = F(
    ("auroras-y-fenomenos-opticos", "auroras-and-optical-phenomena"),
    ("Auroras, arcoíris y luces del cielo", "Auroras, rainbows and lights in the sky"),
    ("Auroras boreales, arcoíris dobles, halos, rayo verde y espejismos: la física detrás de los espectáculos de luz de la atmósfera.",
     "Northern lights, double rainbows, halos, the green flash and mirages: the physics behind the atmosphere's light shows."),
    ("aurora boreal, aurora austral, tormenta geomagnética, auroras en España 2024, arcoíris, arcoíris doble, halo solar, parhelios, rayo verde, espejismo, fata morgana, nubes noctilucentes, fuego de San Telmo, espectro de Brocken",
     "aurora borealis, northern lights, aurora australis, geomagnetic storm, auroras in Spain 2024, rainbow, double rainbow, solar halo, sundogs, green flash, mirage, fata morgana, noctilucent clouds, St Elmo's fire, Brocken spectre"),
    "aurora",
    """
La atmósfera no solo fabrica nubes y lluvia: también es un gigantesco laboratorio de luz. Gotas de agua, cristales de hielo, capas de aire a distinta temperatura y partículas que llegan del Sol crean algunos de los espectáculos más bellos de la naturaleza.

## Auroras

El Sol lanza constantemente partículas cargadas, el **viento solar**. El [campo magnético](@estructura-de-la-tierra) de la Tierra las desvía, pero cerca de los polos algunas se cuelan y chocan con los gases de la atmósfera a entre 100 y 300 km de altura, que se iluminan como el gas de un tubo fluorescente. Son las **auroras**: boreales en el norte y australes en el sur.

- El **verde**, el color más común, lo produce el oxígeno a unos 100-250 km.
- El **rojo** viene del oxígeno a más altura.
- Los **azules y violetas**, del nitrógeno.

Normalmente se ven en un anillo alrededor de los polos: Noruega, Islandia, Finlandia, Canadá o Alaska. Pero cuando el Sol lanza una gran eyección de masa coronal, las auroras bajan hacia el ecuador. El **10 y 11 de mayo de 2024**, la mayor tormenta geomagnética en veinte años tiñó de rosa y violeta el cielo de toda España, y en octubre de ese año se repitió. Muchas cámaras de móvil las captaron mejor que el ojo.

## El arcoíris

Aparece cuando hay sol a tu espalda y lluvia delante. Cada gota actúa como un prisma: la luz entra, se refleja en el fondo de la gota y sale separada en colores, porque cada color se desvía un ángulo un poco distinto. El arco siempre se forma a **42 grados** del punto justo opuesto al Sol, por eso nunca se puede llegar a su pie: se mueve contigo. Cada persona ve su propio arcoíris.

A veces aparece un **arcoíris doble**: el segundo arco es más débil y tiene los colores al revés, porque la luz se ha reflejado dos veces dentro de las gotas. La franja oscura entre los dos se llama **banda de Alejandro**. Desde un avión se puede ver el arcoíris como un círculo completo.

## Halos y falsos soles

Cuando hay nubes altas de cristales de hielo, como los cirros, la luz del Sol o de la Luna se desvía y forma un **halo**: un anillo a 22 grados alrededor del astro. A veces aparecen a los lados dos manchas brillantes, los **parhelios** o «perros del sol», que parecen soles falsos.

## El rayo verde

Justo cuando el último borde del Sol desaparece bajo un horizonte despejado, sobre todo en el mar, a veces destella durante uno o dos segundos un punto **verde**. Lo produce la atmósfera, que actúa como un prisma y separa los colores. Julio Verne le dedicó una novela, *El rayo verde* (1882).

## Espejismos

Cuando hay capas de aire a temperaturas muy distintas, la luz se curva. En una carretera muy caliente, parece que hay charcos de agua: es el reflejo del cielo, un **espejismo inferior**. Sobre el mar frío, a veces los barcos o las costas lejanas aparecen flotando o estirados como torres: es la **fata morgana**, que quizá explica leyendas como la del Holandés Errante.

## Otras rarezas

- **Nubes noctilucentes**: nubes de hielo en la mesosfera, a 80 km, que brillan en azul eléctrico después de la puesta de sol en las noches de verano.
- **Fuego de San Telmo**: un resplandor azulado en los mástiles de los barcos o las alas de los aviones durante las tormentas, causado por la electricidad del aire. Los marineros lo veían como protección de su patrón.
- **Espectro de Brocken**: la sombra gigante de un montañero proyectada sobre la niebla, rodeada de un halo de colores.

> Las auroras también existen en otros planetas. El telescopio Hubble y la sonda Juno han fotografiado auroras en Júpiter cientos de veces más energéticas que las de la Tierra, y también se han visto en Saturno, Urano y Marte.
""",
    """
The atmosphere does not just make clouds and rain: it is also a giant laboratory of light. Water droplets, ice crystals, layers of air at different temperatures and particles from the Sun create some of nature's most beautiful displays.

## Auroras

The Sun constantly sends out charged particles, the **solar wind**. The Earth's [magnetic field](@estructura-de-la-tierra) deflects them, but near the poles some slip through and collide with gases in the atmosphere 100 to 300 km up, which glow like the gas in a fluorescent tube. These are the **auroras**: the northern lights in the north and the southern lights in the south.

- **Green**, the most common colour, comes from oxygen at around 100–250 km.
- **Red** comes from oxygen higher up.
- **Blues and violets** come from nitrogen.

Normally they are seen in a ring around the poles: Norway, Iceland, Finland, Canada or Alaska. But when the Sun hurls out a big coronal mass ejection, auroras spread towards the equator. On **10 and 11 May 2024**, the strongest geomagnetic storm in twenty years painted the sky pink and violet across the whole of Spain, and it happened again that October. Many phone cameras captured them better than the eye.

## The rainbow

It appears when the sun is behind you and rain in front. Each drop acts like a prism: light enters, reflects off the back of the drop and comes out split into colours, because each colour is bent at a slightly different angle. The arc always forms at **42 degrees** from the point directly opposite the Sun, which is why you can never reach its end: it moves with you. Everyone sees their own rainbow.

Sometimes a **double rainbow** appears: the second arc is fainter and has its colours reversed, because the light has reflected twice inside the drops. The dark band between them is called **Alexander's band**. From a plane you can see a rainbow as a full circle.

## Halos and false suns

When there are high clouds of ice crystals, such as cirrus, light from the Sun or Moon is bent into a **halo**: a ring 22 degrees around it. Sometimes two bright spots appear on either side, **sundogs**, which look like false suns.

## The green flash

Just as the last sliver of the Sun disappears below a clear horizon, especially at sea, a **green** spot sometimes flashes for a second or two. It is produced by the atmosphere acting as a prism and separating the colours. Jules Verne devoted a novel to it, *The Green Ray* (1882).

## Mirages

When there are layers of air at very different temperatures, light bends. On a very hot road there seem to be puddles of water: it is a reflection of the sky, an **inferior mirage**. Over cold seas, distant ships or coasts sometimes appear to float or stretch into towers: this is the **fata morgana**, which may explain legends such as the Flying Dutchman.

## Other oddities

- **Noctilucent clouds**: ice clouds in the mesosphere, 80 km up, glowing electric blue after sunset on summer nights.
- **St Elmo's fire**: a bluish glow on ships' masts or aircraft wings during storms, caused by electricity in the air. Sailors saw it as a sign of their patron saint's protection.
- **Brocken spectre**: a climber's giant shadow cast onto fog, surrounded by a halo of colours.

> Auroras exist on other planets too. The Hubble telescope and the Juno probe have photographed auroras on Jupiter hundreds of times more energetic than Earth's, and they have also been seen on Saturn, Uranus and Mars.
""",
    datos=[("Altura de las auroras", "Height of auroras", "100 a 300 km", "100 to 300 km"),
           ("Color más común", "Most common colour", "Verde (oxígeno)", "Green (oxygen)"),
           ("Auroras vistas en España", "Auroras seen from Spain", "Mayo y octubre de 2024", "May and October 2024"),
           ("Ángulo del arcoíris", "Rainbow angle", "42°", "42°"),
           ("Halo solar", "Solar halo", "22° alrededor del Sol", "22° around the Sun")],
    pie=("Aurora boreal sobre un paisaje nevado. Los colores dependen del gas que se ilumina y de su altura.",
         "Northern lights over a snowy landscape. The colours depend on which gas is glowing and at what height."),
)

FICHAS = [ATMOSFERA, TIEMPO, TORMENTAS, CLIMAS, CAMBIO, LUCES]
