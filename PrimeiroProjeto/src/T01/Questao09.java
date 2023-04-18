import java.util.Scanner;

public class Questao09 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.print("Digite um ano: ");
		int ano = sc.nextInt();

	if (ano % 100 == 0) {
		if(ano % 400 == 0) {
			System.out.println("Seu ano é bissexto");
		} else {
			System.out.println("Seu ano não é bissexto");
		}
	} else if(ano % 4 == 0 ) {
			System.out.println("Seu ano é bissexto");
	} else {
		System.out.println("Seu ano não é bissexto");
		}
	}
}