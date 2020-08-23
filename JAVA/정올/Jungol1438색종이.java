import java.util.Scanner;

public class Jungol1438색종이 {
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
                if (j > 100) {
                    break;
                }
                for (int k = under; k < under+10; k++) {
                    if (k > 100) {
                        break;
                    }
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