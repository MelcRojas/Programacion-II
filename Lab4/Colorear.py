from abc import ABC, abstractmethod
import random
import math
# a) 
class Coloreado(ABC):
    @abstractmethod
    def comoColorear(self) -> str:
        pass
# b) 
class Figura(ABC):
    def __init__(self, color="sin color"):
        self.color = color

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def __str__(self):
        return f"Color: {self.color}"

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass
# c) 
class Cuadrado(Figura, Coloreado):
    def __init__(self, lado, color="sin color"):
        super().__init__(color)
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def perimetro(self):
        return 4 * self.lado

    def comoColorear(self):
        return "Colorear los cuatro lados"

# d) 
class Circulo(Figura):
    def __init__(self, radio, color="sin color"):
        super().__init__(color)
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio
# f-g)
figuras = []

tipo = random.randint(1, 2)  
for _ in range(5):
    color = random.choice(["rojo", "azul", "verde", "amarillo"])
    if tipo == 1:
        lado = random.randint(1, 10)
        figura = Cuadrado(lado, color)
    else:
        radio = random.randint(1, 10)
        figura = Circulo(radio, color)
    figuras.append(figura)

for figura in figuras:
    print(f"Figura: {type(figura).__name__}")
    print(f"Color: {figura.getColor()}")
    print(f"Área: {figura.area():.2f}")
    print(f"Perímetro: {figura.perimetro():.2f}")
    if isinstance(figura, Coloreado):
        print(f"Como colorear: {figura.comoColorear()}")
    print("-" * 30)
