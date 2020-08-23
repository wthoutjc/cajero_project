import random

from views.Persistence.DAO import *

class cuentaDAO(DAO):

    def __init__(self):
        DAO.__init__(self)
    
    def crearID(self):
        self.id = random.randint(1000, 9999)
        self.ncursor.execute("SELECT * FROM cuenta")
        self.data = self.ncursor.fetchall()
        for self.elements in self.data:
            if self.elements[0] == self.id:
                self.id = random.randint(1000, 9999)
        return self.id

    def consultarCuenta(self):
        try:
            self.insertCommand = "SELECT * FROM cuenta"
            self.ncursor.execute(self.insertCommand)
            self.data = self.ncursor.fetchall()
            return self.data
        except Error as fail:
            print("Error en conexión: {}".format(fail))

    def registrarCuenta(self, idCuenta, name, apellido, banco, saldo, idPersona, password):
        try:
            self.insertCommand = "INSERT INTO cuenta VALUES(%s,%s,%s,%s,%s,%s,%s)"
            self.ncursor.execute(self.insertCommand, (idCuenta, name, apellido, banco, saldo, idPersona, password))
            self.connection.commit()
            self.offConnection()
        except mysql.connector.Error as fail:
            print("Error al registrar: {}".format(fail))

    def updatePassword(self,idCuenta, password):
        try:
            self.insertCommand = "UPDATE cuenta SET o_password = %s WHERE idCuenta = %s"
            self.ncursor.execute(self.insertCommand, (idCuenta, password))
            self.connection.commit()
            self.offConnection()
        except mysql.connector.Error as fail:
            print("Error al cambiar password: {}".format(fail))

    def updateSaldo(self,idCuenta, saldo):
        try:
            self.insertCommand = "UPDATE cuenta SET q_saldo = %s WHERE idCuenta = %s"
            self.ncursor.execute(self.insertCommand, (idCuenta, saldo))
            self.connection.commit()
            self.offConnection()
        except mysql.connector.Error as fail:
            print("Error al cambiar password: {}".format(fail))