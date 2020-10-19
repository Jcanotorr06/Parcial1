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
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/zapatilla.jpg',
            110.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Isla Colón',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/iscolon.jpg',
            175.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Parque Internacional La Amistad',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/amistad.jpg',
            75.00,
            random.sample(beneficios, random.randint(3,6))
        )
    ],[
        SitioTuristico(
            'Valle de Antón',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/anton.jpg',
            125.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Riviera Pacifica',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/riviera.jpg',
            140.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Parque Arqueologico El Caño',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/caño.jpg',
            80.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'El Copé',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/cope.jpg',
            79.00,
            random.sample(beneficios, random.randint(3,6))
        )
    ],[
        SitioTuristico(
            'Portobelo',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/portobelo.jpg',
            210.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Isla Grande',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/grande.jpg',
            200.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'San Lorenzo',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/lorenzo.jpg',
            110.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Cayo Tortuga',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/tortuga.jpg',
            100.00,
            random.sample(beneficios, random.randint(3,6))
        )
    ],[
        SitioTuristico(
            'Volcán Barú',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/baru.jpg',
            250.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Boquete',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/boquete.jpg',
            210.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Tierras Altas',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/altas.jpg',
            190.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Golfo de Chiriquí',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/golfochiriqui.jpg',
            140.00,
            random.sample(beneficios, random.randint(3,6))
        )
    ],[
        SitioTuristico(
            'Parque Nacional Darien',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/darien.jpg',
            105.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Yaviza',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/yaviza.jpg',
            200.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Garachine',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/garachine.jpg',
            195.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'La Palma',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/palma.jpg',
            120.00,
            random.sample(beneficios, random.randint(3,6))
        )
    ],[
        SitioTuristico(
            'Museo de Arte Religioso Colonial',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/colonial.jpg',
            98.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Parque nacional de Sarigua',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/sarigua.jpg',
            84.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Arena de Herrera',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/arena.jpg',
            115.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Reserva Forestal el Montuoso',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/montuoso.jpg',
            130.00,
            random.sample(beneficios, random.randint(3,6))
        )
    ],[
        SitioTuristico(
            'Playa Venao',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/venao.jpg',
            230.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Parque Nacional Cerro Hoya',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/hoya.jpg',
            155.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Playa El Arenal',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/arenal.jpg',
            110.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Isla Iguana',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/iguana.jpg',
            110.00,
            random.sample(beneficios, random.randint(3,6))
        )
    ],[
        SitioTuristico(
            'Isla Taboga',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/taboga.jpg',
            145.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Panamá Viejo',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/viejo.jpg',
            65.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Casco Antiguo',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/antiguo.jpg',
            270.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Canal de Panama',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/canal.jpg',
            90.00,
            random.sample(beneficios, random.randint(3,6))
        )
    ],[
        SitioTuristico(
            'Parque Nacional Coiba',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/coiba.jpg',
            35.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Santa Fe',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/santa.jpg',
            65.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'La Yeguada',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/yeguada.jpg',
            95.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Playa Morillo',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/morrillo.jpg',
            80.00,
            random.sample(beneficios, random.randint(3,6))
        )
    ],[
        SitioTuristico(
            'Parque Nacional Altos de Campana',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/campana.jpg',
            75.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'La Laguna San Carlos',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/laguna.jpg',
            120.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Punta Chame',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/chame.jpg',
            45.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Altos del María',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/maria.jpg',
            780.00,
            random.sample(beneficios, random.randint(3,6))
        )
    ],[
        SitioTuristico(
            'Cerro Tacarcuna',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/tacarcuna.jpg',
            20.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Parque Nacional Darién',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/darien.jpg',
            40.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Lajas Blancas',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/lajas.jpg',
            125.00,
            random.sample(beneficios, random.randint(3,6))
        )
    ],[
        SitioTuristico(
            'Archipielago de San Blas',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/sanblas.jpg',
            135.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Ukupseni',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/ukupseni.jpg',
            100.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Arridup',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/arridup.jpg',
            70.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Icodub',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/icodub.jpg',
            75.00,
            random.sample(beneficios, random.randint(3,6))
        )
    ],[
        SitioTuristico(
            'Kusapín',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/kusapin.jpg',
            75.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'El Salto de la Tulivieja',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/tulivieja.jpg',
            45.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Salto Qui-Qui',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
            './sitios/canal.quiqui',
            20.00,
            random.sample(beneficios, random.randint(3,6))
        ),
        SitioTuristico(
            'Salto Romelio',
            'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean eu nisi sit amet mi euismod porta. In vehicula nisi nec rutrum faucibus. Nullam at tempor est. Quisque ac tincidunt neque, placerat facilisis ex. Maecenas pharetra ipsum sit amet lectus rutrum, id laoreet elit venenatis. Ut tempus ex nunc, id blandit enim viverra ut. In lacinia tristique rhoncus. Mauris dapibus nisl in risus vehicula efficitur. Ut eget ante in sem mollis finibus sed id nunc.',
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Reservar = QtWidgets.QWidget()
    sitio = QtWidgets.QWidget()
    Provincias = QtWidgets.QWidget()
    main = QtWidgets.QMainWindow()
    ui = Ui_main()
    ui.setupUi(main, Provincias, sitio, Reservar)
    main.show()
    sys.exit(app.exec_())
