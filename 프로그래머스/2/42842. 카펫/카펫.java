
    
class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        
        int area = brown + yellow;
        
        for (int row = 1; row <= area; row++) {
            if (area % row != 0) {
                continue;
            }
            int col = area / row;
            
            if ( (row - 2) * (col - 2) == yellow ) {
                answer[0] = col;
                answer[1] = row;
                break;
            }
        }
        
        return answer;
    }
}