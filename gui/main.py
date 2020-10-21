from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox 
import random

class Provincia:
    def __init__ (self, nombre, descripcion, imagen, sitios ):
        self.nombre = nombre    
        self.descripcion = descripcion
        self.imagen = imagen
        self.sitios = sitios
        
class SitioTuristico:
    def __init__ (self, nombre, descripcion,imagen, precio, beneficios):
        self.nombre = nombre
        self.descripcion = descripcion
        self.imagen = imagen
        self.beneficios = beneficios
        self.precio = precio

class Compra:
    def __init__(self, sitio, nombre, nacionalidad, cedula, edad, cantidad, pago, descuento, abono):
        self.sitio = sitio
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.cedula = cedula
        self.edad = edad
        self.cantidad = cantidad
        self.pago = pago
        self.descuento = descuento
        self.abono = abono

compras = []

beneficios = [
    'Hospedaje',
    'Comidas',
    'Guia Turistico',
    'Transporte',
    'Fotografo Profesional',
    'Vuelo Incluido'
]

sitios = [
    [
        SitioTuristico(
            'Isla Bastimentos',
            'Isla Bastimentos es una de las islas más grandes dentro del archipiélago y aquí esta ubicado el tranquilo pueblo de Old Bank, la comunidad indígena Quebrada de Sal, y el Parque Nacional Marino Isla Bastimentos. También es hogar del complejo de Red Frog Beach y unas playas de postales.',
            './sitios/bastimentos.jpg',
            158.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Cayos Zapatilla',
            'Cayos Zapatilla es un grupo de dos islas deshabitadas, rodeadas de un arrecife de coral, situadas al este de la Isla Bastimentos, en el archipiélago de Bocas del Toro, en la provincia del mismo nombre al noroeste del país centroamericano de Panamá.',
            './sitios/zapatilla.jpg',
            110.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Isla Colón',
            'La capital de la Provincia de Bocas del Toro, es Isla Colón, situada al noreste de la República de Panamá, con una extensión de 8,475 kms2. Bocas posee un litoral muy accidentado, con bahías, puntas y un espectacular archipiélago con 9 islas, 5 islotes y 200 islas rocosas. Isla Colón destaca por su arquitectura caribeña, la hospitalidad de sus habitantes, y la cocina, típica del área, picante, deliciosa y única.',
            './sitios/iscolon.jpg',
            175.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Parque Internacional La Amistad',
            'Creado en 1988 por una iniciativa de los gobiernos de Panamá y Costa Rica, el Parque Internacional La Amistad, conocido popularmente como PILA, se extiende sobre 207,000 hectáreas en los impresionantes macizos de la Cordillera Central, entre las provincias de Chiriquí y Bocas del Toro. ',
            './sitios/amistad.jpg',
            75.00,
            random.sample(beneficios, random.randint(3,6))
        )
    ],[
        SitioTuristico(
            'Valle de Antón',
            'El Valle de Antón es el cráter de un antiguo volcán. Se sitúa a 600 metros sobre el nivel del mar y, en su centro, se ubica el pueblo de El Valle. La presencia de este poblado lo convierte en uno de los pocos cráteres volcánicos permanentemente habitados del planeta.',
            './sitios/anton.jpg',
            125.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Riviera Pacifica',
            'En la Riviera del Pacífico, a las afueras de la ciudad de Panamá, hay un grupo de hermosas playas de arena blanca y aguas cálidas que reflejan el cielo azul. Esta zona costera perteneciente a las provincias de Panamá Oeste y Coclé; Es el hogar de una variedad de resorts de servicio completo, campos de golf, deportes acuáticos y proximidad al destino turístico y volcánico de El Valle.',
            './sitios/riviera.jpg',
            140.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Parque Arqueologico El Caño',
            'El Parque Arqueológico El Caño muestra cómo eran las sociedades que habitaban Panamá antes de la conquista. El sitio arqueológico, donde aún se efectuan excavaciones y estudios, incluye una extensa necrópolis con montículos funerarios y un centro ceremonial con alineamientos de columnas de basalto que fueron utilizados entre los años 700 y 1000.',
            './sitios/caño.jpg',
            80.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'El Copé',
            'El Copé es un pequeño pueblo pintoresco, de gente laboriosa, clima agradable y fresco y muchos atractivos turísticos. Se cultiva la naranja y el café y sus pobladores se dedican en su mayoría a las actividades agrícolas y a la ganadería.',
            './sitios/cope.jpg',
            79.00,
            random.sample(beneficios, random.randint(3,6))
        )
    ],[
        SitioTuristico(
            'Portobelo',
            'Portobelo fue el puerto colonial más importante del Caribe panameño y hoy es la capital de la cultura Congo. Entre los siglos XVI y XVIII, Portobelo recibía los galeones venidos de España y los cargaba con el oro y la plata de América. La llegada de la flota más rica del Caribe la convirtió en el núcleo comercial de la región y en el objetivo de naciones enemigas, de piratas y corsarios.',
            './sitios/portobelo.jpg',
            210.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Isla Grande',
            'Despierta en la paradisíaca Isla Grande con el canto de los pájaros y el sonido de las olas que te invitan a disfrutar de sus playas de arena blanca y aguas cristalinas; ideal para buceo, snorkel y surf. Atraviesa su pintoresca comunidad poblada de personas hospitalarias y felices, y culmina la ruta en la cima del faro',
            './sitios/grande.jpg',
            200.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'San Lorenzo',
            'San Lorenzo guarda las ruinas del fuerte español más poderoso de Panamá, entre la jungla y el mar. Construido en 1601 por órdenes del rey de España, el Castillo de San Lorenzo el Real custodiaba la entrada y salida de la principal ruta de América. Incontables riquezas eran transportadas por el río Chagres que, junto con el camino de Cruces por tierra, formaba una vital vía de comunicación entre los dos océanos. ',
            './sitios/lorenzo.jpg',
            110.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Cayo Tortuga',
            'Ubicada en la Costa Atlántica en la Provincia de Colón, también posee grandes atractivos turísticos y éste es el caso el Corregimiento de Nombre de Dios ubicado en el Distrito de Santa Isabel, donde se encuentra el área de Cayo Tortuga. Con arenas blancas y aguas cristalinas, Cayo Tortuga se convertirá pronto en destino turístico, pues actualmente se encuentra en su primera fase de construcción. ',
            './sitios/tortuga.jpg',
            100.00,
            random.sample(beneficios, random.randint(3,6))
        )
    ],[
        SitioTuristico(
            'Volcán Barú',
            'El Parque Nacional Volcán Barú tiene la cima más alta de Panamá y es el mejor lugar para el senderismo de montaña. De sus 14.322 hectáreas, emerge el imponente Volcán Barú que supera en altura todas las montañas del país. Sus laderas, de arriba a abajo, están envueltas por 5 ecosistemas diferentes y son cruzadas por numerosos arroyos.',
            './sitios/baru.jpg',
            250.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Boquete',
            'Boquete es un entorno natural con temperaturas frescas que lo invitan a disfrutar de su exquisito manjar galardonado en todo el mundo: el café. El aleteo y el canto de los pájaros te llama a caminar por los senderos mientras la madre naturaleza invade tus sentidos. Sus puentes colgantes y paseos relajantes, sus aguas cristalinas, y sus abundantes y diversas flores se convierten en parte de su experiencia en Boquete.',
            './sitios/boquete.jpg',
            210.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Tierras Altas',
            'Su belleza natural, clima agradable y fresco, sus deliciosas fresas, su pesca de truchas y la degustación de su café con un sabor incomparable le transmitirán experiencias que permanecerán en usted. Tierras Altas, un destino ideal para aventureros y familias.',
            './sitios/altas.jpg',
            190.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Golfo de Chiriquí',
            'El Golfo de Chiriquí te cautivará con sus hermosos escenarios dentro de cada amanecer y atardecer. Sus placenteras playas, sus aguas transparentes y tranquilas, sus vividas islas y su naturaleza embellecedora se convertirán en tu aventura perfecta. Aquí podrás realizar pesca deportiva, paseos en botes, avistamiento de cetáceos, y disfrutar de su gastronomía propia de frutos del mar.',
            './sitios/golfochiriqui.jpg',
            140.00,
            random.sample(beneficios, random.randint(3,6))
        )
    ],[
        SitioTuristico(
            'Parque Nacional Darien',
            'El Parque Nacional Darién es un ambiente mágico selvático al que se puede llegar de más de una forma para apreciar impresionantes paisajes de selva virgen. Desde la Ciudad de Panamá vía aérea hasta la comunidad más cercana al Parque, Por su extraordinaria diversidad biológica y su alto valor genético, además de los grupos que guardan y practican tradiciones ancestrales, el Parque Nacional Darién fue declarado en 1981 Reserva de la Biósfera de la Humanidad.',
            './sitios/darien.jpg',
            105.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Yaviza',
            'Yaviza es un corregimeinto de Panamá a unos 97 km de la frontera con Colombia. Da nombre a un pequeño poblado perteneciente al distrito de Pinogana. En Yaviza existen ruinas que eran de la época colonial, conocidas como la Casa-Fuerte de San Gerónimo, fue construida en 1760 frente al río Chucunaque y fue destruida por los gunas en 1780. Los factores medioambientales la han deteriorado y una riada se llevó la mitad del fuerte a mediados del siglo XX.',
            './sitios/yaviza.jpg',
            200.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Garachine',
            'Visitar Garachiné, en la provincia de Darién, Panamá, es para aventureros. No cualquiera puede tolerar el complicado viaje y la falta de amenidades. Los que se atrevan a embarcar en la expedición, serán recompensados con un pueblo lleno de gente amable. Esta localidad bordea la frontera con Colombia, un lugar tradicionalmente considerado como peligroso: narcotráfico, guerrilla y malaria vienen a la mente de muchos.',
            './sitios/garachine.jpg',
            195.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'La Palma',
            'La Palma es la capital de la provincia panameña de Darién,​ situada a orillas del océano Pacífico, en el extremo de una amplia península que separa la desembocadura del río Tuira (sinuoso estuario llamado golfo de San Miguel) de la recogida bahía o ensenada de Garachiné.',
            './sitios/palma.jpg',
            120.00,
            random.sample(beneficios, random.randint(3,6))
        )
    ],[
        SitioTuristico(
            'Museo de Arte Religioso Colonial',
            'El sitio actual del Museo del Arte Religioso Colonial fue anteriormente una capilla, que fue construida posterior al incendio que destruyó el templo y convento original. Cuando se levanta la Capilla de Santo Domingo de Guzmán en el siglo XVIII, la ciudad de Panamá ya tenía más de 2 siglos de existencia. Las piezas que se exhiben en este Museo, pertenecen a familias e iglesias de la Ciudad de Panamá y del interior del País. ',
            './sitios/colonial.jpg',
            98.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Parque nacional de Sarigua',
            'El Parque Nacional Sarigua, ubicado en la comunidad de Parita, Provincia de Herrera, cubre una superficie de 8,000 hectáreas en lo que corresponde a áreas de ecosistema marino y albina semidesertica. Este es un lugar de un importante asentamiento precolombino que data de 11,000 años de antigüedad.',
            './sitios/sarigua.jpg',
            84.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'La Arena',
            'El corregimiento de La Arena es famoso por sus bellas obras de alfarería y cerámicas elaboradas por los artesanos del pueblo que con esmero se levantan cada día a trabajar en sus propios negocios de ventas de potes, tinajas, cazuelas, vajillas, tejas, recordatorios con vivos colores, entre otros. Todos estos artículos son muestra del secreto antiguo de los areneros para moldear el barro.',
            './sitios/arena.jpg',
            115.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Reserva Forestal el Montuoso',
            'La Reserva Forestal se encuentra ubicada en el extremo norte del macizo occidental de Azuero y comprende parches de bosques interconectados con bosques de galería. En el área la mayoría de las pendientes son fuertes, destacándose las siguientes elevaciones: la cordillera de La Huaca y la cordillera de El Montuoso.',
            './sitios/montuoso.jpg',
            130.00,
            random.sample(beneficios, random.randint(3,6))
        )
    ],[
        SitioTuristico(
            'Playa Venao',
            'Playa Venao es un lugar de surf de fama local a 34 km al suroeste de Pedasí. Playa Venao tiene, sin lugar a dudas, el mejor surf de la península de Azuero, con olas que rompen en ambas direcciones y son perfectas para todos los niveles. La playa de arena gris aquí es agradable, se extiende en un gran arco y está rodeada por una ladera con curvas.',
            './sitios/venao.jpg',
            230.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Parque Nacional Cerro Hoya',
            'El Parque Nacional Cerro Hoya o Tres Cerros, se encuentra en el extremo suroccidental de la península de Azuero, sobre las costas del pacífico panameño en la sierra de Azuero, compartido entre la provincia de Los Santos, y el distrito de Mariato. ',
            './sitios/hoya.jpg',
            155.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Playa El Arenal',
            'Playa El Arenal te sorprenderá. Sus aguas son más cristalinas que Playa El Toro y Playa La Garita, las más cercanas al pueblo de Pedasí (ubicado a 5 horas de la Ciudad de Panamá en la Provincia de Los Santos). Pero también es el lugar indicado para tomar las lanchas o botes que te llevarán a uno de los lugares más paradisíacos de Panamá: Isla Iguana.',
            './sitios/arenal.jpg',
            110.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Isla Iguana',
            'Isla Iguana es la principal atracción natural de la Península de Azuero y ofrece la única playa de arena blanca de esa región y hermosas aguas cristalinas. Isla Iguana es un paraíso aislado, considerado un refugio de vida silvestre, habitado solo por aves raras, lagartos gigantes y cangrejos morados y rojos.',
            './sitios/iguana.jpg',
            110.00,
            random.sample(beneficios, random.randint(3,6))
        )
    ],[
        SitioTuristico(
            'Isla Taboga',
            'Taboga es la isla más grande que se ve desde la ciudad y es el perfecto rincón de playa para refugiarse del frenesí de la capital. La escarpada cima de la isla está dominada por el cerro El Vigía de 305 metros de altura, que ofrece una vista incomparable del pueblo, del océano y de la ciudad de Panamá. Taboga se sitúa a solo 20 kilómetros de la costa y es fácilmente accesible por ferry.',
            './sitios/taboga.jpg',
            145.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Panamá Viejo',
            'Panamá Viejo es el conjunto de ruinas de la primera ciudad de Panamá, fundada por el noble castellano Pedrarias Dávila en 1519. Fue el primer asentamiento europeo a orillas del océano Pacífico y fue el lugar en el que se organizaron varias expediciones; incluyendo las de Francisco Pizarro hacia el Perú. Panama Viejo fue declarado Patrimonio Mundial de la Humanidad por la UNESCO en 1997.',
            './sitios/viejo.jpg',
            65.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Casco Antiguo',
            'El Casco Antiguo es el corazón histórico y cultural de la capital panameña. Fue fundado en 1673 como la ciudad de Panamá la Nueva, luego de la destrucción de la ciudad original durante un ataque pirata. Esta rica historia continúa reflejada en los edificios de ladrillos, de cal y canto; que hoy albergan museos, exposiciones, y vibrantes bares y restaurantes.',
            './sitios/antiguo.jpg',
            270.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Canal de Panama',
            'El Canal de Panamá es el mayor atajo del planeta y es una de las maravillas del mundo moderno. Sus 80 kilómetros de longitud conectan los océanos Atlántico y Pacífico a través de la porción más estrecha del continente. Hoy esta maravilla de la tecnología puede ser descubierta en dos centros de visitantes con miradores, exhibiciones y salas de proyección.',
            './sitios/canal.jpg',
            90.00,
            random.sample(beneficios, random.randint(3,6))
        )
    ],[
        SitioTuristico(
            'Parque Nacional Coiba',
            'El Parque Nacional Coiba ofrece atractivos como playas, buceo y pesca a lo largo de todo su perímetro costero. Las arenas muy finas y la transparencia del agua son las características de las playas. Al Parque Nacional Coiba se puede llegar vía aérea desde la Ciudad de Panamá hasta la Ciudad de Santiago en 20 minutos, o por carretera (245 kilómetros) en 5 horas.',
            './sitios/coiba.jpg',
            35.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Santa Fe',
            'Santa Fe se encuentra en las tierras altas de Veraguas, un paraíso ecológico, hogar a una amplia variedad de animales y plantas, incluidas las orquídeas. Nuestra selva tropical es ideal para practicar senderismo y observación de aves. Este hermoso lugar tiene más de 50 cascadas para explorar, nadar y reconectarse con la naturaleza.',
            './sitios/santa.jpg',
            65.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'La Yeguada',
            ' La Yeguada es uno de los mejores lugares donde acampar en Panamá porque tiene unas bonitas vistas y un clima fresco. Es parte de la reserva del bosque para cuidar de la cuenca de la Laguna de La Yeguada.Se compone de numerosas colinas y cascadas que pueden alcanzar 25 metros (Cascade El Desvio). Este tipo de visitas con la posibilidad de acampar en la naturaleza son perfectos para los jóvenes.',
            './sitios/yeguada.jpg',
            95.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Playa Morillo',
            'Playa Morrillo, una playa semidesierta ubicada en la provincia de Veraguas, un poco fuera del mapa, de hecho no está en el mapa. Esta playa es para los más aventureros, aunque tiene hospedaje y camino, está un poco escondida. Esta playa es un destino especial para surfistas de todas las categorías porque ofrece una ola que en su mejor momento es un tubo espectacular, además de que es incluso un lugar secreto panameño.',
            './sitios/morrillo.jpg',
            80.00,
            random.sample(beneficios, random.randint(3,6))
        )
    ],[
        SitioTuristico(
            'Parque Nacional Altos de Campana',
            'A tan solo unos 70 km de la Ciudad de Panamá se encuentra el parque nacional más antiguo del país, el Parque Nacional Altos de Campana. Creado en 1966, este parque cubre 4816 hectáreas en las montañas de Campana, una serranía que se eleva imponente en esta sección de la carretera panamericana',
            './sitios/campana.jpg',
            75.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'La Laguna San Carlos',
            'La Laguna de San Carlos se encuentra a unos 850 metros sobre el nivel del mar, a este misterioso lugar se le desconoce el origen, además de su profundidad, La Laguna se encuentra en las faldas del Cerro Picacho. Este lugar es ideal para desconectarse de la ciudad, del ruido, acostarse en suelo, descansar, leer un buen libro o realizar un picnic, la temperatura es súper agradable.',
            './sitios/laguna.jpg',
            120.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Punta Chame',
            'Punta Chame es un lugar popular para practicar windsurf a lo largo de la Bahía de Chame en el centro de Panamá. Está a solo una hora y media en automóvil de la ciudad de Panamá, lo que lo convierte en un lugar popular entre los adictos a la adrenalina de la ciudad. En muchos sentidos, este es un destino para escapar de todo, ya que hay poco al final de la península aparte de una escuela de windsurf, algunos alojamientos y algunas residencias.',
            './sitios/chame.jpg',
            45.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Altos del María',
            'Altos del María es la comunidad residencial de montaña más exclusiva de Panamá. Con un clima agradable, impresionantes vistas panorámicas, naturaleza exuberante, tranquilidad y con todas las comodidades que ofrece un proyecto de la ciudad.',
            './sitios/maria.jpg',
            780.00,
            random.sample(beneficios, random.randint(3,6))
        )
    ],[
        SitioTuristico(
            'Cerro Tacarcuna',
            'El cerro Tacarcuna es la máxima altura del Darién, a 1.875 msnm.Está ubicado en Panamá, en la serranía del Darién, muy cerca de la frontera entre Colombia y Panamá. Los bosques tropicales del cerro Tacarcuna son reconocidos por su elevadísima biodiversidad y por presentar gran número de endemismos. En Panamá son protegidos por el parque nacional Darién y en Colombia por el parque nacional natural de Los Katíos.',
            './sitios/tacarcuna.jpg',
            20.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Parque Nacional Darién',
            'El Parque Nacional Darién es un ambiente mágico selvático al que se puede llegar de más de una forma para apreciar impresionantes paisajes de selva virgen. Desde la Ciudad de Panamá vía aérea hasta la comunidad más cercana al Parque, Por su extraordinaria diversidad biológica y su alto valor genético, además de los grupos que guardan y practican tradiciones ancestrales, el Parque Nacional Darién fue declarado en 1981 Reserva de la Biósfera de la Humanidad.',
            './sitios/darien.jpg',
            40.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Lajas Blancas',
            'Lajas Blancas es un corregimiento de la comarca indígena panameña de Emberá-Wounaan.',
            './sitios/lajas.jpg',
            125.00,
            random.sample(beneficios, random.randint(3,6))
        )
    ],[
        SitioTuristico(
            'Archipielago de San Blas',
            'El archipiélago de San Blas está compuesto por más de trescientas islas e islotes. Se extiende desde Panamá hasta Colombia y está catalogado como uno de los tres lugares más bellos del mundo.',
            './sitios/sanblas.jpg',
            135.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Ukupseni',
            'Ukupseni es el nombre kuna del pueblo mejor conocido como Playón Chico. El pueblo está ubicado en una isla bastante cercana a la costa. Tanto así que a tierra firme la une un puente peatonal de unos 300 metros de largo.',
            './sitios/ukupseni.jpg',
            100.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Arridup',
            'La isla está a unos 40 minutos de navegación desde el Lodge, pero el trayecto vale la pena ¡y mucho! En cuanto a las playas, sencillamente insuperables. Aguas cristalinas, arenas blancas, fondo de palmeras…. En fin, se pueden empapelar muchas agencias de turismo con fotos de este sitio.',
            './sitios/arridup.jpg',
            70.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Icodub',
            'Con solo 1 hectárea aproximadamente de terreno, se puede nadar y descansar, para amigos, familias o parejas. Puedes pasar el día, acampar o hospedarte. Icodub es la isla ideal para pasar el día.',
            './sitios/icodub.jpg',
            75.00,
            random.sample(beneficios, random.randint(3,6))
        )
    ],[
        SitioTuristico(
            'Kusapín',
            'Kusapín (Sabricotte) es un distrito de la provincia indígena panameña Ngobe Bugle. Su capital es la localidad de Kusapín, tiene una superficie de 1.693,2 km2 y una población de 33.121 habitantes.',
            './sitios/kusapin.jpg',
            75.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'El Salto de la Tulivieja',
            'El Salto de La Tulivieja, es uno de los grandes atractivos turísticos que se encuentra en el distrito de Besiko, comunidad que está ubicada en la comunidad de Karicho y que pertenece al área de Soloy, en la Comarca Ngöbe Buglé.',
            './sitios/tulivieja.jpg',
            45.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Salto Qui-Qui',
            'Se localiza en la comunidad de Soloy, comarca Ngäbe Buglé. También conocida como el chorro de La Maestra debido a que en ese lugar pereció una maestra muy querida por los lugareños.',
            './sitios/quiqui.jpg',
            20.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Salto Romelio',
            'Salto romelio es uno de los saltos más impresionantes de todo el país y probablemente el segundo más alto de todo el país, con una altura de aproximadamente 200 metros.',
            './sitios/romelio.jpg',
            30.00,
            random.sample(beneficios, random.randint(3,6))
        )
    ]
]

