package vector;

import java.util.Scanner;

public class Tridimensional {
    public double x, y, z;
    public Tridimensional() {
        this.x = 0;
        this.y = 0;
        this.z = 0;
    }

    public Tridimensional(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    // a) Suma de vectores
    public Tridimensional sumar(Tridimensional v) {
        return new Tridimensional(this.x + v.x, this.y + v.y, this.z + v.z);
    }

    // b) Multiplicación por un escalar
    public Tridimensional multiplicarPorEscalar(double escalar) {
        return new Tridimensional(this.x * escalar, this.y * escalar, this.z * escalar);
    }

    // c) Longitud del vector
    public double longitud() {
        return Math.sqrt(x * x + y * y + z * z);
    }

    // d) Normalización del vector
    public Tridimensional normalizar() {
        double longitud = longitud();
        if (longitud == 0) {
            throw new ArithmeticException("No se puede normalizar un vector de longitud cero");
        }
        return new Tridimensional(this.x / longitud, this.y / longitud, this.z / longitud);
    }

    // e) Producto escalar
    public double productoEscalar(Tridimensional v) {
        return (this.x * v.x) + (this.y * v.y) + (this.z * v.z);
    }

    // f) Producto vectorial
    public Tridimensional productoVectorial(Tridimensional v) {
        return new Tridimensional(
            this.y * v.z - this.z * v.y,
            this.z * v.x - this.x * v.z,
            this.x * v.y - this.y * v.x
        );
    }

    public void imprimir() {
        System.out.printf("(%.2f, %.2f, %.2f)%n", x, y, z);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Introduzca el vector a (x, y, z):");
        Tridimensional vecA = new Tridimensional(scanner.nextDouble(), scanner.nextDouble(), scanner.nextDouble());

        System.out.println("Introduzca el vector b (x, y, z):");
        Tridimensional vecB = new Tridimensional(scanner.nextDouble(), scanner.nextDouble(), scanner.nextDouble());

        System.out.print("Ingrese el escalar r: ");
        double r = scanner.nextDouble();

        System.out.println("Suma (a + b):");
        vecA.sumar(vecB).imprimir();

        System.out.println("Multiplicación de a por escalar r:");
        vecA.multiplicarPorEscalar(r).imprimir();

        System.out.println("Longitud de a:");
        System.out.printf("%.2f%n", vecA.longitud());

        System.out.println("Vector normalizado de a:");
        try {
            vecA.normalizar().imprimir();
        } catch (ArithmeticException e) {
            System.out.println(e.getMessage());
        }

        System.out.println("Producto escalar (a · b): " + vecA.productoEscalar(vecB));

        System.out.println("Producto vectorial (a × b):");
        vecA.productoVectorial(vecB).imprimir();

        scanner.close();
    }
}