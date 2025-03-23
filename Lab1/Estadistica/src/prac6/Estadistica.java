package prac6;

import java.util.Scanner;

public class Estadistica {
    public static double promedio(double[] numeros) {
        double suma = 0;
        for (double num : numeros) {
            suma += num;
        }
        return suma / numeros.length;
    }

    public static double desviacion(double[] numeros) {
        double prom = promedio(numeros);
        double sumaDiferencias = 0;
        for (double num : numeros) {
            sumaDiferencias += Math.pow(num - prom, 2);
        }
        return Math.sqrt(sumaDiferencias / (numeros.length - 1));
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        double[] numeros = new double[10];
        System.out.println("");
        for (int i = 0; i < 10; i++) {
            numeros[i] = scanner.nextDouble();
        }

        double prom = promedio(numeros);
        double desv = desviacion(numeros);
        
        System.out.printf("El promedio es %.2f\n", prom);
        System.out.printf("La desviación estándar es %.6f\n", desv);

        scanner.close();
    }
}