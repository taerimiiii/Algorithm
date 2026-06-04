class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = {};
        
        int q_len = queries.length;
        
        for (int i = 0; i < q_len; i++) {
            int temp = arr[queries[i][0]];
            arr[queries[i][0]] = arr[queries[i][1]];
            arr[queries[i][1]] = temp;
        }
        
        return arr;
    }
}