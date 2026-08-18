class Solution {
    public String[] solution(String[] quiz) {
        String[] answer = new String[quiz.length];
        
        for (int i = 0; i < quiz.length; i++) {
            String[] parts = quiz[i].split(" ");

            int x = Integer.parseInt(parts[0]);
            String operator = parts[1];
            int y = Integer.parseInt(parts[2]);
            int z = Integer.parseInt(parts[4]);
            
            int calculateResult = 0;
            
            if (operator.equals("+")) {
                calculateResult = x + y;
            } 
            else if (operator.equals("-")) {
                calculateResult = x - y;
            }

            if (calculateResult == z) {
                answer[i] = "O";
            } 
            else {
                answer[i] = "X";
            }
        }
        
        return answer;
    }
}