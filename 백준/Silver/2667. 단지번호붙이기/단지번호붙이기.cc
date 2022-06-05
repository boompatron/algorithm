#include <iostream>
#include <queue>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;
int dxs[4] = { 1, -1, 0, 0 }, dys[4] = { 0, 0, 1, -1 };
int n;
char g[26][26];
bool visited[26][26];
bool inRange(int a, int b) { return 0 <= a && a < n && 0 <= b && b < n; }
int bfs(int a, int b) {
	int size = 1;
	queue<pair<int, int>> q;
	q.push(make_pair(a, b));
	visited[b][a] = true;
	while (!q.empty()) {
		int x = q.front().first, y = q.front().second;
		q.pop();
		for (int dir = 0; dir < 4; dir++) {
			int nx = x + dxs[dir], ny = y + dys[dir];
			if (inRange(nx, ny) && !visited[ny][nx] && g[ny][nx] == '1') {
				size++;
				visited[ny][nx] = true;
				q.push(make_pair(nx, ny));
			}
		}
	}
	return size;
}
int main() {
	vector<int> ans;
	cin >> n;
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++)
			cin >> g[i][j];
	}
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < n; j++) {
			if (g[i][j] == '1' && !visited[i][j])
				ans.push_back(bfs(j, i));
		}
	}
	sort(ans.begin(), ans.end());
	cout << ans.size() << endl;
	for (const int& elem : ans)
		cout << elem << "\n";
	return 0;
}