class Solution {
    public int[] solution(int[] numbers, int num1, int num2) {
        int[] answer = new int[num2 - num1 + 1];
        
        int len = answer.length;
        
        for (int i = 0; i < len; i++) {
            answer[i] = numbers[i + num1];
        }
        
        return answer;
    }
}