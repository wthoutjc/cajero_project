from views.Persistence.cuentaDAO import *
from views.Interfaces import Interfaces
from views.Info import Info

class FunctionBtn():
    def __init__(self, root):

        self.root = root
        self.status = None
        self.operationsSQL = cuentaDAO()
        self.manejoScreens = Interfaces(self.root)
        self.idInfo = Info()

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
        elif self.manejoScreens.getEstado() == 3: #BANCO: CONSULTAR SALDO
            try:
                self.data = self.operationsSQL.consultarCuenta2(self.idInfo.getInfo())
                self.manejoScreens.screenSaldo42(self.data[1], self.data[4])
            except:
                self.manejoScreens.screenError22()

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
                    self.manejoScreens.screenConfirmacion21()
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
                        self.idInfo.setInfo(self.manejoScreens.getIdPersona2())
                        self.manejoScreens.screenAgrario()
                        print("Estado FunDESPUES: " + str(self.manejoScreens.getEstado()))
                    elif self.datos[3] == 'Bancolombia':
                        self.idInfo.setInfo(self.manejoScreens.getIdPersona2())
                        self.manejoScreens.screenBancolombia()
                        print("Estado FunDESPUES: " + str(self.manejoScreens.getEstado()))
                    elif self.datos[3] == 'Davivienda':
                        self.idInfo.setInfo(self.manejoScreens.getIdPersona2())
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
        elif self.manejoScreens.getEstado() == 42: #VOLVER AL MENU DEL BANCO
            self.datos = self.operationsSQL.consultarCuenta2(self.idInfo.getInfo())
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
        elif self.manejoScreens.getEstado() == 43: #CAMBIO CLAVE CONTINUAR
            print("Estado FunAntes: " + str(self.manejoScreens.getEstado()))
            self.data = self.operationsSQL.consultarCuenta2(self.idInfo.getInfo())
            if self.data[6] == self.manejoScreens.getOldPassword():
                print("NEW: "+str(self.manejoScreens.getNewPassword()))
                print("NEW: "+str(self.idInfo.getInfo()))
                self.operationsSQL.updatePassword(self.manejoScreens.getNewPassword(), self.idInfo.getInfo())
                self.manejoScreens.screenConfirmacion21()
                print("Estado FunDESPUES: " + str(self.manejoScreens.getEstado()))

    def Func2(self):
        print("Estado FunANTES: " + str(self.manejoScreens.getEstado()))
        if self.manejoScreens.getEstado() == 3:
            self.manejoScreens.screenClave43()
            print("Estado FunDESPUES: " + str(self.manejoScreens.getEstado()))
        else:
            pass
    
    def Func3(self):

        if self.manejoScreens.getEstado() == 3:
            pass
        else:
            pass
    
    def Func4(self):

        if self.manejoScreens.getEstado() == 3:
            self.manejoScreens.screen0()
        else:
            pass