func solution(n int, control string) int {
    control_len := len(control)
    
    for i := 0; i < control_len; i++ {
        if control[i] == 'w' {
            n += 1
        } else if control[i] == 's' {
            n -= 1
        } else if control[i] == 'd' {
            n += 10
        } else {
            n -= 10
        }
    }
    
    return n
}