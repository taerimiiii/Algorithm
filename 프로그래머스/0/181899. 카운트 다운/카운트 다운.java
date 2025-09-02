class Solution {
    public int[] solution(int start_num, int end_num) {
        int n = start_num - end_num + 1;
        int[] answer = new int[n];
        
        for (int i=0; i<n; i++) {
            answer[i] = start_num - i;
        }
        return answer;
    }
}