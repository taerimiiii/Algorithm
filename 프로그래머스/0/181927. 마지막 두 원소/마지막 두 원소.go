func solution(num_list []int) []int {
    length := len(num_list)

    last := num_list[length-1]
    prev := num_list[length-2]
    
    if last > prev {
        num_list = append(num_list, last - prev)
    } else {
        num_list = append(num_list, last * 2)
    }
    
    return num_list
}