class Solution {
    public int solution(String[] babbling) {
        int answer = 0;
        
        String[] speaks = {"aya", "ye", "woo", "ma"};
        
        for (String babble : babbling) {

            for (String speak : speaks) {
                babble = babble.replace(speak, " ");
            }
            
            if (babble.trim().length() == 0) {
                answer++;
            }
        }
        
        return answer;
    }
}