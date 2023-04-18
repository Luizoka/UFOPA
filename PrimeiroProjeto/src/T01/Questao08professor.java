import java.util.Scanner;

public class Questao08professor {
	public static void main(String[] args) {
		double taxa;
		Scanner sc = new Scanner(System.in);
		System.out.println("Digite o valor: ");
		double valor = sc.nextDouble();
		
		if(valor <= 1200) {
			taxa = 0;
		} else if (valor <= 2500) {
			taxa = 0.1;
		} else if (valor <= 5000) {
			taxa = 0.15;
		} else {
			taxa = 0.2;
		}
		
		double imposto = valor * taxa;
		System.out.printf("Imposto a ser pago:R$ %.2f", imposto);
		
	}
}