import tkinter as tk
from tkinter import ttk
from tkinter import *

from views.Cajero import Cajero
from views.Interfaces import Interfaces

cajero = Cajero()
vi = Interfaces(cajero.getRoot())
vi.screen0()
mainloop()