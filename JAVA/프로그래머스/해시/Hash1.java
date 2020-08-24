import java.util.HashMap;
import java.util.Map;

public class Hash1 {
    public static void main(String []args) {
        String[] participant = {"mislav", "stanko", "mislav", "ana"};
        String[] completion = {"mislav", "ana", "mislav"};
        String answer = hashmethod(participant, completion);
        System.out.println(answer.toString());
    }

    public static String hashmethod(String[] participant, String[] completion) {
        Map<String, Integer> cache = new HashMap<>();
        for (int i = 0; i < participant.length; i++) {
            cache.put(participant[i], 1);
        }
        for (int i = 0; i < completion.length; i++) {
            cache.remove(completion[i]);
        }
        return cache.keySet().toString();
    }
}