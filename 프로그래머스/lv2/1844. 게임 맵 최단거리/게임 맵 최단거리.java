import java.util.*;

class Solution {
    int[] dxs = {1, -1, 0, 0}, dys = {0, 0, 1, -1};
    int n, m;
    
    public boolean inRange(int x, int y){
        return 0 <= x && x < m && 0 <= y && y < n;
    }
    
    public int solution(int[][] maps) {
        n = maps.length;
        m = maps[0].length;
        
        int[][] visited = new int[n][m];
        for (int i = 0; i < n; i++){
            for (int j = 0; j < m; j++)
                visited[i][j] = n * m + 1;
        }
        
        Deque<Pos> dq = new LinkedList<>();
        dq.addFirst(new Pos(0, 0, 1));
        
        while (!dq.isEmpty()){
            Pos cur = dq.poll();
            for (int i = 0; i < 4; i++){
                int nx = cur.x + dxs[i];
                int ny = cur.y + dys[i];
                int nz = cur.z + 1;
                
                if (inRange(nx, ny) && maps[ny][nx] == 1 && visited[ny][nx] > nz){
                    dq.add(new Pos(nx, ny, nz));
                    visited[ny][nx] = nz;
                }
            }
        }
        
        
        
        return visited[n - 1][m - 1] == n * m + 1 ? -1 : visited[n - 1][m - 1];
    }
}

class Pos{
    public int x;
    public int y;
    public int z;
    public Pos(int x, int y, int z){
        this.x = x;
        this.y = y;
        this.z = z;
    }
}