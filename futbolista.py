from persona import Persona
from deportista import Deportista


class Futbolista (Persona, Deportista):
    listaFutbolistas = []
    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        Persona.__init__(self, nombre, edad, altura, sexo)
        Deportista.__init__(self, "Futbol",añosPracticando)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista.listaFutbolistas.append(self)

    #setters and getters for the attributes
    def getGolesMarcados(self):
        return self._golesMarcados
    
    def getTarjetasRojas(self):
        return self._tarjetasRojas
    
    def getPiernaHabil(self):
        return self._piernaHabil

    def setGolesMarcados(self, golesMarcados):
        self._golesMarcados = golesMarcados

    def setTarjetasRojas(self, tarjetasRojas):
        self._tarjetasRojas = tarjetasRojas

    def setPiernaHabil(self, piernaHabil):
        self._piernaHabil = piernaHabil

# “Mi nombre es #Persona.nombre soy profesional en el deporte
# #Deportista.deporte Tengo #Persona.edad años de edad y llevo
# #Deportista.añosParticipando años en el deporte”
    def __str__(self):
        return "Mi nombre es " + self._nombre + " soy profesional en el deporte " + self._deporte + " Tengo " + str(self._edad) + " años de edad y llevo " + str(self._añosPracticando) + " años en el deporte"


# if __name__ == "__main__":
#     def testFutbolista():
#         futbolista = Futbolista("Juan Pablo", 30, "1,80", "M", 12, 400, 1, "Derecha")
#         ok = 1
#         if (futbolista.getNombre() == "Juan Pablo" and futbolista.getEdad() == 30 and futbolista.getAltura()=="1,80" and futbolista.getSexo() == "M" and 
#             futbolista.getAñosPracticando() == 12 and futbolista.getGolesMarcados()==400 and futbolista.getTarjetasRojas() == 1 and futbolista.getPiernaHabil() == "Derecha"):
#             ok = 0
#         return ok
# print(testFutbolista())
    