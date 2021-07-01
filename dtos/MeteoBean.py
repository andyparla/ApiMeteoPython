class MeteoBean():

    def __init__(self, chipId, temperatura, humedad, hic, fechaGrabado):
        self.chipId = chipId
        self.temperatura = temperatura
        self.humedad = humedad
        self.hic = hic
        self.fechaGrabado = fechaGrabado

    def getChipId(self):
        return self.chipId
    def getTemperatura(self):
        return self.temperatura
    def getHumedad(self):
        return self.humedad
    def getHic(self):
        return self.hic
    def getFechaGrabado(self):
        return self.fechaGrabado