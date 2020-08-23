from views.Estado import Estado
from views.Persistence.cuentaDAO import *

class FunctionBtn():
    def __init__(self):

        self.status = Estado()
        self.operationsSQL = cuentaDAO()

    def Func0(self, arreglo):

        self.arreglo = arreglo
        print(self.status.getEstado())

        if self.status.getEstado() == 0:
            try:
                print(self.status.getEstado())
                self.arreglo[1]
            except:
                print("Algo ocurrió")
        elif self.status.getEstado() == 1:
            pass
    
    def Func1(self,arreglo):

        print(self.status.getEstado())

        if self.status.getEstado() == 0:
            try:
                print(self.status.getEstado())
                self.arreglo[1]
                self.status.setEstado(1)
            except:
                print("Algo ocurrió")
        elif self.status.getEstado() == 1:
            pass

    def Func2(self,arreglo):

        if self.status.getEstado() == 0:
            pass
        elif self.status.getEstado() == 1:
            pass
    
    def Func3(self,arreglo):

        if self.status.getEstado() == 0:
            pass
        elif self.status.getEstado() == 1:
            pass
    
    def Func4(self,arreglo):

        if self.status.getEstado() == 0:
            pass
        elif self.status.getEstado() == 1:
            pass