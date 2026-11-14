from universo import F

SLUG = ("estrellas", "stars")
TITULO = ("Estrellas", "Stars")
RESUMEN = ("Cómo nacen, brillan y mueren las estrellas: nebulosas, gigantes rojas, supernovas, estrellas de neutrones, agujeros negros y planetas en otros soles.",
           "How stars are born, shine and die: nebulae, red giants, supernovae, neutron stars, black holes and planets around other suns.")
CLAVES = ("estrellas, vida de las estrellas, tipos de estrellas, nebulosas, supernovas, agujeros negros, estrellas de neutrones, púlsares, exoplanetas, enana blanca, gigante roja",
          "stars, life cycle of stars, types of stars, nebulae, supernovae, black holes, neutron stars, pulsars, exoplanets, white dwarf, red giant")
FOTO = "acantilados_carina"
INTRO = ("""
Cada estrella del cielo es un sol, muchos de ellos mayores y más brillantes que el nuestro. Nacen en nubes de gas, pasan millones o billones de años fusionando átomos y, al morir, siembran el espacio con los elementos que forman los planetas y los seres vivos. Somos, literalmente, polvo de estrellas.
""", """
Every star in the sky is a sun, many of them larger and brighter than ours. They are born in clouds of gas, spend millions or trillions of years fusing atoms and, when they die, seed space with the elements that make up planets and living things. We are, quite literally, stardust.
""")

VIDA = F(
    ("vida-de-las-estrellas", "life-of-stars"),
    ("La vida de las estrellas", "The life of stars"),
    ("Del nacimiento en una nebulosa a la muerte como enana blanca, estrella de neutrones o agujero negro: todo depende de la masa.",
     "From birth in a nebula to death as a white dwarf, neutron star or black hole: it all depends on mass."),
    ("vida de una estrella, ciclo de vida estelar, nacimiento de una estrella, protoestrella, secuencia principal, gigante roja, enana blanca, nebulosa planetaria, supernova, Próxima Centauri, polvo de estrellas, nucleosíntesis",
     "life cycle of a star, stellar evolution, star birth, protostar, main sequence, red giant, white dwarf, planetary nebula, supernova, Proxima Centauri, stardust, nucleosynthesis"),
    "pilares",
    """
Las estrellas no son eternas. Nacen, viven y mueren, aunque sus vidas se miden en millones o miles de millones de años. Lo que decide todo su destino es una sola cosa: **la masa** con la que nacen.

## El nacimiento

Las estrellas nacen dentro de grandes nubes frías de gas y polvo, las [nebulosas](@nebulosas). Cuando una región de la nube se vuelve lo bastante densa, quizá empujada por la explosión de una supernova cercana, empieza a contraerse por su propia gravedad. Al comprimirse se calienta y forma una **protoestrella**, rodeada de un disco de material del que pueden nacer planetas.

Cuando el centro alcanza unos 10 millones de grados, el hidrógeno empieza a fusionarse en helio. La energía liberada frena el colapso: ha nacido una estrella.

!foto acantilados_carina | Los «acantilados cósmicos» de la nebulosa de Carina, un vivero de estrellas, fotografiados por el telescopio James Webb.

## La vida adulta

Durante el 90 % de su vida, una estrella está en la llamada **secuencia principal**: fusiona hidrógeno en su núcleo y mantiene un equilibrio entre la gravedad, que tira hacia dentro, y la presión del gas caliente, que empuja hacia fuera. El Sol está en esta fase desde hace 4.600 millones de años.

Lo curioso es que las estrellas grandes viven menos. Tienen más combustible, pero lo queman a un ritmo enormemente mayor:

| Masa (Sol = 1) | Vida aproximada | Final |
|---|---|---|
| 0,1 (enana roja) | Billones de años | Enana blanca lentísima |
| 1 (como el Sol) | 10.000 millones de años | Gigante roja y enana blanca |
| 10 | 20 millones de años | Supernova y estrella de neutrones |
| 40 o más | Pocos millones de años | Supernova y agujero negro |

## La muerte de una estrella como el Sol

Cuando se acaba el hidrógeno del núcleo, la estrella se hincha y se convierte en una **gigante roja**, cientos de veces más grande. Después expulsa sus capas exteriores formando una preciosa **nebulosa planetaria**, y su núcleo queda al descubierto como una **enana blanca**: una esfera del tamaño de la Tierra pero con la masa de medio Sol. Una cucharadita de su materia pesaría varias toneladas. Se irá enfriando poco a poco durante billones de años.

!foto ojo_gato | La nebulosa Ojo de Gato, los restos de una estrella como el Sol que expulsó sus capas exteriores.

## La muerte de las estrellas gigantes

Las estrellas de más de unas ocho masas solares fabrican elementos cada vez más pesados en su núcleo: carbono, oxígeno, neón, silicio... hasta llegar al **hierro**. El hierro no libera energía al fusionarse, así que el núcleo se hunde de golpe en menos de un segundo y la estrella estalla en una [supernova](@supernovas). Lo que queda es una [estrella de neutrones](@estrellas-de-neutrones) o, si la masa es suficiente, un [agujero negro](@agujeros-negros).

## Somos polvo de estrellas

Casi todo el carbono de tu cuerpo, el oxígeno que respiras, el calcio de tus huesos y el hierro de tu sangre se fabricaron dentro de estrellas que murieron antes de que naciera el Sol. Los elementos más pesados, como el oro o el uranio, se forman en las explosiones de supernovas y en los choques de estrellas de neutrones.

> La estrella más cercana al Sol, **Próxima Centauri**, es una enana roja tan pequeña y tenue que no se ve a simple vista. Vivirá unos 4 billones de años, cientos de veces más que el Sol.
""",
    """
Stars are not eternal. They are born, live and die, although their lives are measured in millions or billions of years. One thing decides their entire fate: the **mass** they are born with.

## Birth

Stars are born inside large, cold clouds of gas and dust, the [nebulae](@nebulosas). When a region of the cloud becomes dense enough, perhaps pushed by the blast of a nearby supernova, it starts to collapse under its own gravity. As it shrinks it heats up and forms a **protostar**, surrounded by a disc of material from which planets may form.

When the centre reaches about 10 million degrees, hydrogen starts fusing into helium. The energy released halts the collapse: a star is born.

!foto acantilados_carina | The "Cosmic Cliffs" of the Carina Nebula, a stellar nursery, photographed by the James Webb telescope.

## Adult life

For 90% of its life a star is on the so-called **main sequence**: it fuses hydrogen in its core and holds a balance between gravity, pulling inwards, and the pressure of hot gas, pushing outwards. The Sun has been in this phase for 4.6 billion years.

The odd thing is that big stars live shorter lives. They have more fuel, but burn it at a vastly greater rate:

| Mass (Sun = 1) | Approximate lifetime | Ending |
|---|---|---|
| 0.1 (red dwarf) | Trillions of years | Very slow white dwarf |
| 1 (like the Sun) | 10 billion years | Red giant and white dwarf |
| 10 | 20 million years | Supernova and neutron star |
| 40 or more | A few million years | Supernova and black hole |

## The death of a Sun-like star

When the hydrogen in the core runs out, the star swells into a **red giant**, hundreds of times larger. It then sheds its outer layers into a beautiful **planetary nebula**, and its core is left exposed as a **white dwarf**: a sphere the size of Earth with the mass of half a Sun. A teaspoon of its matter would weigh several tonnes. It will slowly cool for trillions of years.

!foto ojo_gato | The Cat's Eye Nebula, the remains of a Sun-like star that threw off its outer layers.

## The death of giant stars

Stars of more than about eight solar masses make heavier and heavier elements in their cores: carbon, oxygen, neon, silicon... all the way to **iron**. Iron releases no energy when it fuses, so the core collapses in less than a second and the star explodes as a [supernova](@supernovas). What remains is a [neutron star](@estrellas-de-neutrones) or, if there is enough mass, a [black hole](@agujeros-negros).

## We are stardust

Almost all the carbon in your body, the oxygen you breathe, the calcium in your bones and the iron in your blood were made inside stars that died before the Sun was born. The heaviest elements, such as gold or uranium, are forged in supernova explosions and in collisions between neutron stars.

> The nearest star to the Sun, **Proxima Centauri**, is a red dwarf so small and faint that it cannot be seen with the naked eye. It will live about 4 trillion years, hundreds of times longer than the Sun.
""",
    datos=[("Estrellas en la Vía Láctea", "Stars in the Milky Way", "100.000 a 400.000 millones", "100 to 400 billion"),
           ("Estrella más cercana", "Nearest star", "Próxima Centauri, 4,24 años luz", "Proxima Centauri, 4.24 light years"),
           ("Temperatura para encender la fusión", "Temperature to ignite fusion", "≈ 10 millones de °C", "≈ 10 million °C"),
           ("Masa mínima de una estrella", "Minimum mass of a star", "≈ 0,08 masas solares", "≈ 0.08 solar masses"),
           ("Vida del Sol", "Sun's lifespan", "≈ 10.000 millones de años", "≈ 10 billion years")],
    pie=("Los «Pilares de la Creación», en la nebulosa del Águila: columnas de gas donde nacen estrellas (telescopio Hubble).",
         "The \"Pillars of Creation\" in the Eagle Nebula: columns of gas where stars are born (Hubble telescope)."),
)

