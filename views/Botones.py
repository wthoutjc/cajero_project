import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import Image, ImageTk

from views.FunctionBtn import FunctionBtn

class Botones():

    def __init__(self, root, arreglo):

        self.root = root
        self.functionbtn = FunctionBtn()
        self.arreglo = arreglo
        #Botones
        self.imgbtn = Image.open("Sprites/Button/1.png")
        self.imgbtn = self.imgbtn.resize((100, 65), Image.ANTIALIAS) # Redimension (Alto, Ancho)
        self.imgbtn = ImageTk.PhotoImage(self.imgbtn)
    
    def cero(self):
    
        self.bton = Button(self.root,image=self.imgbtn, command = lambda: self.functionbtn.Func0(self.arreglo))
        self.bton.place(x=623,y=415)
    
    def uno(self):

        self.bton = Button(self.root,image=self.imgbtn, command = lambda: self.functionbtn.Func1(self.arreglo))
        self.bton.place(x=623,y=330)

    def dos(self):

        self.bton = Button(self.root,image=self.imgbtn)
        self.bton.place(x=20,y=415)

    def tres(self):

        self.bton = Button(self.root,image=self.imgbtn)
        self.bton.place(x=20,y=330)

    def cuatro(self):

        self.bton = Button(self.root,image=self.imgbtn)
        self.bton.place(x=623,y=250)

