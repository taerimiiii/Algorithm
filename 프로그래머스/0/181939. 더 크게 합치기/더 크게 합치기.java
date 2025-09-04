class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        int pow = 10;
        int temp;
        int len_a = 1;
        int len_b = 1;
        
        temp = a;
        while (temp >= 10) {
            temp /= pow;
            len_a *= 10;
        }
        
        temp = b;
        while (temp >= 10) {
            temp /= pow;
            len_b *= 10;
        }
        
        int ab = a*len_b*10+b;
        int ba = b*len_a*10+a;
        
        if (ab >= ba) {
            answer = ab;
        }
        else {
            answer = ba;
        }
        return answer;
    }
}