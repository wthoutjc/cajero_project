from views.Persistence.cuentaDAO import *
from views.Interfaces import Interfaces
from views.Info import Info
from views.mediador import mediator

class FunctionBtn():
    def __init__(self, root):

        self.root = root
        self.status = None
        self.operationsSQL = cuentaDAO()
        self.manejoScreens = Interfaces(self.root)
        self.idInfo = Info()

    def Func0(self):

        if self.manejoScreens.getEstado() == 0: # LOGIN
            self.manejoScreens.screen1LogIn()
        elif self.manejoScreens.getEstado() == 11: #VOLVER
            self.manejoScreens.screen0()
        elif self.manejoScreens.getEstado() == 12: #VOLVER
            self.manejoScreens.screen0()
        elif self.manejoScreens.getEstado() == 3: #BANCO: CONSULTAR SALDO
            try:
                self.data = self.operationsSQL.consultarCuenta2(self.idInfo.getInfo())
                self.manejoScreens.screenSaldo42(self.data[1], self.data[4])
            except:
                self.manejoScreens.screenError22()
        elif self.manejoScreens.getEstado() == 43 or self.manejoScreens.getEstado() == 44 or self.manejoScreens.getEstado() == 45: #VOLVER A MENU BANCOS
            self.datos = self.operationsSQL.consultarCuenta2(self.idInfo.getInfo())
            try:
                if self.datos[3] == 'Agrario':
                    self.manejoScreens.screenAgrario()
                elif self.datos[3] == 'Bancolombia':
                    self.manejoScreens.screenBancolombia()
                elif self.datos[3] == 'Davivienda':
                    self.manejoScreens.screenDavivienda()
                else:
                    self.manejoScreens.screenError22()
            except:
                self.manejoScreens.screenError22()

    def Func1(self):

        if self.manejoScreens.getEstado() == 0: # REGISTRARSE
            self.manejoScreens.screen1Register()
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
                else:
                    self.manejoScreens.screenError22()
            except:
                self.manejoScreens.screenError22()

        elif self.manejoScreens.getEstado() == 12: # VALIDAR INFO DE LOGIN Y VOLVER A MENSAJE SUCCES: CARGAR BANCO
            self.datos = self.operationsSQL.consultarCuenta2(self.manejoScreens.getIdPersona2())
            try:
                if self.datos[6] == self.manejoScreens.getPassword2():
                    if self.datos[3] == 'Agrario':
                        self.idInfo.setInfo(self.manejoScreens.getIdPersona2())
                        self.manejoScreens.screenAgrario()
                    elif self.datos[3] == 'Bancolombia':
                        self.idInfo.setInfo(self.manejoScreens.getIdPersona2())
                        self.manejoScreens.screenBancolombia()
                    elif self.datos[3] == 'Davivienda':
                        self.idInfo.setInfo(self.manejoScreens.getIdPersona2())
                        self.manejoScreens.screenDavivienda()
                    else:
                        self.manejoScreens.screenError22()
                else:
                    self.manejoScreens.screenError22()
            except:
                self.manejoScreens.screenError22()
            
        elif self.manejoScreens.getEstado() == 21: #DATOS VALIDADOS: MENU INICIAL
            self.manejoScreens.screen0()

        elif self.manejoScreens.getEstado() == 22: #DATOS INVALIDADOS: MENU INICIAL
            self.manejoScreens.screen0()
        elif self.manejoScreens.getEstado() == 3: #CONSIGNAR
            self.manejoScreens.screenConsignar()
        elif self.manejoScreens.getEstado() == 42: #VOLVER AL MENU DEL BANCO
            self.datos = self.operationsSQL.consultarCuenta2(self.idInfo.getInfo())
            try:
                if self.datos[3] == 'Agrario':
                    self.manejoScreens.screenAgrario()
                elif self.datos[3] == 'Bancolombia':
                    self.manejoScreens.screenBancolombia()
                elif self.datos[3] == 'Davivienda':
                    self.manejoScreens.screenDavivienda()
                else:
                    self.manejoScreens.screenError22()
            except:
                self.manejoScreens.screenError22()
        elif self.manejoScreens.getEstado() == 43: #CAMBIO CLAVE CONTINUAR
            self.data = self.operationsSQL.consultarCuenta2(self.idInfo.getInfo())
            if self.data[6] == self.manejoScreens.getOldPassword():
                self.operationsSQL.updatePassword(self.manejoScreens.getNewPassword(), self.idInfo.getInfo())
                self.manejoScreens.screenConfirmacion21()

        elif self.manejoScreens.getEstado() == 44: #RETIRAR
            self.mediator =mediator(self.idInfo.getInfo(),self.manejoScreens.getValorR(),self.manejoScreens.getEstado())
            self.mediator.conectar()
            self.manejoScreens.screenConfirmacion21()
            #self.operationsSQL.updateSaldoRetirar(self.manejoScreens.getValorR(), self.idInfo.getInfo())
            #self.manejoScreens.screenConfirmacion21()

        elif self.manejoScreens.getEstado() == 45: #CONSIGNAR
            self.mediator =mediator(self.manejoScreens.getIdCuentaC(),self.manejoScreens.getValorC(),self.manejoScreens.getEstado())
            if self.mediator.conectar()==True:
                self.manejoScreens.screenConfirmacion21()
            else:
                self.manejoScreens.screenError22()

            
            #try:
            #    self.operationsSQL.updateSaldoConsignar(self.manejoScreens.getValorC(), self.manejoScreens.getIdCuentaC())
            #    self.manejoScreens.screenConfirmacion21()
            #except:
             #   self.manejoScreens.screenError22()
    def Func2(self):
        if self.manejoScreens.getEstado() == 3:
            self.manejoScreens.screenClave43()
        else:
            pass
    
    def Func3(self):

        if self.manejoScreens.getEstado() == 3:
            self.manejoScreens.screenRetirar()
        else:
            pass
    
    def Func4(self):

        if self.manejoScreens.getEstado() == 3:
            self.manejoScreens.screen0()
        else:
            pass