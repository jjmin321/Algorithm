public class Hash1 {
    public static void main(String []args) {
        String[] participant = {"mislav", "stanko", "mislav", "ana"};
        String[] completion = {"mislav", "ana", "mislav"};
        String answer = solution(participant, completion);
        System.out.println(answer);
    }

    public String hashMap(String[] participant, String[] completion) {
        Map<String, Integer> cache = new HashMap<>();
        for (int i = 0, i < participant.length; i++) {
            String k = participant[i];
            cache.
        }
    }
}