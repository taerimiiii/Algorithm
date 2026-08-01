import java.util.Arrays;

class Solution {
    public int solution(int[] people, int limit) {
        int[] arr = people;
        Arrays.sort(arr);
        
        int answer = 0;
        int left = 0;
        int right = arr.length - 1;
        
        while (left <= right) {
            if (arr[left] + arr[right] <= limit) {
                left++;
            }
            right--;
            answer++;
        }
        
        return answer;
    }
}