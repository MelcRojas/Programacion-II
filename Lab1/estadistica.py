import math

class Estadistica:
    def __init__(self, datos):
        self.__datos = datos

    def promedio(self):
        return sum(self.__datos) / len(self.__datos)

    def desviacion(self):
        prom = self.promedio()
        suma = sum((x - prom) ** 2 for x in self.__datos)
        return math.sqrt(suma / (len(self.__datos) - 1))

    def mostrar_resultados(self):
        print(f"El promedio es {self.promedio():.2f}")
        print(f"La desviación estándar es {self.desviacion():.5f}")

if __name__ == "__main__":
    numeros = list(map(float, input().split()))
    est = Estadistica(numeros)
    est.mostrar_resultados()
