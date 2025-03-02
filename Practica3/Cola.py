class Cola:
    def __init__(self, n):
        self.n = n
        self.arreglo = [-1] * n  
        self.inicio = 0
        self.fin = -1

    def insert(self, e):
        if not self.isFull():
            self.fin += 1
            self.arreglo[self.fin] = e
        else:
            print("Cola llena!")

    def remove(self):
        if not self.isEmpty():
            valor = self.arreglo[self.inicio]
            self.inicio += 1
            return valor
        return -1  

    def peek(self):
        if not self.isEmpty():
            return self.arreglo[self.inicio]
        return -1  

    def isEmpty(self):
        return self.inicio > self.fin

    def isFull(self):
        return self.fin == self.n - 1

    def size(self):
        return self.fin - self.inicio + 1

if __name__ == "__main__":
    cola = Cola(3)
    
    cola.insert(10)
    cola.insert(20)
    cola.insert(30)
    cola.insert(40)

    print("Frente de la cola:", cola.peek())
    print("Tamaño de la cola:", cola.size())
