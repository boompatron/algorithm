import java.util.*;

class Solution {
    public int solution(String begin, String target, String[] words) {
        Map<String, ArrayList<String>> adj = new HashMap<>();
        int n = words.length, m = words[0].length();
        
        adj.put(begin, new ArrayList<String>());
        
        boolean isTargetIn = false;
        
        for (String word: words){
            adj.put(word, new ArrayList<String>());
            int tmp = 0;
            
            for (int i = 0; i < m; i++){
                if (begin.charAt(i) != word.charAt(i)) tmp ++;
            }
            if (tmp == 1)
                adj.get(begin).add(word);
            if (word.equals(target))
                isTargetIn = true;
        }
        
        if (!isTargetIn)
            return 0;
        
        
        for (int i = 0; i < n; i++){
            for (int j = i + 1; j < n; j++){             
                int cnt = 0;
                for (int k = 0; k < m; k++){
                    if (words[i].charAt(k) != words[j].charAt(k))
                        cnt++;
                }
                if (cnt == 1){
                    adj.get(words[i]).add(words[j]);
                    adj.get(words[j]).add(words[i]);
                }
            }
        }
        
        for(String key: adj.keySet()){
            System.out.print("key : " + key + ", values : ");
            for (String value: adj.get(key)){
                System.out.print(value + ", ");
            }
            System.out.println();
        }
        
        int ans = n + 1;
        Deque<Pos> dq = new LinkedList<>();
        Set<String> visited = new HashSet<>();
        dq.add(new Pos(begin, 0));
        visited.add(begin);
        
        while (!dq.isEmpty()){
            Pos cur = dq.poll();
            System.out.println("cur : " + cur.s + ", " + cur.n);
            
            if (target.equals(cur.s))
                ans = Math.min(ans, cur.n);

            
            for (String word: adj.get(cur.s)){
                if (!visited.contains(word)){
                    dq.add(new Pos(word, cur.n + 1));
                    visited.add(word);
                }
            }
        }
        
        return ans;
    }
}

class Pos{
    String s;
    int n;
    public Pos(String s, int n){
        this.s = s;
        this.n = n;
    }
}