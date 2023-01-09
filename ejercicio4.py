class ArtefactosValiosos:
    
    def __init__(self, peso, nombre, precio, caducidad):
        self.peso = peso
        self.nombre = nombre
        self.precio = precio
        self.caducidad = caducidad
    
    def __str__(self):
        print("La conserva se ha creado con exito")
        return "El artefacto {}, tiene un peso de {} kg, un precio de {} euros, y su fecha de caducidad es el {}" .format(self.nombre, self.peso, self.precio, self.caducidad)

artefacto1 = ArtefactosValiosos("3", "reloj", "300", "12-09-2030")
artefacto2 = ArtefactosValiosos("70", "mueble", "550", "22-03-2028")
artefacto3 = ArtefactosValiosos("100", "espejo", "180", "01-04-2040")

print(artefacto1)
print(artefacto2)
print(artefacto3)