TIPOS = F(
    ("tipos-de-estrellas", "types-of-stars"),
    ("Tipos de estrellas y sus colores", "Types of stars and their colours"),
    ("Azules, blancas, amarillas, naranjas y rojas: el color de una estrella revela su temperatura, y su brillo, su tamaño y su edad.",
     "Blue, white, yellow, orange and red: a star's colour reveals its temperature, and its brightness, its size and age."),
    ("tipos de estrellas, color de las estrellas, clasificación estelar, OBAFGKM, diagrama de Hertzsprung-Russell, enana roja, gigante azul, supergigante roja, Betelgeuse, Rigel, Sirio, estrellas dobles, magnitud",
     "types of stars, star colours, stellar classification, OBAFGKM, Hertzsprung-Russell diagram, red dwarf, blue giant, red supergiant, Betelgeuse, Rigel, Sirius, binary stars, magnitude"),
    "pleyades",
    """
A simple vista casi todas las estrellas parecen puntos blancos, pero si te fijas bien verás que **Betelgeuse** es anaranjada y **Rigel**, en la misma constelación de Orión, es azulada. El color de una estrella es como un termómetro.

## El color indica la temperatura

Al contrario que en los grifos, en las estrellas el **azul es lo más caliente** y el **rojo, lo más frío**. Los astrónomos las clasifican con las letras **O, B, A, F, G, K y M**, de más caliente a más fría. Una forma clásica de recordarlas en inglés es *«Oh Be A Fine Girl/Guy, Kiss Me»*.

| Tipo | Color | Temperatura de la superficie | Ejemplo |
|---|---|---|---|
| O | Azul | Más de 30.000 °C | Estrellas de Orión (Mintaka) |
| B | Azul blanquecino | 10.000 a 30.000 °C | Rigel, Spica |
| A | Blanco | 7.500 a 10.000 °C | Sirio, Vega |
| F | Blanco amarillento | 6.000 a 7.500 °C | Proción, la Polar |
| G | Amarillo | 5.200 a 6.000 °C | El Sol, Alfa Centauri A |
| K | Naranja | 3.700 a 5.200 °C | Arturo, Aldebarán |
| M | Rojo | Menos de 3.700 °C | Betelgeuse, Próxima Centauri |

## Enanas, gigantes y supergigantes

Además del color, las estrellas se distinguen por su tamaño y brillo:

- **Enanas rojas**: las más pequeñas y abundantes. Unas tres de cada cuatro estrellas de la galaxia son enanas rojas, aunque no se ve ninguna a simple vista.
- **Estrellas como el Sol**: de tamaño medio, en la mitad de su vida.
- **Gigantes rojas**: estrellas viejas que se han hinchado, como Arturo o Aldebarán.
- **Supergigantes**: las mayores de todas. Betelgeuse es tan grande que, puesta en lugar del Sol, llegaría casi hasta Júpiter.
- **Enanas blancas**: los núcleos apagados de estrellas muertas, como la compañera de Sirio.

!foto sirio | Sirio A, la estrella más brillante del cielo nocturno, y su diminuta compañera Sirio B, una enana blanca (abajo a la izquierda), vistas por el Hubble.

## El diagrama de Hertzsprung-Russell

A principios del siglo XX, el danés Ejnar Hertzsprung y el estadounidense Henry Norris Russell tuvieron la misma idea: dibujar las estrellas en un gráfico según su temperatura y su brillo real. Para sorpresa de todos, no aparecían al azar, sino agrupadas en franjas. La mayoría formaba una diagonal, la **secuencia principal**, y las gigantes y las enanas blancas ocupaban zonas propias. Ese diagrama es, todavía hoy, la herramienta básica para entender la [vida de las estrellas](@vida-de-las-estrellas).

## Estrellas acompañadas

Más de la mitad de las estrellas parecidas al Sol tienen al menos una compañera. Alfa Centauri, el sistema más cercano, es **triple**: dos estrellas como el Sol que giran juntas y la pequeña Próxima Centauri. Otras forman **cúmulos**, como las Pléyades, grupos de cientos de estrellas nacidas a la vez de la misma nube.

## El brillo: magnitudes

Los astrónomos miden el brillo con la **magnitud**, una escala que heredamos del griego Hiparco y que va al revés: cuanto menor es el número, más brillante es la estrella. Las más brillantes tienen magnitud 0 o negativa (Sirio, −1,46) y a simple vista, desde un cielo oscuro, se ven hasta la magnitud 6. Una diferencia de 5 magnitudes equivale a 100 veces más brillo.

> En una noche oscura, lejos de las ciudades, una persona puede ver a simple vista unas 2.500 estrellas a la vez. Desde el centro de una gran ciudad, a veces menos de 50.
""",
    """
To the naked eye almost all stars look like white dots, but look carefully and you will see that **Betelgeuse** is orange and **Rigel**, in the same constellation of Orion, is bluish. A star's colour is like a thermometer.

## Colour shows temperature

Unlike taps, in stars **blue is hottest** and **red is coolest**. Astronomers classify them with the letters **O, B, A, F, G, K and M**, from hottest to coolest. A classic way to remember them is *"Oh Be A Fine Girl/Guy, Kiss Me"*.

| Type | Colour | Surface temperature | Example |
|---|---|---|---|
| O | Blue | Over 30,000 °C | Stars in Orion (Mintaka) |
| B | Bluish white | 10,000 to 30,000 °C | Rigel, Spica |
| A | White | 7,500 to 10,000 °C | Sirius, Vega |
| F | Yellowish white | 6,000 to 7,500 °C | Procyon, Polaris |
| G | Yellow | 5,200 to 6,000 °C | The Sun, Alpha Centauri A |
| K | Orange | 3,700 to 5,200 °C | Arcturus, Aldebaran |
| M | Red | Under 3,700 °C | Betelgeuse, Proxima Centauri |

## Dwarfs, giants and supergiants

Besides colour, stars differ in size and brightness:

- **Red dwarfs**: the smallest and most common. About three in four stars in the galaxy are red dwarfs, although not one is visible to the naked eye.
- **Sun-like stars**: medium-sized, halfway through their lives.
- **Red giants**: old stars that have swollen, like Arcturus or Aldebaran.
- **Supergiants**: the largest of all. Betelgeuse is so big that, placed where the Sun is, it would reach almost to Jupiter.
- **White dwarfs**: the dead cores of stars that have died, like Sirius's companion.

!foto sirio | Sirius A, the brightest star in the night sky, and its tiny companion Sirius B, a white dwarf (lower left), seen by Hubble.

## The Hertzsprung–Russell diagram

In the early 20th century, the Dane Ejnar Hertzsprung and the American Henry Norris Russell had the same idea: plot stars on a chart by temperature and true brightness. To everyone's surprise, they did not fall at random but clustered in bands. Most formed a diagonal, the **main sequence**, while giants and white dwarfs had their own regions. That diagram is still the basic tool for understanding the [life of stars](@vida-de-las-estrellas).

## Stars in company

More than half of Sun-like stars have at least one companion. Alpha Centauri, the nearest system, is **triple**: two Sun-like stars orbiting each other plus little Proxima Centauri. Others form **clusters**, like the Pleiades, groups of hundreds of stars born at the same time from the same cloud.

## Brightness: magnitudes

Astronomers measure brightness in **magnitudes**, a scale inherited from the Greek Hipparchus that runs backwards: the lower the number, the brighter the star. The brightest have magnitude 0 or less (Sirius, −1.46), and from a dark sky the naked eye reaches magnitude 6. A difference of 5 magnitudes means 100 times the brightness.

> On a dark night far from cities, a person can see about 2,500 stars at once with the naked eye. From the centre of a big city, sometimes fewer than 50.
""",
    datos=[("Clases espectrales", "Spectral classes", "O, B, A, F, G, K, M", "O, B, A, F, G, K, M"),
           ("Estrellas más comunes", "Most common stars", "Enanas rojas (≈ 75 %)", "Red dwarfs (≈ 75%)"),
           ("Estrella más brillante del cielo", "Brightest star in the sky", "Sirio, magnitud −1,46", "Sirius, magnitude −1.46"),
           ("Visibles a simple vista", "Visible to the naked eye", "≈ 9.000 en todo el cielo", "≈ 9,000 across the whole sky")],
    pie=("Las Pléyades, un cúmulo de estrellas jóvenes y azules en la constelación de Tauro.",
         "The Pleiades, a cluster of young blue stars in the constellation Taurus."),
)

