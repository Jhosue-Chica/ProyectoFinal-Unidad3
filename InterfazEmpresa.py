'''importar la libreria tkinter para la parte de la interfaz grafica'''
from tkinter import *
import tkinter as tk

import BaseDeDatos

class MyWindow:
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
      self.win=win
      menubar = Menu(win)
      win.config(menu=menubar)

      filemenu = Menu(menubar, tearoff=0)
      filemenu.add_command(label="Propuestas")

      # crearmenu = Menu(menubar, tearoff=0)
      # crearmenu.add_command(label="Crear",command=self.formulario_creacion)

      helpmenu = Menu(menubar, tearoff=0)
      helpmenu.add_command(label="Ayuda")
      helpmenu.add_separator()
      helpmenu.add_command(label="Acerca de...")

      menubar.add_cascade(label="Archivo", menu=filemenu)
      menubar.add_cascade(label="Editar", command=self.formulario_creacion)
      menubar.add_cascade(label="Ayuda", menu=helpmenu)


   def formulario_creacion(self):
      # windowCreacionEmp=Tk()
      # windowCreacionEmp.title("Formulario de creacion de cuenta de Aspirante")
      # windowCreacionEmp.geometry("600x500")
      self.win.clipboard_clear()
      titulo = Label(self.win, text="Busque su trabajo ideal",font=("Arial",15), fg="black").place(x=300,y=10,anchor='center')
      texto1=Label(self.win, text='Tipo 1',font=("Arial",15), fg="black").place(x=100,y=50)
      texto2=Label(self.win, text='Especificacion 1',font=("Arial",15), fg="black").place(x=100,y=150)
      texto3=Label(self.win, text='Tipo 2',font=("Arial",15), fg="black").place(x=100,y=250)
      texto4=Label(self.win, text='Especificacion 2',font=("Arial",15), fg="black").place(x=100,y=350)
      boton1=Button(self.win, text='Buscar',font=("Arial",15), command=self.buscar).place(x=400,y=450,anchor='center')
      boton2=Button(self.win, text='Volver Atras',font=("Arial",15), command=self.salir).place(x=170,y=450,anchor='center')
      self.entrada1=Entry(self.win,bd=3,font=("Arial",15),bg="light grey")
      self.entrada2=Entry(self.win,bd=3,font=("Arial",15),bg="light grey")
      self.entrada3=Entry(self.win,bd=3,font=("Arial",15),bg="light grey")
      self.entrada4=Entry(self.win,bd=3,font=("Arial",15),bg="light grey")
      self.entrada1.place(x=400, y=50+20,anchor='center')
      self.entrada2.place(x=400, y=150+20,anchor='center')
      self.entrada3.place(x=400, y=250+20,anchor='center')
      self.entrada4.place(x=400, y=350+20,anchor='center')

   
   def buscar(self):
      '''
      Se pasan los parametros de especificacion en la busqueda y
      presenta la lista objetos resultantes en la busqueda.
      ...
      Parametros
      ----------
      *No tiene parametros*
      '''
      par1=str(self.entrada1.get())
      esp1=str(self.entrada2.get())
      par2=str(self.entrada3.get())
      esp2=str(self.entrada4.get())
      '''Se comprueba si la primera especificacion es de tipo numerico'''
      if esp1.isnumeric() == True:
         esp1=int(esp1)
      '''Se comprueba si la segunda especificacion es de tipo numerico'''
      if esp2.isnumeric() == True:
         esp2=int(esp2)
      '''Creamos la ventana de fondo'''
      root = tk.Toplevel()
      '''Creamos un Widgets Listbox'''
      listb = Listbox(root)
      myquery = {par1: {"$eq": esp1},par2: {"$eq": esp2}}
      mydoc = BaseDeDatos.coleccion.find(myquery)
      '''Insertamos los nombres de la lista en el Listbox'''
      for item in mydoc:
        listb.insert(0,item)
      '''Hacemos el pack del widget'''
      listb.configure(width=150, height=30)
      listb.pack()
      
   def salir():
      '''Salir'''
      salida=Tk()
      salida.destroy()


def main():
   '''Instanciar objeto de la clase Tk'''
   windowEmp=Tk()
   #windowEmp.clear
   textoMayor=Label(windowEmp,text="¿Que desea realizar el dia de hoy?:",font=("Arial",15)).place(x=300,y=100,anchor='center')
   '''Instanciar objeto de la clase MyWindow'''
   mywin=MyWindow(windowEmp)
   windowEmp.clear
   '''Especificacion del titulo de la ventana emergente'''
   windowEmp.title('Menu Empresa')
   '''Especificacion del tamaño de la ventana emergente'''
   windowEmp.geometry("600x500")
   '''ventana emergente'''
   windowEmp.mainloop()
