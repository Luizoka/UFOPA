import java.util.Scanner;

public class Questao05 {
	public static void main(String[] args) {
   	 Scanner sc = new Scanner(System.in);
   	 
   	 System.out.print("Digite o primeiro número: ");
   	 int a = sc.nextInt();
   	 System.out.print("Digite o segundo número: ");
   	 int b = sc.nextInt();
   	System.out.print("Digite o segundo número: ");
  	 int c = sc.nextInt();
  	 
   	if(a >= b && a >= c) {
   		System.out.printf("O %d é maior", a);
   	}else if(b >= a && b >= c) {
   			System.out.printf("O %d é maior", b);
   		}else {
   			System.out.printf("O %d é maior", c);
   		}
   	}
}

