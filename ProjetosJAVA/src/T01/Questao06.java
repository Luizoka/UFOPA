import java.util.Scanner;

public class Questao06 {
	public static void main(String[] args) {
	   	 Scanner sc = new Scanner(System.in);
	   	 
	   	 int count = 3;
	   	 System.out.println("Digite um número");
   		 int n = sc.nextInt();
   	     int valorMaximo = n;
	   	 
	   	 for(int i = 0; i<count - 1; i++) {
	   		 System.out.print("Digite um número");
	   		 n = sc.nextInt();
	   	     valorMaximo = Math.max(valorMaximo, n);
	   	 }
	   	 
	   	System.out.println(valorMaximo);
    }
}
