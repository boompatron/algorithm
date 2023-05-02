import java.util.*;

class Solution {
    public int[] solution(String[] operations) {
        PriorityQueue<Integer> minPq = new PriorityQueue<>();
        PriorityQueue<Integer> maxPq = new PriorityQueue<>(Collections.reverseOrder());
        Set<Integer> deleted = new HashSet<>();
        int[] answer = {0, 0};

        for (String operation: operations){
            String[] inst = operation.split(" ");
            int num = Integer.parseInt(inst[1]);

            if (inst[0].equals("D")){
                if (num == 1){
                    while (!maxPq.isEmpty() && deleted.contains(maxPq.peek()))
                        maxPq.poll();
                    if (!maxPq.isEmpty()) {
                        deleted.add(maxPq.poll());
                    }
                } else {
                    while (!minPq.isEmpty() && deleted.contains(minPq.peek()))
                        minPq.poll();
                    if (!maxPq.isEmpty()) {
                        deleted.add(minPq.poll());
                    }
                }
            } else {
                maxPq.add(num);
                minPq.add(num);
            }
        }

        while (!maxPq.isEmpty() && deleted.contains(maxPq.peek()))
            maxPq.poll();
        while (!minPq.isEmpty() && deleted.contains(minPq.peek()))
            minPq.poll();

        answer[0] = maxPq.isEmpty() ? 0 : maxPq.peek();
        answer[1] = minPq.isEmpty() ? 0 : minPq.peek();
        return answer;
    }
}
