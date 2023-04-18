import java.io.*;
import java.util.Scanner;

public class Questao02 {
	public static void main(String[] args) {
		File in = new File("entrada.txt");
		File fout = new File("saida.txt");
		try {
			Scanner sc = new Scanner(in);

			// Entrada
			System.out.print("Digite a tempratura em Fahrenheit: ");
			double fahrenheit = sc.nextDouble();

			// Processamento
			double celson = 5.0 / 9 * (fahrenheit - 32);

			// Saida
			PrintStream out = new PrintStream(fout);
			//System.out.printf("\nSua temperatura era %.1f°F", fahrenheit);
			//System.out.printf("\nSua temperatura é %.1f°C", celson);
		} catch (Exception e) {
			// TODO: handle exception
		}
	}
}
