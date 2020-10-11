/*
https://programmers.co.kr/learn/courses/30/lessons/42578

풀이 : clothes 배열을 순회하며 맵에 <의상 종류, 의상 개수>로 모두 저장하였습니다.
    맵의 값들만을 순회하여 경우의 수 공식 (A종류의 의상 개수+아무것도 안 입을때의 경우) * (B종류의 의상 개수+아무것도 안 입을 때의 경우) * ...
    을 통해 모든 경우의 수를 구한 후 아무것도 안 입었을 때의 경우 1가지를 빼면 답이 나옵니다.
*/

package main

import "fmt"

func main() {
	clothes := [][]string{{"yellow_hat", "headgear"}, {"blue_sunglasses", "eyewear"},
		{"green_turban", "headgear"}}
	fmt.Println(solution(clothes))
}

func solution(clothes [][]string) int {
	answer := 1
	cache := make(map[string]int)
	for i := 0; i < len(clothes); i++ {
		if 0 < cache[clothes[i][1]] {
			cache[clothes[i][1]]++
		} else {
			cache[clothes[i][1]] = 1
		}
	}
	for _, v := range cache {
		answer = answer * (v + 1)
	}

	return answer - 1
}
