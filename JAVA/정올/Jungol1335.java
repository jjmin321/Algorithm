/*
http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=614&sca=30
정올 1335 : 색종이 만들기(영역구분)

문제 : 아래 <그림 1>과 같이 여러개의 정사각형칸들로 이루어진 정사각형 모양의 종이가 주어져 있고, 
각 정사각형들은 하얀색으로 칠해져 있거나 파란색으로 칠해져 있다. 
주어진 종이를 일정한 규칙에 따라 잘라서 다양한 크기를 가진 정사각형 모양의 하얀색 또는 파란색 색종이를 만들려고 한다. 

전체 종이의 크기가 N×N(N=2k, k는 1 이상 7 이하의 자연수) 이라면 종이를 자르는 규칙은 다음과 같다.
 
전체 종이가 모두 같은 색으로 칠해져 있지 않으면 가로와 세로로 중간 부분을 잘라서 
<그림 2>의 I, II, III, IV와 같이 똑같은 크기의 네 개의 N/2 × N/2색종이로 나눈다.
나누어진 종이 I, II, III, IV 각각에 대해서도 앞에서와 마찬가지로 모두 같은 색으로 칠해져 있지 않으면 
같은 방법으로 똑같은 크기의 네 개의 색종이로 나눈다. 
이와 같은 과정을 잘라진 종이가 모두 하얀색 또는 모두 파란색으로 칠해져 있거나, 
하나의 정사각형 칸이 되어 더 이상 자를 수 없을 때까지 반복한다.
 
위와 같은 규칙에 따라 잘랐을 때 <그림 3>은 <그림 1>의 종이를 처음 나눈 후의 상태를,
<그림 4>는 두 번째 나눈 후의 상태를, 
<그림 5>는 최종적으로 만들어진 다양한 크기의 9장의 하얀색 색종이와 7장의 파란색 색종이를 보여주고 있다. 

입력으로 주어진 종이의 한 변의 길이 N과 각 정사각형칸의 색(하얀색 또는 파란색)이 주어질 때 
잘라진 하얀색 색종이와 파란색 색종이의 개수를 구하는 프로그램을 작성하시오.

풀이 : 값을 입력받아 2차원 배열을 통해 정사각형 모양의 종이를 만든 후 재귀함수를 통해 색종이의 개수를 셌습니다.
재귀함수에서는 전체 배열을 돌며 파랑인지 흰색인지 구분을 하였고 만약 한 색으로 통일되었다면 그 색의 카운트 수를 1 더한 후 종료.
만약 정사각형칸이 1개가 될 때까지 색이 통일되지 않았다면 그 정사각형칸의 색을 그 색의 카운트 수를 1 더한 후 종료.
*/

import java.util.Scanner;

public class Jungol1335 {
    static int white = 0;
	static int blue = 0;
	public static void main(String []args) {
		System.out.println("n을 입력하세요");
		Scanner scanner = new Scanner(System.in);
		int n = scanner.nextInt();
		int [][] square = new int[n][n];
		// 입력 값 받음
		for (int i = 0; i < n; i++) {
			System.out.println((i+1)+"번째 줄에 넣을 값을 입력하세요.");
			for (int j = 0; j < n; j++) {
				square[i][j] = scanner.nextInt();
			}
		}
		scanner.close();
		// slice(square , 세로 시작, 세로 끝 , 가로 시작, 가로 끝)
		slice(square, 0, 0, n);
		System.out.println(white);
		System.out.println(blue);
	}
	
	public static void slice(int [][] square, int horizontal, int vertical, int size) {
		int is_white = 0;
		// 파랑인지 흰색인지 구분하기 위해 전체 배열을 도는 로직
		for (int i = vertical; i < vertical+size; i++) {
			for (int j = horizontal; j < horizontal+size; j++) {
				if (square[i][j] == 0) {
					is_white++;
				}
			}
		}
		// 정사각형의 칸이 2x2라면 각 색종이 수를 더하고 그 정사각형은 끝
		// 만약 한 색으로 통일되었다면 통일된 색 색종이 수를 더하고 그 정사각형은 끝
		// 2x2와 한 색으로 통일된 게 모두 아니라면 2x2가 될 때 또는 한 색으로 통일될 때까지 종이를 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래를 계속 잘라가며 구함  
		if (is_white == size * size) {
			white += 1;
		} else if (is_white == 0) {
			blue += 1;
		} else if (size == 2){
			white += is_white;
			blue += (4 - is_white);
		} else {
			slice(square, horizontal, vertical, size/2);
			slice(square, horizontal, vertical+size/2, size/2);
			slice(square, horizontal+size/2, vertical, size/2);
			slice(square, horizontal+size/2, vertical+size/2, size/2);
		}
	}
}