provincias = [
    Provincia(
    'Bocas del Toro',
    'Bocas del Toro es una provincia de Panamá y su capital es la ciudad homónima de Bocas del Toro. Tiene una extensión de 4643,9 km², una población de 170,320 habitantes y sus límites: al norte con el mar Caribe, al sur con la provincia de Chiriquí, al este y sureste con la comarca Ngäbe-Buglé, al oeste y noroeste con la provincia de Limón de Costa Rica; y al suroeste con la provincia de Puntarenas de Costa Rica.',
    './provincias/bocasdeltoro.png',
    sitios[0]
    ),Provincia(
    'Coclé',
    'Coclé es una provincia del centro de Panamá. Su superficie es de 4,927km² y cuenta con 260 292 habitantes. Su capital es Penonomé. Limita al norte con la provincia de Colón, al este con la provincia de Panamá Oeste, al sur con la de Herrera y el golfo de Parita y al oeste con la de Veraguas. El centro y norte de la provincia esta accidentados por la cordillera central; al sur pertenece las llanuras centrales, tierras bajas muy fértiles que se extienden hasta el litoral.',
    './provincias/cocle.png',
    sitios[1]
    ),Provincia(
    'Colón',
    'Colón es una de las 10 provincias de la República de Panamá. Su extensión territorial es de 4.868,4 km². Su población es de 294.060 habitantes y su densidad es de 60,4 habitantes por km². En su territorio se localiza la sección norte del canal de Panamá. Limita al norte con el mar Caribe, al sur con las provincias de Panamá, Panamá Oeste y Coclé, al este con la Comarca de Guna Yala y al oeste con la provincia de Veraguas.',
    './provincias/colon.png',
    sitios[2]
    ),Provincia(
    'Chiriquí',
    'Chiriquí es una provincia de Panamá. Su capital es David. La provincia de Chiriquí se encuentra ubicada en el sector occidental de Panamá teniendo como límites al norte la provincia de Bocas del Toro y la comarca Ngäbe-Buglé, al oeste la provincia de Puntarenas (en la República de Costa Rica), al este la provincia de Veraguas y al sur el océano Pacífico.',
    './provincias/chiriqui.png',
    sitios[3]
    ),Provincia(
    'Darién',
    'Darién es una de las diez provincias de Panamá.​ Su capital es la ciudad de La Palma. Tiene una extensión de 11 896,5 km², siendo por lo tanto la más extensa del país. Está ubicada en el extremo oriental del país y limita al norte con la provincia de Panamá y la comarca Guna Yala. Al sur limita con el océano Pacífico y la República de Colombia. Al este limita con el departamento de Chocó en la República de Colombia y al oeste limita con el Océano Pacífico y la Provincia de Panamá.',
    './provincias/darien.png',
    sitios[4]
    ),Provincia(
    'Herrera',
    'Herrera es una provincia panameña situada en el norte de la península de Azuero y su cabecera es la ciudad de Chitré. Limita al norte con las provincias de Veraguas y Coclé, al sur con la provincia de Los Santos, al este con el golfo de Parita y la provincia de Los Santos y al oeste con la provincia de Veraguas concretamente con el distrito de Mariato. Tiene una extensión de 2.340,7 km² y en 2008 contaba con una población de 111.647 habitantes,​ población que se estimó en 107.911 habitantes en 2010.',
    './provincias/herrera.png',
    sitios[5]
    ),Provincia(
    'Los Santos',
    'Los Santos es una provincia panameña, situada al sureste de la península de Azuero. Las Tablas es su capital y localidad más poblada. Está compuesta por los distritos de Los Santos, Guararé, Las Tablas, Macaracas, Pedasí, Pocrí y Tonosí. Con una superficie de 3 809,4 km² y una población de 89 592 habitantes,limita al sur y al este con el océano Pacífico, al norte con el océano Pacífico y la provincia de Herrera, y al oeste con la provincia de Veraguas, concretamente con el distrito de Mariato.',
    './provincias/lossantos.png',
    sitios[6]
    ),Provincia(
    'Panamá',
    'Panamá es una de las diez provincias de Panamá.​ Su capital es la ciudad de Panamá, que es también la capital de la República. La misma tiene una superficie de 9 mil 166 km²,3​ la cual limita al norte con la provincia de Colón y la Comarca Guna Yala, al sur con el Océano Pacífico; al este con la provincia de Darién y la comarca Wargandí y al oeste con la provincia de Panamá Oeste. Panamá es la provincia más poblada del país, con 1.713.070 habitantes.',
    './provincias/panama.png',
    sitios[7]
    ),Provincia(
    'Veraguas',
    'Veraguas es una de las diez provincias de Panamá. Su capital es la ciudad de Santiago de Veraguas. Tiene una superficie de 10 629 km²,​ que en términos de extensión es similar a la de Líbano, una población de 246,280 habitantes. Limita al norte con el mar Caribe, al sur con el océano Pacífico, al este con las provincias de Colón, Coclé, Herrera, Los Santos y al oeste con la provincia de Chiriquí y la Comarca Ngäbe-Buglé. Es la única provincia de Panamá que tiene costas en los océanos Atlántico y Pacífico.',
    './provincias/bocasdeltoro.png',
    sitios[8]
    ),Provincia(
    'Panamá Oeste',
    'Panamá Oeste es una de las diez provincias de Panamá, creada el 1.º de enero de 2014 a partir de territorios segregados de la provincia de Panamá ubicados al oeste del canal de Panamá. Está conformado por 5 distritos: Arraiján, Capira, Chame, La Chorrera y San Carlos. Su capital es La Chorrera. Limita al norte con la provincia de Colón, al sur con el océano Pacífico; al este con la provincia de Panamá y al oeste con la provincia de Coclé.',
    './provincias/panamaoeste.png',
    sitios[9]
    )
]

