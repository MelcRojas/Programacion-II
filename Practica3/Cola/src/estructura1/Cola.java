package estructura1;

public class Cola {
    private long[] arreglo;
    private int inicio;
    private int fin;
    private int n;

    public Cola(int n) {
        this.n = n;
        arreglo = new long[n];
        inicio = 0;
        fin = -1;
    }

    public void insert(long e) {
        if (!isFull()) {
            arreglo[++fin] = e;
        } else {
            System.out.println("Cola llena");
        }
    }

    public long remove() {
        if (!isEmpty()) {
            return arreglo[inicio++];
        }
        System.out.println("Cola vacía");
        return -1;
    }

    public long peek() {
        if (!isEmpty()) {
            return arreglo[inicio];
        }
        System.out.println("Cola vacía");
        return -1;
    }

    public boolean isEmpty() {
        return inicio > fin;
    }

    public boolean isFull() {
        return fin == n - 1;
    }

    public int size() {
        return fin - inicio + 1;
    }

    public static void main(String[] args) {
        Cola cola = new Cola(3);
        
        cola.insert(10);
        cola.insert(20);
        cola.insert(30);

        System.out.println("Frente de la cola: " + cola.peek());
        System.out.println("Tamaño de la cola: " + cola.size());

        System.out.println("Eliminando: " + cola.remove());
        System.out.println("Nuevo frente de la cola: " + cola.peek());
        System.out.println("Tamaño de la cola: " + cola.size());
    }
}

