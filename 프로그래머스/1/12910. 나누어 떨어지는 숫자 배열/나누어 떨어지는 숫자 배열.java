import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        List<Integer> ans = new ArrayList<>();
        Arrays.sort(arr);
        for (int i : arr) {
            if (i % divisor == 0) {
                ans.add(i);
            }
        }
        if (ans.isEmpty()) {
            return new int[] {-1};
        }
        int[] answer = new int[ans.size()];
        for (int i = 0; i < ans.size(); i++) {
            answer[i] = ans.get(i);
        }
        return answer;
    }
}