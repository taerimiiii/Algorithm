class Solution {
    public String solution(String polynomial) {
        int xCount = 0;
        int numCount = 0;
        
        String[] terms = polynomial.split(" \\+ ");
        
        for (String term : terms) {
            
            if (term.contains("x")) {
                
                if (term.equals("x")) {
                    xCount += 1;
                } 
                else {
                    String coefficient = term.replace("x", "");
                    xCount += Integer.parseInt(coefficient);
                }
            } 
            
            else {
                numCount += Integer.parseInt(term);
            }
        }
        
        
        StringBuilder answer = new StringBuilder();
        
        if (xCount > 0) {
            if (xCount == 1) {
                answer.append("x");
            } 
            else {
                answer.append(xCount).append("x");
            }
        }
        
        if (numCount > 0) {
            if (xCount > 0) {
                answer.append(" + ");
            }
            answer.append(numCount);
        }
        
        return answer.toString();
    }
}