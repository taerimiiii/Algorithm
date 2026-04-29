import "strings"

func solution(myString string, pat string) int {
    str := strings.Map(func(r rune) rune {
        if r == 'A' {
            return 'B'
        }
        return 'A'
    }, myString)
    if strings.Contains(str, pat) {
        return 1
    }
    return 0
}