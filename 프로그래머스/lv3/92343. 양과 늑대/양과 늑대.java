class Solution {
    boolean[] visited;
    int[] i;
    int[][] e;
    int ans = -1, n = 0;
    public int solution(int[] info, int[][] edges) {
        n = info.length;
        visited = new boolean[n];
        e = new int[edges.length][];
		for (int i = 0; i < n; i++) visited[i] = false;

		i = info.clone();
        for (int i = 0; i < edges.length; i++) e[i] = edges[i].clone();

		visited[0] = true;
		dfs(1, 0);

        return ans;
    }

    void dfs(int sheep, int wolf) {
        if (sheep > wolf) ans = Math.max(ans, sheep);
        else return;

        for (int[] next: e){
            if (visited[next[0]] && !visited[next[1]]) {
                visited[next[1]] = true;

                if (i[next[1]] == 0)    dfs(sheep + 1, wolf);
                else                    dfs(sheep, wolf + 1);

                visited[next[1]] = false;
            }
        }
    }
}