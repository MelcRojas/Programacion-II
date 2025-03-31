import math

class Tridimensional:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def sumar(self, v):
        return Tridimensional(self.x + v.x, self.y + v.y, self.z + v.z)

    def multiplicar_por_escalar(self, escalar):
        return Tridimensional(self.x * escalar, self.y * escalar, self.z * escalar)

    def longitud(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def normalizar(self):
        longitud = self.longitud()
        if longitud == 0:
            raise ArithmeticError("No se puede normalizar un vector de longitud cero.")
        return Tridimensional(self.x / longitud, self.y / longitud, self.z / longitud)

    def producto_escalar(self, v):
        return (self.x * v.x) + (self.y * v.y) + (self.z * v.z)

    def producto_vectorial(self, v):
        return Tridimensional(
            self.y * v.z - self.z * v.y,
            self.z * v.x - self.x * v.z,
            self.x * v.y - self.y * v.x
        )

    def imprimir(self):
        print(f"({self.x:.2f}, {self.y:.2f}, {self.z:.2f})")


def main():
    x1, y1, z1 = map(float, input("Introduzca el vector a (x, y, z): ").split())
    vec_a = Tridimensional(x1, y1, z1)
    
    x2, y2, z2 = map(float, input("Introduzca el vector b (x, y, z): ").split())
    vec_b = Tridimensional(x2, y2, z2)
    
    r = float(input("Ingrese el escalar r: "))
    
    print("Suma (a + b):")
    vec_a.sumar(vec_b).imprimir()
    
    print("Multiplicación de a por escalar r:")
    vec_a.multiplicar_por_escalar(r).imprimir()
    
    print("Longitud de a:")
    print(f"{vec_a.longitud():.2f}")
    
    print("Vector normalizado de a:")
    try:
        vec_a.normalizar().imprimir()
    except ArithmeticError as e:
        print(e)
    
    print("Producto escalar (a · b):", vec_a.producto_escalar(vec_b))
    
    print("Producto vectorial (a × b):")
    vec_a.producto_vectorial(vec_b).imprimir()


if __name__ == "__main__":
    main()

