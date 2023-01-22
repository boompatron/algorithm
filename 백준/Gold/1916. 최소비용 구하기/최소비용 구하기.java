import java.io.*;
import java.util.*;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;
    private static StringBuilder sb = new StringBuilder();
    private static PriorityQueue<Edge> pq = new PriorityQueue<>();

    private static ArrayList<ArrayList<Edge>> adj = new ArrayList<>();
    private static int v, e, v1, v2;
//    private static int[][] ans;
    private static int[] ans;

    public static void main(String args[]) throws IOException {
        st = new StringTokenizer(br.readLine());
        v = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        e = Integer.parseInt(st.nextToken());

        for(int i = 0; i < v + 1; i++)
            adj.add(new ArrayList<>());
//        ans = new int[3][v + 1];
        ans = new int[v + 1];
        for(int i = 1; i < v + 1; i++)
            ans[i] = Integer.MAX_VALUE;

        for(int i = 0; i < e; i++){
            st = new StringTokenizer(br.readLine());
            int a, b, c;
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            c = Integer.parseInt(st.nextToken());

            adj.get(a).add(new Edge(b, c));
            // adj.get(b).add(new Edge(a, c));
        }
        st = new StringTokenizer(br.readLine());
        v1 = Integer.parseInt(st.nextToken());
        v2 = Integer.parseInt(st.nextToken());

        dijkstra(ans, v1);
        sb.append(ans[v2]);

        bw.write(sb.toString());

        bw.flush();
        bw.close();
        br.close();
    }
    private static void dijkstra(int[] ans, int start){
        ans[start] = 0;
        pq.add(new Edge(0, start));
        while(!pq.isEmpty()){
            Edge cur = pq.poll();
            if(ans[cur.y] < cur.x) continue;
            for(Edge e :adj.get(cur.y)){
                int next_idx = e.x, next_dis = e.y + cur.x;
                if(ans[next_idx] > next_dis){
                    ans[next_idx] = next_dis;
                    pq.add(new Edge(next_dis, next_idx));
                }
            }
        }
    }
}
class Edge implements Comparable<Edge>{
    int x, y;
    public Edge(int x, int y){
        this.x = x;
        this.y = y;
    }

    @Override
    public int compareTo(Edge target){
        return this.x > target.x ? 1 : -1;
    }
}