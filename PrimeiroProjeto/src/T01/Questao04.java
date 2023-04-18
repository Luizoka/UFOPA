import java.util.*;
public class Questao04 {
     public static void main(String[] args) {
    	 Scanner sc = new Scanner(System.in);
    	 
    	 System.out.print("Digite o primeiro número: ");
    	 int a = sc.nextInt();
    	 System.out.print("Digite o segundo número: ");
    	 int b = sc.nextInt();
    	 
    	 if(a == b) {
    		 System.out.println("São iguais");
    	 }else{
    		 if(a > b) {
    			 System.out.printf("O número %d é maior", a);
    		 }else{
    			 System.out.printf("O número %d é maior", b);
    		 }
    	 } 
     }
}
