class Mochila:
    
    def __init__(self, peso, precios, indice):
        self.peso = peso
        self.precios = precios
        self.indice = indice
        self.coef = precios // peso
    
    def pesomax(self, peso, precios, capacidad):
        arraySort = []
        for i in range (len(peso)):
            arraySort.append(Mochila (peso [i], precios[i], i))

        arraySort.sort(reverse=True)

        counterValue = 0 

        for objeto in arraySort:
            pesoActual = int(objeto.peso)
            precioActual = int(objeto.precio)
            if capacidad - pesoActual >= 0:
                capacidad -= pesoActual
                counterValue += precioActual
        return counterValue

precio = [103, 60, 70, 5, 15]
peso = [12, 23, 11, 15, 7]