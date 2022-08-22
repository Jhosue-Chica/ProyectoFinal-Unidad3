from tkinter import *
import tkinter as tk
import InterfazMenuAs
import InterfazMenuEmp
import pymongo

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

class InterfazMenuPrincipal():
    def __init__(self,windowPri):
        self.menubar = Menu(windowPri)
    
    def menu_superior(self):
        windowPri.config(menu=self.menubar)
        helpmenu = Menu(self.menubar, tearoff=0)
        helpmenu.add_command(label="Ayuda")
        helpmenu.add_separator()
        helpmenu.add_command(label="Acerca de...")
        self.menubar.add_cascade(font=("Arial",15),label="Aspirante",command=self.entrarasp) 
        self.menubar.add_cascade(font=("Arial",15),label="Empresa", command=self.entraremp)
        #self.menubar.add_cascade(font=("Arial",15),label="Imprimmir", command=(imprimirpdf))
        self.menubar.add_cascade(font=("Arial",15),label="Salir", command=windowPri.quit)
        self.menubar.add_cascade(font=("Arial",15),label="Ayuda", menu=helpmenu)

    def entrarasp(self):
        aspirante1.__init__(windowPri)
        
    def entraremp(self):
        empresa1.__init__(windowPri)


def imprimirpdf():
    micliente = pymongo.MongoClient("mongodb://localhost:27017/")
    midb = micliente["dbCheckJob"] #base de datos
    micol=midb["registro"] #coleccion
    #lista=[x]
    for x in micol.find():
        w, h = A4
        c = canvas.Canvas("hola-mundo.pdf", pagesize=A4)
        #c.drawString(50, h - 50,lista)
        c.showPage()
        c.save()

def limpiar_entrada(verificacion, entry):
    if verificacion:
        entry.configure( bg="pink")
        entry.delete(0,"end")
    else:
        entry.configure( bg="green2")


def main():
    '''Instanciar objeto de la clase Tk'''
    windowPri.title("Menu Principal")
    windowPri.geometry("600x500")
    menuPri=InterfazMenuPrincipal(windowPri)
    menuPri.menu_superior()
    aspirante1.__init__(windowPri)
    # windowPri=Label(text="¿Que desea realizar el dia de hoy?:",font=("Arial",15)).place(x=300,y=100,anchor='center')
    # windowPri=Button(text='Ingresar como Aspirante',font=("Arial",15), command=opcion1).place(x=300, y=200, anchor='center')
    # windowPri=Button(text='Ingresar como Empresa',font=("Arial",15), command=opcion2).place(x=300, y=300, anchor='center')
    # windowPri=Button(text='Salir',font=("Arial",15), command=salir).place(x=300, y=400, anchor='center')
    '''ventana emergente'''
    mainloop()
        
windowPri=Tk()
aspirante1=InterfazMenuAs.MyWindowMenAsp(windowPri)
empresa1=InterfazMenuEmp.MyWindowMenEmp(windowPri)
