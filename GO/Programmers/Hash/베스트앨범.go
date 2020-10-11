/*
https://programmers.co.kr/learn/courses/30/lessons/42579

풀이 :
*/

package main

import (
	"fmt"
)

func main() {
	genres := []string{"classic", "pop", "classic", "classic", "pop"}
	plays := []int{500, 600, 150, 800, 2500}
	fmt.Println("결과 : ", solution(genres, plays))

}

// 맵으로 클래식 3000, 팝송 1500 해서 숫자 큰 거 대로 정렬한 뒤 또 돌려서 거기서 큰 거 두개씩만 갖고오기
// 클래식, 팝송, 발라드 나온다치면 클래식 2개 넣고 팝송 2개 넣고 발라드 2개 넣으면될듯

func solution(genres []string, plays []int) []int {
	genrePlays := make(map[string]int)
	genreInterface := []interface{}{}
	// genrePlays : [classic] = 1450 , [pop] = 3100 이런 식으로 되게끔 넣음
	for i := 0; i < len(genres); i++ {
		if 0 < genrePlays[genres[i]] {
			genrePlays[genres[i]] += plays[i]
		} else {
			genrePlays[genres[i]] = plays[i]
		}
	}
	for i, v := range genrePlays {
		genreInterface = append(genreInterface, i, v)
	}
	for i := 1; i < len(genreInterface)-2; i += 2 {
		if genreInterface[i+2] != nil {
			if genreInterface[i].(int) < genreInterface[i+2].(int) {
				genreInterface[i-1], genreInterface[i], genreInterface[i+1], genreInterface[i+2] =
					genreInterface[i+1], genreInterface[i+2], genreInterface[i-1], genreInterface[i]
			}
		}
	}
	fmt.Println("genreInterface : ", genreInterface)
	return plays
}
