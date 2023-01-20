import java.io.*;
import java.util.*;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;
    private static StringBuilder sb = new StringBuilder();

    private static ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
    private static int v, e, start;
    private static boolean[] visited;
    public static void main(String args[]) throws IOException {
        st = new StringTokenizer(br.readLine());
        v = Integer.parseInt(st.nextToken());
        e = Integer.parseInt(st.nextToken());
        start = Integer.parseInt(st.nextToken());
        visited = new boolean[v + 1];
        for(int i = 0; i < v + 1; i++)
            adj.add(new ArrayList<>());
        for(int i = 0; i < e; i++){
            st = new StringTokenizer(br.readLine());
            int a, b;
            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());
            adj.get(a).add(b);
            adj.get(b).add(a);
        }
        for(int i = 0; i < v + 1; i++)
            Collections.sort(adj.get(i));

        clearVisited();
        DFS(start);
        clearVisited();
        BFS(start);
        bw.write(sb.toString());

        bw.flush();
        bw.close();
        br.close();
    }
    private static void clearVisited(){
        for(int i = 0; i < v + 1; i++)
            visited[i] = false;
    }
    private static void BFS(int start){
        sb.append("\n");
        Queue<Integer> q = new LinkedList<>();
        q.add(start);
        sb.append(start + " ");
        visited[start] = true;
        while(!q.isEmpty()) {
            int cur = q.poll();
            for (Integer idx : adj.get(cur)) {
                if (!visited[idx]) {
                    q.add(idx);
                    visited[idx] = true;
                    sb.append(idx + " ");
                }
            }
        }
    }
    private static void DFS(int idx){
        visited[idx] = true;
        sb.append(idx + " ");
        for(Integer n: adj.get(idx)){
            if(!visited[n])
                DFS(n);
        }
    }
}