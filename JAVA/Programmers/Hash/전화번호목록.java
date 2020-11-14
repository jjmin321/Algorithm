/*
https://programmers.co.kr/learn/courses/30/lessons/42577

풀이 : 먼저 전화번호 배열을 정렬한 후, 배열의 첫 번째 인덱스를 기준으로 잡고, for문을 통해 기준이 되는 인덱스보다 문자열이 짧거나 같은 인덱스들은 무시한 후 
나머지 값들을 순회합니다. 순회하는 도중 startsWith라는 내장함수를 통해 접두어 여부를 확인하고 접두어인 경우 false를 return, 없는 경우 true를 return하게 프로그램을 작성하였습니다.
*/


import java.util.Arrays;

public class HashLevel2 {
    public static void main(String[] args) {
        String[] phone_book = {"010111", "010", "1195524421"};
        System.out.println(solution(phone_book));
    }

    public static boolean solution(String[] phone_book) {
        Arrays.sort(phone_book);
        String first = phone_book[0];
        for (int i = 1; i < phone_book.length; i++) {
            if (phone_book[i].length() <= first.length()) {
                continue;
            } else if (phone_book[i].startsWith(first) == true){
                return false;
            }
        }
        return true;
    }
} 