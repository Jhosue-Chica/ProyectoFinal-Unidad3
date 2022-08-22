'''Se importa la libreria de mongo ya que python necesita un driver para
acceder a la base de datos de MongoDB'''
import pymongo

MONGO_HOST="localhost"
MONGO_PUERTO="27017"
MONGO_TIEMPO_FUERA=1000
'''Seleccionar la direcion especifica de la base'''
MONGO_URI="mongodb://"+MONGO_HOST+":"+MONGO_PUERTO+"/"
'''Seleccionar la base de datos especifica'''
MONGO_BASEDATOS="dbCheckJob"
'''Seleccionar la colleccion especifica'''
MONGO_COLECCION="registro"
'''Instanciacion de objeto a partir de la clase pymongo'''
cliente=pymongo.MongoClient(MONGO_URI,serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
'''Especificacion de la base de datos'''
baseDatos=cliente[MONGO_BASEDATOS]
'''Especificacion de la coleccion'''
coleccion=baseDatos[MONGO_COLECCION]

def guardar_registro(nombre, ide, telefono, provincia, canton, codigoPostal, direccion, correo, accion):
    micliente = pymongo.MongoClient("mongodb://localhost:27017/")
    midb = micliente["dbCheckJob"] #base de datos
    micol=midb["registro"] #coleccion
    '''Crear un dicionario e insertarlo dentro de la coleccion'''
    midiccionario = { "_id" : ide,
                        "nombre" : nombre,
                        "codigo" : codigoPostal,
                        "direccion" : direccion,
                        "telefono" : telefono,
                        "provincia" : provincia,
                        "canton" : canton,
                        "correo" : correo,
                        "accion" : accion} #diccionario
    micol.insert_one(midiccionario) #insertar el documento a la coleccion

def guardar_aspirante(nombre, edad, cedula, telefono, provincia, canton, codigoPostal, direccion,correo, usuario, clave):
    micliente = pymongo.MongoClient("mongodb://localhost:27017/")
    midb = micliente["dbCheckJob"] #base de datos
    micol=midb["aspirantes"] #coleccion
    '''Crear un dicionario e insertarlo dentro de la coleccion'''
    midiccionario = { "_id" : cedula,
                        "nombre" : nombre,
                        "edad" : edad,
                        "codigo" : codigoPostal,
                        "direccion" : direccion,
                        "telefono" : telefono,
                        "provincia" : provincia,
                        "canton" : canton,
                        "correo" : correo,
                        "usuario" : usuario,
                        "clave" : clave} #diccionario
    micol.insert_one(midiccionario) #insertar el documento a la coleccion

def guardar_empresa(nombre, RUC, telefono, provincia, canton, codigoPostal, direccion, correo, usuario, clave):
    micliente = pymongo.MongoClient("mongodb://localhost:27017/")
    midb = micliente["dbCheckJob"] #base de datos
    micol=midb["empresas"] #coleccion
    '''Crear un dicionario e insertarlo dentro de la coleccion'''
    midiccionario = { "_id" : RUC,
                        "nombre" : nombre,
                        "codigo" : codigoPostal,
                        "direccion" : direccion,
                        "telefono" : telefono,
                        "provincia" : provincia,
                        "canton" : canton,
                        "correo" : correo,
                        "usuario" : usuario,
                        "clave" : clave} #diccionario
    micol.insert_one(midiccionario) #insertar el documento a la coleccion

provinciasEC=['Azuay', 
            'Bolívar',
            'Cañar',
            'Carchi',
            'Chimborazo',
            'Cotopaxi',
            'El Oro',
            'Esmeraldas',
            'Galápagos',
            'Guayas',
            'Imbabura',
            'Loja',
            'Los Ríos',
            'Manabí',
            'Morona Santiago',
            'Napo',
            'Orellana',
            'Pastaza',
            'Pichincha',
            'Santa Elena',
            'Santo Domingo de los Tsáchilas	',
            'Sucumbíos',
            'Tungurahua',
            'Zamora Chinchipe',
            ' ']

cantonesEC=[["Cantón Sevilla de Oro","Cantón Paute","Cantón Guachapala","Cantón El Pan","Cantón Gualaceo","Cantón Chordeleg","Cantón Sígsig","Cantón Cuenca","Cantón Santa Isabel","Cantón Pucará","Cantón Camilo Ponce Enríquez","Cantón San Fernando","Cantón Girón","Cantón Nabón","Cantón Oña"], # Azuay
            ["Cantón Guaranda","Cantón Las Naves","Cantón Echeandía","Cantón Caluma","Cantón Chimbo","Cantón San Miguel","Cantón Chillanes"], # Bolívar
            ["Cantón La Troncal","Cantón Cañar","Cantón Suscal","Cantón El Tambo","Cantón Azogues","Cantón Biblián","Cantón Déleg"], # Cañar
            ["Cantón Tulcán","Cantón Mira","Cantón Espejo","Cantón Montúfar","Cantón San Pedro de Huaca","Cantón Bolívar (Carchi)"], # Carchi
            ["Cantón Guano","Cantón Penipe","Cantón Riobamba","Cantón Colta","Cantón Chambo","Cantón Pallatanga","Cantón Guamote","Cantón Alausí","Cantón Cumandá","Cantón Chunchi"], #Chimborazo
            ["Cantón Sigchos","Cantón La Maná","Cantón Latacunga","Cantón Saquisilí","Cantón Pujilí","Cantón Pangua","Cantón Salcedo"], # Cotopaxi
            ["Cantón El Guabo","Cantón Machala","Cantón Pasaje","Cantón Chilla","Cantón Zaruma","Cantón Santa Rosa","Cantón Atahualpa","Cantón Arenillas","Cantón Huaquillas","Cantón Las Lajas","Cantón Marcabelí","Cantón Balsas","Cantón Piñas","Cantón Portovelo"], # El Oro
            ["Cantón San Lorenzo","Cantón Eloy Alfaro","Cantón Rioverde","Cantón Esmeraldas","Cantón Muisne","Cantón Atacames","Cantón Quinindé"], # Esmeraldas
            ["Cantón Isabela","Cantón San Cristóbal","Cantón Santa Cruz"], # Galápagos
            ["Cantón El Empalme","Cantón Balzar","Cantón Colimes","Cantón Palestina","Cantón Santa Lucía","Cantón Pedro Carbo","Cantón Isidro Ayora","Cantón Lomas de Sargentillo","Cantón Nobol","Cantón Daule","Cantón Salitre","Cantón Samborondón","Cantón Yaguachi","Cantón Alfredo Baquerizo Moreno","Cantón Milagro","Cantón Simón Bolívar","Cantón Naranjito","Cantón General Antonio Elizalde","Cantón Coronel Marcelino Maridueña","Cantón El Triunfo","Cantón Durán","Cantón Guayaquil","Cantón Playas","Cantón Naranjal","Cantón Balao"], # Guayas
            ["Cantón Ibarra","Cantón San Miguel de Urcuquí","Cantón Cotacachi","Cantón Antonio Ante","Cantón Otavalo","Cantón Pimampiro"], # Imbabura
            ["Cantón Saraguro","Cantón Loja","Cantón Chaguarpamba","Cantón Olmedo (Loja)","Cantón Catamayo","Cantón Paltas","Cantón Puyango","Cantón Pindal","Cantón Celica","Cantón Zapotillo","Cantón Macará","Cantón Sozoranga","Cantón Calvas","Cantón Gonzanamá","Cantón Quilanga","Cantón Espíndola"], # Loja
            ["Cantón Buena Fe","Cantón Valencia","Cantón Quevedo","Cantón Quinsaloma","Cantón Palenque","Cantón Mocache","Cantón Ventanas","Cantón Vinces","Cantón Baba","Cantón Puebloviejo","Cantón Urdaneta","Cantón Babahoyo","Cantón Montalvo"], # Los Ríos
            ["Cantón Pedernales","Cantón Chone","Cantón Flavio Alfaro","Cantón El Carmen","Cantón Jama","Cantón San Vicente","Cantón Sucre","Cantón Tosagua","Cantón Rocafuerte","Cantón Junín","Cantón Bolívar (Manabí)","Cantón Pichincha","Cantón Portoviejo","Cantón Jaramijó","Cantón Manta","Cantón Montecristi","Cantón Santa Ana","Cantón Jipijapa","Cantón Veinticuatro de Mayo","Cantón Olmedo (Manabí)","Cantón Puerto López","Cantón Paján"], # Manabí
            ["Cantón Palora","Cantón Pablo Sexto","Cantón Huamboya","Cantón Morona","Cantón Taisha","Cantón Sucúa","Cantón Santiago","Cantón Logroño","Cantón Tiwintza","Cantón Limón Indanza","Cantón San Juan Bosco","Cantón Gualaquiza"], # Morona Santiago
            ["Cantón El Chaco","Cantón Quijos","Cantón Archidona","Cantón Tena","Cantón Carlos Julio Arosemena Tola"], # Napo
            ["Cantón Loreto","Cantón Francisco de Orellana","Cantón La Joya de los Sachas","Cantón Aguarico"], # Orellana
            ["Cantón Mera","Cantón Santa Clara","Cantón Arajuno","Cantón Pastaza"], # Pastaza
            ["Cantón Puerto Quito","Cantón Pedro Vicente Maldonado","Cantón San Miguel de Los Bancos","Distrito Metropolitano de Quito","Cantón Pedro Moncayo","Cantón Cayambe","Cantón Rumiñahui","Cantón Mejía"], # Pichincha
            ["Cantón Santa Elena","Cantón La Libertad","Cantón Salinas"], # Santa Elena
            ["Cantón La Concordia","Cantón Santo Domingo"], # Santo Domingo de los Tsáchilas
            ["Cantón Sucumbíos","Cantón Gonzalo Pizarro","Cantón Cascales","Cantón Lago Agrio","Cantón Putumayo","Cantón Cuyabeno","Cantón Shushufindi"], # Sucumbíos
            ["Cantón Ambato","Cantón Píllaro","Cantón Patate","Cantón Baños","Cantón Pelileo","Cantón Cevallos","Cantón Tisaleo","Cantón Mocha","Cantón Quero"], # Tungurahua
            ["Cantón Yacuambi","Cantón Yantzaza","Cantón El Pangui","Cantón Zamora","Cantón Centinela del Cóndor","Cantón Paquisha","Cantón Nangaritza","Cantón Palanda","Cantón Chinchipe"], # Zamora Chinchipe
            [" "," "]]
