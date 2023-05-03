import java.util.*;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        List<Integer> ans = new ArrayList<>();
        
        
        for (int[] command: commands) {
            int[] tmp = new int[command[1] - command[0] + 1];
            for (int i = 0; i < command[1] - command[0] + 1; i++){
                tmp[i] = array[i + command[0] - 1];
            }
            
            Arrays.sort(tmp);
            ans.add(tmp[command[2] - 1]);
        }
        return ans.stream().mapToInt(i -> i).toArray();
    }
}