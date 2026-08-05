class Solution {
    public int[] solution(int n, long left, long right) {
        int[] answer = new int[(int) (right - left + 1)];
        
        for (int i = 0; i < answer.length; i++) {
            // 현재 구해야 하는 1차원 배열의 실제 인덱스
            long curr_idx = left + i;
            
            // 1차원 인덱스를 2차원 배열의 행과 열로 변환
            long row = curr_idx / n;
            long col = curr_idx % n;
            
            // 두 좌표 중 큰 값에 1을 더한 것이 해당 칸의 숫자
            answer[i] = (int) (Math.max(row, col) + 1);
        }
        
        return answer;
    }
}