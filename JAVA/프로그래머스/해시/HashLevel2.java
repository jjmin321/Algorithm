import java.util.HashMap;
import java.util.Map;

public class HashLevel2 {
    public static void main(String[] args) {
        String[] phone_book = {"119", "97674223", "1195524421"};
        solution(phone_book);
    }

    public static boolean solution(String[] phone_book) {
        Map<Integer, String> cache = new HashMap<>();
        for (int i = 0; i < phone_book.length; i++) {
            cache.put(i, phone_book[i]);
        }
        return true;
    }
}