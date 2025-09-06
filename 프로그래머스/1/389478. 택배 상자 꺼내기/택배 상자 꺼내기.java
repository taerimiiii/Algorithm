class Solution {
    private boolean in_range(int x, int y, int[][] arr) {
        return (0 <= x && x < arr.length) && (0 <= y && y < arr[0].length);
    }
    
    public int solution(int n, int w, int num) {
        int answer = 0;
        int[][] arr = new int[101][w];
        
        int[] dys = {1, -1};
        int direct = 0;
        int x = 0, y = 0;
        int nx, ny;
        
        arr[x][y] = 1;
        for (int elem=2; elem<=n; elem++) {
            ny = y + dys[direct];
            
            if (in_range(x, ny, arr)) {
                y = ny;
            }
            else {
                direct = (direct + 1) % 2;
                x += 1;
            }
            
            arr[x][y] = elem;
        }
        
        int target_x, target_y;
        target_x = (num-1) / w;
        target_y = (num-1) % w;
        if (target_x % 2 == 1) {
            target_y = w - 1 - target_y;
        }
        
        while (arr[target_x][target_y] != 0) {
            answer += 1;
            target_x += 1;
        }
        
        return answer;
    }
}