NEBULOSAS = F(
    ("nebulosas", "nebulae"),
    ("Nebulosas", "Nebulae"),
    ("Nubes de gas y polvo donde nacen las estrellas y donde quedan sus restos: los paisajes más bellos del cielo.",
     "Clouds of gas and dust where stars are born and where their remains end up: the most beautiful landscapes in the sky."),
    ("nebulosas, nebulosa de Orión, Pilares de la Creación, nebulosa del Águila, nebulosa de Carina, nebulosa planetaria, nebulosa de emisión, nebulosa oscura, Cabeza de Caballo, Ojo de Gato, catálogo Messier",
     "nebulae, Orion Nebula, Pillars of Creation, Eagle Nebula, Carina Nebula, planetary nebula, emission nebula, dark nebula, Horsehead, Cat's Eye, Messier catalogue"),
    "orion_nebulosa",
    """
La palabra *nebulosa* viene del latín y significa «nube». Antes de los grandes telescopios, se llamaba así a cualquier mancha borrosa del cielo, incluidas las galaxias. Hoy el término se reserva para las nubes de gas y polvo del espacio interestelar, que son a la vez **cunas y tumbas de estrellas**.

## Tipos de nebulosas

- **De emisión**: el gas brilla con luz propia, sobre todo en rojo, porque las estrellas jóvenes y calientes de su interior lo excitan con radiación ultravioleta. La de Orión es el ejemplo más famoso.
- **De reflexión**: el polvo refleja la luz de estrellas cercanas y se ve azulado, como el cielo. Las Pléyades están envueltas en una.
- **Oscuras**: nubes tan densas que tapan la luz de lo que hay detrás, como la célebre **Cabeza de Caballo**.
- **Planetarias**: las capas que expulsa una estrella como el Sol al final de su vida. No tienen nada que ver con planetas: el nombre viene de que, con telescopios pequeños, parecían discos de planetas.
- **Restos de supernova**: las nubes que deja la explosión de una estrella gigante, como la **nebulosa del Cangrejo**.

## La nebulosa de Orión

A 1.350 años luz, es la región de formación de estrellas grande más cercana a la Tierra. Se ve a simple vista como una pequeña mancha en la «espada» de Orión, debajo de las tres estrellas del cinturón. En su interior, el telescopio Hubble ha encontrado cientos de estrellas recién nacidas y **discos protoplanetarios**, sistemas solares en plena formación.

## Los Pilares de la Creación

En 1995, el Hubble fotografió en la **nebulosa del Águila** unas columnas de gas y polvo de varios años luz de altura. La imagen se convirtió en una de las más famosas de la historia de la ciencia. En su interior se están formando estrellas. En 2022 el telescopio James Webb volvió a fotografiarlas en infrarrojo, viendo a través del polvo.

!foto eta_carinae | Eta Carinae, una estrella gigantesca e inestable envuelta en la nube que expulsó en una gran erupción en el siglo XIX.

## La nebulosa del Cangrejo

El 4 de julio de 1054, astrónomos chinos registraron una «estrella invitada» tan brillante que se vio de día durante 23 días. Era una supernova. Hoy, en ese lugar del cielo, está la nebulosa del Cangrejo, una nube de restos que se expande a 1.500 km/s, con un [púlsar](@estrellas-de-neutrones) en el centro que gira 30 veces por segundo.

!foto cangrejo | La nebulosa del Cangrejo, restos de una supernova observada en el año 1054.

## Charles Messier y su lista

En el siglo XVIII, el francés Charles Messier buscaba cometas y se encontraba una y otra vez con manchas que no se movían. Para no confundirse hizo una lista de 110 objetos «molestos». Hoy el **catálogo Messier** es la lista favorita de los aficionados: M1 es el Cangrejo, M42 es Orión y M31 es la [galaxia de Andrómeda](@galaxias-vecinas).

> Los colores de las fotos de nebulosas no son inventados, pero a menudo están realzados o traducidos: cada color suele representar un elemento químico (rojo para el hidrógeno o el azufre, verde o azul para el oxígeno) o luz infrarroja que el ojo no ve.
""",
    """
The word *nebula* comes from Latin and means "cloud". Before large telescopes, any fuzzy patch in the sky was called that, including galaxies. Today the term is reserved for clouds of gas and dust in interstellar space, which are both **cradles and graves of stars**.

## Types of nebulae

- **Emission nebulae**: the gas glows with its own light, mostly red, because young, hot stars inside excite it with ultraviolet radiation. Orion is the most famous example.
- **Reflection nebulae**: dust reflects the light of nearby stars and looks bluish, like the sky. The Pleiades are wrapped in one.
- **Dark nebulae**: clouds so dense that they block the light from behind, like the famous **Horsehead**.
- **Planetary nebulae**: the layers shed by a Sun-like star at the end of its life. They have nothing to do with planets: the name comes from the fact that, in small telescopes, they looked like planetary discs.
- **Supernova remnants**: the clouds left by the explosion of a giant star, like the **Crab Nebula**.

## The Orion Nebula

At 1,350 light years, it is the closest large star-forming region to Earth. It can be seen with the naked eye as a small smudge in Orion's "sword", below the three belt stars. Inside it, the Hubble telescope has found hundreds of newborn stars and **protoplanetary discs**, solar systems in the making.

## The Pillars of Creation

In 1995 Hubble photographed columns of gas and dust several light years tall in the **Eagle Nebula**. The image became one of the most famous in the history of science. Stars are forming inside them. In 2022 the James Webb telescope photographed them again in infrared, seeing through the dust.

!foto eta_carinae | Eta Carinae, a huge, unstable star wrapped in the cloud it threw out in a great eruption in the 19th century.

## The Crab Nebula

On 4 July 1054, Chinese astronomers recorded a "guest star" so bright it was visible in daylight for 23 days. It was a supernova. Today, in that spot in the sky, lies the Crab Nebula, a cloud of debris expanding at 1,500 km/s, with a [pulsar](@estrellas-de-neutrones) at its centre spinning 30 times a second.

!foto cangrejo | The Crab Nebula, the remains of a supernova seen in the year 1054.

## Charles Messier and his list

In the 18th century the Frenchman Charles Messier was hunting comets and kept running into smudges that did not move. To avoid confusion he made a list of 110 "annoying" objects. Today the **Messier catalogue** is amateurs' favourite list: M1 is the Crab, M42 is Orion and M31 is the [Andromeda galaxy](@galaxias-vecinas).

> The colours in nebula photos are not made up, but they are often enhanced or translated: each colour usually represents a chemical element (red for hydrogen or sulphur, green or blue for oxygen) or infrared light the eye cannot see.
""",
    datos=[("Nebulosa de Orión (M42)", "Orion Nebula (M42)", "1.350 años luz", "1,350 light years"),
           ("Nebulosa del Águila (M16)", "Eagle Nebula (M16)", "≈ 6.500 años luz", "≈ 6,500 light years"),
           ("Nebulosa del Cangrejo (M1)", "Crab Nebula (M1)", "≈ 6.500 años luz; supernova de 1054", "≈ 6,500 light years; 1054 supernova"),
           ("Objetos del catálogo Messier", "Messier catalogue objects", "110", "110")],
    pie=("La nebulosa de Orión en un mosaico del telescopio espacial Hubble.", "The Orion Nebula in a mosaic from the Hubble Space Telescope."),
)

