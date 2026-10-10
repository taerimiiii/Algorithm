class Solution {
    public String solution(String my_string, String letter) {
        String answer = "";
        
        char[] my_string_list = my_string.toCharArray();
        
        for (char c : my_string_list) {
            if (c != letter.charAt(0)) {
                answer += c;
            }
        }
        
        return answer;
    }
}