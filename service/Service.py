from dao.ConexionMariaDB import ConexionMariaDB

class MeteoService():

    def obtenerInfoById(self):
        conexion = ConexionMariaDB().obtenerInfoById(1)

    def saveInfo(self):
        pass
