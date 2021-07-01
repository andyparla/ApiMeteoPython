from dao.ConexionMariaDB import ConexionMariaDB

class MeteoService():

    def obtenerInfoById(self, id:int):
        conexion = ConexionMariaDB().obtenerInfoById(id)

    def saveInfo(self):
        pass
