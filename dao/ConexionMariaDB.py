from . import singleton, mariadb
from dtos.MeteoBean import MeteoBean
from utils.leer_properties import LeerProperty


@singleton
class ConexionMariaDB:
    def __init__(self):
        self.conexion = None

    def getInstancia(self):
        if self.conexion is None:
            print("Conectando con el servidor MariaDB")
            try:
                self.conexion = mariadb.connect(
                    user=LeerProperty.get_property_value("sql.user"),
                    password=LeerProperty.get_property_value("sql.password"),
                    host=LeerProperty.get_property_value("sql.host"),
                    port=int(LeerProperty.get_property_value("sql.port")),
                    database=LeerProperty.get_property_value("sql.database"))
                print("Conectado..")
            except mariadb.OperationalError as e:
                print(f"Error TimeOut en MariaDB: {e}")
            except mariadb.Error as e:
                print(f"Error conectando a MariaDB: {e}")
        else:
            print("Ya tiene conector", self.conexion)

    def obtener_info_by_chipid(self, idValor: int) -> []:
        # Get Cursor
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM ESTA_METEO_DATA WHERE CHIP_ID=?", (idValor,))
        lstMeteoBean = []
        for fila in cursor:
            print(f"ID: {fila[0]}, CHIP_ID: {fila[1]}, TEMPERATURA: {fila[2]}, HUMEDAD: {fila[3]}, "
                  f"HIC: {fila[4]}, FECHA_CREACION: {fila[5]}")
            meteoBean = MeteoBean(fila[0], fila[1], fila[2], fila[3], fila[4], fila[5])
            lstMeteoBean.append(meteoBean)
        cursor.close()
        return lstMeteoBean

    def obtener_by_chip(self, chipId: str):
        cursor = self.conexion.cursor()
        cursor.execute("SELECT * FROM ESTA_METEO_DATA WHERE CHIP_ID=?", (chipId,))
        for fila in cursor:
            print(f"ID: {fila[0]}, CHIP_ID: {fila[1]}, TEMPERATURA: {fila[2]}, HUMEDAD: {fila[3]}, "
                  f"HIC: {fila[4]}, FECHA_CREACION: {fila[5]}")
        cursor.close()

    def save_info_chip(self, meteoBean: MeteoBean):
        cursor = self.conexion.cursor()
        try:
            cursor.execute("INSERT INTO PRODUCT (CHIP_ID, TEMPERATURA, HUMEDAD, hic, FEC_GRABADO) VALUES (?,?,?,?,?)",
                           (meteoBean.getChipId(), meteoBean.getTemperatura(),
                            meteoBean.getHumedad(), meteoBean.getHic(),
                            meteoBean.getFechaGrabado()))
        except mariadb.Error as e:
            print(f"Error: {e}")

        print(f"{cursor.rowcount}, details inserted")
        self.conexion.commit()
