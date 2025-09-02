import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        StringBuilder answer = new StringBuilder();
        
        for (char c : a.toCharArray()) {
            if (Character.isUpperCase(c)) {
                answer.append(Character.toLowerCase(c));
            }
            else if (Character.isLowerCase(c)) {
                answer.append(Character.toUpperCase(c));
            }
        }
        
        System.out.print(answer);
    }
}
