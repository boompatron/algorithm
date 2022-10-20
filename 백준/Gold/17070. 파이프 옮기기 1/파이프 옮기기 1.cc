#include <iostream>
using namespace std;
bool g[17][17];
int n, tmp, i = 0, j = 0, ans = 0;
void dfs(int x, int y, int d) {
	if (x == n - 1 && y == n - 1) {
		ans++;
		return;
	}
	if (d == 0 || d == 1) if (x + 1 < n) if (g[y][x + 1]) dfs(x + 1, y, 0);
	if (d == 2 || d == 1) if (y + 1 < n) if (g[y + 1][x]) dfs(x, y + 1, 2);
	if (x + 1 < n && y + 1 < n) if (g[y + 1][x + 1] && g[y + 1][x] && g[y][x + 1]) dfs(x + 1, y + 1, 1);
}
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	cin >> n;

	for (i = 0; i < n; i++) {
		for (j = 0; j < n; j++) {
			cin >> tmp;
			g[i][j] = (tmp == 0) ? true : false;
		}
	}
	dfs(1, 0, 0);
	cout << ans << "\n";
	return 0;
}