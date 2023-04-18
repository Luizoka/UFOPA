import java.util.Scanner;

public class Questao08 {
	public static void main(String[] args) {
		Double x;
		Scanner sc = new Scanner(System.in);
		System.out.print("Digite a quanto vc recebe: ");
		double n = sc.nextDouble();
		
		if (n <= 1200) {
			System.out.printf("Você é isento! Parabéns");
		}else if (n <= 2500) {
			x = n * 0.1;
			System.out.printf("Seu imposto é R$ %.2f, seu total é %.2f", x, x + n );
		}else if (n <= 5000) {
			x = n * 0.15;
			System.out.printf("Seu imposto é R$ %.2f, seu total é %.2f", x, x + n);
		}else {
			x = n * 0.2;
			System.out.printf("Seu imposto é R$ %.2f, seu total é %.2f", x, x + n);
		}
	}
}
