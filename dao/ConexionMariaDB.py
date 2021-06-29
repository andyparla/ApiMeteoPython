import mariadb
import sys

def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

@singleton
class ConexionMariaDB():
    conexion = None

    def getInstancia(self): 
        if self.conexion is None:
            print("Conectando con el servidor MariaDB")
            try:
                self.conexion = mariadb.connect(
                    user="andyparla",
                    password="Trasto,.01",
                    host="192.168.4.130",
                    port=3306,
                    database="ESTACION_METEOROLOGICA")
                print("Conectado..")            
            except mariadb.OperationalError as e:
                print(f"Error TimeOut en MariaDB: {e}")
            except mariadb.Error as e:
                print(f"Error conectando a MariaDB: {e}")
        else:
            print("Ya tiene conector", self.conexion)
        

ConexionMariaDB().getInstancia()
ConexionMariaDB().getInstancia()