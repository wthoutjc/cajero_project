import random

from views.Persistence.DAO import *

class cuentaDAO(DAO):

    def __init__(self):
        DAO.__init__(self)
    
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
        print(self.idPersona)

        try:
            self.onConnection()
            self.insertCommand = "SELECT * FROM cuenta WHERE k_persona = %s"
            self.ncursor.execute(self.insertCommand, (self.idPersona, ))
            self.data = self.ncursor.fetchone()
            return self.data
            self.offConnection()
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

    def updatePassword(self, idPersona, password):
        try:
            self.onConnection()
            self.insertCommand = "UPDATE cuenta SET o_password = %s WHERE k_persona = %s"
            self.ncursor.execute(self.insertCommand, (idPersona, password))
            self.connection.commit()
            self.offConnection()
        except mysql.connector.Error as fail:
            print("Error al cambiar password: {}".format(fail))

    def updateSaldo(self,idCuenta, saldo):
        try:
            self.onConnection()
            self.insertCommand = "UPDATE cuenta SET q_saldo = %s WHERE idCuenta = %s"
            self.ncursor.execute(self.insertCommand, (idCuenta, saldo))
            self.connection.commit()
            self.offConnection()
        except mysql.connector.Error as fail:
            print("Error al cambiar password: {}".format(fail))