class Deportista:
    #Inicializador y atributos.
    def __init__(self, deporte, añosPracticando):
        self._deporte = deporte
        self._añosPracticando = añosPracticando

    # Setters y getters
    def setDeporte(self, deporte):
        self._deporte = deporte

    def getDeporte(self):
        return self._deporte

    def setAñosPracticando(self, añosPracticando):
        self._añosPracticando = añosPracticando

    def getAñosPracticando(self):
        return self._añosPracticando