
public class Questao09professor {
	public static void main(String[] args) {
		int ano = 1986;
		
	}

	public static boolean isLeapYear(int ano) {
		boolean result = false;
		
		if (ano % 100 == 0) {
			if (ano %400 == 0) {
				return true;
			}
		} else {
			if (ano % 4 == 0) {
				return true;
			}
		}
		return result;
	}
}