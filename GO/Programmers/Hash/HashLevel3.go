/*
https://programmers.co.kr/learn/courses/30/lessons/42579
프로그래머스 코딩테스트 연습 - 해시 : 베스트앨범

문제 : 스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.
속한 노래가 많이 재생된 장르를 먼저 수록합니다.
장르 내에서 많이 재생된 노래를 먼저 수록합니다.
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때, 베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

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
