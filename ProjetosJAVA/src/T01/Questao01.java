
public class Questao01 {

	public static void main(String[] args) {
		int minutos = 100;
		int materias = 6;
		int result = minutos / materias;	
		int tempoLivre = minutos % materias;
		
		System.out.println("Seu tempo de estudo (em minutos) será: " + result);	
		System.out.println("Seu tempo livre (em minutos) será: " + tempoLivre);
		
	}
}
