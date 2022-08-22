from time import localtime, asctime
import re

class Usuario():
    ''' 
    Clase en donde se guardaran todos los datos que ingresa el 
    Clienta como el usuario y la clave de este mismo.
    ...
    Atributos
    ----------
    nombre : str
        Nombre del usuario registrado en el sistema
    telefono : int
        Telefono del usuario registrado en el sistema 
    provincia : str
        Priovincia del usuario registrado en el sistema en la cual el
        se encuentra el aspirante o la sede de la empresa.
    direccion : str
        Direccion del usuario registrado en el sistema en la cual el
        se encuentra el aspirante o la sede de la empresa.
    email : str
        E-mail de contacto del usuario registrado en el sistema 
    tiempo : lista
        Registro de las acciones realizadas por el usuario
    ...
    Metodos
    -------
    __init__(self):
        Construye todos los atributos necesarios para el objeto Usuario.
    registro_tiempo(self,accion):
        Metodo que añade una accion al registro del tiempo. Retorna la ultima accion realizada.
    registro_acciones(self):
        Metodo que presenta la lista de acciones registradas por tiempo.
    '''
    
    def __init__(self, nombre, telefono, provincia, canton, codigoPostal, callePrincipal, calleSecundaria, email):
        ''' 
        Construye todos los atributos necesarios para el objeto Cliente.
        ...
        Parametros
        ----------
        nombre : str
            Nombre del usuario registrado en el sistema
        telefono : int
            Telefono del usuario registrado en el sistema 
        provincia : str
            Priovincia del usuario registrado en el sistema en la cual el
            se encuentra el aspirante o la sede de la empresa.
        direccion : str
            Direccion del usuario registrado en el sistema en la cual el
            se encuentra el aspirante o la sede de la empresa.
        email : str
            E-mail de contacto del usuario registrado en el sistema 
        '''
        # atributo protegido
        self.nombre = nombre
        self.telefono = telefono
        self.provincia = provincia
        self.canton = canton
        self.codigoPostal = codigoPostal
        self.callePrincipal = callePrincipal
        self.calleSecundaria = calleSecundaria
        self.email = email
        self.tiempo=[]
        
    def registro_tiempo(self,accion):
        '''
        Metodo que añade una accion al registro del tiempo. 
        ...
        Parametros
        ----------
        accion : str
            Accion que se registra en el tiempo determinada.
        ...
        Retorna
        ----------
        return registro
            Retorna la ultima accion realizada.
        '''
        registro=accion+": "+asctime(localtime())
        self.tiempo.append(registro)
        
        return registro
        
    def registro_acciones(self):
        '''
        Metodo que presenta la lista de acciones registradas por tiempo.
        ...
        Parametros
        ----------
        *No tiene parametros*
        '''
        for i in range (0,len(self.tiempo)):
            print(self.tiempo[i])
            
    def verificar_correo(self, correoIngresado):
        expresion_regular_correo = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
        return re.match(expresion_regular_correo, correoIngresado) is not None
        
    def verificar_nombre(self, nombreIngresada):
        if bool(re.search(r'\d', nombreIngresada)):
            return True
        else:
            return False

