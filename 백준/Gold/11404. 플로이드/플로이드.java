import java.io.*;
import java.util.*;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringBuilder sb = new StringBuilder();
    private static StringTokenizer st;
    private static int[][] g;
    private static int v, e;
    public static void main(String args[]) throws IOException {
        st = new StringTokenizer(br.readLine());
        v = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        e = Integer.parseInt(st.nextToken());
        g = new int[v + 1][v + 1];
        for(int i = 1; i < v + 1; i++)
            for(int j = 1; j < v + 1; j++)
                g[i][j] = i == j ? 0 : Integer.MAX_VALUE / 3;

        for(int i = 0; i < e; i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            g[a][b] = Math.min(g[a][b], c);
        }
        floydWarshall();
        printG();
        bw.write(sb.toString());
        bw.flush();
        bw.close();
        br.close();
    }
    private static void floydWarshall(){
        for(int k = 1; k < v + 1; k++)
            for(int i = 1; i < v + 1; i++)
                for(int j = 1; j < v + 1; j++)
                    g[i][j] = Math.min(g[i][j], g[i][k] + g[k][j]);
    }
    private static void printG(){
        for(int i = 1; i < v + 1; i++){
            for(int j = 1; j < v + 1; j++){
                sb.append(g[i][j] != Integer.MAX_VALUE / 3 ? g[i][j] : 0).append(' ');
            }
            sb.append('\n');
        }
    }
}
