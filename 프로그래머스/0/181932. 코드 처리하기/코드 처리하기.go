package main

import "strings"

func solution(code string) string {
	var ret strings.Builder
    
	mode := 0

	for i := 0; i < len(code); i++ {
		if code[i] == '1' {
			mode = 1 - mode
		} else {
			if mode == 0 && i % 2 == 0 {
				ret.WriteByte(code[i])
			} else if mode == 1 && i % 2 != 0 {
				ret.WriteByte(code[i])
			}
		}
	}

	// 만들어진 문자열이 빈 문자열이라면 "EMPTY" 반환
	if ret.Len() == 0 {
		return "EMPTY"
	}

	return ret.String()
}