func solution(myString string) string {
    result := []rune(myString)
    
    for i, char := range result {
        if char < 'l' {
            result[i] = 'l'
        }
    }
    
    return string(result)
}