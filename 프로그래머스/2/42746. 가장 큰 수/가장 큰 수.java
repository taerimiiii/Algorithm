import java.util.Arrays;

class Solution {
    public String solution(int[] numbers) {
        String[] arr = new String[numbers.length];
        
        // 정수 배열을 문자열 배열로 변환
        for (int i = 0; i < numbers.length; i++) {
            arr[i] = String.valueOf(numbers[i]);
        }
        
        // 두 문자열을 이어 붙였을 때 더 큰 쪽이 앞으로 오도록 정렬
        Arrays.sort(arr, (str_first, str_second) -> {
            String first = str_first + str_second;
            String second = str_second + str_first;
            
            return second.compareTo(first);
        });
        
        // 가장 큰 수가 0으로 시작한다면, 모든 수가 0인 경우이므로 0 반환
        if (arr[0].equals("0")) {
            return "0";
        }
        
        StringBuilder answer = new StringBuilder();
        
        for (String elem : arr) {
            answer.append(elem);
        }
        
        return answer.toString();
    }
}