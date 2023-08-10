import java.io.*;
import java.util.*;

public class Main {
	private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringBuilder sb = new StringBuilder();
    private static StringTokenizer st;

	private static int[] dxs = {1, 0, -1, 0}, dys = {0, 1, 0, -1};

	private static int n, m, k;
	private static final int INF = Integer.MAX_VALUE;
	private static char[][] g;
	private static int[][][] dp;
	private static int ans = INF;



	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());

		g = new char[n][m];
		dp = new int[n][m][k + 1];


		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			String cur = st.nextToken();
			for (int j = 0; j < m; j++) {
				g[i][j] = cur.charAt(j);
				for (int l = 0; l < k + 1; l++){
					dp[i][j][l] = INF;
				}
			}
		}

		dp[0][0][k] = 1;

		bfs();

		for (int i = 0; i < k + 1; i++) {
			ans = Math.min(ans, dp[n - 1][m - 1][i]);
		}

		sb.append(ans != INF ? ans : -1);
		bw.write(sb.toString());
        bw.flush();
        bw.close();
        br.close();
	}

	static boolean inRange(int x, int y) {
		return 0 <= x && x < m && 0 <= y && y < n;
	}

	static void bfs() {
		Deque<Pos> dq = new LinkedList<>();
		dq.addFirst(new Pos(0, 0, 1, k));
		while (!dq.isEmpty()) {
			Pos cur = dq.getLast();
			int x = cur.x, y = cur.y, dis = cur.dis, wall = cur.wall;
			dq.removeLast();

			for (int i = 0; i < 4; i++) {
				int nx = x + dxs[i], ny = y + dys[i];

				if (inRange(nx, ny)) {
					if (g[ny][nx] == '0' && dp[ny][nx][wall] > dis + 1) {
						dq.addFirst(new Pos(nx, ny, dis + 1, wall));
						dp[ny][nx][wall] = dis + 1;
					} else if (g[ny][nx] == '1' && wall > 0 && dp[ny][nx][wall - 1] > dis + 1) {
					if (dis % 2 == 1) {
						dq.addFirst(new Pos(nx, ny, dis + 1, wall - 1));
						dp[ny][nx][wall - 1] = dis + 1;
					} else {
						dq.addFirst(new Pos(x, y, dis + 1, wall));
					}
				}
				}
			}

		}
	}

	static class Pos{
		int x, y, dis, wall;
		Pos (int x, int y, int dis, int wall) {
			this.x = x;
			this.y = y;
			this.wall = wall;
			this.dis = dis;
		}
	}
}
