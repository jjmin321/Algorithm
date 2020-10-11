/*
https://programmers.co.kr/learn/courses/30/lessons/42577
프로그래머스 코딩테스트 연습 - 해시 : 전화번호 목록

문제 : 전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.
구조대 : 119
박준영 : 97 674 223
지영석 : 11 9552 4421
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 
어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

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