import java.util.Arrays;

class Solution {
    public int solution(int[][] board) {
        int answer = 0;
        
        // 안전한지 여부를 저장할 배열 선언 및 초기화
        boolean[][] safe = new boolean[board.length][board.length];
        for (int i = 0; i < safe.length; i++) {
            Arrays.fill(safe[i], true);
        }
        
        int[] dxs = {0, 1, 1, 1, 0, -1, -1, -1};
        int[] dys = {1, 1, 0, -1, -1, -1, 0, 1};
        
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board.length; j++) {
                if (board[i][j] == 1) {
                    safe[i][j] = false;
                    
                    for (int direct = 0; direct < 8; direct++) {
                        int nx = i + dxs[direct];
                        int ny = j + dys[direct];
                        if (in_range(nx, ny, board.length) && safe[nx][ny]) {
                            safe[nx][ny] = false;
                        }
                    }
                }
            }
        }
        
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board.length; j++) {
                if (safe[i][j]) {
                    answer++;
                }
            }
        }
        
        return answer;
    }
    
    private boolean in_range(int x, int y, int n) {
        if (0 <= x && x < n && 0 <= y && y < n) {
            return true;
        }
        else {
            return false;
        }
    }
}