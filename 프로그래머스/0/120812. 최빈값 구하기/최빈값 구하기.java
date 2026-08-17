class Solution {
    public int solution(int[] array) {
        int answer = 0;
        
        int[] count_arr = new int[1001];
        boolean success = true;
        int max_cnt = 0;
        
        for (int i = 0; i < array.length; i++) {
            count_arr[array[i]]++;
        }
        
        for (int i = 0; i < 1001; i++) {
            if (count_arr[i] > max_cnt) {
                answer = i;
                max_cnt = count_arr[i];
                success = true;
            }
            else if (count_arr[i] == max_cnt) {
                success = false;
            }
        }
        
        if (!success) {
            answer = -1;
        }
        
        return answer;
    }
}