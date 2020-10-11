/*
http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=614&sca=30

풀이 : 값을 입력받아 2차원 배열을 만든 후 4진트리 재귀함수를 만들었습니다.
재귀함수에서는 전체 배열을 돌며 파랑인지 흰색인지 구분을 하였고 만약 한 색으로 통일되었다면 그 색의 카운트 수를 1 더한 후 종료, 아니라면 또 다시 4진트리 재귀함수를 돌리며
정사각형칸이 1이 될 때까지 구합니다.
만약 정사각형칸이 1이 될 경우 그 정사각형칸의 값에 따라 카운트를 하여 모두 더한 결과를 출력하였습니다.
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