/*
http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=712&sca=2060
정올 1438 : 색종이(초)

문제 : 가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있다.
이 도화지 위에 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이를 색종이의 변과 도화지의 변이 평행하도록 붙인다.
이러한 방식으로 색종이를 한 장 또는 여러 장 붙인 후 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램을 작성하시오.

풀이 : 2차원 배열을 만들어 값을 입력받아서 색종이가 붙혀진 곳은 값을 구별하기 위해 1을 넣었습니다.
그리고 2차원 배열을 순회하며 1이 있는 인덱스를 모두 합친 값을 구하였습니다.
*/

package main

import "fmt"

func main() {
	paper := [100][100]int{}
	cnt := 0
	var coloredPaper int
	fmt.Println("한 개의 자연수를 입력하세요. 입력하는 자연수는 색종이의 수를 지정하는 수입니다.")
	fmt.Scan(&coloredPaper)
	left := 0
	under := 0
	for i := 0; i < coloredPaper; i++ {
		fmt.Println("두 개의 자연수를 입력하세요. 첫 번째 자연수는 색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리이고, 두 번째 자연수는 색종이의 아래쪽 변과 도화지의 아래쪽 변 사이의 거리입니다.")
		fmt.Scan(&left)
		fmt.Scan(&under)
		for j := left; j < left+10; j++ {
			for k := under; k < under+10; k++ {
				paper[j][k] = 1
			}
		}
	}
	for i := 0; i < 100; i++ {
		for j := 0; j < 100; j++ {
			if paper[i][j] == 1 {
				cnt++
			}
		}
	}
	fmt.Println(cnt)
}
