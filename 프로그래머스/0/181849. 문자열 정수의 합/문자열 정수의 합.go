func solution(numbers string) int {
    ret := 0
    for _, item := range numbers {
        ret += int(item - '0')
    }
    return ret
}