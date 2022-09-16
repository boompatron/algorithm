class Solution {
    private static int cnt = 1;
    public int solution(int n) {
        int end = 1, partial_sum = 0;
        for(int start= 1; start < n; start++){
            while(end < n && partial_sum < n) partial_sum += end++;
            if(partial_sum == n) cnt++;
            partial_sum -= start;
        }
        return cnt;
    }
}