comarcas = [
    Provincia(
    'Emberá-Wounaan',
    'Emberá-Wounaan es una comarca indígena de Panamá. Fue creada en 1983 a partir de dos enclaves ubicados en la provincia de Darién, específicamente de los distritos de Chepigana y Pinogana. Su capital es Unión Chocó. Su extensión abarca 4383,5 km² y posee una población de 9.544 habitantes,​ la mayoría de estos pertenecen a las etnias emberá y wounaan, distribuidas en 40 comunidades.',
    './provincias/embera.png',
    sitios[10]
    ),Provincia(
    'Guna Yala',
    'Guna Yala es una comarca indígena en Panamá, habitada por la etnia Guna. Antiguamente la comarca se llamaba San Blas hasta 1998 y Kuna Yala hasta 2010. Su capital es Gairgirgordub. Limita al norte con el mar Caribe, al sur con la provincia de Darién y la comarca Emberá Wounnan, al este con Colombia y al oeste con la provincia de Colón.',
    './provincias/guna.png',
    sitios[11]
    ),Provincia(
    'Ngäbe-Buglé',
    'Ngäbe-Buglé es una comarca panameña definida como una división política especial​. Limita al norte con el mar Caribe, al sur con las provincias de Chiriquí y Veraguas, al este con la provincia de Veraguas y al oeste con las provincias de Bocas del Toro y Chiriquí, contando con enclaves en la provincia de Chiriquí y Veraguas. El territorio Ngäbe-Buglé abarca un área de 6968 km² y su población se estima en 213 860 habitantes en 2018, lo que da una densidad de población de 30.7 habitantes por km².',
    './provincias/ngabe.png',
    sitios[12]
    )
]

