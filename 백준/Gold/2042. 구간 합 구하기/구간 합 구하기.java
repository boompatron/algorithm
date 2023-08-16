import java.io.*;
import java.util.*;

public class Main {
	private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    private static StringBuilder sb = new StringBuilder();
    private static StringTokenizer st;


	private static int n, m, k;
	private static long[] g;
	private static long[] tree;

	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		k = Integer.parseInt(st.nextToken());

		g = new long[n + 1];
		tree = new long[n * 4];

		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			g[i] = Long.parseLong(st.nextToken());
		}

		init_tree(0, n - 1, 1);

		for (int i = 0; i < m + k; i++) {
			int a, b;
			long c;
			st = new StringTokenizer(br.readLine());
			a = Integer.parseInt(st.nextToken());
			b = Integer.parseInt(st.nextToken());
			c = Long.parseLong(st.nextToken());

			if (a == 1) {
				long diff = c - g[b - 1];
				g[b - 1] = c;
				update_tree(0, n - 1, 1, b - 1, diff);
			} else {
				sb.append(prefix_sum(0, n - 1, 1, b - 1, (int)(c - 1)));
				sb.append("\n");
			}
		}

		bw.write(sb.toString());
        bw.flush();
        bw.close();
        br.close();
	}

	static long init_tree(int start, int end, int node){
		if (start == end){
			tree[node] = g[start];
			return tree[node];
		}
		int mid = (start + end) / 2;
		tree[node] = init_tree(start, mid, node * 2) + init_tree(mid + 1, end, node * 2 + 1);
		return tree[node];
	}

	static long prefix_sum(int start, int end, int node, int left, int right) {
		if (left > end || right < start) return 0;

		if (left <= start && end <= right) return tree[node];

		int mid = (start + end ) / 2;

		return prefix_sum(start, mid, node * 2, left, right) + prefix_sum(mid + 1, end, node * 2 + 1, left, right);
	}

	static void update_tree(int start, int end, int node, int index, long diff) {
		if (index > end || index < start) return;
		tree[node] += diff;

		if (start == end) return;

		int mid = (start + end) / 2;
		update_tree(start, mid, node * 2, index, diff);
		update_tree(mid + 1, end, node * 2 + 1, index, diff);
	}
}
