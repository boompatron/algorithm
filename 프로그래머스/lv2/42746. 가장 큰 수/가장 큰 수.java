import java.util.*;

class Solution {
    public String solution(int[] numbers) {
        String[] tmp = new String[numbers.length];
        
        for (int i = 0; i < numbers.length; i++) {
            tmp[i] = Integer.toString(numbers[i]);
        }
        
        Arrays.sort(tmp, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return (o2 + o1).compareTo(o1 + o2);
            }
        });
        
        if (tmp[0].equals("0")) return "0";
        
        StringBuilder answer = new StringBuilder();
        
        for (String t: tmp) answer.append(t);
        return answer.toString();
    }
}
