import java.util.Stack;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        Stack<Character> stack = new Stack<>();
        
        for (int i = 0; i < s.length(); i++) {
            char curr_s = s.charAt(i);
            
            if (curr_s == '(') {
                stack.push(curr_s);
            }
            else {
                if (stack.isEmpty()) {
                    answer = false;
                    break;
                }
                else {
                    stack.pop();
                }
            }
        }

        if (!stack.isEmpty()) {
            answer = false;
        }

        return answer;
    }
}