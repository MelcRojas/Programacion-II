class A:
    def __init__(self, x, z):
        self.x = x
        self.z = z

    def incrementaXZ(self):
        self.x += 1
        self.z += 1

    def incrementaZ(self):
        self.z += 1


class B:
    def __init__(self, y, z):
        self.y = y
        self.z = z

    def incrementaYZ(self):
        self.y += 1
        self.z += 1

    def incrementaZ(self):
        self.z += 1


class D(A, B):
    def __init__(self, x, y, z):
        A.__init__(self, x, z)
        B.__init__(self, y, z)

    def incrementaXYZ(self):
        self.x += 1
        self.y += 1
        self.z += 1


if __name__ == "__main__":
    # Crear objeto de la clase D con los mismos datos que en Java
    obj = D(1, 2, 3)  # Valores iniciales x=1, y=2, z=3

    # Mostrar valores iniciales
    print("Valores iniciales:")
    print("x:", obj.x)  # x = 1
    print("y:", obj.y)  # y = 2
    print("z:", obj.z)  # z = 3

    # Cambiar el valor de x directamente
    obj.x = 3  # Cambiar x a 3, como lo quieres

    # Llamar a incrementaXYZ
    obj.incrementaXYZ()

    # Mostrar valores después del cambio
    print("\nDespués de cambiar x y aplicar incrementaXYZ():")
    print("x:", obj.x)  # x = 3
    print("y:", obj.y)  # y = 3 + 1 = 4
    print("z:", obj.z)  # z = 3 + 1 + 3 = 7
