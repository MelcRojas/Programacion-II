package tarea;

import java.util.Scanner;

class AlgebraVectorial {
    public double x, y, z;

    public AlgebraVectorial() {
        this.x = 0;
        this.y = 0;
        this.z = 0;
    }

    public AlgebraVectorial(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    public AlgebraVectorial sumar(AlgebraVectorial v) {
        return new AlgebraVectorial(this.x + v.x, this.y + v.y, this.z + v.z);
    }

    public AlgebraVectorial restar(AlgebraVectorial v) {
        return new AlgebraVectorial(this.x - v.x, this.y - v.y, this.z - v.z);
    }

    public double norma() {
        return Math.sqrt(x * x + y * y + z * z);
    }

    public double productoEscalar(AlgebraVectorial v) {
        return (this.x * v.x) + (this.y * v.y) + (this.z * v.z);
    }

    public AlgebraVectorial productoVectorial(AlgebraVectorial v) {
        return new AlgebraVectorial(
            this.y * v.z - this.z * v.y,
            this.z * v.x - this.x * v.z,
            this.x * v.y - this.y * v.x
        );
    }

    public AlgebraVectorial proyeccionSobre(AlgebraVectorial v) {
        double normaV = v.norma();
        if (normaV == 0) {
            System.out.println("Error: No se puede proyectar sobre un vector nulo.");
            return new AlgebraVectorial(0, 0, 0);
        }
        double factor = this.productoEscalar(v) / (normaV * normaV);
        return new AlgebraVectorial(v.x * factor, v.y * factor, v.z * factor);
    }

    public double componenteEn(AlgebraVectorial v) {
        double normaV = v.norma();
        if (normaV == 0) {
            System.out.println("Error: No se puede calcular el componente sobre un vector nulo.");
            return 0;
        }
        return this.productoEscalar(v) / normaV;
    }

    public boolean esPerpendicular(AlgebraVectorial v) {
        return Math.abs(this.productoEscalar(v)) < 1e-9; // Mejor comparación 
    }

    public boolean esParalelo(AlgebraVectorial v) {
        AlgebraVectorial productoCruzado = this.productoVectorial(v);
        return Math.abs(productoCruzado.x) < 1e-9 && Math.abs(productoCruzado.y) < 1e-9 && Math.abs(productoCruzado.z) < 1e-9;
    }

    public void imprimir() {
        System.out.printf("(%.2f, %.2f, %.2f)%n", x, y, z);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Introduzca el vector a : ");
        double a1 = scanner.nextDouble();
        double b1 = scanner.nextDouble();
        double c1 = scanner.nextDouble();
        AlgebraVectorial vecA = new AlgebraVectorial(a1, b1, c1);

        System.out.println("Introduzca el vector b : ");
        double a2 = scanner.nextDouble();
        double b2 = scanner.nextDouble();
        double c2 = scanner.nextDouble();
        AlgebraVectorial vecB = new AlgebraVectorial(a2, b2, c2);

        AlgebraVectorial resultadoSuma = vecA.sumar(vecB);
        System.out.println("a + b:");
        resultadoSuma.imprimir();

        AlgebraVectorial resultadoResta = vecA.restar(vecB);
        System.out.println("a - b:");
        resultadoResta.imprimir();

        double productoPunto = vecA.productoEscalar(vecB);
        System.out.println("Producto escalar (a·b): " + productoPunto);

        System.out.println("¿Son perpendiculares?");
        if (vecA.esPerpendicular(vecB)) {
            System.out.println("Sí, a y b son ortogonales (perpendiculares)");
        } else {
            System.out.println("No, a y b no son ortogonales");
        }

        System.out.println("¿Son paralelos?");
        if (vecA.esParalelo(vecB)) {
            System.out.println("Sí, a y b son paralelos");
        } else {
            System.out.println("No, a y b no son paralelos");
        }

        System.out.println("Proyección de a sobre b:");
        AlgebraVectorial proyeccion = vecA.proyeccionSobre(vecB);
        proyeccion.imprimir();

        System.out.println("Componente de a en la dirección de b:");
        System.out.printf("%.2f%n", vecA.componenteEn(vecB));

        scanner.close();
    }
}

