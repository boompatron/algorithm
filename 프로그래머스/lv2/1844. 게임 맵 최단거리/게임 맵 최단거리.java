import java.util.Deque;
import java.util.LinkedList;
class Solution {
    private static int[] dxs = {1, -1, 0, 0}, dys = {0, 0, 1, -1};
    private static int n, m;
    private static int[][] distance;

    private static boolean inRange(int x, int y){
        return 0 <= x && x < m && 0 <= y && y < n;
    }
    public int solution(int[][] maps) {
        n = maps.length; m = maps[0].length;
        distance = new int[n][m];
        for(int i = 0; i < n; i++) for(int j = 0; j < m; j++) distance[i][j] = Integer.MAX_VALUE;

        Deque<Pos> dq = new LinkedList<>();
        dq.add(new Pos(0, 0, 1));

        while(!dq.isEmpty()){
            Pos cur = dq.pop();
            for(int i = 0; i < 4; i++){
                int nx = cur.x + dxs[i], ny = cur.y + dys[i];
                if(inRange(nx, ny) && maps[ny][nx] == 1 && distance[ny][nx] > cur.dis + 1){
                    distance[ny][nx] = cur.dis + 1;
                    dq.add(new Pos(nx, ny, cur.dis + 1));
                }
            }
        }

        return distance[n - 1][m - 1] != Integer.MAX_VALUE ? distance[n - 1][m - 1] : -1;
    }
}
class Pos{
    public int x, y, dis;
    public Pos(int x, int y, int dis){
        this.x = x;
        this.y = y;
        this.dis = dis;
    }
}