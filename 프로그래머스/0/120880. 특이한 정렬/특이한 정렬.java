import java.util.Arrays;

class Solution {
    public int[] solution(int[] numlist, int n) {
        return Arrays.stream(numlist)
            .boxed() // int(원시 타입) 배열을 Integer(객체) 스트림으로 변환
            .sorted((a, b) -> {
                int distA = Math.abs(a - n);
                int distB = Math.abs(b - n);
                
                // 거리가 같다면, 더 큰 수가 앞에 오도록 내림차순 정렬
                if (distA == distB) {
                    return b - a; 
                }
                // 거리가 다르다면, 거리가 가까운 순으로 오름차순 정렬
                return distA - distB; 
            })
            .mapToInt(Integer::intValue) // 다시 int 배열로 변환
            .toArray();
    }
}