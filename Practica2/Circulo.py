import turtle

class Punto:
    def __init__(self, x, y): self.x, self.y = x, y
    def __str__(self): return f"({self.x}, {self.y})"

class Circulo:
    def __init__(self, centro, radio): self.centro, self.radio = centro, radio
    def __str__(self): return f"Círculo con centro en {self.centro} y radio {self.radio}"
    
    def dibujaCirculo(self):
        t = turtle.Turtle()
        t.speed(10)
        t.penup()
        t.goto(self.centro.x, self.centro.y - self.radio)  
        t.pendown()
        t.circle(self.radio)
        turtle.done()

p, c = Punto(0, 0), Circulo(Punto(0, 0), 100)
print(c)
c.dibujaCirculo()
