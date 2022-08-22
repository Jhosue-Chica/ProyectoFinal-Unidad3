import ClaseUsuario
import pymongo

class Aspirante(ClaseUsuario.Usuario):
    ''' 
    Clase en donde se guardaran todos los datos que ingresa el 
    Aspirante como un usuario y la clave de este mismo.
    ...
    Atributos
    ----------
    nombre : str
        Nombre del usuario registrado en el sistema
    edad : int
        Edad del usuario registrado en el sistema
    cedula : int
        Documento de Identidad del apirante registrado en el sistema
    telefono : int
        Telefono del usuario registrado en el sistema 
    provincia : str
        Priovincia del usuario registrado en el sistema en la cual el
        se encuentra el aspirante.
    direccion : str
        Direccion del usuario registrado en el sistema en la cual el
        se encuentra el aspirante o la sede de la empresa.
    email : str
        E-mail de contacto del usuario registrado en el sistema
    _usuarioAsp: str
        El usuario del cliente asignada por el sistema a partir del
        resto de datos ingresados por el usuario
    _claveAsp: str
        La clave del cliente asignada por el sistema a partir del
        resto de datos ingresados por el usuario
    ...
    Metodos
    -------
    __init__(self):
        Construye todos los atributos necesarios para el objeto Aspirante.
    crearCuentaAspirante(self):
        Se realizan el ingreso de los datos principales del cliente para
        poder crear el usuario y la clave a partir de estos datos.
    iniciarSesionAspirante(self, usuarioIngresado, claveIngresado):
        Se realiza el ingreso de usuario y la clave, y se los compara con
        los valores de usuario y clave anteriormente registrados en el sistema
    '''
    def __init__(self, nombre, edad, cedula, telefono, provincia, canton, codigoPostal, callePrincipal, calleSecundaria, email):
        ''' 
        Construye todos los atributos necesarios para el objeto Aspirante.
        ...
        Parametros
        ----------
        nombre : str
            Nombre del usuario registrado en el sistema
        edad : int
            Edad del usuario registrado en el sistema
        cedula : int
            Documento de Identidad del apirante registrado en el sistema
        telefono : int
            Telefono del usuario registrado en el sistema 
        provincia : str
            Priovincia del usuario registrado en el sistema en la cual el
            se encuentra el aspirante.
        direccion : str
            Direccion del usuario registrado en el sistema en la cual el
            se encuentra el aspirante o la sede de la empresa.
        email : str
            E-mail de contacto del usuario registrado en el sistema
        '''
        self.edad = edad
        self.cedula = cedula
        super().__init__(nombre, telefono, provincia, canton, codigoPostal, callePrincipal, calleSecundaria, email)
        '''atributo protegido'''
        self._usuarioAsp = "usuario"
        self._claveAsp = "clave"
        
    def crearCuentaAspirante(self):
        '''
        Se realizan el ingreso de los datos principales del usuario para
        poder crear la cuenta de aspirante y la clave a partir de estos datos.
        ...
        Parametros
        ----------
        *No tiene parametros*
        ...
        Retorna
        ----------
        return "Su usuario sera: ", self._usuarioAsp,". Su clave sera: ", self._claveAsp
            Retorna si el usuario y la clave han sido procesados.
        '''
        self._usuarioAsp=self.nombre+self.provincia[:3]+self.cedula[7:]
        self._claveAsp=self.provincia[:3]+self.telefono[6:8]+self.codigoPostal[:3]
        self._usuarioAsp.replace(" ", "")
        self._claveAsp.replace(" ", "")
        return "Su usuario sera: ", self._usuarioAsp,". Su clave sera: ", self._claveAsp
        
    def iniciarSesionAspirante(self, usuarioIngresado, claveIngresado):
        '''
        Se realiza el ingreso de usuario y la clave, y se los compara con
        los valores de usuario y clave anteriormente registrados en el sistema.
        ...
        Parametros
        ----------
        usuarioIngresado : str
            Ususario ingresado para combrobar si es el mismo que el registrado en el sistema.
        claveIngresado : str
            Clave ingresada para combrobar si es el mismo que el registrado en el sistema.
        ...
        Retorna
        ----------
        return False
            Retorna False si la usuario o la clave estan mal ingresado.
        return True
            Retorna True si la usuario y la clave estan bien ingresado.
        '''
        micliente = pymongo.MongoClient("mongodb://localhost:27017/")
        midb = micliente["dbCheckJob"] #base de datos
        micol=midb["aspirantes"] #coleccion
        '''Creamos un Widgets Listbox'''
        myquery = {"usuario": {"$eq": usuarioIngresado},"clave": {"$eq": claveIngresado}}
        mydoc = micol.find(myquery)
        '''Insertamos los nombres de la lista en el Listbox'''
        for x in mydoc:
            return x
    
    
    def comprobarCuenta(self, idUsuario):
        '''
        Se realiza el ingreso de usuario y la clave, y se los compara con
        los valores de usuario y clave anteriormente registrados en el sistema.
        ...
        Parametros
        ----------
        usuarioIngresado : str
            Ususario ingresado para combrobar si es el mismo que el registrado en el sistema.
        claveIngresado : str
            Clave ingresada para combrobar si es el mismo que el registrado en el sistema.
        ...
        Retorna
        ----------
        return False
            Retorna False si la usuario o la clave estan mal ingresado.
        return True
            Retorna True si la usuario y la clave estan bien ingresado.
        '''
        micliente = pymongo.MongoClient("mongodb://localhost:27017/")
        midb = micliente["dbCheckJob"] #base de datos
        micol=midb["aspirantes"] #coleccion
        '''Creamos un Widgets Listbox'''
        myquery = {"_id": {"$eq": idUsuario}}
        mydoc = micol.find(myquery)
        '''Insertamos los nombres de la lista en el Listbox'''
        for x in mydoc:
            return x
    
            
