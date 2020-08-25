import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

class DAO():

    def __init__(self):
        self.onConnection()
    
    def onConnection(self):
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="mysql2019",
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



