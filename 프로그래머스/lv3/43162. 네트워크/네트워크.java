import java.util.*;

class Solution {
    int[] parent;
    
    public int solution(int n, int[][] computers) {
        parent = new int[n];
        for (int i = 0; i < n; i++)
            parent[i] = i;
        
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++){
                if (computers[i][j] == 1)
                    unionParent(i, j);
            }
        }
        
                    
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < n; i++){
            set.add(getParent(i));
        }
        return set.size();
    }
    
    int getParent(int x){
        if (parent[x] != x)
            parent[x] = getParent(parent[x]);
        return parent[x];
    }
    
    void unionParent(int a, int b){
        a = getParent(a);
        b = getParent(b);
        if (a > b)
            parent[a] = b;
        else if (a < b)
            parent[b] = a;
        else
            return;
    }
}