class Solution {
    public int[] solution(int numer1, int denom1, int numer2, int denom2) {
        int num = (numer1 * denom2) + (numer2 * denom1);
        int den = denom1 * denom2;
        
        int gcd = getGCD(num, den);
        
        int[] answer = {num / gcd, den / gcd};
        
        return answer;
    }
    
    private int getGCD(int a, int b) {
        while (b != 0) {
            int r = a % b;
            a = b;
            b = r;
        }
        return a;
    }
}