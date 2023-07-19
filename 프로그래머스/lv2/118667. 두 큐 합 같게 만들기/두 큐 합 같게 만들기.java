import java.util.*;

class Solution {
    public int solution(int[] queue1, int[] queue2) {
        Deque<Long> dq1 = new LinkedList<>();
        Deque<Long> dq2 = new LinkedList<>();
        int cnt = 0;
        long sum1 = 0, sum2 = 0;
        for(int i = 0; i < queue1.length; i++){
            dq1.addLast((long)queue1[i]);
            dq2.addLast((long)queue2[i]);
            sum1 += queue1[i];
            sum2 += queue2[i];
        }
        for(int i = 0; i < queue1.length * 3; i++){
            if(sum1 == sum2)
                return cnt;
            else if(sum1 > sum2){
                long tmp = dq1.pollFirst();
                dq2.addLast(tmp);
                sum1 -= tmp;
                sum2 += tmp;
            }
            else{
                long tmp = dq2.pollFirst();
                dq1.addLast(tmp);
                sum2 -= tmp;
                sum1 += tmp;
            }
            cnt++;
        }
        return -1;
    }
}