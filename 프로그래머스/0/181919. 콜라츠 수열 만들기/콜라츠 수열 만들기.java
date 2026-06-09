import java.util.ArrayList;

class Solution {
    public int[] solution(int n) {
        
        ArrayList<Integer> seq = new ArrayList<>();
        
        while (true) {
            seq.add(n);
            
            if (n == 1) {
                break;
            }
            
            if (n % 2 == 1) {
                n = 3 * n + 1;
            }
            else {
                n /= 2;
            }
        }
        
        int[] answer = new int[seq.size()];
        for (int i = 0; i < seq.size(); i++) {
            answer[i] = seq.get(i);
        }
        
        return answer;
    }
}