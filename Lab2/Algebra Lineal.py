import math

class AlgebraVectorial:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def sumar(self, v):
        return AlgebraVectorial(self.x + v.x, self.y + v.y, self.z + v.z)

    def restar(self, v):
        return AlgebraVectorial(self.x - v.x, self.y - v.y, self.z - v.z)

    def norma(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def producto_escalar(self, v):
        return self.x * v.x + self.y * v.y + self.z * v.z

    def producto_vectorial(self, v):
        return AlgebraVectorial(
            self.y * v.z - self.z * v.y,
            self.z * v.x - self.x * v.z,
            self.x * v.y - self.y * v.x
        )

    def proyeccion_sobre(self, v):
        norma_v = v.norma()
        if norma_v == 0:
            print("Error: No se puede proyectar sobre un vector nulo.")
            return AlgebraVectorial(0, 0, 0)
        factor = self.producto_escalar(v) / (norma_v ** 2)
        return AlgebraVectorial(v.x * factor, v.y * factor, v.z * factor)

    def componente_en(self, v):
        norma_v = v.norma()
        if norma_v == 0:
            print("Error: No se puede calcular el componente sobre un vector nulo.")
            return 0
        return self.producto_escalar(v) / norma_v

    def es_perpendicular(self, v):
        return abs(self.producto_escalar(v)) < 1e-9

    def es_paralelo(self, v):
        producto_cruzado = self.producto_vectorial(v)
        return abs(producto_cruzado.x) < 1e-9 and abs(producto_cruzado.y) < 1e-9 and abs(producto_cruzado.z) < 1e-9

    def imprimir(self):
        print(f"({self.x:.2f}, {self.y:.2f}, {self.z:.2f})")

if __name__ == "__main__":
    a1, b1, c1 = map(float, input("Introduzca el vector a (x y z): ").split())
    vecA = AlgebraVectorial(a1, b1, c1)
    
    a2, b2, c2 = map(float, input("Introduzca el vector b (x y z): ").split())
    vecB = AlgebraVectorial(a2, b2, c2)
    
    print("a + b:")
    vecA.sumar(vecB).imprimir()
    
    print("a - b:")
    vecA.restar(vecB).imprimir()
    
    print(f"Producto escalar (a·b): {vecA.producto_escalar(vecB):.2f}")
    
    print("¿Son perpendiculares?")
    print("Sí" if vecA.es_perpendicular(vecB) else "No")
    
    print("¿Son paralelos?")
    print("Sí" if vecA.es_paralelo(vecB) else "No")
    
    print("Proyección de a sobre b:")
    vecA.proyeccion_sobre(vecB).imprimir()
    
    print("Componente de a en la dirección de b:")
    print(f"{vecA.componente_en(vecB):.2f}")

