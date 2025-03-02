package estructura;

public class Pila {
    private long[] arreglo;
    private int top;
    private int n;

    public Pila(int n) {
        this.n = n;
        this.arreglo = new long[n];
        this.top = -1;
    }

    public void push(long e) {
        if (isFull()) {
            System.out.println("Pila llena");
            return;
        }
        arreglo[++top] = e;
    }

    public long pop() {
        if (isEmpty()) {
            System.out.println("Pila vacía");
            return -1;
        }
        return arreglo[top--];
    }

    public long peek() {
        if (isEmpty()) {
            System.out.println("Pila vacía");
            return -1;
        }
        return arreglo[top];
    }

    public boolean isEmpty() {
        return top == -1;
    }

    public boolean isFull() {
        return top == n - 1;
    }

    public static void main(String[] args) {
        Pila pila = new Pila(6);

        System.out.println("Elemento eliminado: " + pila.pop());
        System.out.println("Elemento en la cima: " + pila.peek());
    }
}

