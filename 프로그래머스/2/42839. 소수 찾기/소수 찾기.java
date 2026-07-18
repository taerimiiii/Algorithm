import java.util.Arrays;

class Solution {
    public int solution(String numbers) {
        int answer = 0;
        
        // 주어진 숫자를 내림차순 정렬해서 만들 수 있는 가장 큰 수 구하기
        char[] chars = numbers.toCharArray();
        Arrays.sort(chars);
        StringBuilder sb = new StringBuilder(new String(chars));
        int max_num = Integer.parseInt(sb.reverse().toString());
        
        // 2부터 가장 큰 수까지 모든 숫자를 하나씩 검사
        for (int num = 2; num <= max_num; num++) {
            // num이 소수이고, 동시에 주어진 numbers 카드로 만들 수 있는 숫자인지 확인
            if (isPrime(num) && isSuccess(num, numbers)) {
                answer++;
            }
        }
        
        return answer;
    }

    // 소수 판별 함수
    private boolean isPrime(int num) {
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }

    // 가진 숫자 카드로 타겟을 만들 수 있는지 검사하는 함수
    private boolean isSuccess(int target, String numbers) {
        // 내가 가진 숫자 카드의 개수를 세어둘 배열
        int[] card_cnt = new int[10];
        
        // 카드 개수 세기
        for (char c : numbers.toCharArray()) {
            card_cnt[c - '0']++;
        }
        
        // 타겟의 각 자리수를 보며 카드 개수를 줄여나감
        while (target > 0) {
            int digit = target % 10; // 일의 자리 숫자 가져오기
            
            if (card_cnt[digit] == 0) {
                return false; // 필요한 카드가 없으면 탈락
            }
            card_cnt[digit]--; // 카드가 있다면 한 장 소비
            
            target /= 10; // 다음 자리수로 이동
        }
        
        return true; // 무사히 통과하면 만들 수 있는 숫자임!
    }
}