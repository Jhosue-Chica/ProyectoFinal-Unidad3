'''importar la libreria tkinter para la parte de la interfaz grafica'''
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showinfo
from tkinter import ttk
'''Se importan todas las clases que se pueden necesitar en esta parte del programa'''
import BaseDeDatos
import InterfazPrincipal
import ClaseAspirante
import InterfazAspirante 


class MyWindowMenAsp:
    ''' 
    Clase en donde se genera la interfaz grafica del menu de la parte del usuario 
    de tipo Aspirante. 
    ...
    Atributos
    ----------
    cantonAsp : Lista
        Guarda los cantones segun la provincia elegida por medio de la interfaz
    boton1 : Button
        Boton que ejecuta la busqueda.
    entrada1 : Entry
        Entrada del usuario del Aspirante registrado.
    entrada2 : Entry
        Entrada de la clave del Aspirante registrado.
    ...
    Metodos
    -------
    __init__(self,win):
        Construye todos los atributos necesarios para el objeto MyWindow.
    iniciarSesion(self):
    formularioCreaAsp(self):
    
    buscar(self):
        Se pasan los 2 parametros de especificacion en la busqueda y
        presenta la lista objetos resultantes en la busqueda.
    '''
    def __init__(self,win):
        '''
        Construye todos los atributos necesarios para el objeto MyWindowMenAsp.
        ...
        Parametros
        ----------
        win : Tk
            Variable que designa la Interfaz de usuario principal
        '''
        self.cantonAsp=[]
        win['bg']='white'
        win.title("Formulario de inicio de sesion de Aspirante")
        textSup=Label(text='CHECK JOB',font=("Tahoma",20,"bold italic"), fg="green", bg="white").place(x=300,y=40,anchor='center')
        text1=Label(text='Ingrese sus datos',font=("Tahoma",17,"bold"), fg="black", bg="white").place(x=300,y=100,anchor='center')
        text2=Label(text='Usuario Aspirante',font=("Tahoma",15), fg="black", bg="white").place(x=50,y=120+30)
        text3=Label(text='Contraseña Aspirante',font=("Tahoma",15), fg="black", bg="white").place(x=50,y=200+30)
        
        boton1=Button(text='Ingresar como Aspirante',font=("Consolas",15), command=self.iniciarSesion).place(x=300, y=350, anchor='center')
        boton2=Button(text='Crear Cuenta de Aspirante',font=("Consolas",15), command=self.formularioCreaAsp).place(x=300, y=430, anchor='center')

        self.entrada1=Entry(bd=3,font=("Arial",15),bg="light grey")
        self.entrada2=Entry(bd=3,font=("Arial",15),bg="light grey")
        self.entrada1.place(x=400, y=120+40,anchor='center')
        self.entrada2.place(x=400, y=200+40,anchor='center')
    

    def iniciarSesion(self):
        '''
        Como primera opcion se ingresan los datos de aspirante y se
        llama al metodo de iniciar sesion, para despues continuar con el menu
        ...
        Parametros
        ----------
        *No tiene parametros*
        '''
        usuarioIngresado=str(self.entrada1.get())
        claveIngresado=str(self.entrada2.get())
        variableInicio = aspirante1.iniciarSesionAspirante(usuarioIngresado,claveIngresado)
        if (variableInicio != None):
            InterfazPrincipal.limpiar_entrada(False,self.entrada1)
            InterfazPrincipal.limpiar_entrada(False,self.entrada2)
            messagebox.showinfo("Correcto","Usuario y clave registrado correctamente")
            InterfazAspirante.main()
        else:
            InterfazPrincipal.limpiar_entrada(True,self.entrada1)
            InterfazPrincipal.limpiar_entrada(True,self.entrada2)
            messagebox.showwarning("Error","Usuario o clave registrado incorrectamente")


    def formularioCreaAsp(self):
        '''
        Como segunda opcion se registra una cuenta de Aspirante en la aplicacion
        ...
        Parametros
        ----------
        *No tiene parametros*
        '''
        self.windowCreaAsp=Tk()
        self.windowCreaAsp.title("Formulario de creacion de cuenta de Aspirante")
        self.windowCreaAsp.geometry("600x700")
        text1=Label(self.windowCreaAsp, text='Ingrese sus datos',font=("Tahoma",17,"bold"), fg="black").place(x=300,y=50-20,anchor='center')
        text2=Label(self.windowCreaAsp, text='Nombre Completo',font=("Tahoma",15), fg="black").place(x=50,y=100-20)
        text3=Label(self.windowCreaAsp, text='Edad',font=("Tahoma",15), fg="black").place(x=50,y=150-20)
        text4=Label(self.windowCreaAsp, text='Cedula',font=("Tahoma",15), fg="black").place(x=50,y=200-20)
        text5=Label(self.windowCreaAsp, text='Telefono',font=("Tahoma",15), fg="black").place(x=50,y=250-20)
        text6=Label(self.windowCreaAsp, text='Provincia',font=("Tahoma",15), fg="black").place(x=50,y=300-20)
        text7=Label(self.windowCreaAsp, text='Canton',font=("Tahoma",15), fg="black").place(x=50,y=350-20)
        text8=Label(self.windowCreaAsp, text='Codigo Postal',font=("Tahoma",15), fg="black").place(x=50,y=400-20)
        text9=Label(self.windowCreaAsp, text='Calle Principal',font=("Tahoma",15), fg="black").place(x=50,y=450-20)
        text10=Label(self.windowCreaAsp, text='Calle Secundaria',font=("Tahoma",15), fg="black").place(x=50,y=500-20)
        text11=Label(self.windowCreaAsp, text='E-mail',font=("Tahoma",15), fg="black").place(x=50,y=550-20)
        
        boton1=Button(self.windowCreaAsp,text='Crear Cuenta',font=("Consolas",15), command=self.crearCuenta).place(x=300, y=600, anchor='center')
        
        self.entrada1=Entry(self.windowCreaAsp,bd=3,font=("Tahoma",15),bg="light grey")
        self.entrada2=Entry(self.windowCreaAsp,bd=3,font=("Tahoma",15),bg="light grey")
        self.entrada3=Entry(self.windowCreaAsp,bd=3,font=("Tahoma",15),bg="light grey")
        self.entrada4=Entry(self.windowCreaAsp,bd=3,font=("Tahoma",15),bg="light grey")
        self.entrada5 = ttk.Combobox(self.windowCreaAsp,font=("Tahoma",15))
        # Adding combobox drop down list
        self.entrada5['values'] = (BaseDeDatos.provinciasEC)
        self.entrada5['state'] = 'readonly'
        self.entrada5.bind('<<ComboboxSelected>>', self.eleccion_canton)
        self.entrada5.current()
        
        self.entrada6 = ttk.Combobox(self.windowCreaAsp,font=("Tahoma",15))
        self.entrada6['state'] = 'readonly'
        self.entrada6.current()

        self.entrada7=Entry(self.windowCreaAsp,bd=3,font=("Tahoma",15),bg="light grey")
        self.entrada8=Entry(self.windowCreaAsp,bd=3,font=("Tahoma",15),bg="light grey")
        self.entrada9=Entry(self.windowCreaAsp,bd=3,font=("Tahoma",15),bg="light grey")
        self.entrada10=Entry(self.windowCreaAsp,bd=3,font=("Tahoma",15),bg="light grey")
        
        self.entrada1.place(x=400, y=100,anchor='center')
        self.entrada2.place(x=400, y=150,anchor='center')
        self.entrada3.place(x=400, y=200,anchor='center')
        self.entrada4.place(x=400, y=250,anchor='center')
        self.entrada5.place(x=400, y=300,anchor='center')
        self.entrada6.place(x=400, y=350,anchor='center')
        self.entrada7.place(x=400, y=400,anchor='center')
        self.entrada8.place(x=400, y=450,anchor='center')
        self.entrada9.place(x=400, y=500,anchor='center')
        self.entrada10.place(x=400, y=550,anchor='center')

    def eleccion_canton(self, event):
        """ handle the month changed event """
        provinciaAsp=str(self.entrada5.get())
        self.entrada6['values'] = (BaseDeDatos.cantonesEC[24])
        self.entrada6.current(0)
        for i in range (0,24):
            if (provinciaAsp == BaseDeDatos.provinciasEC[i]):
                self.cantonAsp = (BaseDeDatos.cantonesEC[i])
                self.entrada6['values'] = (self.cantonAsp)


    def crearCuenta(self):
        aspirante1=ClaseAspirante.Aspirante(0,0,0,0,0,0,0,0,0,0) 
        nombreAsp=str(self.entrada1.get())
        edadAsp=int(self.entrada2.get())
        cedulaAsp=str(self.entrada3.get())
        telefonoAsp=str(self.entrada4.get())
        provinciaAsp=str(self.entrada5.get())
        cantonAsp=str(self.entrada6.get())
        codigoPostal=str(self.entrada7.get())
        callePrincipalAsp=str(self.entrada8.get())
        calleSecundariaAsp=str(self.entrada9.get())
        emailAsp=str(self.entrada10.get())
        
        self.entrada1.config(bg="chartreuse2")
        self.entrada2.config(bg="chartreuse2")
        self.entrada3.config(bg="chartreuse2")
        self.entrada4.config(bg="chartreuse2")
        self.entrada7.config(bg="chartreuse2")
        self.entrada8.config(bg="chartreuse2")
        self.entrada9.config(bg="chartreuse2")
        self.entrada10.config(bg="chartreuse2")
        
        mensajeError = "Se presentaron los siquientes prblemas: \n"
                
        if (ClaseAspirante.Aspirante.verificar_nombre(aspirante1,nombreAsp)):
            if (str.isdigit(nombreAsp)):
                mensajeError += "Nombre ingresado incorrectamente. \n"
                InterfazPrincipal.limpiar_entrada(True,self.entrada1)
        
        varificarCuenta = ClaseAspirante.Aspirante.comprobarCuenta(aspirante1,cedulaAsp)
        if (varificarCuenta != None):
            mensajeError = "Ya existe una cuenta creada con este IDE. \n"
            InterfazPrincipal.limpiar_entrada(True,self.entrada3)
            if (int(cedulaAsp) < 1000000000 or int(cedulaAsp) >=10000000000):
                mensajeError = mensajeError + "Cedula ingresada incorrectamente. \n"
                InterfazPrincipal.limpiar_entrada(True,self.entrada3)
        
        if (edadAsp<18 or edadAsp>65):
            mensajeError += "Edad fuera de rango. \n"
            InterfazPrincipal.limpiar_entrada(True,self.entrada2)

        if ((telefonoAsp[:2] != "09") and (len(telefonoAsp) != 9)):
                mensajeError = mensajeError +  "Telefono Ingresado incorrectamente. \n"
                InterfazPrincipal.limpiar_entrada(True,self.entrada4)
        
        if (not ClaseAspirante.Aspirante.verificar_correo(aspirante1,emailAsp)):
            mensajeError = mensajeError + "Correo Ingresado incorrectamente. \n"
            InterfazPrincipal.limpiar_entrada(True,self.entrada10)

        if (varificarCuenta == None):
            if (ClaseAspirante.Aspirante.verificar_nombre(aspirante1,nombreAsp)):
                print("nombre si")
                if (int(cedulaAsp) >= 1000000000 and int(cedulaAsp) <10000000000):
                    if (telefonoAsp[:2] == "09"):
                        if (int(telefonoAsp) >= 900000000 and  int(telefonoAsp) <999999999):
                            if edadAsp>=18 and edadAsp<65:
                                if (ClaseAspirante.Aspirante.verificar_correo(aspirante1,emailAsp)):
                                    aspirante1=ClaseAspirante.Aspirante(nombreAsp, edadAsp, cedulaAsp, telefonoAsp, provinciaAsp, cantonAsp, codigoPostal, callePrincipalAsp, calleSecundariaAsp, emailAsp)
                                    registrado=aspirante1.registro_tiempo("Regitro de cuenta de Aspirante")
                                    direccion=[callePrincipalAsp,calleSecundariaAsp]
                                    BaseDeDatos.guardar_registro(nombreAsp, cedulaAsp, telefonoAsp, provinciaAsp, cantonAsp, codigoPostal, direccion, emailAsp, registrado)
                                    mensaje = aspirante1.crearCuentaAspirante()
                                    BaseDeDatos.guardar_aspirante(nombreAsp, edadAsp, cedulaAsp, telefonoAsp, provinciaAsp, cantonAsp, codigoPostal, direccion, emailAsp, aspirante1._usuarioAsp, aspirante1._claveAsp)
                                    messagebox.showinfo("Cuenta creada exitosamente", mensajeError)
                                    self.windowCreaAsp.quit()
                                else:
                                    messagebox.showwarning("Error", mensajeError)
                            else:
                                messagebox.showwarning("Error", mensajeError)
                        else:
                            messagebox.showwarning("Error", mensajeError)
                    else:
                        messagebox.showwarning("Error", mensajeError)
                else:
                    messagebox.showwarning("Error", mensajeError)
            else:
                messagebox.showwarning("Error", mensajeError)
        else:
            messagebox.showwarning("Error", mensajeError)



aspirante1=ClaseAspirante.Aspirante(0,0,0,0,0,0,0,0,0,0) 
