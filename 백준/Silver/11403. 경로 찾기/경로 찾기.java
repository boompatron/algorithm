import java.io.*;
import java.util.*;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringTokenizer st;
    private static StringBuilder sb = new StringBuilder();

    private static int v, tmp;
    private static boolean[][] g;
    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        v = Integer.parseInt(st.nextToken());
        g = new boolean[v][v];

        for(int i = 0; i < v; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < v; j++){
                tmp = Integer.parseInt(st.nextToken());
                g[i][j] = tmp == 1 ? true : false;
            }
        }

        floydWarshall();

        for(int i = 0; i < v; i++){
            for(int j = 0; j < v; j++){
                sb.append(g[i][j] ? 1 : 0).append(" ");
            }
            sb.append("\n");
        }

        bw.write(sb.toString());
        bw.flush();
        bw.close();
        br.close();
    }
    private static void floydWarshall(){
        for(int k = 0; k < v; k++){
            for(int i = 0; i < v; i++){
                for(int j = 0; j < v; j++){
                    if (g[i][k] && g[k][j])
                        g[i][j] = true;
                }
            }
        }
    }
}