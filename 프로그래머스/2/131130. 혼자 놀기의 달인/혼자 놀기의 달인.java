import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

class Solution {
    public int solution(int[] cards) {
        int[] arr = cards; // 요구사항에 따라 배열 변수명을 arr로 지정
        int arr_length = arr.length;
        boolean[] is_visited = new boolean[arr_length];
        List<Integer> group_sizes = new ArrayList<>();

        for (int i = 0; i < arr_length; i++) {
            if (!is_visited[i]) {
                int curr = i; // 요구사항에 따라 현재 인덱스를 curr로 지정
                int current_group_size = 0;

                while (!is_visited[curr]) {
                    is_visited[curr] = true;
                    curr = arr[curr] - 1; // 카드의 숫자는 1부터 시작하므로 인덱스 접근을 위해 1을 뺌
                    current_group_size++;
                }
                
                group_sizes.add(current_group_size);
            }
        }

        // 그룹이 하나밖에 없다면 문제 조건에 따라 0을 반환
        if (group_sizes.size() <= 1) {
            return 0;
        }

        // 그룹 크기들을 내림차순으로 정렬
        Collections.sort(group_sizes, Collections.reverseOrder());

        // 가장 큰 두 그룹의 크기를 곱하여 반환
        int max_score = group_sizes.get(0) * group_sizes.get(1);

        return max_score;
    }
}