import java.util.*;

class Solution {
    public int solution(int[] citations) {
        Integer[] cite = new Integer[citations.length];
        for (int i = 0; i < citations.length; i++)
            cite[i] = citations[i];
        
        Arrays.sort(cite, Collections.reverseOrder());
        
        int ans = 0;
        for (int i = 0; i < citations.length; i++){
            int tmp = Math.min(i + 1, cite[i]);
            ans = Math.max(ans, tmp);
        }
        return ans;
    }
}