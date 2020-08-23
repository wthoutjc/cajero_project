import tkinter as tk
from tkinter import ttk
from tkinter import *

from PIL import Image, ImageTk

from views.configScreen import configScreen
from views.Estado import Estado

class Interfaces():

    def __init__(self, root):

        self.root = root
        self.config = configScreen()
        self.status = Estado()

    def screen0(self):

        self.status.setEstado(0)

        self.fondo = Label(self.root,image=self.config.setScreen(0), width = 445, height = 365 )
        self.fondo.place(x=150,y=125)
        self.text1 = Label(self.root, text = "Registrarse" )
        self.text1.place(x=423, y = 455)
        self.text2 = Label(self.root, text = "Iniciar Sesión" )
        self.text2.place(x=423, y = 360)     

    def screen1(self):

        self.status.setEstado(1)

        self.fondo = Label(self.root,image=self.config.setScreen(1), width = 445, height = 365 )
        self.fondo.place(x=150,y=125)
        self.text1 = Label(self.root, text = "Continuar" )
        self.text1.place(x=423, y = 455)
        self.text2 = Label(self.root, text = "Volver" )
        self.text2.place(x=423, y = 360)
        
    def screen2(self):

        self.status.setEstado(2)

        self.fondo = Label(self.root,image=self.config.setScreen(2), width = 445, height = 365 )
        self.fondo.place(x=150,y=125)
        self.text1 = Label(self.root, text = "Continuar" )
        self.text1.place(x=423, y = 455)

    def screenAgrario(self):

        self.status.setEstado(3) # Estado 3 = Agrario 3,4,5 -> BANCOS

        self.fondo = Label(self.root,image=self.config.setScreen(3), width = 445, height = 365 )
        self.fondo.place(x=150,y=125)
        self.text1 = Label(self.root, text = "Saldo" )
        self.text1.place(x=423, y = 455)
        self.text2 = Label(self.root, text = "Volver" )
        self.text2.place(x=423, y = 360)
    
    def screenBancolombia(self):

        self.status.setEstado(4)

        self.fondo = Label(self.root,image=self.config.setScreen(3), width = 445, height = 365 )
        self.fondo.place(x=150,y=125)
        self.text1 = Label(self.root, text = "Saldo" )
        self.text1.place(x=423, y = 455)
        self.text2 = Label(self.root, text = "Volver" )
        self.text2.place(x=423, y = 360)
    
    def screenDavivienda(self):

        self.status.setEstado(5)

        self.fondo = Label(self.root,image=self.config.setScreen(3), width = 445, height = 365 )
        self.fondo.place(x=150,y=125)
        self.text1 = Label(self.root, text = "Saldo" )
        self.text1.place(x=423, y = 455)
        self.text2 = Label(self.root, text = "Volver" )
        self.text2.place(x=423, y = 360)
        
    def arregloScreens(self):

        self.arreglo = [self.screen0(), self.screen1(), self.screen2()]
        return self.arreglo