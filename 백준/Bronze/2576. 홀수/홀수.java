import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws Exception {
        Scanner sc = new Scanner(System.in);

        int sum_val = 0;
        int min_val = Integer.MAX_VALUE;
        boolean success = false;
        for (int i = 0; i < 7; i++) {
            int n = sc.nextInt();
            if (n % 2 == 1) {
                success = true;
                if (min_val > n) {
                    min_val = n;
                }
                sum_val += n;
            }
        }

        if (success) {
            System.out.println(sum_val);
            System.out.print(min_val);
        }
        else {
            System.out.print(-1);
        }

        sc.close();
    }
}
