import java.io.*;
import java.util.*;

public class Main {
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringBuilder sb = new StringBuilder();
    private static StringTokenizer st;
    private static String s1, s2;
    private static int[][] g;
    public static void main(String args[]) throws IOException {
        st = new StringTokenizer(br.readLine());
        s1 = st.nextToken();
        st = new StringTokenizer(br.readLine());
        s2 = st.nextToken();
        g = new int[s1.length() + 1][s2.length() + 1];
        for(int i = 0; i < s1.length() + 1; i++)
            for (int j = 0; j < s2.length() + 1; j++)
                g[i][j] = 0;
        lcs();
        sb.append(g[s1.length()][s2.length()]).append('\n');
        bw.write(sb.toString());
        bw.flush();
        bw.close();
        br.close();
    }

    private static void lcs(){
        for(int i = 1; i < s1.length() + 1; i++){
            for(int j = 1; j < s2.length() + 1; j++){
                if (s2.charAt(j - 1) == s1.charAt(i - 1))
                    g[i][j] = g[i - 1][j  - 1] + 1;
                else
                    g[i][j] = Math.max(g[i - 1][j], g[i][j - 1]);
            }
        }
    }
}