SUPERNOVAS = F(
    ("supernovas", "supernovae"),
    ("Supernovas", "Supernovae"),
    ("Las explosiones más violentas desde el Big Bang: una estrella que brilla más que toda su galaxia y fabrica el oro y el hierro del universo.",
     "The most violent explosions since the Big Bang: a star that outshines its whole galaxy and forges the universe's gold and iron."),
    ("supernova, explosión de estrella, supernova de 1054, supernova de Kepler, supernova de Tycho, SN 1987A, Betelgeuse, Cassiopeia A, supernova tipo Ia, kilonova, origen del oro",
     "supernova, exploding star, 1054 supernova, Kepler's supernova, Tycho's supernova, SN 1987A, Betelgeuse, Cassiopeia A, type Ia supernova, kilonova, origin of gold"),
    "cassiopeia",
    """
Una supernova es la explosión de una estrella. Durante unas semanas, una sola estrella puede brillar tanto como **miles de millones de soles**, más que la galaxia entera que la contiene. En una galaxia como la nuestra se produce, de media, una o dos cada siglo.

## Dos formas de estallar

- **Colapso del núcleo**: cuando una estrella de más de unas ocho masas solares agota su combustible, su núcleo de hierro se desploma sobre sí mismo en menos de un segundo. El material que cae rebota y sale despedido a decenas de miles de kilómetros por segundo. En el centro queda una [estrella de neutrones](@estrellas-de-neutrones) o un [agujero negro](@agujeros-negros).
- **Tipo Ia**: una enana blanca que forma pareja con otra estrella le roba materia poco a poco. Cuando supera un límite de masa, unas 1,4 veces la del Sol, se enciende de golpe y se desintegra por completo.

Las de tipo Ia tienen casi siempre el mismo brillo máximo. Por eso sirven como «candelas estándar» para medir distancias. Gracias a ellas se descubrió en 1998 que la expansión del universo se está **acelerando**, un hallazgo que ganó el Premio Nobel en 2011 y que dio lugar a la idea de la [energía oscura](@materia-y-energia-oscura).

## Supernovas históricas

- **1006**: la estrella más brillante que se recuerda, visible durante meses y registrada en China, Egipto, Irak, Japón, Suiza y quizá en pinturas rupestres de Norteamérica.
- **1054**: vista por astrónomos chinos y árabes. Sus restos forman la [nebulosa del Cangrejo](@nebulosas).
- **1572**: la observó Tycho Brahe y demostró que el cielo no era inmutable, como se creía desde Aristóteles.
- **1604**: la última vista en nuestra galaxia, estudiada por Johannes Kepler.
- **1987**: **SN 1987A**, en la Gran Nube de Magallanes, la más cercana en casi cuatro siglos. Por primera vez se detectaron los **neutrinos** de una supernova, horas antes de verse la luz.

!foto cassiopeia | Cassiopeia A, los restos de una estrella que explotó hace unos 340 años, en una imagen del telescopio Spitzer.

## Fábricas de elementos

Las supernovas esparcen por el espacio los elementos que la estrella fabricó durante su vida, y en la propia explosión forman otros nuevos. Sin ellas no existiría el hierro de nuestra sangre ni el oxígeno que respiramos. Los elementos más pesados, como el **oro** y el platino, se forman sobre todo en las *kilonovas*, los choques de dos estrellas de neutrones. El oro de un anillo procede de una catástrofe cósmica anterior al Sol.

## ¿Peligro para la Tierra?

Una supernova a menos de unos 30 años luz podría dañar la capa de ozono. Por suerte, no hay ninguna estrella candidata tan cerca. **Betelgeuse**, la más famosa de las que explotarán «pronto», está a unos 550 años luz. Cuando estalle, quizá dentro de 100.000 años, se verá en el cielo tan brillante como la media luna, incluso de día, durante semanas, sin ningún riesgo para nosotros.

> El telescopio Webb ha encontrado tantas supernovas en el universo lejano que, en una sola zona pequeña del cielo, detectó unas 80 en 2023. Algunas explotaron cuando el universo tenía menos de 2.000 millones de años.
""",
    """
A supernova is the explosion of a star. For a few weeks, a single star can shine as brightly as **billions of suns**, more than the entire galaxy around it. In a galaxy like ours, one or two happen every century on average.

## Two ways to explode

- **Core collapse**: when a star of more than about eight solar masses runs out of fuel, its iron core collapses in less than a second. The infalling material rebounds and is blasted outwards at tens of thousands of kilometres per second. At the centre a [neutron star](@estrellas-de-neutrones) or a [black hole](@agujeros-negros) is left.
- **Type Ia**: a white dwarf paired with another star slowly steals matter from it. When it passes a mass limit, about 1.4 times the Sun's, it ignites all at once and blows itself apart completely.

Type Ia supernovae almost always reach the same peak brightness. That makes them "standard candles" for measuring distances. Thanks to them, it was discovered in 1998 that the expansion of the universe is **accelerating**, a finding that won the 2011 Nobel Prize and gave rise to the idea of [dark energy](@materia-y-energia-oscura).

## Historic supernovae

- **1006**: the brightest star on record, visible for months and noted in China, Egypt, Iraq, Japan, Switzerland and perhaps in North American rock art.
- **1054**: seen by Chinese and Arab astronomers. Its remains form the [Crab Nebula](@nebulosas).
- **1572**: observed by Tycho Brahe, it proved that the heavens were not unchanging, as had been believed since Aristotle.
- **1604**: the last one seen in our galaxy, studied by Johannes Kepler.
- **1987**: **SN 1987A**, in the Large Magellanic Cloud, the closest in almost four centuries. For the first time the **neutrinos** from a supernova were detected, hours before the light was seen.

!foto cassiopeia | Cassiopeia A, the remains of a star that exploded about 340 years ago, in an image from the Spitzer telescope.

## Element factories

Supernovae scatter the elements the star made during its life across space, and create new ones in the explosion itself. Without them there would be no iron in our blood and no oxygen to breathe. The heaviest elements, such as **gold** and platinum, are made mostly in *kilonovae*, collisions between two neutron stars. The gold in a ring comes from a cosmic catastrophe older than the Sun.

## A danger to Earth?

A supernova closer than about 30 light years could damage the ozone layer. Fortunately, there is no candidate star that close. **Betelgeuse**, the most famous of the stars that will explode "soon", is about 550 light years away. When it goes, perhaps 100,000 years from now, it will appear in the sky as bright as a half Moon, even in daylight, for weeks, with no risk to us.

> The Webb telescope has found so many supernovae in the distant universe that, in one small patch of sky, it detected about 80 in 2023. Some exploded when the universe was less than 2 billion years old.
""",
    datos=[("Brillo máximo", "Peak brightness", "Miles de millones de soles", "Billions of suns"),
           ("Frecuencia en la Vía Láctea", "Rate in the Milky Way", "1 o 2 por siglo", "1 or 2 per century"),
           ("Última vista en nuestra galaxia", "Last seen in our galaxy", "1604 (Kepler)", "1604 (Kepler)"),
           ("Más cercana reciente", "Nearest recent one", "SN 1987A, 168.000 años luz", "SN 1987A, 168,000 light years"),
           ("Masa mínima para estallar", "Minimum mass to explode", "≈ 8 masas solares", "≈ 8 solar masses")],
    pie=("Cassiopeia A, resto de una supernova, en infrarrojo.", "Cassiopeia A, a supernova remnant, in infrared."),
)

