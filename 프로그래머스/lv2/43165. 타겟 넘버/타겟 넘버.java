import java.util.*;

class Solution {
    int[] nums;
    int cnt = 0, len = 0, t;
    public int solution(int[] numbers, int target) {
        nums = numbers;
        len = numbers.length;
        t = target;
        
        // for (int num: nums)
        //     System.out.println(num);
        // System.out.println(cnt);
        // System.out.println(len);
        // System.out.println(t);
        dfs(0, 0);
        
        return cnt;
    }
    public void dfs(int n, int cur){
        if (n == len){
            if (cur == t){
                cnt++;
            }
            return;
        }
        dfs(n + 1, cur + nums[n]);
        dfs(n + 1, cur - nums[n]);
    }
}