class Ui_Reservar(object):
    def setupUi(self, Reservar, sitio_elec):
        self.sitio_elec = sitio_elec
        Reservar.setObjectName("Reservar")
        Reservar.setEnabled(True)
        Reservar.resize(800, 543)
        Reservar.setMinimumSize(QtCore.QSize(800, 543))
        Reservar.setMaximumSize(QtCore.QSize(800, 543))
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(Reservar)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 780, 521))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lb_sitio = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lb_sitio.setFont(font)
        self.lb_sitio.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_sitio.setObjectName("lb_sitio")
        self.lb_sitio.setStyleSheet('background-color: #a2c4fc')
        self.verticalLayout_3.addWidget(self.lb_sitio)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.input_nombre = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.input_nombre.setFont(font)
        self.input_nombre.setObjectName("input_nombre")
        self.verticalLayout.addWidget(self.input_nombre)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.input_cedula = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.input_cedula.setFont(font)
        self.input_cedula.setObjectName("input_cedula")
        self.verticalLayout.addWidget(self.input_cedula)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.input_edad = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.input_edad.setFont(font)
        self.input_edad.setText("")
        self.input_edad.setObjectName("input_edad")
        self.verticalLayout.addWidget(self.input_edad)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.input_nacionalidad = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.input_nacionalidad.setFont(font)
        self.input_nacionalidad.setObjectName("input_nacionalidad")
        self.verticalLayout.addWidget(self.input_nacionalidad)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.input_telefono = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.input_telefono.setFont(font)
        self.input_telefono.setText("")
        self.input_telefono.setObjectName("input_telefono")
        self.verticalLayout.addWidget(self.input_telefono)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.input_acompanantes = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.input_acompanantes.setFont(font)
        self.input_acompanantes.setText("")
        self.input_acompanantes.setObjectName("input_acompanantes")
        self.verticalLayout.addWidget(self.input_acompanantes)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 250)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.check_abono = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.check_abono.setFont(font)
        self.check_abono.setObjectName("check_abono")
        self.check_abono.stateChanged.connect(lambda:self.check())
        self.verticalLayout_2.addWidget(self.check_abono)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.input_abono = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        self.input_abono.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.input_abono.setFont(font)
        self.input_abono.setText("")
        self.input_abono.setObjectName("input_abono")
        self.verticalLayout_2.addWidget(self.input_abono)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_pagar = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_pagar.setFont(font)
        self.btn_pagar.setObjectName("btn_pagar")
        self.btn_pagar.clicked.connect(lambda:self.pagar(Reservar))
        self.horizontalLayout_2.addWidget(self.btn_pagar)
        self.btn_abonar = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btn_abonar.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_abonar.setFont(font)
        self.btn_abonar.setObjectName("btn_abonar")
        self.btn_abonar.clicked.connect(lambda:self.abonar(Reservar))
        self.horizontalLayout_2.addWidget(self.btn_abonar)
        self.btn_salir = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_salir.setFont(font)
        self.btn_salir.setStyleSheet("color: rgb(255, 255, 255);\n"
        "background-color: rgb(255, 35, 39);")
        self.btn_salir.setObjectName("btn_salir")
        self.btn_salir.clicked.connect(Reservar.close)
        self.horizontalLayout_2.addWidget(self.btn_salir)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Reservar)
        QtCore.QMetaObject.connectSlotsByName(Reservar)

    def check(self):
        self.btn_pagar.setEnabled(not self.btn_pagar.isEnabled())
        self.btn_abonar.setEnabled(not self.btn_abonar.isEnabled())
        self.input_abono.setEnabled(not self.input_abono.isEnabled())

    def abonar(self, Reservar):
        nombre = self.input_nombre.text()
        cedula = self.input_cedula.text()
        edad = self.input_edad.text()
        nacionalidad = self.input_nacionalidad.text()
        telefono = self.input_telefono.text()
        acompañantes = self.input_acompanantes.text()
        precio = self.sitio_elec.precio
        abono = self.input_abono.text()
        msg = QMessageBox()
        if('' not in {nombre, cedula, edad, nacionalidad, telefono, acompañantes, abono}):
            if precio*(1+int(acompañantes)) >= 2000:
               descuento = precio * 0.05
            else:
                descuento = 0 
            if int(edad) >= 60:
                descuentoTotal = descuento + ((precio-descuento)*0.1)
            else:
                descuentoTotal = descuento + 0
            subtotal = precio - descuentoTotal
            total = subtotal * (1 + int(acompañantes))
            descuentoTotal = descuentoTotal *(1 + int(acompañantes)) 
            compras.append(Compra(self.sitio_elec.nombre, nombre, nacionalidad, cedula, edad, int(acompañantes)+1, float(abono), descuentoTotal, True))
            msg.setWindowTitle('Abono Exitoso')
            msg.setText(f'Abono para {self.sitio_elec.nombre} realizado exitosamente')
            msg.setIcon(QMessageBox.Information)
            msg.setInformativeText(f'Abono para {self.sitio_elec.nombre} por {float(abono):.2f}$ a nombre de {nombre} realizado. ')
            msg.setDetailedText(f'Subtotal: {precio:.2f}$'+
                f'\nTotal: {total:.2f}\nCantidad Abonada: {float(abono):.2f}$'
                f'\nPago Restante: {(total-float(abono)):.2f}$\nNombre: {nombre}'+
                f'\nCedula: {cedula}\nTelefono: {telefono}'+
                f'\nEdad: {edad}\nNacionalidad: {nacionalidad}'+
                f'\nCupos Abonados: {int(acompañantes)+1}')
            Reservar.close()
        else:
            msg.setWindowTitle('Reserva Fallida')
            msg.setText('Advertencia')
            msg.setIcon(QMessageBox.Warning)
            msg.setInformativeText('Debe llenar todos los campos')
        x = msg.exec_()

    def pagar(self, Reservar):
        nombre = self.input_nombre.text()
        cedula = self.input_cedula.text()
        edad = self.input_edad.text()
        nacionalidad = self.input_nacionalidad.text()
        telefono = self.input_telefono.text()
        acompañantes = self.input_acompanantes.text()
        precio = self.sitio_elec.precio
        
        msg = QMessageBox()
        if('' not in {nombre, cedula, edad, nacionalidad, telefono, acompañantes}):
            if precio*(1+int(acompañantes)) >= 2000:
               descuento = precio * 0.05
            else:
                descuento = 0 
            if int(edad) >= 60:
                descuentoTotal = descuento + ((precio-descuento)*0.1)
            else:
                descuentoTotal = descuento + 0
            subtotal = precio - descuentoTotal
            total = subtotal * (1 + int(acompañantes))
            descuentoTotal = descuentoTotal *(1 + int(acompañantes)) 
            compras.append(Compra(self.sitio_elec.nombre, nombre, nacionalidad, cedula, edad, int(acompañantes)+1, total, descuentoTotal, False))
            msg.setWindowTitle('Reserva Exitosa')
            msg.setText(f'Reserva para {self.sitio_elec.nombre} realizada exitosamente')
            msg.setIcon(QMessageBox.Information)
            msg.setInformativeText(f'Reserva de {self.sitio_elec.nombre} por {total:.2f}$ a nombre de {nombre} realizado.')
            msg.setDetailedText(f'Subtotal: {(precio*(1+int(acompañantes))):.2f}$'+
                f'\nTotal: {total:.2f}$'+
                f'\nDescuento: {descuentoTotal:.2f}$\nNombre: {nombre}'+
                f'\nCedula: {cedula}\nTelefono: {telefono}'+
                f'\nEdad: {edad}\nNacionalidad: {nacionalidad}'+
                f'\nCupos Reservados: {int(acompañantes)+1}')
            Reservar.close()
        else:
            msg.setWindowTitle('Reserva Fallida')
            msg.setText('Advertencia')
            msg.setIcon(QMessageBox.Warning)
            msg.setInformativeText('Debe llenar todos los campos')
        x = msg.exec_()

    def retranslateUi(self, Reservar):
        _translate = QtCore.QCoreApplication.translate
        Reservar.setWindowTitle(_translate("Reservar", "Form"))
        self.lb_sitio.setText(_translate("Reservar", f"Reservar: {self.sitio_elec.nombre} por {self.sitio_elec.precio:.2f}$ c/u"))
        self.label_2.setText(_translate("Reservar", "Nombre"))
        self.input_nombre.setPlaceholderText(_translate("Reservar", "Nombre"))
        self.label_4.setText(_translate("Reservar", "Cedula"))
        self.input_cedula.setPlaceholderText(_translate("Reservar", "Cedula"))
        self.label_5.setText(_translate("Reservar", "Edad"))
        self.input_edad.setPlaceholderText(_translate("Reservar", "Edad"))
        self.label_3.setText(_translate("Reservar", "Nacionalidad"))
        self.input_nacionalidad.setPlaceholderText(_translate("Reservar", "Nacionalidad"))
        self.label_6.setText(_translate("Reservar", "Telefono"))
        self.input_telefono.setPlaceholderText(_translate("Reservar", "Telefono"))
        self.label_7.setText(_translate("Reservar", "Cantidad de Acompañantes"))
        self.input_acompanantes.setPlaceholderText(_translate("Reservar", "Acompañantes"))
        self.check_abono.setText(_translate("Reservar", "Abonar?"))
        self.label_8.setText(_translate("Reservar", "Cantidad de Abono"))
        self.input_abono.setPlaceholderText(_translate("Reservar", "Cantidad de Abono"))
        self.btn_pagar.setText(_translate("Reservar", "Pagar"))
        self.btn_abonar.setText(_translate("Reservar", "Abonar"))
        self.btn_salir.setText(_translate("Reservar", "Salir"))

