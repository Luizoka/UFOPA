package T02;

import java.util.*;

public class Main {
	public static void main(String[] args) {
		/*
		char c = 'a';                              // transformando char em int
		int i = c;
		System.out.println(c);
		System.out.println(i);
		
		
		int a = 67;                                // forçando int para char
		char b = (char) a;
		System.out.println(a);
		System.out.println(b);
		
		
		String aa = "/uD83E";                      // usando unicode (deu errado :/)
		int bb = (int) aa;
		System.out.println(bb); 
		
		
		ArrayList<Integer> l = new ArrayList<>(); // array de num int 
		l.add(5);                                 // incrementando no array
		System.out.println(l.get(0) + 2);         // adicioando 2 casas na tabela  
		
		
		String r = "UFOPA";                       // comparando strings
		String s = "UFOPA";
		System.out.println(r == s);               // true (se fosse com Scanner daria "false")
		System.out.println(r.equals(s));          // true
		*/
		
		String a = "SIM";
		
		if (a.toLowerCase().equals("sim")) {
			System.out.println("opa");
		} else {
			System.out.println("Oh my god");
		}
		
		
		String b = "Eu amo JAVA";
		System.out.println(b.replace('a', '*'));
		
		String cpf = "123.456.789-10";
		String nova = cpf.replace(".", "").replace("-", "");
		System.out.println(nova.substring(0,3)+".***.***-" + nova.substring(9,11));
	}
}
	