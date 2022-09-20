import java.io.*;
import java.util.*;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
     private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
     private static ArrayList<ArrayList<Edge>> adj = new ArrayList<>();
     private static StringBuilder sb = new StringBuilder();
    private static int v, e, s;
    private static StringTokenizer st;
    public static void main(String args[]) throws IOException {
        st = new StringTokenizer(br.readLine());
        v = Integer.parseInt(st.nextToken());
        e = Integer.parseInt(st.nextToken());
        for(int i = 0; i < v + 1; i++)
            adj.add(new ArrayList<>());
        int[] ans = new int[v + 1];
        for(int i = 0; i < v + 1; i++) ans[i] = Integer.MAX_VALUE;

        st = new StringTokenizer(br.readLine());
        s = Integer.parseInt(st.nextToken());
        for(int i = 0; i < e; i++){
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            adj.get(u).add(new Edge(v, w));
        }
        dijkstra(ans);
        for(int i = 1; i < v + 1; i++)
            sb.append(ans[i] == Integer.MAX_VALUE ? "INF" : ans[i]).append("\n");

        bw.write(sb.toString());
        bw.flush();
        bw.close();
        br.close();
    }

    private static void dijkstra(int[] ansList){
        ansList[s] = 0;
        Queue<Edge> pq = new PriorityQueue<>();
        pq.add(new Edge(0, s));
        while(!pq.isEmpty()){
            Edge cur = pq.poll();
            int dis = cur.first, cur_idx = cur.second;
            if(ansList[cur_idx] < dis) continue;
            for(Edge e : adj.get(cur_idx)){
                int next_idx = e.first, next_dis = e.second + dis;
                if(next_dis < ansList[next_idx]){
                    ansList[next_idx] = next_dis;
                    pq.add(new Edge(next_dis, next_idx));
                }
            }
        }
    }
    private static class Edge implements Comparable<Edge>{
        private int first, second;

        public Edge(int first, int second){
            this.first = first;
            this.second = second;
        }
        @Override
        public int compareTo(Edge target){
            return Integer.compare(this.first, target.first);
        }
    }
}

