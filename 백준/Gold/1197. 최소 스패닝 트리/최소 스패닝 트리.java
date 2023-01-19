import java.io.*;
import java.util.*;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;
    private static int v, e, ans = 0, i;
    private static int[] parent;
    private static PriorityQueue<Edge> pq;
    private static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        v = Integer.parseInt(st.nextToken());
        e = Integer.parseInt(st.nextToken());
        parent = new int[v + 1];
        pq = new PriorityQueue<>();
        for(i = 0; i < v + 1; i++)
            parent[i] = i;
        for(i = 0; i < e; i++){
            int a, b, c;
            st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            c = Integer.parseInt(st.nextToken());
            pq.add(new Edge(a, b, c));
        }
        while(!pq.isEmpty()){
            Edge cur = pq.poll();
            if(getParent(cur.a) != getParent(cur.b)){
                unionParent(cur.a, cur.b);
                ans += cur.c;
            }
        }
        sb.append(ans);
        bw.write(sb.toString());
        bw.flush();
        bw.close();
        br.close();
    }
    private static int getParent(int x){
        if(parent[x] != x)
            parent[x] = getParent(parent[x]);
        return parent[x];
    }
    private static void unionParent(int a, int b){
        a = getParent(a);
        b = getParent(b);
        if(a < b)       parent[b] = a;
        else if(a > b)  parent[a] = b;
    }
}
class Edge implements Comparable<Edge>{
    int a, b, c;
    public Edge(int a, int b, int c){
        this.a = a;
        this.b = b;
        this.c = c;
    }
    @Override
    public int compareTo(Edge e){
        return this.c > e.c ? 1 : -1;
    }
}