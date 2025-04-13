package Herencia;

public class D implements IA, IB {
    public int x;
    public int y;
    public int z;

    // Constructor
    public D(int x, int y, int z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    // Métodos de la interfaz IA
    public void incrementaXZ() {
        x++;
        z++;
    }

    // Métodos de la interfaz IB
    public void incrementaYZ() {
        y++;
        z++;
    }

    public void incrementaZ() {
        z++;
    }

    public void incrementaXYZ() {
        x++;
        y++;
        z++;
    }

    public void mostrarValores() {
        System.out.println("x: " + x);
        System.out.println("y: " + y);
        System.out.println("z: " + z);
    }

    // Método main dentro de la clase D
    public static void main(String[] args) {
        D objeto = new D(1, 2, 3);

        System.out.println("Valores iniciales:");
        objeto.mostrarValores();

        // Simula "cambiar x"
        objeto.x = 3;

        // Aplica incremento a todos
        objeto.incrementaXYZ();

        System.out.println("\nDespués de cambiar x y aplicar incrementaXYZ():");
        objeto.mostrarValores();
    }
}
