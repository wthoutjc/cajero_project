import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk

from views.Cajero import Cajero
from views.Persistence.cuentaDAO import *

class Botones():

    def __init__(self):

        self.operations = cuentaDAO()

        #Botones
        self.imgbtn = Image.open("Sprites/Button/1.png")
        self.imgbtn = self.imgbtn.resize((100, 65), Image.ANTIALIAS) # Redimension (Alto, Ancho)
        self.imgbtn = ImageTk.PhotoImage(self.imgbtn)
    
    def cero(self, root):
        
        self.root = root

        self.bton = Button(self.root,image=self.imgbtn, command = lambda : self.btnSeguir(self.root, self.estado))
        self.bton.place(x=623,y=415)
    
    def uno(self, root):

        self.root = root

        self.bton = Button(self.root,image=self.imgbtn)
        self.bton.place(x=623,y=330)

    def dos(self, root, estado):

        self.root = root
        self.estado = estado

        self.bton = Button(self.root,image=self.imgbtn)
        self.bton.place(x=20,y=415)

    def tres(self, root, estado):

        self.root = root
        self.estado = estado

        self.bton = Button(self.root,image=self.imgbtn)
        self.bton.place(x=20,y=330)

    def cuatro(self, root, estado):

        self.root = root
        self.estado = estado

        self.bton = Button(self.root,image=self.imgbtn)
        self.bton.place(x=623,y=250)

    def btnSeguir(self, root, estado):

        self.root = root
        self.estado = estado

        if self.estado==1:
            pass

    def btnAtras(self, estado):

        self.estado = estado
