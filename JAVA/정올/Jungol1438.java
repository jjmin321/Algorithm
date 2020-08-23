/*
http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=712&sca=2060
정올 1438 : 색종이(초)
문제 : 가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있다.
이 도화지 위에 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이를 색종이의 변과 도화지의 변이 평행하도록 붙인다. 
이러한 방식으로 색종이를 한 장 또는 여러 장 붙인 후 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램을 작성하시오.
*/

import java.util.Scanner;

public class Jungol1438 {
    public static void main(String[] args) {
        int[][] count = new int[100][100];
        int value = 0;
        Scanner sc = new Scanner(System.in);
        System.out.println("한 개의 자연수를 입력하세요. 입력하는 자연수는 색종이의 수를 지정하는 수입니다.");
        int first = sc.nextInt();
        int left = 0;
        int under = 0;
        for (int i = 0; i < first; i++) {
            System.out.println("두 개의 자연수를 입력하세요. 첫 번째 자연수는 색종이의 왼쪽 변과 도화지의 왼쪽 변 사이의 거리이고, 두 번째 자연수는 색종이의 아래쪽 변과 도화지의 아래쪽 변 사이의 거리입니다.");
            left = sc.nextInt();
            under = sc.nextInt();
            for (int j = left; j < left+10; j++) {
                for (int k = under; k < under+10; k++) {
                    count[j][k] = 1;
                }
            }
        }
        sc.close();
            for (int i = 0; i < 100; i++) {
                for (int j = 0; j < 100; j++) {
                    if (count[i][j] == 1) {
                        value++;
                    }
                }
            }
            System.out.println(value);
    }
}