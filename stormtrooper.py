class Stormtrooper:

    def __init__(self, nombre, rango):
        self.nombre = nombre
        self.rango = rango
    
    def __str__(self):
        return "El stormtrooper {} se ha creado con exito" . format(self.nombre)
    
    def calificacion(self, codigo, cohoerte, siglo, escuadra, numero):
        self.codigo = codigo
        self.cohoerte = cohoerte
        self.siglo = siglo
        self.escuadra = escuadra
        self.numero = numero

soldado1 = ["GP", "4", "3", "9", "3"]
soldado2 = ["TK", "2", "2", "7", "1"]
soldado3 = ["JL", "3", "9", "4", "5"]

lista = [soldado1, soldado2, soldado3]

print(Stormtrooper.soldado1())