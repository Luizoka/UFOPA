import java.util.Scanner;
public class Questao07 {
	public static void main(String[] args) {
	  Scanner sc = new Scanner(System.in);
	  System.out.print("Digite um número: ");
	  
	  int n = sc.nextInt();
	  int valorMaximo = 0;
	  
	  do{
		  System.out.print("Digite um número: ");
		  n = sc.nextInt();
		  if (n != 0 && valorMaximo== 0) {
			  valorMaximo = n;
		  }else {
			  valorMaximo = Math.max(valorMaximo, n);
		  }
	  } while (n != 0);
		
	  if(valorMaximo == 0) {
		  System.out.print("Você não digitou nenhum valor válido");
	  }else {
		   System.out.printf("Este é o valor Máximo: %d", valorMaximo);
	  }
	}
}
 
