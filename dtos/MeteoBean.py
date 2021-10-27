class MeteoBean:

    def __init__(self, id, chip_id, temperatura, humedad, hic, fecha_grabado):
        self.id = id
        self.chipId = chip_id
        self.temperatura = temperatura
        self.humedad = humedad
        self.hic = hic
        self.fechaGrabado = fecha_grabado

    def get_id(self):
        return self.id

    def get_chip_id(self):
        return self.chipId

    def get_temperatura(self):
        return self.temperatura

    def get_humedad(self):
        return self.humedad

    def getHic(self):
        return self.hic

    def get_fecha_grabado(self):
        return self.fechaGrabado
