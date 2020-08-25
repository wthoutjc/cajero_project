import random
from tkinter import messagebox as mb
from views.Persistence.DAO import *

class cuentaDAO(DAO):
    
    def crearID(self):
        self.onConnection()
        self.id = random.randint(1000, 9999)
        self.ncursor.execute("SELECT * FROM cuenta")
        self.data = self.ncursor.fetchall()
        for self.elements in self.data:
            if self.elements[0] == self.id:
                self.id = random.randint(1000, 9999)
        return self.id
        self.offConnection()
    
    def consultarCuenta(self):

        try:
            self.onConnection()
            self.insertCommand = "SELECT * FROM cuenta"
            self.ncursor.execute(self.insertCommand)
            self.data = self.ncursor.fetchall()
            return self.data
            self.offConnection()
        except Error as fail:
            print("Error en consulta: {}".format(fail))
            return None

    def consultarCuenta2(self, idPersona):

        self.idPersona = idPersona
 
        try:
            self.onConnection()
            self.insertCommand = "SELECT * FROM cuenta WHERE k_persona = %s"
            self.ncursor.execute(self.insertCommand, (self.idPersona, ))
            self.data = self.ncursor.fetchone()
            self.offConnection()
            return self.data
        except Error as fail:
            print("Error en consulta: {}".format(fail))
            return None

    def registrarCuenta(self, idCuenta, name, apellido, banco, saldo, idPersona, password):
        try:
            self.onConnection()
            self.insertCommand = "INSERT INTO cuenta VALUES(%s,%s,%s,%s,%s,%s,%s)"
            self.ncursor.execute(self.insertCommand, (idCuenta, name, apellido, banco, saldo, idPersona, password))
            self.connection.commit()
            self.offConnection()
        except mysql.connector.Error as fail:
            print("Error al registrar: {}".format(fail))

    def updatePassword(self, password, idPersona):

        self.password = password
        self.idPersona = idPersona
        
        try:
            self.onConnection()
            self.ncursor.execute("SET SQL_SAFE_UPDATES = 0")
            self.ncursor.execute("UPDATE cuenta SET o_password = %s WHERE k_persona = %s", (self.password ,self.idPersona))
            self.ncursor.execute("SET SQL_SAFE_UPDATES = 1")
            self.connection.commit()
            self.offConnection()
        except mysql.connector.Error as fail:
            print("Error al cambiar password: {}".format(fail))

    def entregaSaldoReti(self, idPersona):        
        self.idCuenta = idPersona
        try:
            self.onConnection()
            self.ncursor.execute("SELECT * FROM cuenta WHERE k_persona = %s", ((self.idCuenta), ))
            self.data = self.ncursor.fetchone()
            self.valor = int (self.data[4])
            self.offConnection()
            return self.valor
        except mysql.connector.Error as fail:
            print("Error: {}".format(fail))

    def entregaSaldoCon(self, idCuenta):        
        self.idCuenta = idCuenta
        try:
            self.onConnection()
            self.ncursor.execute("SELECT * FROM cuenta WHERE k_cuenta = %s", ((self.idCuenta), ))
            self.data = self.ncursor.fetchone()
            self.valor = self.data
            self.offConnection()
            return self.valor
        except mysql.connector.Error as fail:
            print("Error: {}".format(fail))

    def updateConsignarPlatica(self, dinero,idPersona):
        
        self.dinero = dinero
        self.idPersona = idPersona
        
        try:
            self.onConnection()
            if self.dinero!=None:
                self.ncursor.execute("SET SQL_SAFE_UPDATES = 0")
                self.ncursor.execute("UPDATE cuenta SET q_saldo = %s WHERE k_persona = %s", (self.dinero ,self.idPersona))
                self.ncursor.execute("SET SQL_SAFE_UPDATES = 1")
                self.connection.commit()
                self.offConnection()
                return True
            else:
                mb.showerror("Cuidado","excediste en el monto a retirar")
                return False
        except mysql.connector.Error as fail:
            print("Error: {}".format(fail))
        