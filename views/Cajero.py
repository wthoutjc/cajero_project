import tkinter as tk
from tkinter import ttk
from tkinter import *

from PIL import Image, ImageTk

from views.Botones import Botones
from views.Interfaces import Interfaces

class Cajero():

    def __init__(self):
    
        ##ventana
        self.root = tk.Tk()
        self.root.title("Cajero")
        self.root.geometry("749x721")
        self.root.resizable(width=0, height=0)

        self.intfz = Interfaces(self.root)
        self.manejoBtn = Botones(self.root, self.intfz.arregloScreens())
        
        ##fondo // ifo = Imagen Fondo Original
        self.ifo = Image.open("Sprites/Cajero/DiseñoSprites.png")
        self.ifo.thumbnail((749,721))
        self.ifo = ImageTk.PhotoImage(self.ifo)
        self.imgprincipal = Label(self.root, image=self.ifo, width = 1000, height = 980)
        self.imgprincipal.pack()
        self.manejoBtn.cero()
        self.manejoBtn.uno()
        self.manejoBtn.dos()
        self.manejoBtn.tres()
        self.manejoBtn.cuatro()

    def getRoot(self):
        return self.root
