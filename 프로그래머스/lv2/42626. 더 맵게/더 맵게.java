import java.util.*;


class Solution {
    public int solution(int[] scoville, int k) {
        int cnt = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int s: scoville){
            pq.add(s);
        }
        
        while (pq.peek() < k) {
            if (pq.size() < 2)
                return -1;
            cnt++;
            int a = pq.poll();
            int b = pq.poll();
            
            pq.add(a + (b * 2));
        }
        return cnt;
    }
}