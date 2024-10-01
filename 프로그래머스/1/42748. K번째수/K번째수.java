import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

class Solution {
    public Integer[] solution(int[] array, int[][] commands) {
        
        List<Integer> ans = new ArrayList<>();
        for (int i = 0; i < commands.length; i++) {
            List<Integer> list = new ArrayList<>();
            for (int j = commands[i][0] - 1; j < commands[i][1]; j++) {
                list.add(array[j]);
            }
            Collections.sort(list);
            ans.add(list.get(commands[i][2] - 1));
        }
        Integer[] answer = ans.toArray(new Integer[0]);
        return answer;
    }
}