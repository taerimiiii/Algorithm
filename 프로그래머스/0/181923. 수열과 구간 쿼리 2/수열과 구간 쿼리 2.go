func solution(arr []int, queries [][]int) []int {
    answer := []int{}
    
    query_len := len(queries)
    
    
    for i:=0; i<query_len; i++ {
        min_val := 1000001
        for j:=queries[i][0]; j<=queries[i][1]; j++ {
            if arr[j] > queries[i][2] && arr[j] < min_val {
                min_val = arr[j]
            }
        }
        
        if min_val == 1000001 {
            answer = append(answer, -1)
        } else {
            answer = append(answer, min_val)
        }
    }
    
    return answer
}