class Futbolista:
    #Atributo de clase.
    listaFutbolistas = None

    #Inicializador y atributos.
    def __init__(self, golesMarcados, tarjetasRojas, piernaHabil):
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        #Init de los padres

    def setGolesMarcados(self, golesMarcados):
        self._golesMarcados = golesMarcados

    def getGolesMarcados(self):
        return self._golesMarcados

    def setTarjetasRojas(self, tarjetasRojas):
        self._tarjetasRojas = tarjetasRojas

    def getTarjetasRojas(self):
        return self._tarjetasRojas

    def setPiernaHabil(self, piernaHabil):
        self._piernaHabil = piernaHabil

    def getPiernaHabil(self):
        return self._piernaHabil