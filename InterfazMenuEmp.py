'''importar la libreria tkinter para la parte de la interfaz grafica'''
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

import BaseDeDatos
import ClaseEmpresa
import InterfazPrincipal 
import InterfazEmpresa

class MyWindowMenEmp:
    ''' 
    Clase en donde se ingresan todos los datos que especifican los limites de la busqueda
    dentro de la libreria de MongoDB. 
    ...
    Atributos
    ----------
    boton1 : Button
        Boton que ejecuta la busqueda.
    entrada1 : Entry
        Primera de entrada de tipo de parametro.
    entrada2 : Entry
        Primera de entrada de especificacion del tipo de parametro.
    entrada3 : Entry
        Segunda de entrada de tipo de parametro.
    entrada4 : Entry
        Segunda de entrada de especificacion del tipo de parametro.
    ...
    Metodos
    -------
    __init__(self,win):
        Construye todos los atributos necesarios para el objeto MyWindow.
    buscar(self):
        Se pasan los 2 parametros de especificacion en la busqueda y
        presenta la lista objetos resultantes en la busqueda.
    '''
    def __init__(self, win):
        '''
        Construye todos los atributos necesarios para el objeto MyWindow.
        ...
        Parametros
        ----------
        win : Tk
        '''
        self.cantonEmp=[]
        self.win=win
        win['bg']='white'
        win.title("Formulario de inicio de sesion de Empresa")
        textSup=Label(text='CHECK JOB',font=("Tahoma",20,"bold italic"), fg="green", bg="white").place(x=300,y=40,anchor='center')
        text1=Label(text='Ingrese sus datos',font=("Tahoma",17,"bold"), fg="black", bg="white").place(x=300,y=100,anchor='center')
        text2=Label(text='Usuario Empresa ',font=("Tahoma",15), fg="black", bg="white").place(x=50,y=120+30)
        text3=Label(text='Contraseña Empresa ',font=("Tahoma",15), fg="black", bg="white").place(x=50,y=200+30)
        
        boton1=Button(text=' Ingresar como Empresa ',font=("Consolas",15), command=self.iniciarSesion).place(x=300, y=350, anchor='center')
        boton2=Button(text=' Crear Cuenta de Empresa ',font=("Consolas",15), command=self.formularioCreaEmp).place(x=300, y=430, anchor='center')

        self.entrada1=Entry(bd=3,font=("Arial",15),bg="light grey")
        self.entrada2=Entry(bd=3,font=("Arial",15),bg="light grey")
        self.entrada1.place(x=400, y=120+40,anchor='center')
        self.entrada2.place(x=400, y=200+40,anchor='center')


    
    def iniciarSesion(self):
        '''
        Como primera opcion se ingresan los datos de Empresa y se
        llama al metodo de iniciar sesion, para despues continuar con el menu
        ...
        Parametros
        ----------
        *No tiene parametros*
        '''
        usuarioIngresado=str(self.entrada1.get())
        claveIngresado=str(self.entrada2.get())
        variableInicio = empresa1.iniciarSesionEmpresa(usuarioIngresado,claveIngresado)
        if (variableInicio != None):
            messagebox.showinfo("Correcto","Usuario y clave registrado correctamente")
            self.win.quit()
            InterfazEmpresa.main()
        else:
            messagebox.showwarning("Error","Usuario o clave registrado incorrectamente")

        
    def formularioCreaEmp(self):
        '''
        Como segunda opcion se registra una cuenta de Empresa en la aplicacion
        ...
        Parametros
        ----------
        *No tiene parametros*
        '''
        self.windowCreaEmp=Tk()
        self.windowCreaEmp.title("Formulario de creacion de cuenta de Empresa")
        self.windowCreaEmp.geometry("600x700")
        text1=Label(self.windowCreaEmp, text='Ingrese sus datos',font=("Tahoma",17,"bold"), fg="black").place(x=300,y=50-20,anchor='center')
        text2=Label(self.windowCreaEmp, text='Nombre Completo',font=("Tahoma",15), fg="black").place(x=50,y=100-20)
        text3=Label(self.windowCreaEmp, text='RUC',font=("Tahoma",15), fg="black").place(x=50,y=150-20)
        text4=Label(self.windowCreaEmp, text='Telefono',font=("Tahoma",15), fg="black").place(x=50,y=200-20)
        text5=Label(self.windowCreaEmp, text='Provincia',font=("Tahoma",15), fg="black").place(x=50,y=250-20)
        text6=Label(self.windowCreaEmp, text='Canton',font=("Tahoma",15), fg="black").place(x=50,y=300-20)
        text7=Label(self.windowCreaEmp, text='Codigo Postal',font=("Tahoma",15), fg="black").place(x=50,y=350-20)
        text8=Label(self.windowCreaEmp, text='Calle Principal',font=("Tahoma",15), fg="black").place(x=50,y=400-20)
        text9=Label(self.windowCreaEmp, text='Calle Secundaria',font=("Tahoma",15), fg="black").place(x=50,y=450-20)
        text10=Label(self.windowCreaEmp, text='E-mail',font=("Tahoma",15), fg="black").place(x=50,y=500-20)
        
        boton1=Button(self.windowCreaEmp,text='Crear Cuenta',font=("Consolas",15), command=self.crearCuenta).place(x=300, y=550, anchor='center')
        
        self.entrada1=Entry(self.windowCreaEmp,bd=3,font=("Arial",15),bg="light grey")
        self.entrada2=Entry(self.windowCreaEmp,bd=3,font=("Arial",15),bg="light grey")
        self.entrada3=Entry(self.windowCreaEmp,bd=3,font=("Arial",15),bg="light grey")
        self.entrada4 = ttk.Combobox(self.windowCreaEmp,font=("Arial",15))
        # Adding combobox drop down list
        self.entrada4['values'] = (BaseDeDatos.provinciasEC)
        self.entrada4['state'] = 'readonly'
        self.entrada4.bind('<<ComboboxSelected>>', self.eleccion_canton)
        self.entrada4.current()
        
        self.entrada5 = ttk.Combobox(self.windowCreaEmp,font=("Tahoma",15))
        self.entrada5['state'] = 'readonly'
        self.entrada5.current()
        
        self.entrada6=Entry(self.windowCreaEmp,bd=3,font=("Arial",15),bg="light grey")
        self.entrada7=Entry(self.windowCreaEmp,bd=3,font=("Arial",15),bg="light grey")
        self.entrada8=Entry(self.windowCreaEmp,bd=3,font=("Arial",15),bg="light grey")
        self.entrada9=Entry(self.windowCreaEmp,bd=3,font=("Arial",15),bg="light grey")
        
        self.entrada1.place(x=400, y=100,anchor='center')
        self.entrada2.place(x=400, y=150,anchor='center')
        self.entrada3.place(x=400, y=200,anchor='center')
        self.entrada4.place(x=400, y=250,anchor='center')
        self.entrada5.place(x=400, y=300,anchor='center')
        self.entrada6.place(x=400, y=350,anchor='center')
        self.entrada7.place(x=400, y=400,anchor='center')
        self.entrada8.place(x=400, y=450,anchor='center')
        self.entrada9.place(x=400, y=500,anchor='center')

    def eleccion_canton(self, event):
        """ handle the month changed event """
        provinciaEmp=str(self.entrada4.get())
        self.entrada5['values'] = (BaseDeDatos.cantonesEC[24])
        self.entrada5.current(0)
        for i in range (0,24):
            if (provinciaEmp == BaseDeDatos.provinciasEC[i]):
                self.cantonEmp = (BaseDeDatos.cantonesEC[i])
                self.entrada5['values'] = (self.cantonEmp)

    def crearCuenta(self):
        empresa1=ClaseEmpresa.Empresa(0,0,0,0,0,0,0,0,0) 
        nombreEmp=str(self.entrada1.get())
        RUCEmp=str(self.entrada2.get())
        telefonoEmp=str(self.entrada3.get())
        provinciaEmp=str(self.entrada4.get())
        cantonEmp=str(self.entrada5.get())
        codigoPostal=str(self.entrada6.get())
        callePrincipalEmp=str(self.entrada7.get())
        calleSecundariaEmp=str(self.entrada8.get())
        emailEmp=str(self.entrada8.get())

        self.entrada1.config(bg="chartreuse2")
        self.entrada2.config(bg="chartreuse2")
        self.entrada3.config(bg="chartreuse2")
        self.entrada6.config(bg="chartreuse2")
        self.entrada7.config(bg="chartreuse2")
        self.entrada8.config(bg="chartreuse2")
        self.entrada9.config(bg="chartreuse2")

        
        mensajeError = "Se presentaron los siquientes prblemas: \n"
                
        if (ClaseEmpresa.Empresa.verificar_nombre(empresa1,nombreEmp)):
            if (str.isdigit(nombreEmp)):
                mensajeError += "Nombre ingresado incorrectamente. \n"
                InterfazPrincipal.limpiar_entrada(True,self.entrada1)
        
        varificarCuenta = ClaseEmpresa.Empresa.comprobarCuenta(empresa1,RUCEmp)
        if (varificarCuenta != None):
            mensajeError = "Ya existe una cuenta creada con este IDE. \n"
            InterfazPrincipal.limpiar_entrada(True,self.entrada3)
            if (int(RUCEmp) < 1000000000001 or int(RUCEmp) >=999999999001):
                mensajeError = mensajeError + "Cedula ingresada incorrectamente. \n"
                InterfazPrincipal.limpiar_entrada(True,self.entrada2)

        if ((telefonoEmp[:2] != "09") and (len(telefonoEmp) != 9)):
                mensajeError = mensajeError +  "Telefono Ingresado incorrectamente. \n"
                InterfazPrincipal.limpiar_entrada(True,self.entrada3)
        
        if (not ClaseEmpresa.Empresa.verificar_correo(empresa1,emailEmp)):
            mensajeError = mensajeError + "Correo Ingresado incorrectamente. \n"
            InterfazPrincipal.limpiar_entrada(True,self.entrada9)
        
        varificarCuenta = ClaseEmpresa.Empresa.comprobarCuenta(empresa1,RUCEmp)
        if (varificarCuenta == None):
            if (ClaseEmpresa.Empresa.verificar_nombre(empresa1,nombreEmp)):
                print("nombre si")
                if (int(RUCEmp) >= 1000000000001 and int(RUCEmp) <=999999999001):
                    if (telefonoEmp[:2] == "09"):
                        if (int(telefonoEmp) >= 900000000 and  int(telefonoEmp) <999999999):
                            if (ClaseEmpresa.Empresa.verificar_correo(empresa1,emailEmp)):
                    
                                empresa1=ClaseEmpresa.Empresa(nombreEmp, RUCEmp, telefonoEmp, provinciaEmp, cantonEmp, codigoPostal, callePrincipalEmp, calleSecundariaEmp, emailEmp)
                                registrado=empresa1.registro_tiempo("Regitro de cuenta de Empresa")
                                direccion=[callePrincipalEmp,calleSecundariaEmp]
                                BaseDeDatos.guardar_registro(nombreEmp, RUCEmp, telefonoEmp, provinciaEmp, cantonEmp, codigoPostal, direccion, emailEmp, registrado)
                                mensaje = empresa1.crearCuentaEmpresa()
                                BaseDeDatos.guardar_empresa(nombreEmp, RUCEmp, telefonoEmp, provinciaEmp, cantonEmp, codigoPostal, direccion, emailEmp, empresa1._usuarioEmp, empresa1._claveEmp)
                                messagebox.showinfo("Cuenta creada exitosamente",mensaje)
                                self.windowCreaEmp.quit()
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


empresa1=ClaseEmpresa.Empresa(0,0,0,0,0,0,0,0,0) 
