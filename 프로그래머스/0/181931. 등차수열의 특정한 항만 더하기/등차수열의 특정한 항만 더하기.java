class Solution {
    public int solution(int a, int d, boolean[] included) {
        int answer = 0;
        
        int sumVal = a;
        for (int i = 0; i < included.length; i++) {
            if (included[i]) {
                answer += sumVal;
            }
            sumVal += d;
        }
        
        return answer;
    }
}