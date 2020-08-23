import tkinter as tk
from tkinter import ttk
from tkinter import *

from PIL import Image, ImageTk

from views.Cajero import Cajero
from views.Interfaces import Interfaces
from views.Botones import Botones

cajero = Cajero()
interfaz = Interfaces()
btnes = Botones()

#arregloScreens = [interfaz.screen0(cajero.getRoot()), interfaz.screen1(cajero.getRoot()), interfaz.screen2(cajero.getRoot())]

#arregloScreens[0]
estado = 0
interfaz.screen0(cajero.getRoot())
btnes.cero(cajero.getRoot(), estado)
btnes.uno(cajero.getRoot(), estado)

mainloop()