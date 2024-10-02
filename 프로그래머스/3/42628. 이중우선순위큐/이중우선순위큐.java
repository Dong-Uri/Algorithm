import java.util.PriorityQueue;
import java.util.Collections;
import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(String[] operations) {
        int[] answer = {0, 0};
        PriorityQueue <Integer> minHeap = new PriorityQueue<>();
        PriorityQueue <Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        for (String oper : operations) {
            String[] opers = oper.split(" ");
            if (opers[0].equals("I")) {
                Integer num = Integer.parseInt(opers[1]);
                maxHeap.add(num);
                minHeap.add(num);
            }
            else if (opers[1].equals("1") && !maxHeap.isEmpty()) {
                Integer num = maxHeap.poll();
                minHeap.remove(num);
            }
            else if (!minHeap.isEmpty()) {
                Integer num = minHeap.poll();
                maxHeap.remove(num);
            }
        }
        if (!maxHeap.isEmpty()) {
            answer[0] = maxHeap.poll();
        }
        if (!minHeap.isEmpty()) {
            answer[1] = minHeap.poll();
        }
        return answer;
    }
}