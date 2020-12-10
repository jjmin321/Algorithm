package main

import (
	"strconv"
)

func solution(s string) int {
	answer, _ := strconv.Atoi(s)
	return answer
}

func main() {
	s := "1234"
	println(solution(s))
}
