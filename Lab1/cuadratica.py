import math

class Cuadratica:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def getDiscriminante(self):
        return self.__b ** 2 - 4 * self.__a * self.__c

    def getRaiz1(self):
        d = self.getDiscriminante()
        if d < 0:
            return None
        return (-self.__b + math.sqrt(d)) / (2 * self.__a)

    def getRaiz2(self):
        d = self.getDiscriminante()
        if d < 0:
            return None
        return (-self.__b - math.sqrt(d)) / (2 * self.__a)

    def resolver(self):
        d = self.getDiscriminante()
        if d > 0:
            print(f"La ecuación tiene dos raíces {self.getRaiz1():.6f} y {self.getRaiz2():.6f}")
        elif d == 0:
            print(f"La ecuación tiene una raíz {self.getRaiz1():.0f}")
        else:
            print("La ecuación no tiene raíces reales")

if __name__ == "__main__":  
    a, b, c = map(float, input("Ingrese a, b, c: ").split())
    ecuacion = Cuadratica(a, b, c)
    ecuacion.resolver()
