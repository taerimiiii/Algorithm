class Solution {
    public String solution(String my_string) {
        String answer = "";
        
        char[] my_string_arr = my_string.toCharArray();
        
        for (int i = my_string_arr.length - 1; i >= 0; i--) {
            answer += my_string_arr[i];
        }
        
        return answer;
    }
}