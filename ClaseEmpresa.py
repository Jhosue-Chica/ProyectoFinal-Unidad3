import ClaseUsuario
import pymongo

class Empresa(ClaseUsuario.Usuario):
    ''' 
    Clase en donde se guardaran todos los datos que ingresa el 
    Empresa como un usuario y la clave de este mismo.
    ...
    Atributos
    ----------
    nombre : str
        Nombre de la Empresa registrada en el sistema
    RUC : str
        Registro Único de Contribuyentes de la Empresa registrada en el sistema
    telefono : int
        Telefono de la Empresa registrada en el sistema 
    provincia : str
        Priovincia de la Empresa registrada en el sistema en la cual el
        se encuentra la sede de la empresa.
    direccion : str
        Direccion de la Empresa registrada en el sistema en la cual el
        se encuentra la sede de la empresa.
    email : str
        E-mail de contacto de la Empresa registrada en el sistema
    _usuarioEmp: str
        El usuario del cliente asignada por el sistema a partir del
        resto de datos ingresados por el usuario
    _claveEmp: str
        La clave del cliente asignada por el sistema a partir del
        resto de datos ingresados por el usuario
    ...
    Metodos
    -------
    __init__(self):
        Construye todos los atributos necesarios para el objeto Empresa.
    crearCuentaEmpresa(self):
        Se realizan el ingreso de los datos principales de la Empresa para
        poder crear el usuario y la clave a partir de estos datos.
    iniciarSesionEmpresa(self, usuarioIngresado, claveIngresado):
        Se realiza el ingreso de usuario y la clave, y se los compara con
        los valores de usuario y clave anteriormente registrados en el sistema
    '''
    def __init__(self, nombre, RUC, telefono, provincia, canton, codigoPostal, callePrincipal, calleSecundaria, email):
        ''' 
        Construye todos los atributos necesarios para el objeto Empresa.
        ...
        Parametros
        ----------
        nombre : str
            Nombre de la Empresa registrada en el sistema
        RUC : str
            Registro Único de Contribuyentes de la Empresa registrada en el sistema
        telefono : int
            Telefono de la Empresa registrada en el sistema 
        provincia : str
            Priovincia de la Empresa registrada en el sistema en la cual el
            se encuentra la sede de la empresa.
        direccion : str
            Direccion de la Empresa registrada en el sistema en la cual el
            se encuentra la sede de la empresa.
        email : str
            E-mail de contacto de la Empresa registrada en el sistema
        '''
        self.RUC = RUC
        super().__init__(nombre, telefono, provincia, canton, codigoPostal, callePrincipal, calleSecundaria, email)
        '''atributo protegido'''
        self._usuarioEmp = "usuario"
        self._claveEmp = "clave"
        
    def crearCuentaEmpresa(self):
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
        self._usuarioEmp=self.nombre+self.provincia[:3]+self.RUC[7:]
        self._claveEmp=self.callePrincipal[:3]+self.telefono[6:8]+self.RUC[7:]
        self._usuarioEmp.replace(" ", "")
        self._claveEmp.replace(" ", "")
        return "Su usuario sera: ", self._usuarioEmp,". Su clave sera: ", self._claveEmp
        
    def iniciarSesionEmpresa(self, usuarioIngresado, claveIngresado):
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
        micol=midb["empresas"] #coleccion
        '''Creamos un Widgets Listbox'''
        myquery = {"usuario": {"$eq": usuarioIngresado},"clave": {"$eq": claveIngresado}}
        mydoc = micol.find(myquery)
        '''Insertamos los nombres de la lista en el Listbox'''
        for x in mydoc:
            return x  
        
    def comprobarCuenta(self, RUC):
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
        micol=midb["empresas"] #coleccion
        '''Creamos un Widgets Listbox'''
        myquery = {"_id": {"$eq": RUC}}
        mydoc = micol.find(myquery)
        '''Insertamos los nombres de la lista en el Listbox'''
        for x in mydoc:
            return x