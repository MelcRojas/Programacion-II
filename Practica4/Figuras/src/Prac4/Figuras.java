package Prac4;

public class Figuras {

    // Sobrecarga para el área del círculo
    public static double calcularArea(double radio) {
        return Math.PI * radio * radio;
    }

    // Sobrecarga para el área del rectángulo
    public static double calcularArea(double base, double altura) {
        return base * altura;
    }

    // Sobrecarga para el área del triángulo
    public static double calcularArea(double base, double altura, String tipo) {
        if (tipo.equalsIgnoreCase("triangulo")) {
            return (base * altura) / 2;
        }
        return -1;
    }

    // Sobrecarga para el área del trapecio
    public static double calcularArea(double baseMayor, double baseMenor, double altura, String tipo) {
        if (tipo.equalsIgnoreCase("trapecio")) {
            return ((baseMayor + baseMenor) * altura) / 2;
        }
        return -1; 
    }

    // Sobrecarga para el área del pentágono
    public static double calcularArea(double lado, double apotema, int lados) {
        if (lados == 5) {
            return (5 * lado * apotema) / 2;
        }
        return -1; 
    }

    public static void main(String[] args) {
        System.out.println("Área del círculo: " + calcularArea(5));  // Círculo
        System.out.println("Área del rectángulo: " + calcularArea(4, 6));  // Rectángulo
        System.out.println("Área del triángulo: " + calcularArea(4, 6, "triangulo"));  // Triángulo
        System.out.println("Área del trapecio: " + calcularArea(8, 4, 5, "trapecio"));  // Trapecio
        System.out.println("Área del pentágono: " + calcularArea(6, 4, 5));  // Pentágono
    }
}
