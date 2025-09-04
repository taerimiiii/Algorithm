class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        String answer = "";
        int len_m = my_string.length();
        int len_o = overwrite_string.length();
            
        for (int i=0; i<len_m; i++) {
            if (i>=s && i<s+len_o) {
                answer += overwrite_string.charAt(i - s);
            }
            else {
                answer += my_string.charAt(i);
            }
        }
        return answer;
    }
}