class Solution {
    public int solution(int a, int b, int c, int d) {
        int answer = 0;
        
        if (a == b && b == c && c == d) {
            answer = 1111 * a;
        }
        // 3개가 같은 경우
        else if (a == b && b == c) {
            answer = (int) Math.pow(10 * a + d, 2) ;
        }
        else if (a == b && b == d) {
            answer = (int) Math.pow(10 * a + c, 2) ;
        }
        else if (a == c && c == d) {
            answer = (int) Math.pow(10 * a + b, 2) ;
        }
        else if (b == c && c == d) {
            answer = (int) Math.pow(10 * b + a, 2) ;
        }
        // 2개가 같은 경우
        else if (a == b) {
            if (c == d) { // 2개가 2쌍씩 같은 경우
                answer = (a + c) * Math.abs(a - c);
            }
            else {
                answer = c * d;
            }
        }
        else if (a == c) {
            if (b == d) {
                answer = (a + b) * Math.abs(a - b);
            }
            else {
                answer = b * d;
            }
        }
        else if (a == d) {
            if (b == c) {
                answer = (a + b) * Math.abs(a - b);
            }
            else {
                answer = b * c;
            }
        }
        else if (b == c) {
            answer = a * d;
        }
        else if (b == d) {
            answer = a * c;
        }
        else if (c == d) {
            answer = a * b;
        }
        else {
            int min_val = a;
            int[] arr = {b, c, d};
            for (int elem : arr) {
                if (elem < min_val) {
                    min_val = elem;
                }
            }
            answer = min_val;
        }
        
        return answer;
    }
}