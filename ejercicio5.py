class Mochila:
    
    def __init__(self, peso, valor, indice):
        self.peso = peso
        self.valor = valor
        self.indice = indice
        self.coef = valor // peso
    
    def valormax(self, peso, valores, capacidad):
        arraySort = []
        for i in range (len(peso)):
            arraySort.append(Mochila (peso [i], valores[i], i))

        arraySort.sort(reverse=True)

        counterValue = 0 

        for objeto in arraySort:
            pesoActual = int(objeto.peso)
            precioActual = int(objeto.precio)
            if capacidad - pesoActual >= 0:
                capacidad -= pesoActual
                counterValue += precioActual
        return counterValue