class Persona:
    #Inicializador y atributos
    def __int__(self, nombre, edad, altura, sexo):
        self._nombre = nombre
        self._edad = edad
        self._altura = altura
        self._sexo = sexo

    #Setters y getters
    def setNombre(self, nombre):
        self._nombre = nombre

    def getNombre(self):
        return self._nombre

    def setEdad(self, edad):
        self._edad = edad

    def getEdad(self):
        return self._edad

    def setAltura(self, altura):
        self._altura = altura

    def getAltura(self):
        return self._altura

    def setSexo(self, sexo):
        self._sexo

    def getSexo(self):
        return self._sexo

class Deportista:
    #Inicializador y atributos.
    def __init__(self, deporte, añosPracticando):
        self._deporte = deporte
        self._añosPracticando = añosPracticando

    def setDeporte(self, deporte):
        self._deporte = deporte

    def getDeporte(self):
        return self._deporte

    def setAñosPracticando(self, añosPracticando):
        self._añosPracticando = añosPracticando

    def getAñosPracticando(self):
        return self._añosPracticando

class Futbolista(Persona, Deportista):
    #Atributo de clase.
    listaFutbolistas = None

    #Inicializador y atributos.
    def __init__(self, nombre, edad, altura, sexo, deporte, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, deporte, añosPracticando)

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