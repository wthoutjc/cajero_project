import tkinter as tk
from tkinter import ttk
from tkinter import *

from PIL import Image, ImageTk

from views.Cajero import Cajero
from views.Interfaces import Interfaces
from views.Estado import Estado

cajero = Cajero()
interfaz = Interfaces(cajero.getRoot())

#arregloScreens = [interfaz.screen0(cajero.getRoot()), interfaz.screen1(cajero.getRoot()), interfaz.screen2(cajero.getRoot())]

#arregloScreens[0]
interfaz.screen0()

mainloop()