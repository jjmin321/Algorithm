import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class HashLevel2_2 {
    public static void main(String[] args) {
        String[][] clothes = { { "yellow_hat", "headgear" }, { "blue_sunglasses", "eyewear" },
                { "green_turban", "headgear" } };
        System.out.println(solution(clothes));
    }

    public static int solution(String[][] clothes) {
        int answer = 0;
        Map<String, Integer> cache = new HashMap<>();
        List<Integer> clothCount = new ArrayList<>();
        for (int i = 0; i < clothes.length; i++) {
            if (0 < cache.getOrDefault(clothes[i][1], 0)) 
                cache.replace(clothes[i][1], cache.get(clothes[i][1])+1);
            else 
                cache.put(clothes[i][1], 1);
        }
        for (Integer item : cache.values()) {
            clothCount.add(item);
        }  
        for (int i = 0; i < clothCount.size(); i++) {
            if (clothCount.size() == 1)
                return clothCount.get(0);
            else if (clothCount.size() == i+1) 
                break;
            else if (i == 0)
                answer += (clothCount.get(i)+1) * (clothCount.get(i+1)+1);
            else 
                answer += answer * clothCount.get(i+1)+1;
        }
        return answer-(clothCount.size()-1);
    }
}