class Ui_sitio(object):
    def setupUi(self, sitio, sitio_elec, Reservar):
        self.sitio_elec = sitio_elec
        self.Reservar = Reservar
        sitio.setObjectName("sitio")
        sitio.resize(773, 580)
        sitio.setMinimumSize(QtCore.QSize(773, 580))
        sitio.setMaximumSize(QtCore.QSize(773, 580))
        self.widget = QtWidgets.QWidget(sitio)
        self.widget.setGeometry(QtCore.QRect(30, 50, 461, 504))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lb_sitio = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lb_sitio.setFont(font)
        self.lb_sitio.setAlignment(QtCore.Qt.AlignCenter)
        self.lb_sitio.setObjectName("lb_sitio")
        self.lb_sitio.setStyleSheet("background-color: #ffffff")
        self.gridLayout.addWidget(self.lb_sitio, 0, 0, 1, 2)
        self.foto_sitio = QtWidgets.QLabel(self.widget)
        self.foto_sitio.setText("")
        self.foto_sitio.setPixmap(QtGui.QPixmap(self.sitio_elec.imagen))
        self.foto_sitio.setScaledContents(True)
        self.foto_sitio.setObjectName("foto_sitio")
        self.gridLayout.addWidget(self.foto_sitio, 1, 0, 1, 2)
        self.desc_sitio = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(12)
        self.desc_sitio.setFont(font)
        self.desc_sitio.setTextFormat(QtCore.Qt.AutoText)
        self.desc_sitio.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.desc_sitio.setWordWrap(True)
        self.desc_sitio.setObjectName("desc_sitio")
        self.desc_sitio.setStyleSheet('background-color: #ffffff')
        self.gridLayout.addWidget(self.desc_sitio, 2, 0, 1, 2)
        self.btn_reservar = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_reservar.setFont(font)
        self.btn_reservar.setObjectName("btn_reservar")
        self.btn_reservar.clicked.connect(lambda:self.reservar())
        self.gridLayout.addWidget(self.btn_reservar, 3, 0, 1, 1)
        self.btn_salir = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_salir.setFont(font)
        self.btn_salir.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 23, 27);")
        self.btn_salir.setObjectName("btn_salir")
        self.btn_salir.clicked.connect(sitio.close)
        self.gridLayout.addWidget(self.btn_salir, 3, 1, 1, 1)
        self.widget1 = QtWidgets.QWidget(sitio)
        self.widget1.setGeometry(QtCore.QRect(500, 50, 258, 501))
        self.widget1.setObjectName("widget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lb_beneficios = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lb_beneficios.setFont(font)
        self.lb_beneficios.setObjectName("lb_beneficios")
        self.gridLayout_2.addWidget(self.lb_beneficios, 0, 0, 1, 1)
        self.lista_beneficios = QtWidgets.QListWidget(self.widget1)
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lista_beneficios.setFont(font)
        self.lista_beneficios.setObjectName("lista_beneficios")
        self.setBeneficios()
        self.gridLayout_2.addWidget(self.lista_beneficios, 1, 0, 1, 1)

        self.retranslateUi(sitio)
        QtCore.QMetaObject.connectSlotsByName(sitio)

    def setBeneficios(self):
        _translate = QtCore.QCoreApplication.translate
        i = 0
        for beneficio in self.sitio_elec.beneficios:
            item = QtWidgets.QListWidgetItem()
            self.lista_beneficios.addItem(item)
            item = self.lista_beneficios.item(i)
            item.setText(_translate('sitio', beneficio))
            i += 1

    def reservar(self):
        rui = Ui_Reservar()
        rui.setupUi(self.Reservar, self.sitio_elec)
        self.Reservar.show()

    def retranslateUi(self, sitio):
        _translate = QtCore.QCoreApplication.translate
        sitio.setWindowTitle(_translate("sitio", "Form"))
        self.lb_sitio.setText(_translate("sitio", self.sitio_elec.nombre))
        self.desc_sitio.setText(_translate("sitio", "\n"+self.sitio_elec.descripcion))
        self.btn_reservar.setText(_translate("sitio", "Reservar"))
        self.btn_salir.setText(_translate("sitio", "Salir"))
        self.lb_beneficios.setText(_translate("sitio", "Beneficios"))
        __sortingEnabled = self.lista_beneficios.isSortingEnabled()
        self.lista_beneficios.setSortingEnabled(False)

        
        self.lista_beneficios.setSortingEnabled(__sortingEnabled)


class Ui_provincias(object):

    def setupUi(self, provincias, prov_elec, Sitio, Reservar):
        self.Sitio = Sitio
        self.Reservar = Reservar
        self.prov_elec = prov_elec
        provincias.setObjectName("provincias")
        provincias.resize(698, 442)
        provincias.setMinimumSize(QtCore.QSize(698, 442))
        provincias.setMaximumSize(QtCore.QSize(698, 442))
        self.verticalLayoutWidget = QtWidgets.QWidget(provincias)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 20, 650, 394))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.provincia_nombre = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.provincia_nombre.setFont(font)
        self.provincia_nombre.setAlignment(QtCore.Qt.AlignCenter)
        self.provincia_nombre.setObjectName("provincia_nombre")
        self.provincia_nombre.setStyleSheet("background-color:#ffffff")
        self.provincia_nombre.clear()
        self.verticalLayout.addWidget(self.provincia_nombre)
        self.provincia_foto = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.provincia_foto.setText("")
        self.provincia_foto.setPixmap(QtGui.QPixmap(""))
        self.provincia_foto.setPixmap(QtGui.QPixmap(self.prov_elec.imagen))
        self.provincia_foto.setScaledContents(True)
        self.provincia_foto.setObjectName("provincia_foto")
        self.verticalLayout.addWidget(self.provincia_foto)
        self.lista_sitios = QtWidgets.QComboBox(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(16)
        self.lista_sitios.setFont(font)
        self.lista_sitios.setObjectName("lista_sitios")
        self.createComboBox()
        self.verticalLayout.addWidget(self.lista_sitios)

        self.retranslateUi(provincias)
        QtCore.QMetaObject.connectSlotsByName(provincias)


    def createComboBox(self):
        self.x = None
        _translate = QtCore.QCoreApplication.translate
        i = 0
        self.provincia_nombre.clear()
        self.provincia_nombre.setText(_translate("provincias", self.prov_elec.nombre))
        for sitio in self.prov_elec.sitios:
            self.lista_sitios.addItem('')
            self.lista_sitios.setItemText(i, _translate("provincias", sitio.nombre))
            self.lista_sitios.activated.connect(self.elegir)
            i += 1
        self.lista_sitios.activated.connect(lambda:self.seeSites())

    def elegir(self):
        self.x = self.lista_sitios.currentIndex()

    def seeSites(self):
        sitio_elec = self.prov_elec.sitios[self.x]
        ui = Ui_sitio()
        ui.setupUi(self.Sitio, sitio_elec, self.Reservar)
        self.Sitio.show()

    def retranslateUi(self, provincias):
        _translate = QtCore.QCoreApplication.translate
        provincias.setWindowTitle(_translate("provincias", "Form"))

class Ui_main(object):
    def setupUi(self, main, Provincias, sitio, Reservar):
        self.Provincias = Provincias
        self.Sitio = sitio
        self.Reservar = Reservar
        main.setObjectName("main")
        main.resize(481, 221)
        main.setMinimumSize(QtCore.QSize(481, 221))
        main.setMaximumSize(QtCore.QSize(481, 221))
        main.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(main)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 10, 481, 191))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.list_comarcas = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(14)
        self.list_comarcas.setFont(font)
        self.list_comarcas.setObjectName("list_comarcas")
        self.gridLayout.addWidget(self.list_comarcas, 1, 1, 1, 1)
        self.list_provincias = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(14)
        self.list_provincias.setFont(font)
        self.list_provincias.setObjectName("list_provincias")
        self.createComboBox()
        self.gridLayout.addWidget(self.list_provincias, 1, 0, 1, 1)
        self.lb1 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lb1.setFont(font)
        self.lb1.setScaledContents(True)
        self.lb1.setAlignment(QtCore.Qt.AlignCenter)
        self.lb1.setObjectName("lb1")
        self.gridLayout.addWidget(self.lb1, 0, 0, 1, 2)
        self.bt_salir = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.bt_salir.setFont(font)
        self.bt_salir.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 20, 32);")
        self.bt_salir.setFlat(False)
        self.bt_salir.setObjectName("bt_salir")
        self.bt_salir.clicked.connect(lambda:self.quit(main))
        self.gridLayout.addWidget(self.bt_salir, 3, 0, 1, 2)
        self.gridLayout.setRowStretch(0, 5)
        self.gridLayout.setRowStretch(1, 5)
        self.gridLayout.setRowStretch(2, 5)
        self.gridLayout.setRowStretch(3, 5)
        main.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(main)
        self.statusbar.setObjectName("statusbar")
        main.setStatusBar(self.statusbar)

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def quit(self, main):
        cant = 0
        total = 0
        res = 0
        cant_res = 0
        ab = 0
        cant_ab = 0
        msg = QMessageBox()
        msg.setWindowTitle('Gracias por su Visita')
        if compras:
            for compra in compras:
                total += compra.pago
                cant += compra.cantidad
                if compra.abono:
                    ab += compra.pago
                    cant_ab += compra.cantidad
                else:
                    res += compra.pago
                    cant_res += compra.cantidad
            msg.setText(f'Informacion de Reservas')
            msg.setIcon(QMessageBox.Information)
            msg.setInformativeText(f'Cupos Solicitados: {cant}\nTotal Pagado: {total:.2f}$')
            msg.setDetailedText(f'Cupos Solicitados: {cant}\nTotal Pagado: {total:.2f}$'+
                f'\nCantidad de Abonos: {cant_ab}\n Total de Abonos: {ab:.2f}$'+
                f'\nCantidad de Reservas: {cant_res}\n Total de Reservas: {res:.2f}$ ')
        else:
            msg.setText('Gracias por su Atención')
        x = msg.exec_()
        main.close()

    def createComboBox(self):
        _translate = QtCore.QCoreApplication.translate
        i = 0
        self.x = None
        y = 0
        for estado in provincias:
            self.list_provincias.addItem('')
            self.list_provincias.setItemText(i, _translate("main", estado.nombre))
            self.list_provincias.activated.connect(lambda:self.elegir(self.list_provincias))
            i += 1
        i = 0
        for comarca in comarcas:
            self.list_comarcas.addItem('')
            self.list_comarcas.setItemText(i, _translate("main", comarca.nombre))
            self.list_comarcas.activated.connect(lambda:self.elegir(self.list_comarcas))
            i += 1
        self.list_provincias.activated.connect(lambda:self.seeProv(self.x, 0))
        self.list_comarcas.activated.connect(lambda:self.seeProv(self.x, 1))


    def elegir(self, lista):
        self.x = lista.currentIndex()

    def seeProv(self, provincia, tipo):
        if tipo==0:
            prov_elec = provincias[provincia]
        elif tipo==1:
            prov_elec = comarcas[provincia]
        pui = Ui_provincias()
        pui.setupUi(self.Provincias, prov_elec, self.Sitio, self.Reservar)
        Provincias.show()

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "MainWindow"))
        self.lb1.setText(_translate("main", "Actividades Turisticas en Panamá"))
        self.bt_salir.setText(_translate("main", "Salir"))


