import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;
import java.util.HashMap;

class Solution {
    public String solution(String[] participant, String[] completion) {
        
        HashMap<String, Integer> map = new HashMap<>();
        for (String name : participant) {
            if (map.containsKey(name)) {
                map.replace(name, map.get(name) + 1);
            }
            else {
                map.put(name, 1);
            }
        }
        for (String name : completion) {
            if (map.containsKey(name)) {
                map.replace(name, map.get(name) - 1);
            }
        }
        String answer = "";
        for (String name : map.keySet()) {
            if (map.get(name) >= 1) {
                answer = name;
            }
        }
        return answer;
    }
}