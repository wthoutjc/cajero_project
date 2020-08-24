from views.Persistence.cuentaDAO import *
from views.Interfaces import Interfaces

class FunctionBtn():
    def __init__(self, root):

        self.root = root
        self.status = None
        self.operationsSQL = cuentaDAO()
        self.manejoScreens = Interfaces(self.root)

    def Func0(self):

        print("Estado FunANTES: " + str(self.manejoScreens.getEstado()))
        if self.manejoScreens.getEstado() == 0: # LOGIN
            self.manejoScreens.screen1LogIn()
            print("Estado FunDESPUES: " + str(self.manejoScreens.getEstado()))
        elif self.manejoScreens.getEstado() == 11: #VOLVER
            self.manejoScreens.screen0()
            print("Estado FunDESPUES: " + str(self.manejoScreens.getEstado()))
        elif self.manejoScreens.getEstado() == 12: #VOLVER
            self.manejoScreens.screen0()
            print("Estado FunDESPUES: " + str(self.manejoScreens.getEstado()))

    def Func1(self):

        print("Estado FunANTES: " + str(self.manejoScreens.getEstado()))
        if self.manejoScreens.getEstado() == 0: # REGISTRARSE
            self.manejoScreens.screen1Register()
            print("Estado FunDESPUES: " + str(self.manejoScreens.getEstado()))
        elif self.manejoScreens.getEstado() == 11: # VALIDAR INFO DE REGISTRARSE Y VOLVER A MENSAJE SUCCES: CUENTA CREADA
            self.validate = True
            try:
                self.data = self.operationsSQL.consultarCuenta()
                for self.elements in self.data:
                    if int(self.elements[5]) == int(self.manejoScreens.getIdPersona()):
                        self.validate = False
                if self.validate == True:
                    self.operationsSQL.registrarCuenta(self.operationsSQL.crearID(), self.manejoScreens.getNombre(), self.manejoScreens.getApellido(), self.manejoScreens.getBanco(), self.manejoScreens.getSaldo(), self.manejoScreens.getIdPersona(), self.manejoScreens.getPassword())
                    self.manejoScreens.screenConfirmación21()
                    print("Estado FunDESPUES: " + str(self.manejoScreens.getEstado()))
                else:
                    self.manejoScreens.screenError22()
                    print("Estado FunDESPUES: " + str(self.manejoScreens.getEstado()))
            except:
                self.manejoScreens.screenError22()
                print("Estado FunDESPUES: " + str(self.manejoScreens.getEstado()))

        elif self.manejoScreens.getEstado() == 12: # VALIDAR INFO DE LOGIN Y VOLVER A MENSAJE SUCCES: CARGAR BANCO
            self.datos = self.operationsSQL.consultarCuenta2(self.manejoScreens.getIdPersona2())
            try:
                if self.datos[6] == self.manejoScreens.getPassword2():
                    if self.datos[3] == 'Agrario':
                        self.manejoScreens.screenAgrario()
                        print("Estado FunDESPUES: " + str(self.manejoScreens.getEstado()))
                    elif self.datos[3] == 'Bancolombia':
                        self.manejoScreens.screenBancolombia()
                        print("Estado FunDESPUES: " + str(self.manejoScreens.getEstado()))
                    elif self.datos[3] == 'Davivienda':
                        self.manejoScreens.screenDavivienda()
                        print("Estado FunDESPUES: " + str(self.manejoScreens.getEstado()))
                    else:
                        self.manejoScreens.screenError22()
                        print("Estado FunDESPUES: " + str(self.manejoScreens.getEstado()))
                else:
                    self.manejoScreens.screenError22()
                    print("Estado FunDESPUES: " + str(self.manejoScreens.getEstado()))
            except:
                self.manejoScreens.screenError22()
                print("Estado FunDESPUES: " + str(self.manejoScreens.getEstado()))
            
        elif self.manejoScreens.getEstado() == 21: #DATOS VALIDADOS: MENU INICIAL
            self.manejoScreens.screen0()
            print("Estado FunDESPUES: " + str(self.manejoScreens.getEstado()))

        elif self.manejoScreens.getEstado() == 22: #DATOS INVALIDADOS: MENU INICIAL
            self.manejoScreens.screen0()
            print("Estado FunDESPUES: " + str(self.manejoScreens.getEstado()))

    def Func2(self):

        if self.manejoScreens.getEstado() == 3:
            pass
        else:
            pass
    
    def Func3(self):

        if self.manejoScreens.getEstado() == 3:
            pass
        else:
            pass
    
    def Func4(self):

        if self.manejoScreens.getEstado() == 3:
            pass
        else:
            pass