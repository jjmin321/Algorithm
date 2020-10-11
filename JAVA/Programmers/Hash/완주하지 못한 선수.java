/*
https://programmers.co.kr/learn/courses/30/lessons/42576

풀이 : (배열과 맵 두 가지를 통해 풀 수 있는데 저는 맵을 사용하였습니다.)
맵에서 Key를 참가자들, Value를 1로 순회하면서 값을 넣었습니다, 만약 Value가 1이상일 경우 1을 넣지 않고 더하였습니다.
맵을 순회하며 완주자가 Key에 존재하다면 Value를 1을 빼서 최종적으로 Value가 0이 아닌 값을 출력하여 중복이름까지 걸러냈습니다.
*/
import java.util.HashMap;
import java.util.Map;

public class HashLevel1 {
    public static void main(String []args) {
        String[] participant = {"mislav", "stanko", "mislav", "ana"};
        String[] completion = {"stanko", "ana", "mislav"};
        String answer = solution(participant, completion);
        System.out.println(answer);
    }

    public static String solution(String[] participant, String[] completion) {
        Map<String, Integer> cache = new HashMap<>();
        for (int i = 0; i < participant.length; i++) 
            if (0 < cache.getOrDefault(participant[i], 0)) 
                cache.replace(participant[i], cache.get(participant[i]) + 1);
            else 
                cache.put(participant[i], 1);

        for (int i = 0; i < completion.length; i++) {
            if (0 < cache.get(completion[i])) 
                cache.replace(completion[i], cache.get(completion[i]) - 1);
        }
        for (Map.Entry<String, Integer> item : cache.entrySet()) {
            if (0 < item.getValue()) 
                return item.getKey();
        }
        return null;
    }
}