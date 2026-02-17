import java.util.Scanner;
 
public class Main {
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		
		String A = sc.next();
		String B = sc.next();
		String C = sc.next();
		String D = sc.next();

		long num1 = Long.parseLong(A+B);
        long num2 = Long.parseLong(C+D);

		long ans = num1 + num2;
		
		System.out.print(ans);

        sc.close();
	}
	
}