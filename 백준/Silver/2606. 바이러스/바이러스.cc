#include <iostream>
#include <vector>
using namespace std;
const int MAX = 101;
int ans = 0;
vector<int> adj[MAX];
bool visited[MAX];
void DFS(int x) {
	visited[x] = true;
	ans++;
	for (const int& elem : adj[x]) {
		if (!visited[elem])
			DFS(elem);
	}
}
int main() {
	int v, e;
	cin >> v >> e;
	for (int i = 0; i < e; i++) {
		int a, b;
		cin >> a >> b;
		adj[a].push_back(b);
		adj[b].push_back(a);
	}
	DFS(1);
	cout << ans - 1;
	return 0;
}