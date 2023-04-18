import java.util.*;
public class Questao03 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Quantas séries ?");
		int n  = sc.nextInt();
		int soma = 0;
		for (int i = 1; i <=5; i++) {
		  soma += i; // Mesma coisa que soma = soma + i;
		}
		System.out.print(soma);
	}

}
