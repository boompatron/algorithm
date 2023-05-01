import java.util.*;

public class Solution {
    public int[] solution(int []arr) {
        List<Integer> ans = new ArrayList<>();
        Stack<Integer> stack = new Stack<>();

        stack.push(arr[0]);
        ans.add(arr[0]);

        for (int i = 1; i < arr.length; i++) {
            if (stack.peek() != arr[i]){
                ans.add(arr[i]);
            }
            stack.push(arr[i]);
        }

        int[] answer = new int[ans.size()];
        for (int i = 0; i < ans.size(); i++) {
            answer[i] = ans.get(i);
        }

        return answer;
    }
}