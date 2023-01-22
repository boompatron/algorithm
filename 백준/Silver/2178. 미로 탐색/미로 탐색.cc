#include <iostream>
#include <queue>
#include <utility>
#define INF 123456789
using namespace std;
int n, m;
int dxs[4] = { 1, -1, 0, 0 }, dys[4] = { 0, 0, 1, -1 };
char g[101][101];
int maze[101][101];
bool inRange(int a, int b) { return 0 <= a && a < m && 0 <= b && b < n; }
void bfs() {
	queue<pair<int, int>> q;
	q.push(make_pair(0, 0));
	maze[0][0] = 0;
	while (!q.empty()) {
		int x = q.front().first, y = q.front().second;
		q.pop();
		for (int dir = 0; dir < 4; dir++) {
			int nx = x + dxs[dir], ny = y + dys[dir];
			if (inRange(nx, ny) && g[ny][nx] == '1' && maze[y][x] + 1 < maze[ny][nx] ) {
				q.push(make_pair(nx, ny));
				maze[ny][nx] = maze[y][x] + 1;
			}
		}
	}

}
int main() {
	cin >> n >> m;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> g[i][j];
			maze[i][j] = INF;
		}
	}
	bfs();
	cout << maze[n - 1][m - 1] + 1;
	return 0;
}