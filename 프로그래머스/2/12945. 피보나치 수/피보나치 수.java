class Solution {
    public int solution(int n) {
        if (n <= 1) {
            return n;
        }
        
        int f0 = 0; // F(0)
        int f1 = 1;      // F(1)
        int answer = 0;   // F(i)

        for (int i = 2; i <= n; i++) {
            answer = (f0 + f1) % 1234567;
            f0 = f1;
            f1 = answer;
        }

        return answer;
    }
}