import java.util.Arrays;
import java.util.Comparator;
class Solution {
    public String solution(int[] numbers) {
        String[] strings = new String[numbers.length];
        for(int i = 0; i < numbers.length; i++){
            strings[i] = Integer.toString(numbers[i]);
        }
        Arrays.sort(strings, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                return (o2 + o1).compareTo(o1 + o2);
            }
        });
        if(strings[0].equals("0")) return "0";
        String ans = "";
        for(String s : strings) ans += s;
        return ans;
    }
}