from models.cuenta import Cuenta

class CuentaController():
    
    def __init__(self, arregloCuenta):
        self.__arregloCuenta = arregloCuenta

    def getSize(self):
        return len(self.__arregloCuenta)