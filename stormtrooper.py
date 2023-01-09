class Stormtrooper:

    def __init__(self, nombre, rango):
        self.nombre = nombre
        self.rango = rango
    
    def __str__(self):
        return "El stormtrooper {} se ha creado con exito" . format(self.nombre)
    
class Calificacion(Stormtrooper):
    def __init__(self,nombre , rango, codigo, cohoerte, siglo, escuadra, numero):
        self.nombre = nombre
        self.rango = rango
        self.codigo = codigo
        self.cohoerte = cohoerte
        self.siglo = siglo
        self.escuadra = escuadra
        self.numero = numero
    
    def __str__(self):
        return "El solado {} de rango {}: {} - {}{}{}{}" . format(self.nombre, self.rango, self.codigo, self.cohoerte, self.siglo, self.escuadra, self.numero)

soldado1 = Calificacion("Thomas", "Sargento", "GP", "4", "3", "9", "3")
soldado2 = Calificacion("John", "Capitan", "CV", "4", "3", "9", "3")
soldado3 = Calificacion("Andrew", "Solado raso", "JK", "3", "9", "4", "5")

lista = [soldado1, soldado2, soldado3]

#print(Calificacion.lista())
print(soldado1)
print(soldado2)
print(soldado3)