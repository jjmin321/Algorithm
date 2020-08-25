/*
http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=2900&sca=3010
정올 3560 : 색종이 만들기2 (4진트리)

문제 : 재우는 분할정복을 공부중이다.
그래서 1335:색종이 만들기 문제를 풀었다.
좀 더 공부하고 싶은 재우는​ 다음과 같은 문제를 생각해 보았다.
 
한 변의 길이가 2의 제곱수인 정사각형에 주어질 때,
주어진 정사각형에 포함된 숫자가 모두 0이면 0,
주어진 정사각형에 포함된 숫자가 모두 1이면 1 로 나타낸다.
그렇지 않고 주어진 정사각형에 포함된 숫자가 0, 1이 함께 있다면 
대문자 X로 그 영역을 나타내고 해당 영역을 4등분하여
재귀적으로 호출하여 같은 규칙을 적용한다.
4등분한 영역의 호출 순서는 좌상, 우상, 좌하, 우하 이다.
 
예를 들면 아래와 같은 정보가 주어지면
8
1 0 1 1 1 1 1 1
0 1 1 1 1 1 1 1
0 0 0 0 1 1 1 1
0 0 0 0 1 1 1 1
1 1 0 0 0 0 0 0
1 1 0 0 0 0 0 0
0 0 1 1 0 0 0 0
0 0 1 1 0 0 0 0​ 
 
위의 규칙을 따르면 다음과 같은 결과가 만들어진다.
XXX10011001X10010​  

풀이 : 값을 입력받아 2차원 배열을 만든 후 4진트리 재귀함수를 만들었습니다.
재귀함수에서는 전체 배열을 돌며 파랑인지 흰색인지 구분을 하였고 만약 한 색으로 통일되었다면 그 색의 카운트 수를 1 더한 후 종료, 아니라면 또 다시 4진트리 재귀함수를 돌리며
정사각형칸이 1이 될 때까지 구합니다.
만약 정사각형칸이 1이 될 경우 그 정사각형칸의 값에 따라 카운트를 하여 모두 더한 결과를 출력하였습니다.
*/

import java.util.ArrayList;
import java.util.Scanner;

public class Jungol3560 {
    static ArrayList<String> result = new ArrayList<String>();
    public static void main(String[] args) {
        System.out.println("n을 입력하세요");
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int [][] square = new int[n][n];
        for (int i = 0; i < n; i++) {
            System.out.println((i+1)+"번째 줄에 넣을 값을 입력하세요.");
			for (int j = 0; j < n; j++) {
				square[i][j] = scanner.nextInt();
			}
        }
        scanner.close();
        slice(square, 0, 0, n);
        for (int i=0; i < result.size(); i++) {
			System.out.print(result.get(i));
		}
    }

    public static void slice(int [][]square, int horizontal, int vertical, int size){
        boolean is_same = true;
        for (int i = horizontal; i < horizontal+size; i++) {
            for (int j = vertical; j < vertical+size; j++) {
                if (square[i][j] != square[horizontal][vertical]) {
                    is_same = false;
                }
            }
        }
        if (is_same == false) {
            result.add("X");
            slice(square, horizontal, vertical, size/2);
            slice(square, horizontal, vertical+size/2, size/2);
            slice(square, horizontal+size/2, vertical, size/2);
            slice(square, horizontal+size/2, vertical+size/2, size/2);
        } else {
            result.add((Integer.toString(square[horizontal][vertical])));
        }
    }
}