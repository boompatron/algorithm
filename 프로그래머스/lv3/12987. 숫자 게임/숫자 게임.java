import java.util.*;


class Solution {
    public int solution(int[] A, int[] B) {
        Arrays.sort(A);
        Arrays.sort(B);
        int idx = A.length - 1;
        int cnt = 0;
        
        for (int i = A.length - 1; i > -1; i--){
            if (A[i] < B[idx]){
                cnt++;
                idx--;
            }
        }
        
        return cnt;
    }
}