class Mochila:

    def __init__(self):
        self.items = ["Sable", "Capa", "Anillo"]
    
    def desapilar(self):
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("La mochila esta vacía")
    
    def es_vacia(self):
        return self.items == []

p = Mochila()
print(p.desapilar())
print(p.desapilar())
print(p.desapilar())
