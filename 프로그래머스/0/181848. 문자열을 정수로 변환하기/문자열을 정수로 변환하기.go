package cote

import "strconv"

func solution(str string) int {
    ret, _ := strconv.ParseInt(str, 10, 64)
    return int(ret)
}