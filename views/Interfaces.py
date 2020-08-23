import tkinter as tk
from tkinter import ttk
from tkinter import *

from PIL import Image, ImageTk

from views.Botones import Botones
from views.Cajero import Cajero
from views.configScreen import configScreen

class Interfaces():

    def __init__(self):

        self.manejoBtn = Botones()
        self.config = configScreen()

    def screen0(self, root):

        self.root = root

        self.fondo = Label(self.root,image=self.config.setScreen(0), width = 445, height = 365 )
        self.fondo.place(x=150,y=125)
        self.text1 = Label(self.root, text = "Registrarse" )
        self.text1.place(x=423, y = 455)
        self.text2 = Label(self.root, text = "Iniciar Sesión" )
        self.text2.place(x=423, y = 360)
        self.manejoBtn.cero(self.root)
        self.manejoBtn.uno(self.root)

    def screen1(self, root):

        self.root = root

        self.fondo = Label(self.root,image=self.config.setScreen(1), width = 445, height = 365 )
        self.fondo.place(x=150,y=125)
        self.text1 = Label(self.root, text = "Continuar" )
        self.text1.place(x=423, y = 455)
        self.text2 = Label(self.root, text = "Volver" )
        self.text2.place(x=423, y = 360)

    def screen2(self, root):

        self.root = root

        self.fondo = Label(self.root,image=self.config.setScreen(2), width = 445, height = 365 )
        self.fondo.place(x=150,y=125)
        self.text1 = Label(self.root, text = "Continuar" )
        self.text1.place(x=423, y = 455)

    def screenAgrario(self, root):

        self.root = root

        self.fondo = Label(self.root,image=self.config.setScreen(3), width = 445, height = 365 )
        self.fondo.place(x=150,y=125)
        self.text1 = Label(self.root, text = "Saldo" )
        self.text1.place(x=423, y = 455)
        self.text2 = Label(self.root, text = "Volver" )
        self.text2.place(x=423, y = 360)
        
        