AGUJEROS = F(
    ("agujeros-negros", "black-holes"),
    ("Agujeros negros", "Black holes"),
    ("Regiones donde la gravedad es tan intensa que ni la luz escapa: cómo se forman, qué pasaría si cayeras en uno y cómo se fotografiaron.",
     "Regions where gravity is so strong that not even light escapes: how they form, what would happen if you fell in and how they were photographed."),
    ("agujero negro, horizonte de sucesos, singularidad, Sagitario A*, M87, Event Horizon Telescope, foto agujero negro, agujero negro supermasivo, radiación de Hawking, espaguetificación, ondas gravitacionales, Einstein",
     "black hole, event horizon, singularity, Sagittarius A*, M87, Event Horizon Telescope, black hole photo, supermassive black hole, Hawking radiation, spaghettification, gravitational waves, Einstein"),
    "agujero_m87",
    """
Un agujero negro es una región del espacio donde la materia está tan concentrada que su gravedad no deja escapar nada, ni siquiera la luz. No es un agujero en el sentido de un hueco, sino un objeto: muchísima masa en un espacio diminuto.

## Cómo se forman

La mayoría de los agujeros negros de tamaño estelar nacen cuando una estrella de más de unas 20 masas solares se queda sin combustible y su núcleo se hunde en una [supernova](@supernovas). Nada puede detener el colapso. Si comprimiéramos la Tierra hasta convertirla en agujero negro, cabría en una canica de **9 milímetros**; el Sol, en una esfera de 6 kilómetros.

## Las partes de un agujero negro

- **Horizonte de sucesos**: la frontera de no retorno. Lo que la cruza ya no puede salir. Desde fuera no se ve nada de lo que hay dentro.
- **Singularidad**: el punto central donde, según la relatividad de Einstein, la densidad se haría infinita. Probablemente significa que nuestra física aún no sabe describir ese lugar.
- **Disco de acreción**: el gas que gira alrededor antes de caer, calentado a millones de grados por la fricción. Es lo que hace que muchos agujeros negros sean, paradójicamente, de los objetos más brillantes del universo.

## Tipos según su tamaño

- **Estelares**: de unas pocas a decenas de masas solares. Solo en la Vía Láctea podría haber unos 100 millones.
- **Intermedios**: de cientos a cientos de miles de masas solares, muy difíciles de encontrar.
- **Supermasivos**: de millones a miles de millones de masas solares, en el centro de casi todas las galaxias grandes. El de la nuestra, **Sagitario A\\***, tiene unos 4,3 millones de masas solares.

## La primera foto

Para fotografiar un agujero negro hace falta un telescopio del tamaño de la Tierra. El **Event Horizon Telescope** lo consiguió uniendo radiotelescopios de todo el mundo, entre ellos el IRAM de Sierra Nevada (Granada). En 2019 presentó la imagen del agujero negro de la galaxia **M87**, de 6.500 millones de masas solares, y en 2022 la de Sagitario A\\*. En ambas se ve la «sombra» oscura rodeada de un anillo de luz, tal como predecía la teoría.

## ¿Qué pasaría si cayeras en uno?

Cerca de un agujero negro pequeño, la gravedad tiraría de tus pies mucho más que de tu cabeza y te estiraría como un espagueti: los físicos lo llaman, en serio, **espaguetificación**. En uno supermasivo, en cambio, podrías cruzar el horizonte sin notar nada especial. Para alguien que te mirara desde lejos, parecerías ir cada vez más despacio y enrojecerte hasta quedar congelado en el borde.

## Los agujeros negros se evaporan

En 1974, **Stephen Hawking** calculó que los agujeros negros no son del todo negros: por efectos cuánticos emiten una débil radiación y pierden masa muy lentamente. Uno como el Sol tardaría en evaporarse muchísimo más que la edad actual del universo.

## Cuando chocan

En 2015, los detectores LIGO registraron por primera vez las **ondas gravitacionales** del choque de dos agujeros negros, de 36 y 29 masas solares. En la fusión, el equivalente a tres soles se convirtió en energía en una fracción de segundo. Desde entonces se han detectado cientos de choques parecidos.

> Si el Sol se convirtiera en un agujero negro de su misma masa, la Tierra no sería absorbida: seguiría en la misma órbita. Eso sí, nos quedaríamos a oscuras y helados.
""",
    """
A black hole is a region of space where matter is so concentrated that its gravity lets nothing escape, not even light. It is not a hole in the sense of a gap but an object: an enormous amount of mass in a tiny space.

## How they form

Most stellar-sized black holes are born when a star of more than about 20 solar masses runs out of fuel and its core collapses in a [supernova](@supernovas). Nothing can stop the collapse. If Earth were squeezed into a black hole, it would fit in a **9 millimetre** marble; the Sun, in a sphere 6 kilometres across.

## The parts of a black hole

- **Event horizon**: the point of no return. Whatever crosses it cannot get out again. From outside, nothing inside can be seen.
- **Singularity**: the central point where, according to Einstein's relativity, density would become infinite. It probably means our physics does not yet know how to describe that place.
- **Accretion disc**: gas swirling around before it falls in, heated to millions of degrees by friction. It is what makes many black holes, paradoxically, among the brightest objects in the universe.

## Types by size

- **Stellar**: from a few to tens of solar masses. The Milky Way alone may hold some 100 million.
- **Intermediate**: hundreds to hundreds of thousands of solar masses, very hard to find.
- **Supermassive**: millions to billions of solar masses, at the centre of almost every large galaxy. Ours, **Sagittarius A\\***, has about 4.3 million solar masses.

## The first photo

Photographing a black hole needs a telescope the size of Earth. The **Event Horizon Telescope** did it by linking radio telescopes around the world, including IRAM in Sierra Nevada (Granada, Spain). In 2019 it unveiled the image of the black hole in galaxy **M87**, 6.5 billion solar masses, and in 2022 that of Sagittarius A\\*. Both show the dark "shadow" surrounded by a ring of light, just as theory predicted.

## What would happen if you fell in?

Near a small black hole, gravity would pull on your feet far more than on your head and stretch you like a noodle: physicists really call it **spaghettification**. In a supermassive one, however, you could cross the horizon without noticing anything special. To someone watching from afar, you would seem to slow down and redden until you froze at the edge.

## Black holes evaporate

In 1974 **Stephen Hawking** calculated that black holes are not completely black: quantum effects make them give off faint radiation and lose mass very slowly. One the mass of the Sun would take vastly longer than the current age of the universe to evaporate.

## When they collide

In 2015 the LIGO detectors recorded, for the first time, the **gravitational waves** from two black holes colliding, of 36 and 29 solar masses. In the merger, the equivalent of three suns turned into energy in a fraction of a second. Hundreds of similar collisions have been detected since.

> If the Sun turned into a black hole of the same mass, Earth would not be sucked in: it would keep the same orbit. We would, however, be left in the dark and frozen.
""",
    datos=[("Agujero negro de la Vía Láctea", "Milky Way's black hole", "Sagitario A*, 4,3 millones de soles", "Sagittarius A*, 4.3 million suns"),
           ("Distancia a Sagitario A*", "Distance to Sagittarius A*", "26.000 años luz", "26,000 light years"),
           ("Agujero negro de M87", "M87 black hole", "6.500 millones de soles", "6.5 billion suns"),
           ("Primera foto", "First photo", "10 de abril de 2019", "10 April 2019"),
           ("Primeras ondas gravitacionales", "First gravitational waves", "14 de septiembre de 2015", "14 September 2015"),
           ("Tamaño de la Tierra como agujero negro", "Earth as a black hole", "≈ 9 mm", "≈ 9 mm")],
    pie=("El agujero negro supermasivo de la galaxia M87, fotografiado por el Event Horizon Telescope (2019).",
         "The supermassive black hole in galaxy M87, photographed by the Event Horizon Telescope (2019)."),
)

