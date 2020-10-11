/*
https://programmers.co.kr/learn/courses/30/lessons/42578

풀이 : clothes 배열을 순회하며 맵에 <의상 종류, 의상 개수>로 모두 저장하였습니다. 
    맵의 값들만을 순회하여 경우의 수 공식 (A종류의 의상 개수+아무것도 안 입을때의 경우) * (B종류의 의상 개수+아무것도 안 입을 때의 경우) * ... 
    을 통해 모든 경우의 수를 구한 후 아무것도 안 입었을 때의 경우 1가지를 빼면 답이 나옵니다.
*/

import java.util.HashMap;
import java.util.Map;

public class HashLevel2_2 {
    public static void main(String[] args) {
        String[][] clothes = { { "yellow_hat", "headgear" }, { "blue_sunglasses", "eyewear" },
                { "green_turban", "headgear" } };
        System.out.println(solution(clothes));
    }

    public static int solution(String[][] clothes) {
        int answer = 1;
        Map<String, Integer> cache = new HashMap<>();
        for (int i = 0; i < clothes.length; i++) {
            if (0 < cache.getOrDefault(clothes[i][1], 0)) 
                cache.replace(clothes[i][1], cache.get(clothes[i][1])+1);
            else 
                cache.put(clothes[i][1], 1);
        }
        for (Integer item : cache.values()) {
            answer = answer * (item+1);
        }
        return answer-1;
    }
}