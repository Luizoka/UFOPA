import java.util.*;

public class Questao11 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int z = 0, count = 0;
		
		System.out.print("Digite um numero de incio: ");
		int x = sc.nextInt();
		System.out.print("Digite um numero para o final: ");
		int y = sc.nextInt();
		
		// Minha versão 
		for(int i = x; i <= y; i++) {   
			System.out.printf("%d", i);
			z++; 
			if (z % 3 == 0 ) {
				System.out.println();
				} else {
					System.out.print("-");
				}
			}
		
		/* Versão do professor
		for (int c = x; c<= y; c++) {
			if (count % 3 != 0) System.out.print("-");
			count++;
			System.out.print("%d", c);
			if (count % 5 == 0){
				System.out.println();
			}
		} */
		
	}
}
