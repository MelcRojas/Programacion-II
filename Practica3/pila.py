class Pila:
    def __init__(self, n: int):
        self.arreglo: list[int] = [0] * n
        self.top: int = -1
        self.n: int = n

    def push(self, e: int):
        if self.isFull():
            print("Pila llena!")
        else:
            self.top += 1
            self.arreglo[self.top] = e

    def pop(self) -> int:
        if self.isEmpty():
            print("Pila vacía")
            return -1
        elemento: int = self.arreglo[self.top]
        self.top -= 1
        return elemento

    def peek(self) -> int:
        if self.isEmpty():
            print("Pila vacía")
            return -1
        return self.arreglo[self.top]

    def isEmpty(self) -> bool:
        return self.top == -1

    def isFull(self) -> bool:
        return self.top == self.n - 1

if __name__ == "__main__":
    pila = Pila(3)
    pila.push(10)
    pila.push(20)
    pila.push(30) 
    print(f"Elemento eliminado: {pila.pop()}")
    print(f"Elemento en la cima: {pila.peek()}")
