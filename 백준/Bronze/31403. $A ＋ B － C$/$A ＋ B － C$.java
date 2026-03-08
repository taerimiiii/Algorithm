import java.util.*;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int a, b, c;
        a = sc.nextInt();
        b = sc.nextInt();
        c = sc.nextInt();
        
        String d = "";
        
        d += a;
        d += b;
        
        int e = Integer.parseInt(d);
        
        System.out.println(a + b - c);
        System.out.println(e - c);
    }
}