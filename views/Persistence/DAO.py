import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

class DAO():

    _DAO_instance = None

    def __init__(self):
        self.onConnection()
    
    @classmethod
    def get_instance(cls):

        if not DAO._DAO_instance:
            _DAO_instance = cls()
            _DAO_instance.onConnection()
        return _DAO_instance

    def onConnection(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="Valhalla%27",
                database="cajero")
            
            self.ncursor = self.connection.cursor()
            print("Conexión exitosa")
        except mysql.connector.Error as fail:
            print("(onConnection) Algo ocurrió: {}".format(fail))

    def offConnection(self):
        try:
            self.connection.close()
        except mysql.connector.Error as fail:
            print("(offConnection) Algo ocurrió: {}".format(fail))



