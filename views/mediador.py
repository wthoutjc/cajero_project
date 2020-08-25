from views.Persistence.cuentaDAO import *
class mediator():
    def __init__(self,idperson,diner,accion):
       self.id=idperson
       self.Dinero = int (diner)
       self.accion =accion 
       self.basesD = cuentaDAO()


    def sumar(self,dine1,dine2):
        self.suma=dine1 + dine2
        return self.suma

    def restar(self,dine1,dine2):
        if dine1<dine2:
            return None
        elif dine1>=dine2:
            self.resta=dine1-dine2
            return self.resta


    def conectar(self):
        print(self.id)        
        if self.accion==45:
            self.arr=self.basesD.entregaSaldoCon(self.id)
            self.dine1= int (self.arr[4])
            self.idperson = self.arr[5] 
            print(self.idperson)           
            self.resultado=self.sumar(self.dine1,self.Dinero)
            return self.basesD.updateConsignarPlatica(self.resultado,self.idperson)
        elif self.accion==44:
            self.dine1 =self.basesD.entregaSaldoReti(self.id)
            self.resultado=self.restar(self.dine1,self.Dinero)
            return self.basesD.updateConsignarPlatica(self.resultado,self.id)   