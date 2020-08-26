/*
https://programmers.co.kr/learn/courses/30/lessons/42576
프로그래머스 코딩테스트 연습 - 해시 : 완주하지 못한 선수

문제 : 수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 
완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

풀이 : 배열과 맵 두
*/

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Hash1 {
    public static void main(String []args) {
        String[] participant = {"mislav", "stanko", "mislav", "ana"};
        String[] completion = {"stanko", "ana", "mislav"};
        String answer = solution(participant, completion);
        System.out.println(answer);
    }

    public static String solution(String[] participant, String[] completion) {
        Map<String, Integer> cache = new HashMap<>();
        for (int i = 0; i < participant.length; i++) {
            if (0 < cache.getOrDefault(participant[i], 0)) {
                cache.replace(participant[i], cache.get(participant[i]) + 1);
            }else {
                cache.put(participant[i], 1);
            }
        }
        for (int i = 0; i < completion.length; i++) {
            if (0 < cache.get(completion[i])) {
                cache.replace(completion[i], cache.get(completion[i]) - 1);
            }
        }
        for (Map.Entry<String, Integer> item : cache.entrySet()) {
            if (0 < item.getValue()) 
                return item.getKey();
        }
        return null;
    }
}