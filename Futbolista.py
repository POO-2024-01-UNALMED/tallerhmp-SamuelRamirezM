import Persona
import Deportista

class Futbolista(Persona, Deportista):
    #Atributo de clase.
    listaFutbolistas = None

    #Inicializador y atributos.
    def __init__(self, golesMarcados, tarjetasRojas, piernaHabil):
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Persona.__init__()

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

    def __str__(self):
        return "Mi nombre es " + super().getNombre() + " soy profesional en el deporte " + super().getDeporte() + "Tengo " + super().getEdad() + " años de edad y llevo " + super().getAñosPracticando + "años en el deporte"