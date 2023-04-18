
public class Questao10 {
	public static void main(String[] args) {
		int x = 0, d = 0, soma = 0;
		
		// Minha versão
		for(int i = 1; i <= 1000; i++) {
			if (i % 2 != 0) {
				if (i % 3 == 0) {
					x += i;
				}
			}	
		}	
		
		// Versão do professor 1.0
		for(int c = 1; c <= 1000; c++) {
			if (c % 3 == 0 && c % 2 != 0) {
				d += c;
			}
		}
		
		// Versão do professor 2.0
		for(int e = 3; e < 1000; e += 6) {
			soma += e;
		}
		
	System.out.printf("A soma deu %d e %d e %d", x, d, soma);
	}
}
