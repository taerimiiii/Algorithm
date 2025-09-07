class Solution {
    public int solution(int[] schedules, int[][] timelogs, int startday) {
        int answer = 0;
        int n, minute;
        boolean success;
        
        n = schedules.length;
        for (int i=0; i<n; i++) {
            schedules[i] += 10;
            minute = schedules[i] % 100;
            if (minute >= 60) {
                schedules[i] = schedules[i] + 100 - 60;
            }
        }
        
        for (int i=0; i<n; i++) {
            success = true;
            for (int j=0; j<7; j++) {
                if (startday != 6 && startday != 7 && timelogs[i][j] > schedules[i]) {
                    success = false;
                }
                startday = (startday + 1) % 7;
                if (startday == 0) {
                    startday = 7;
                }
            }
            if (success) {
                answer += 1;
            }
        }
        return answer;
    }
}