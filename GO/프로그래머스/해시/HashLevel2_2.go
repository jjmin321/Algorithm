/*
https://programmers.co.kr/learn/courses/30/lessons/42578
프로그래머스 코딩테스트 연습 - 해시 : 위장

문제 : 스파이들은 매일 다른 옷을 조합하여 입어 자신을 위장합니다.
예를 들어 스파이가 가진 옷이 아래와 같고 오늘 스파이가 동그란 안경, 긴 코트, 파란색 티셔츠를 입었다면 다음날은 청바지를 추가로 입거나 동그란 안경 대신 검정 선글라스를 착용하거나 해야 합니다.
종류	이름
얼굴	동그란 안경, 검정 선글라스
상의	파란색 티셔츠
하의	청바지
겉옷	긴 코트
스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때 서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.

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
	for i := 0; i < len(clothes) i++ {
	}
	
	return answer - 1
}
