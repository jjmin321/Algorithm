import java.util.Scanner;

public class Jungol1671 {
    public static void main(String[] args) {
		int[][] count = new int[100][100];
		int value = 0;
		Scanner sc = new Scanner(System.in);
		int first = sc.nextInt();
		int left = 0;
		int under = 0;
		for (int i = 0; i < first; i++) {
			System.out.println("왼쪽에서부터랑 밑에서부터 얼마나 거리 벌릴건지 입력해라");
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
					if ((count[i+1][j] == 0 || count[i-1][j] == 0) && (count[i][j+1] == 0 || count[i][j-1] == 0)) {
						value += 2;
					}else if (count[i+1][j] == 0 || count[i-1][j] == 0 || count[i][j+1] == 0 || count[i][j-1] == 0) {
						value++;
					}
				}
			}
		}
			System.out.println(value);
	}
}