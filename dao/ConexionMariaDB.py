import mariadb
import sys
from dtos.MeteoBean import MeteoBean

def singleton(class_):
    instances = {}
    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return getinstance

@singleton
class ConexionMariaDB ():
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

    def obtenerInfoById(self, idValor: int):
        # Get Cursor
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM ESTA_METEO_DATA WHERE ID=?", (idValor,))
        for fila in cursor:
            print(f"ID: {fila[0]}, CHIP_ID: {fila[1]}, TEMPERATURA: {fila[2]}, HUMEDAD: {fila[3]}, "
                  f"HIC: {fila[4]}, FECHA_CREACION: {fila[5]}")
        cursor.close()
        self.conexion.close()

    def obtenerByChip(self, chipId: str):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM ESTA_METEO_DATA WHERE CHIP_ID=?", (chipId,))
        for fila in cursor:
            print(f"ID: {fila[0]}, CHIP_ID: {fila[1]}, TEMPERATURA: {fila[2]}, HUMEDAD: {fila[3]}, "
                  f"HIC: {fila[4]}, FECHA_CREACION: {fila[5]}")
        cursor.close()
        self.conexion.close()

    def saveInfoChip(self, meteoBean: MeteoBean):
        cursor = self.conexion.cursor()
        try:
            cursor.execute("INSERT INTO PRODUCT (CHIP_ID, TEMPERATURA, HUMEDAD, hic, FEC_GRABADO) VALUES (?,?,?,?,?)",\
                (meteoBean.getChipId(), meteoBean.getTemperatura(),
                 meteoBean.getHumedad(), meteoBean.getHic(),
                 meteoBean.getFechaGrabado()))
        except mariadb.Error as e:
            print(f"Error: {e}")

        print(f"{cursor.rowcount}, details inserted")
        self.conexion.commit()
        self.conexion.close()
