import tkinter as tk
from tkinter import ttk
from tkinter import *

from PIL import Image, ImageTk


class Cajero():

    def __init__(self):
    
        ##ventana
        self.root = tk.Tk()
        self.root.title("Cajero")
        self.root.geometry("749x721")
        self.root.resizable(width=0, height=0)
        
        ##fondo // ifo = Imagen Fondo Original
        self.ifo = Image.open("Sprites/Cajero/DiseñoSprites.png")
        self.ifo.thumbnail((749,721))
        self.ifo = ImageTk.PhotoImage(self.ifo)
        self.imgprincipal = Label(self.root, image=self.ifo, width = 1000, height = 980)
        self.imgprincipal.pack()

    def getRoot(self):
        return self.root
