import java.util.ArrayList;
import java.util.Collections;
class Solution {
    public String solution(String s) {
        String answer = "";
        ArrayList<Integer> a = new ArrayList<>();
        String[] nums = s.split(" ");
        for(String ss : nums)
            a.add(Integer.parseInt(ss));
        answer += Collections.min(a) + " " + Collections.max(a);
        return answer;
    }
}