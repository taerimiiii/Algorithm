class Solution {
    private int[] answer = new int[2];
    
    private boolean is_uniform(int[][] arr, int x, int y, int size) {
        int start_value = arr[x][y];
        
        for (int i = x; i < x + size; i++) {
            for (int j = y; j < y + size; j++) {
                if (arr[i][j] != start_value) {
                    return false;
                }
            }
        }
        return true;
    }

    // 재귀
    private void compress(int[][] arr, int x, int y, int size) {
        if (is_uniform(arr, x, y, size)) {
            answer[arr[x][y]]++;
            return;
        }
        int next_size = size / 2;
        
        compress(arr, x, y, next_size);
        compress(arr, x, y + next_size, next_size);
        compress(arr, x + next_size, y, next_size);
        compress(arr, x + next_size, y + next_size, next_size);
    }

    public int[] solution(int[][] arr) {
        compress(arr, 0, 0, arr.length);
        return answer;
    }
}