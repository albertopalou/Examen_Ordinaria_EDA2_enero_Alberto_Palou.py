class Stormtrooper:

    def __init__(self, nombre, rango):
        self.nombre = nombre
        self.rango = rango
    
    def __str__(self):
        return "El stormtrooper {} se ha creado con exito" . format(self.nombre)