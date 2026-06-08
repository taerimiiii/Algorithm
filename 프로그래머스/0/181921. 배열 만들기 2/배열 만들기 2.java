import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int l, int r) {
        // 가변 길이의 데이터를 저장하기 위해 List 사용
        List<Integer> list = new ArrayList<>();
        
        for (int i = l; i <= r; i++) {
            int temp = i;
            boolean isValid = true; // 0과 5로만 이루어져 있는지 체크하는 플래그
            
            // 숫자의 각 자릿수를 확인
            while (temp > 0) {
                int digit = temp % 10; // 1의 자리 숫자 추출
                // 0이나 5가 아니면 조건에 맞지 않음
                if (digit != 0 && digit != 5) {
                    isValid = false;
                    break;
                }
                temp /= 10; // 다음 자릿수 확인을 위해 10으로 나눔
            }
            
            // 0과 5로만 이루어진 숫자라면 리스트에 추가
            if (isValid) {
                list.add(i);
            }
        }
        
        // 조건에 맞는 숫자가 없다면 [-1] 리턴
        if (list.isEmpty()) {
            return new int[]{-1};
        }
        
        // List를 int[] 배열로 변환하여 리턴
        int[] answer = new int[list.size()];
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i);
        }
        
        return answer;
    }
}