NEUTRONES = F(
    ("estrellas-de-neutrones", "neutron-stars"),
    ("Estrellas de neutrones y púlsares", "Neutron stars and pulsars"),
    ("Una ciudad de 20 km con más masa que el Sol, que gira cientos de veces por segundo: los objetos más densos después de los agujeros negros.",
     "A city-sized ball 20 km across with more mass than the Sun, spinning hundreds of times a second: the densest objects after black holes."),
    ("estrella de neutrones, púlsar, magnetar, Jocelyn Bell, LGM-1, kilonova, densidad, púlsar del Cangrejo, choque de estrellas de neutrones, GW170817",
     "neutron star, pulsar, magnetar, Jocelyn Bell, LGM-1, kilonova, density, Crab pulsar, neutron star collision, GW170817"),
    "cangrejo",
    """
Cuando una estrella gigante estalla en [supernova](@supernovas) pero no tiene masa suficiente para formar un agujero negro, su núcleo queda comprimido en una **estrella de neutrones**: una esfera de unos **20 kilómetros de diámetro**, el tamaño de una ciudad, con entre 1,4 y 2 veces la masa del Sol.

## La materia más densa

En una estrella de neutrones, los átomos están aplastados: los electrones se han fundido con los protones y solo quedan neutrones apretados unos contra otros. **Una cucharadita** de esa materia pesaría unos 1.000 millones de toneladas, como una montaña entera. Su gravedad es tan intensa que una montaña en su superficie no podría medir más de unos milímetros.

## Púlsares: faros cósmicos

Al encogerse, la estrella gira cada vez más rápido, como una patinadora que recoge los brazos. Muchas estrellas de neutrones giran decenas o cientos de veces por segundo y emiten dos haces de ondas de radio desde sus polos magnéticos. Si uno de esos haces barre la Tierra, recibimos un pulso en cada vuelta, con la regularidad de un reloj atómico: es un **púlsar**.

## LGM-1: «hombrecillos verdes»

En 1967, la estudiante de doctorado **Jocelyn Bell Burnell** encontró en los datos de un radiotelescopio una señal que se repetía exactamente cada 1,34 segundos. Era tan regular que, medio en broma, la bautizaron **LGM-1**, de *Little Green Men* (hombrecillos verdes), por si fuera un mensaje extraterrestre. Era el primer púlsar. El Premio Nobel por el descubrimiento fue en 1974 a su director de tesis, no a ella, una decisión que hoy se considera una gran injusticia. En 2018 recibió el Premio Breakthrough y donó los 3 millones de dólares para becas.

## Magnetares

Algunas estrellas de neutrones tienen campos magnéticos de **mil billones de veces** el de la Tierra. Son los *magnetares*, los imanes más potentes del universo. A 1.000 kilómetros de uno, su campo borraría los datos de todas las tarjetas de crédito de la Tierra, y a menos distancia deformaría los átomos de nuestro cuerpo. En 2004, un estallido de un magnetar situado al otro lado de la galaxia llegó a alterar la parte alta de la atmósfera terrestre.

## Choques que fabrican oro

El 17 de agosto de 2017, los detectores de ondas gravitacionales captaron el choque de dos estrellas de neutrones, **GW170817**, y 70 telescopios de todo el mundo observaron a la vez el destello. Era una *kilonova*. En los restos se detectó la huella de elementos pesados: se calcula que el choque produjo varias veces la masa de la Tierra en **oro y platino**.

> El púlsar más rápido conocido gira 716 veces por segundo. Su superficie se mueve a casi una cuarta parte de la velocidad de la luz.
""",
    """
When a giant star explodes as a [supernova](@supernovas) but lacks the mass to form a black hole, its core is crushed into a **neutron star**: a sphere about **20 kilometres across**, the size of a city, with between 1.4 and 2 times the mass of the Sun.

## The densest matter

In a neutron star, atoms are crushed: electrons have merged with protons, leaving only neutrons packed against each other. **A teaspoon** of that matter would weigh about a billion tonnes, like a whole mountain. Its gravity is so strong that a mountain on its surface could be no more than a few millimetres high.

## Pulsars: cosmic lighthouses

As it shrinks, the star spins faster and faster, like a skater pulling in her arms. Many neutron stars spin tens or hundreds of times a second and emit two beams of radio waves from their magnetic poles. If one of those beams sweeps across Earth, we receive a pulse on each turn, as regular as an atomic clock: a **pulsar**.

## LGM-1: "little green men"

In 1967 the PhD student **Jocelyn Bell Burnell** found a signal in radio telescope data that repeated exactly every 1.34 seconds. It was so regular that, half jokingly, it was nicknamed **LGM-1**, for *Little Green Men*, in case it was an alien message. It was the first pulsar. The 1974 Nobel Prize for the discovery went to her thesis supervisor, not to her, a decision now widely seen as a great injustice. In 2018 she won the Breakthrough Prize and donated the 3 million dollars to scholarships.

## Magnetars

Some neutron stars have magnetic fields a **quadrillion times** Earth's. They are *magnetars*, the most powerful magnets in the universe. From 1,000 kilometres away, one would wipe every credit card on Earth, and any closer it would distort the atoms in our bodies. In 2004, a flare from a magnetar on the far side of the galaxy disturbed Earth's upper atmosphere.

## Collisions that forge gold

On 17 August 2017, gravitational wave detectors picked up the collision of two neutron stars, **GW170817**, and 70 telescopes around the world watched the flash at the same time. It was a *kilonova*. The debris showed the fingerprint of heavy elements: the collision is estimated to have produced several Earth masses of **gold and platinum**.

> The fastest known pulsar spins 716 times a second. Its surface moves at almost a quarter of the speed of light.
""",
    datos=[("Diámetro típico", "Typical diameter", "≈ 20 km", "≈ 20 km"),
           ("Masa", "Mass", "1,4 a 2 soles", "1.4 to 2 suns"),
           ("Una cucharadita pesa", "A teaspoon weighs", "≈ 1.000 millones de toneladas", "≈ 1 billion tonnes"),
           ("Púlsar más rápido", "Fastest pulsar", "716 vueltas por segundo", "716 turns per second"),
           ("Primer púlsar", "First pulsar", "Jocelyn Bell Burnell, 1967", "Jocelyn Bell Burnell, 1967")],
    pie=("La nebulosa del Cangrejo, con un púlsar en su centro que gira 30 veces por segundo.",
         "The Crab Nebula, with a pulsar at its centre spinning 30 times a second."),
)

