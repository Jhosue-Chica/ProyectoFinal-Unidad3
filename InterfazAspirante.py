'''importar la libreria tkinter para la parte de la interfaz grafica'''
from tkinter import *
'''Se importa la libreria de mongo ya que python necesita un driver para
acceder a la base de datos de MongoDB'''
import pymongo

import BaseDeDatos
import InterfazPrincipal

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
      menubar = Menu(self.win)
      self.win.config(menu=menubar)

      helpmenu = Menu(menubar, tearoff=0)
      helpmenu.add_command(label="Ayuda")
      helpmenu.add_separator()
      helpmenu.add_command(label="Acerca de...")

      menubar.add_cascade(font=("Arial",15),label="Todo",command=self.formulario_todo) 
      menubar.add_cascade(font=("Arial",15),label="Buscar", command=(self.formulario_buscar))
      menubar.add_cascade(font=("Arial",15),label="Imprimmir", command=(InterfazPrincipal.imprimirpdf))
      menubar.add_cascade(font=("Arial",15),label="Salir", command=self.win.quit)
      menubar.add_cascade(font=("Arial",15),label="Ayuda", menu=helpmenu)
      self.formulario_todo()
      
   def formulario_todo(self):
      micliente = pymongo.MongoClient("mongodb://localhost:27017/")
      midb = micliente["dbCheckJob"] #base de datos
      micol=midb["registro"] #coleccion
      i=20
      for x in micol.find():
         self.label=Label(self.win, text=x,font=("Arial",12), fg="black").place(x=5,y=i)
         i+=50
      
   def formulario_buscar(self):
      self.titulo = Label(self.win, text="Busque su trabajo ideal",font=("Arial",15), fg="black").place(x=300,y=10,anchor='center')
      self.texto1=Label(self.win, text='Tipo 1',font=("Arial",15), fg="black").place(x=100,y=50)
      self.texto2=Label(self.win, text='Especificacion 1',font=("Arial",15), fg="black").place(x=100,y=150)
      self.texto3=Label(self.win, text='Tipo 2',font=("Arial",15), fg="black").place(x=100,y=250)
      self.texto4=Label(self.win, text='Especificacion 2',font=("Arial",15), fg="black").place(x=100,y=350)
      self.boton1=Button(self.win, text='Buscar',font=("Arial",15), command=self.buscar).place(x=400,y=450,anchor='center')
      self.boton2=Button(self.win, text='Volver Atras',font=("Arial",15), command=self.volver_atras).place(x=170,y=450,anchor='center')
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
      root = Tk()
      '''Creamos un Widgets Listbox'''
      listb = Listbox(root)
      myquery = {par1: {"$eq": esp1},par2: {"$eq": esp2}}
      mydoc = BaseDeDatos.coleccion.find(myquery)
      '''Insertamos los nombres de la lista en el Listbox'''
      for item in mydoc:
        listb.insert(0,item)
      '''Hacemos el pack del widget'''
      listb.configure(width=100,height=31)
      listb.pack()
      
   def volver_atras(self):
      InterfazPrincipal.main()

def main():
   '''Instanciar objeto de la clase Tk'''
   '''Instanciar objeto de la clase MyWindow'''

   window=Tk()

   mywin=MyWindow(window)
   '''Especificacion del titulo de la ventana emergente'''
   window.title('Busqueda de objeto especifico')
   '''Especificacion del tamaño de la ventana emergente'''
   window.geometry("600x500")
   '''ventana emergente'''
   window.mainloop()
   
