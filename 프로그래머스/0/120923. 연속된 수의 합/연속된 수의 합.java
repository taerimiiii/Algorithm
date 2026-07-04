class Solution {
    public int[] solution(int num, int total) {
        int[] answer = new int[num];
        
        int start;
        
        if (num % 2 == 1) {
            start = total / num - (num / 2);
        }
        else {
            start = total / num - (num / 2 - 1);
        }
        
        for (int i = 0; i < num; i++) {
            answer[i] = start;
            start++;
        }
        
        return answer;
    }
}