EXOPLANETAS = F(
    ("exoplanetas-y-vida", "exoplanets-and-life"),
    ("Exoplanetas y vida en el universo", "Exoplanets and life in the universe"),
    ("Más de 6.000 planetas alrededor de otras estrellas, mundos que podrían tener agua y la gran pregunta: ¿estamos solos?",
     "More than 6,000 planets around other stars, worlds that could have water and the big question: are we alone?"),
    ("exoplanetas, planetas extrasolares, vida extraterrestre, zona habitable, TRAPPIST-1, Kepler, TESS, Próxima b, K2-18b, ecuación de Drake, paradoja de Fermi, SETI, astrobiología, biofirmas",
     "exoplanets, extrasolar planets, alien life, habitable zone, TRAPPIST-1, Kepler, TESS, Proxima b, K2-18b, Drake equation, Fermi paradox, SETI, astrobiology, biosignatures"),
    "trappist",
    """
Hace solo tres décadas no sabíamos si existían planetas fuera del sistema solar. Hoy se han confirmado **más de 6.000 exoplanetas**, y los astrónomos calculan que en nuestra galaxia hay más planetas que estrellas.

## Cómo se encuentran

Los exoplanetas son muy difíciles de ver directamente, porque su estrella los deslumbra. Por eso casi todos se han descubierto de forma indirecta:

- **Tránsitos**: cuando el planeta pasa por delante de su estrella, la luz de esta baja un poquito. Así trabajaron los telescopios espaciales **Kepler** (2009–2018) y **TESS** (desde 2018).
- **Velocidad radial**: el planeta hace que la estrella se balancee ligeramente, y ese vaivén se detecta en su luz. Así se encontró el primero alrededor de una estrella como el Sol, **51 Pegasi b**, en 1995.
- **Imagen directa**: tapando la luz de la estrella se pueden fotografiar algunos planetas jóvenes y grandes.

## Un zoo de mundos

Hay **júpiteres calientes** que dan una vuelta a su estrella en menos de tres días, **supertierras** y **minineptunos** que no tienen equivalente en el sistema solar, planetas que giran alrededor de dos soles, como Tatooine en *La guerra de las galaxias*, y planetas errantes que vagan por el espacio sin estrella. Uno, **55 Cancri e**, podría tener un océano de lava; en otro, WASP-76b, se cree que llueve hierro.

## Mundos que podrían ser habitables

- **Próxima Centauri b**, alrededor de la estrella más cercana, a 4,24 años luz, está en la zona habitable.
- **TRAPPIST-1**, a 40 años luz, tiene siete planetas del tamaño de la Tierra; tres están a la distancia adecuada para tener agua líquida.
- **K2-18b**, a 124 años luz, es un planeta mayor que la Tierra en el que el telescopio Webb ha detectado metano y dióxido de carbono. Se estudia si podría tener un océano.

!foto trappist | Recreación artística de TRAPPIST-1 e, uno de los siete planetas del tamaño de la Tierra de ese sistema.

## ¿Cómo se buscaría vida?

Los astrónomos buscan **biofirmas**: combinaciones de gases en la atmósfera de un planeta que difícilmente se explicarían sin seres vivos, como oxígeno y metano juntos. Dentro del sistema solar, los lugares más prometedores son [Marte](@marte), el océano de Europa y los géiseres de Encélado. Ver la ficha de las [lunas](@lunas).

## La ecuación de Drake y la paradoja de Fermi

En 1961, el radioastrónomo **Frank Drake** escribió una ecuación para estimar cuántas civilizaciones capaces de comunicarse podría haber en la galaxia. Multiplica el ritmo de formación de estrellas, la fracción que tiene planetas, los que podrían albergar vida, los que la desarrollan, los que llegan a inteligencia... Según los números que se pongan, el resultado va de casi cero a millones.

El físico **Enrico Fermi** planteó la pregunta en una comida en 1950: si debería haber tantas civilizaciones, «¿dónde está todo el mundo?». Es la **paradoja de Fermi**, y aún no tiene respuesta. El proyecto **SETI** lleva décadas escuchando el cielo con radiotelescopios.

> En 1977, un radiotelescopio de Ohio captó una señal tan intensa y extraña que el astrónomo Jerry Ehman escribió «Wow!» en el papel impreso. Nunca se ha vuelto a detectar, y hoy se cree que pudo tener un origen natural.
""",
    """
Only three decades ago we did not know whether planets existed outside the solar system. Today **more than 6,000 exoplanets** have been confirmed, and astronomers estimate that our galaxy holds more planets than stars.

## How they are found

Exoplanets are very hard to see directly, because their star outshines them. So almost all have been discovered indirectly:

- **Transits**: when a planet passes in front of its star, the star's light dips very slightly. This is how the **Kepler** (2009–2018) and **TESS** (since 2018) space telescopes worked.
- **Radial velocity**: the planet makes the star wobble slightly, and that wobble shows up in its light. This is how the first planet around a Sun-like star, **51 Pegasi b**, was found in 1995.
- **Direct imaging**: by blocking the star's light, some young, large planets can be photographed.

## A zoo of worlds

There are **hot Jupiters** that orbit their star in under three days, **super-Earths** and **mini-Neptunes** with no equivalent in the solar system, planets orbiting two suns, like Tatooine in *Star Wars*, and rogue planets drifting through space with no star. One, **55 Cancri e**, may have an ocean of lava; on another, WASP-76b, it is thought to rain iron.

## Worlds that might be habitable

- **Proxima Centauri b**, orbiting the nearest star 4.24 light years away, lies in the habitable zone.
- **TRAPPIST-1**, 40 light years away, has seven Earth-sized planets; three are at the right distance to have liquid water.
- **K2-18b**, 124 light years away, is a planet larger than Earth where the Webb telescope has detected methane and carbon dioxide. Whether it could have an ocean is being studied.

!foto trappist | Artist's impression of TRAPPIST-1 e, one of the system's seven Earth-sized planets.

## How would we look for life?

Astronomers look for **biosignatures**: combinations of gases in a planet's atmosphere that would be hard to explain without living things, such as oxygen and methane together. Within the solar system, the most promising places are [Mars](@marte), Europa's ocean and the geysers of Enceladus. See the article on [moons](@lunas).

## The Drake equation and the Fermi paradox

In 1961 the radio astronomer **Frank Drake** wrote an equation to estimate how many civilisations capable of communicating there might be in the galaxy. It multiplies the rate of star formation, the fraction with planets, those that could host life, those where it arises, those that become intelligent... Depending on the numbers used, the answer ranges from almost zero to millions.

The physicist **Enrico Fermi** asked the question over lunch in 1950: if there should be so many civilisations, "where is everybody?" It is the **Fermi paradox**, and it still has no answer. The **SETI** project has spent decades listening to the sky with radio telescopes.

> In 1977 a radio telescope in Ohio picked up a signal so strong and strange that astronomer Jerry Ehman wrote "Wow!" on the printout. It has never been detected again, and it is now thought it may have had a natural origin.
""",
    datos=[("Exoplanetas confirmados", "Confirmed exoplanets", "Más de 6.000", "More than 6,000"),
           ("Primero en una estrella como el Sol", "First around a Sun-like star", "51 Pegasi b, 1995", "51 Pegasi b, 1995"),
           ("Exoplaneta más cercano", "Nearest exoplanet", "Próxima Centauri b, 4,24 años luz", "Proxima Centauri b, 4.24 light years"),
           ("Sistema con más planetas tipo Tierra", "System with most Earth-like planets", "TRAPPIST-1 (7)", "TRAPPIST-1 (7)"),
           ("Premio Nobel", "Nobel Prize", "Mayor y Queloz, 2019", "Mayor and Queloz, 2019")],
    pie=("Recreación artística de TRAPPIST-1 e (NASA, ESA, CSA, STScI).", "Artist's impression of TRAPPIST-1 e (NASA, ESA, CSA, STScI)."),
)

FICHAS = [VIDA, TIPOS, NEBULOSAS, SUPERNOVAS, AGUJEROS, NEUTRONES, EXOPLANETAS]
