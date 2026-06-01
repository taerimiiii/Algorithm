func solution(num_list []int) int {
    mult := 1
    sum := 0
    answer := 0
    
    for i:=0; i<len(num_list); i++ {
        mult *= num_list[i]
        sum += num_list[i]
    }
    
    if mult < sum * sum {
        answer = 1
    }
    
    return answer
}