import java.util.*;

class Solution {
    public int solution(int n, int[][] edge) {
        Map<Integer, ArrayList<Integer>> adj = new HashMap<>();
        
        for (int i = 0; i <= n; i++){
            
            adj.put(i, new ArrayList<Integer>());
        }
        
        for (int[] e: edge){
            adj.get(e[0]).add(e[1]);
            adj.get(e[1]).add(e[0]);
        }
        
        Deque<Coord> dq = new LinkedList<>();
        int[] visited = new int[n + 1];
        
        for (int i = 2; i <= n; i++)
            visited[i] = n + 1;
        visited[0] = 0;
        visited[1] = 0;
        
        dq.add(new Coord(1, 0));
        
        while (!dq.isEmpty()){
            Coord cur = dq.poll();
            for (Integer next: adj.get(cur.a)){
                if (visited[next] > cur.b + 1){
                    visited[next] = cur.b + 1;
                    dq.add(new Coord(next, cur.b + 1));
                }
            }   
        }
        
        int cnt = 0;
        int maxValue = Arrays.stream(visited).max().getAsInt();
    
        
        // for (int i = 0; i <= n; i++){
        //     System.out.println(i + ", " + visited[i]);
        // }
        
        for (int distance: visited){
            if (distance == maxValue)
                cnt++;
        }   
        
        return cnt;
    }
}

class Coord{
    int a;
    int b;
    public Coord(int a, int b){
        this.a = a;
        this.b = b;
    }
}