class Ui_Presentacion(object):
    def setupUi(self, Presentacion, main):
        Presentacion.setObjectName("Presentacion")
        Presentacion.resize(564, 690)
        self.presentacion = QtWidgets.QLabel(Presentacion)
        self.presentacion.setGeometry(QtCore.QRect(0, 0, 561, 611))
        self.presentacion.setText("")
        self.presentacion.setPixmap(QtGui.QPixmap("presentacion.png"))
        self.presentacion.setScaledContents(True)
        self.presentacion.setObjectName("presentacion")
        self.btn_cont = QtWidgets.QPushButton(Presentacion)
        self.btn_cont.setGeometry(QtCore.QRect(400, 610, 151, 71))
        font = QtGui.QFont()
        font.setFamily("SansSerif")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btn_cont.setFont(font)
        self.btn_cont.setObjectName("btn_cont")
        self.btn_cont.clicked.connect(lambda:self.continuar(main, Presentacion))

        self.retranslateUi(Presentacion)
        QtCore.QMetaObject.connectSlotsByName(Presentacion)

    def continuar(self, main, Presentacion):
        main.show()
        Presentacion.close()
        
    def retranslateUi(self, Presentacion):
        _translate = QtCore.QCoreApplication.translate
        Presentacion.setWindowTitle(_translate("Presentacion", "Presentación"))
        self.btn_cont.setText(_translate("Presentacion", "Continuar"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Reservar = QtWidgets.QWidget()
    sitio = QtWidgets.QWidget()
    Provincias = QtWidgets.QWidget()
    main = QtWidgets.QMainWindow()
    ui = Ui_main()
    ui.setupUi(main, Provincias, sitio, Reservar)
    Presentacion = QtWidgets.QWidget()
    pui = Ui_Presentacion()
    pui.setupUi(Presentacion, main)
    Presentacion.show()
    sys.exit(app.exec_())
