import java.io.*;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;
    private static StringBuilder sb = new StringBuilder();
    private static boolean[][] visited;
    private static int[][] g;
    private static int[] dxs = {1, -1, 0, 0}, dys = {0, 0, 1, -1};
    private static int n, m, wall = 0;
    public static void main(String args[]) throws IOException {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        g = new int[n][m];
        visited = new boolean[n][m];

        for(int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < m; j++){
                g[i][j] = Integer.parseInt(st.nextToken());
                if(g[i][j] == 1) wall++;
            }
        }
        int virus = Integer.MAX_VALUE;
        for(int first = 0; first < n * m; first++){
            int fX = first % m, fY = first / m;
            if (g[fY][fX] != 0) continue;
            for(int second = first + 1; second < n * m; second++){
                int sX = second % m, sY = second / m;
                if (g[sY][sX] != 0) continue;
                for(int third = second + 1; third < n * m; third++){
                    int tX = third % m, tY = third / m;
                    if (g[tY][tX] != 0) continue;

                    int tmp = 0;
                    clearVisited();
                    g[fY][fX] = g[sY][sX] = g[tY][tX] = 1;
                    for(int i = 0; i < n; i++){
                        for(int j = 0; j < m; j++){
                            if (g[i][j] == 2 && !visited[i][j])
                                tmp += spreadVirus(j, i);
                        }
                    }
                    virus = Math.min(virus, tmp);
                    g[fY][fX] = g[sY][sX] = g[tY][tX] = 0;
                }
            }
        }
        int ans = n * m - (wall + 3) - virus;
        sb.append(ans).append('\n');
        bw.write(sb.toString());
        bw.flush();
        bw.close();
        br.close();
    }
    private static int spreadVirus(int x, int y){
        int size = 1;
        Queue<Pos> q = new LinkedList<>();
        q.add(new Pos(x, y));
        visited[y][x] = true;
        while(!q.isEmpty()){
            Pos cur = q.poll();
            for(int dir = 0; dir < 4; dir++){
                int nx = cur.x + dxs[dir], ny = cur.y + dys[dir];
                if(inRange(nx, ny) && g[ny][nx] == 0 && !visited[ny][nx]){
                    size++;
                    visited[ny][nx] = true;
                    q.add(new Pos(nx, ny));
                }
            }
        }
        return size;
    }
    private static void clearVisited(){
        for(int i = 0; i < n; i++)
            for(int j = 0; j < m; j++)
                visited[i][j] = false;
    }
    private static boolean inRange(int x, int y){
        return 0 <= x && x < m && 0 <= y && y < n;
    }
}
class Pos{
    public int x, y;
    public Pos(int x, int y){
        this.x = x;
        this.y = y;
    }
}