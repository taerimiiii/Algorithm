class Solution {
    public int solution(int[] numbers, int target) {
        // 주어지는 숫자의 처음부터 끝까지 DFS
        return dfs(numbers, target, 0, 0);
    }
    
    private int dfs(int[] numbers, int target, int idx, int sum) {
        if (idx == numbers.length) {
            // 지금까지 계산한 합이 타겟 넘버와 같다면 방법 1개 발견
            if (sum == target) {
                return 1;
            }
            // 타겟 넘버를 만들지 못했다면 0 반환
            return 0;
        }
        
        // 현재 숫자를 더하는 경우와 빼는 경우 2가지로 갈라짐
        int plus_case = dfs(numbers, target, idx + 1, sum + numbers[idx]);
        int minus_case = dfs(numbers, target, idx + 1, sum - numbers[idx]);
        
        // 두 갈래 길에서 각각 만들어진 성공 횟수를 합쳐서 반환
        return plus_case + minus_case;
    }
}