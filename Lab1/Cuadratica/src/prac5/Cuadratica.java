package prac5;

import java.util.Scanner;

public class Cuadratica {

	public static double getDiscriminante(double a, double b, double c) {
		return b * b - 4 * a * c;
	}

	public static Double getRaiz1(double a, double b, double discriminante) {
		if (discriminante < 0)
			return null;
		return (-b + Math.sqrt(discriminante)) / (2 * a);
	}

	public static Double getRaiz2(double a, double b, double discriminante) {
		if (discriminante < 0)
			return null;
		return (-b - Math.sqrt(discriminante)) / (2 * a);
	}

	public static void resolverEcuacion(double a, double b, double c) {
		double discriminante = getDiscriminante(a, b, c);

		if (discriminante > 0) {
			System.out.printf("La ecuación tiene dos raíces %.6f y %.6f%n", getRaiz1(a, b, discriminante),
					getRaiz2(a, b, discriminante));
		} else if (discriminante == 0) {
			System.out.printf("La ecuación tiene una raíz %.0f%n", getRaiz1(a, b, discriminante));
		} else {
			System.out.println("La ecuación no tiene raíces reales");
		}
	}

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

		System.out.print("Ingrese a, b, c: ");
		double a = scanner.nextDouble();
		double b = scanner.nextDouble();
		double c = scanner.nextDouble();

		resolverEcuacion(a, b, c);
		scanner.close();
	}
}