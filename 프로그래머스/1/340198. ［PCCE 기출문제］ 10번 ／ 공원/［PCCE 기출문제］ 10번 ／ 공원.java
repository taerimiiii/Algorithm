class Solution {
    public int solution(int[] mats, String[][] park) {
        int answer = 0;
        int row, col;
        int max_val;
        boolean success;
        
        max_val = -1;
        
        row = park.length;
        col = park[0].length;
        
        for (int x : mats) {
            for (int i=0; i<=row-x; i++) {
                for (int j=0; j<=col-x; j++) {
                    if (park[i][j].equals("-1")) {
                        success = true;
                        for (int k=0; k<x; k++) {
                            for (int l=0; l<x; l++) {
                                if (park[i+k][j+l].equals("-1")) {
                                    continue;
                                }
                                else {
                                    success = false;
                                    break;
                                }
                            }
                            if (success == false) {
                                break;
                            }
                        }
                        if (success == true) {
                            if (max_val < x) {
                                max_val = x;
                            }
                        }
                    }
                }
            }
        }
        answer = max_val;
        return answer;
    }
}