/*
http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=2900&sca=3010

풀이 : 먼저 ArrayList를 선언하고 값을 입력받아 2차원 배열을 만든 후 4진트리 재귀함수를 만들었습니다.
재귀함수에서는 전체 배열을 돌며 숫자가 통일될 때까지 좌상, 우상, 좌하, 우하 순으로 계속 돌리며 구합니다. 
만약 숫자가 통일 될 경우 그 함수 내에서 더이상의 재귀함수는 호출하지 않고, 통일되지 않을 경우 정사각형칸이 1이 될 때까지 계속 재귀함수를 호출합니다.
만약 정사각형칸이 1이 될 경우 그 정사각형칸의 값을 ArrayList에 담았으며 마지막 메인 메소드에서 ArrayList를 순회하며 값을 출력하였습니다.
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
        for (String item : result) {
			System.out.print(item);
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