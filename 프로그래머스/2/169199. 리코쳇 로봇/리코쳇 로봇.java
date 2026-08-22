import java.util.*;

class Solution {
    public int solution(String[] board) {
        int row = board.length;
        int col = board[0].length();
        int start_row = -1, start_col = -1, goal_row = -1, goal_col = -1;
        
        // 로봇의 처음 위치와 목표 지점 찾기
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (board[i].charAt(j) == 'R') {
                    start_row = i;
                    start_col = j;
                } 
                else if (board[i].charAt(j) == 'G') {
                    goal_row = i;
                    goal_col = j;
                }
            }
        }
        
        // 초기화 및 변수 선언
        Queue<int[]> queue = new LinkedList<>();
        boolean[][] visited = new boolean[row][col];
        queue.offer(new int[]{start_row, start_col, 0});
        visited[start_row][start_col] = true;

        int[] dxs = {-1, 1, 0, 0};
        int[] dys = {0, 0, -1, 1};
        
        // bfs
        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int x = curr[0];
            int y = curr[1];
            int moves = curr[2];
            
            if (x == goal_row && y == goal_col) {
                return moves;
            }
            
            for (int i = 0; i < 4; i++) {
                int nx = x;
                int ny = y;
                
                while (nx + dxs[i] >= 0 && nx + dxs[i] < row && ny + dys[i] >= 0 && ny + dys[i] < col && board[nx + dxs[i]].charAt(ny + dys[i]) != 'D') {
                    nx += dxs[i];
                    ny += dys[i];
                }
                
                if (!visited[nx][ny]) {
                    visited[nx][ny] = true;
                    queue.offer(new int[]{nx, ny, moves + 1});
                }
            }
        }
        
        return -1;
    }
}