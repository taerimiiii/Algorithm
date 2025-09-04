class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        String strA = String.valueOf(a);
        String strB = String.valueOf(b);
        int addAB = Integer.valueOf(strA+strB);
        
        if (addAB >= 2*a*b) {
            answer = addAB;
        }
        else {
            answer = 2*a*b;
        }
        return answer;
    }
}