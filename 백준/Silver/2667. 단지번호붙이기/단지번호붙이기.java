import java.io.*;
import java.nio.file.Path;
import java.util.*;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringBuilder sb = new StringBuilder();
    private static int n;
    private static int[] dxs = {1, -1, 0, 0}, dys = {0, 0, 1, -1};
    private static char[][] g;
    private static boolean[][] visited;
    private static StringTokenizer st;
    public static void main(String args[]) throws IOException {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        g = new char[n][n];
        visited = new boolean[n][n];
        for(int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());
            String s = st.nextToken();
            for(int j = 0; j < n; j++) {
                g[i][j] = s.charAt(j);
                visited[i][j] = false;
            }
        }
        int cnt = 0;
        ArrayList<Integer> ai = new ArrayList<>();
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(g[i][j] == '1' && !visited[i][j]){
                    cnt++;
                    ai.add(BFS(j, i));
                }
            }
        }
        sb.append(cnt + "\n");
        Collections.sort(ai);
        Iterator itr = ai.iterator();
        while(itr.hasNext()) sb.append(itr.next() + "\n");
        bw.write(sb.toString());
        bw.flush();
        bw.close();
        br.close();
    }
    private static int BFS(int x, int y){
        int size = 1;
        Queue<Pair> q = new LinkedList<>();
        q.add(new Pair(x, y));
        visited[y][x] = true;
        while(!q.isEmpty()){
            Pair curPair = q.poll();
            int a = curPair.first();
            int b = curPair.second();

            for(int dir = 0; dir < 4; dir++){
                int nx = a + dxs[dir], ny = b + dys[dir];
                if (inRange(nx, ny) && g[ny][nx] == '1' && !visited[ny][nx]){
                    size++;
                    q.add(new Pair(nx, ny));
                    visited[ny][nx] = true;
                }
            }

        }
        return size;
    }
    private static boolean inRange(int x, int y){
        return 0 <= x && x < n && 0 <= y && y < n;
    }
}
class Pair{
    Integer x, y;
    public Pair(int x, int y){
        this.x = x;
        this.y = y;
    }
    public Integer first(){
        return this.x;
    }
    public Integer second(){
        return this.y;
    }
}
