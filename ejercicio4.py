class ArtefactosValiosos:
    
    def __init__(self, peso, nombre, precio, caducidad):
        self.peso = peso
        self.nombre = nombre
        self.precio = precio
        self.caducidad = caducidad
    
    def __str__(self):
        print("La conserva se ha creado con exito")
        return "El objeto {}, tiene un peso de {} kg, un precio de {} euros, y su fecha de caducidad es el {}" .format(self.nombre, self.peso, self.precio, self.caducidad)

artefacto1 = ArtefactosValiosos("")