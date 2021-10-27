from dao.ConexionMariaDB import ConexionMariaDB


class MeteoService:
    def __init__(self):
        self.dao = ConexionMariaDB()

    def obtenerInfoById(self, id: int) -> []:
        lstMeteo= self.dao.obtener_info_by_chipid(id)
        print(f"tamaño de la lista retornada {len(lstMeteo)}")

        return lstMeteo

    def saveInfo(self):
        pass
