#include <iostream>
#include <cstring>
#define MAX_SIZE 100001
using namespace std;
int g[MAX_SIZE];
bool done[MAX_SIZE], visited[MAX_SIZE];
int ans;
void dfs(int num) {
	visited[num] = true;
	
	int cur = g[num];
	if (!visited[cur]) dfs(cur);
	else if (!done[cur]) {
		for (int j = cur; j != num; j = g[j]) ans++;
		ans++;
	}
	done[num] = true;
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);
	int tc, n;
	cin >> tc;
	while (tc--) {
		cin >> n;
		ans = 0;
		memset(done, false, sizeof(done));
		memset(visited, false, sizeof(visited));
		for (int i = 1; i <= n; i++) cin >> g[i];
		for (int i = 1; i <= n; i++) if (!visited[i]) dfs(i);
		cout << n - ans << "\n";
	}
	return 0;
}
