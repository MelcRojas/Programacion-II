import turtle

class Punto:
    def __init__(self, x, y):  
        self.x = x
        self.y = y

class Linea:
    def __init__(self, p1, p2): 
        self.p1 = p1
        self.p2 = p2

    def __str__(self):  
        return f"Línea desde ({self.p1.x}, {self.p1.y}) hasta ({self.p2.x}, {self.p2.y})"

    def dibujaLinea(self):
        t = turtle.Turtle()
        t.speed(3)
        t.penup()
        t.goto(self.p1.x, self.p1.y)
        t.pendown()
        t.goto(self.p2.x, self.p2.y)
        turtle.done()

p1 = Punto(0, -100)   
p2 = Punto(0, 100)
linea = Linea(p1, p2)
print(linea)
linea.dibujaLinea()
