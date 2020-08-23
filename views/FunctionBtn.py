from views.Interfaces import Interfaces
from views.Persistence.cuentaDAO import *

class FunctionBtn():
    def __init__(self):
        self.interfaz = Interfaces()
        self.operationsSQL = cuentaDAO()

    def Func0(self, root, estado):

        self.estado = estado
        self.root = root

        if self.estado == 0:
            try:
                self.interfaz.screen1(self.root)
            except:
                print("Algo ocurrió")
        elif self.estado == 1:
            pass
    
    def Func1(self, root , estado):

        self.estado = estado
        self.root = root

        if self.estado == 0:
            try:
                self.interfaz.screen0(self.root)
            except:
                print("Algo ocurrió")
        elif self.estado == 1:
            pass