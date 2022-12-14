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
            'Bol??var',
            'Ca??ar',
            'Carchi',
            'Chimborazo',
            'Cotopaxi',
            'El Oro',
            'Esmeraldas',
            'Gal??pagos',
            'Guayas',
            'Imbabura',
            'Loja',
            'Los R??os',
            'Manab??',
            'Morona Santiago',
            'Napo',
            'Orellana',
            'Pastaza',
            'Pichincha',
            'Santa Elena',
            'Santo Domingo de los Ts??chilas	',
            'Sucumb??os',
            'Tungurahua',
            'Zamora Chinchipe',
            ' ']

cantonesEC=[["Cant??n Sevilla de Oro","Cant??n Paute","Cant??n Guachapala","Cant??n El Pan","Cant??n Gualaceo","Cant??n Chordeleg","Cant??n S??gsig","Cant??n Cuenca","Cant??n Santa Isabel","Cant??n Pucar??","Cant??n Camilo Ponce Enr??quez","Cant??n San Fernando","Cant??n Gir??n","Cant??n Nab??n","Cant??n O??a"], # Azuay
            ["Cant??n Guaranda","Cant??n Las Naves","Cant??n Echeand??a","Cant??n Caluma","Cant??n Chimbo","Cant??n San Miguel","Cant??n Chillanes"], # Bol??var
            ["Cant??n La Troncal","Cant??n Ca??ar","Cant??n Suscal","Cant??n El Tambo","Cant??n Azogues","Cant??n Bibli??n","Cant??n D??leg"], # Ca??ar
            ["Cant??n Tulc??n","Cant??n Mira","Cant??n Espejo","Cant??n Mont??far","Cant??n San Pedro de Huaca","Cant??n Bol??var (Carchi)"], # Carchi
            ["Cant??n Guano","Cant??n Penipe","Cant??n Riobamba","Cant??n Colta","Cant??n Chambo","Cant??n Pallatanga","Cant??n Guamote","Cant??n Alaus??","Cant??n Cumand??","Cant??n Chunchi"], #Chimborazo
            ["Cant??n Sigchos","Cant??n La Man??","Cant??n Latacunga","Cant??n Saquisil??","Cant??n Pujil??","Cant??n Pangua","Cant??n Salcedo"], # Cotopaxi
            ["Cant??n El Guabo","Cant??n Machala","Cant??n Pasaje","Cant??n Chilla","Cant??n Zaruma","Cant??n Santa Rosa","Cant??n Atahualpa","Cant??n Arenillas","Cant??n Huaquillas","Cant??n Las Lajas","Cant??n Marcabel??","Cant??n Balsas","Cant??n Pi??as","Cant??n Portovelo"], # El Oro
            ["Cant??n San Lorenzo","Cant??n Eloy Alfaro","Cant??n Rioverde","Cant??n Esmeraldas","Cant??n Muisne","Cant??n Atacames","Cant??n Quinind??"], # Esmeraldas
            ["Cant??n Isabela","Cant??n San Crist??bal","Cant??n Santa Cruz"], # Gal??pagos
            ["Cant??n El Empalme","Cant??n Balzar","Cant??n Colimes","Cant??n Palestina","Cant??n Santa Luc??a","Cant??n Pedro Carbo","Cant??n Isidro Ayora","Cant??n Lomas de Sargentillo","Cant??n Nobol","Cant??n Daule","Cant??n Salitre","Cant??n Samborond??n","Cant??n Yaguachi","Cant??n Alfredo Baquerizo Moreno","Cant??n Milagro","Cant??n Sim??n Bol??var","Cant??n Naranjito","Cant??n General Antonio Elizalde","Cant??n Coronel Marcelino Maridue??a","Cant??n El Triunfo","Cant??n Dur??n","Cant??n Guayaquil","Cant??n Playas","Cant??n Naranjal","Cant??n Balao"], # Guayas
            ["Cant??n Ibarra","Cant??n San Miguel de Urcuqu??","Cant??n Cotacachi","Cant??n Antonio Ante","Cant??n Otavalo","Cant??n Pimampiro"], # Imbabura
            ["Cant??n Saraguro","Cant??n Loja","Cant??n Chaguarpamba","Cant??n Olmedo (Loja)","Cant??n Catamayo","Cant??n Paltas","Cant??n Puyango","Cant??n Pindal","Cant??n Celica","Cant??n Zapotillo","Cant??n Macar??","Cant??n Sozoranga","Cant??n Calvas","Cant??n Gonzanam??","Cant??n Quilanga","Cant??n Esp??ndola"], # Loja
            ["Cant??n Buena Fe","Cant??n Valencia","Cant??n Quevedo","Cant??n Quinsaloma","Cant??n Palenque","Cant??n Mocache","Cant??n Ventanas","Cant??n Vinces","Cant??n Baba","Cant??n Puebloviejo","Cant??n Urdaneta","Cant??n Babahoyo","Cant??n Montalvo"], # Los R??os
            ["Cant??n Pedernales","Cant??n Chone","Cant??n Flavio Alfaro","Cant??n El Carmen","Cant??n Jama","Cant??n San Vicente","Cant??n Sucre","Cant??n Tosagua","Cant??n Rocafuerte","Cant??n Jun??n","Cant??n Bol??var (Manab??)","Cant??n Pichincha","Cant??n Portoviejo","Cant??n Jaramij??","Cant??n Manta","Cant??n Montecristi","Cant??n Santa Ana","Cant??n Jipijapa","Cant??n Veinticuatro de Mayo","Cant??n Olmedo (Manab??)","Cant??n Puerto L??pez","Cant??n Paj??n"], # Manab??
            ["Cant??n Palora","Cant??n Pablo Sexto","Cant??n Huamboya","Cant??n Morona","Cant??n Taisha","Cant??n Suc??a","Cant??n Santiago","Cant??n Logro??o","Cant??n Tiwintza","Cant??n Lim??n Indanza","Cant??n San Juan Bosco","Cant??n Gualaquiza"], # Morona Santiago
            ["Cant??n El Chaco","Cant??n Quijos","Cant??n Archidona","Cant??n Tena","Cant??n Carlos Julio Arosemena Tola"], # Napo
            ["Cant??n Loreto","Cant??n Francisco de Orellana","Cant??n La Joya de los Sachas","Cant??n Aguarico"], # Orellana
            ["Cant??n Mera","Cant??n Santa Clara","Cant??n Arajuno","Cant??n Pastaza"], # Pastaza
            ["Cant??n Puerto Quito","Cant??n Pedro Vicente Maldonado","Cant??n San Miguel de Los Bancos","Distrito Metropolitano de Quito","Cant??n Pedro Moncayo","Cant??n Cayambe","Cant??n Rumi??ahui","Cant??n Mej??a"], # Pichincha
            ["Cant??n Santa Elena","Cant??n La Libertad","Cant??n Salinas"], # Santa Elena
            ["Cant??n La Concordia","Cant??n Santo Domingo"], # Santo Domingo de los Ts??chilas
            ["Cant??n Sucumb??os","Cant??n Gonzalo Pizarro","Cant??n Cascales","Cant??n Lago Agrio","Cant??n Putumayo","Cant??n Cuyabeno","Cant??n Shushufindi"], # Sucumb??os
            ["Cant??n Ambato","Cant??n P??llaro","Cant??n Patate","Cant??n Ba??os","Cant??n Pelileo","Cant??n Cevallos","Cant??n Tisaleo","Cant??n Mocha","Cant??n Quero"], # Tungurahua
            ["Cant??n Yacuambi","Cant??n Yantzaza","Cant??n El Pangui","Cant??n Zamora","Cant??n Centinela del C??ndor","Cant??n Paquisha","Cant??n Nangaritza","Cant??n Palanda","Cant??n Chinchipe"], # Zamora Chinchipe
            [" "," "]]
