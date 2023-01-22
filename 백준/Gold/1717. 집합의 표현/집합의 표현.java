import java.io.*;
import java.net.Inet4Address;
import java.util.*;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringBuilder sb = new StringBuilder();
    private static int v, e;
    private static int[] parent;
    private static StringTokenizer st;
    public static void main(String args[]) throws IOException {
        st = new StringTokenizer(br.readLine());
        v = Integer.parseInt(st.nextToken());
        e = Integer.parseInt(st.nextToken());
        parent = new int[v + 1];
        for(int i = 0; i < v + 1; i++) parent[i] = i;
        for(int i = 0; i < e; i++){
            st = new StringTokenizer(br.readLine());
            int c = Integer.parseInt(st.nextToken());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            if (c == 1)
                sb.append((get_parent(parent, a) == get_parent(parent, b)) ? "YES\n" : "NO\n");
            else
                union_parent(parent, a, b);
        }
        bw.write(sb.toString());
        bw.flush();
        bw.close();
        br.close();
    }

    private static int get_parent(int[] p, int x){
        if (p[x] != x){
            p[x] = get_parent(p, p[x]);
        }
        return p[x];
    }
    private static void union_parent(int[] p, int a, int b){
        a = get_parent(p, a);
        b = get_parent(p, b);
        if      (a < b) p[b] = a;
        else if (a > b) p[a] = b;
        else return;
    }
}
