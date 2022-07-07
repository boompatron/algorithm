#include <iostream>
#include <vector>
using namespace std;
const int MAX = 1002;
bool visited[MAX];
vector<int> adj[MAX];
void DFS(int n) {
	visited[n] = true;
	for (const int& elem : adj[n]) {
		if (!visited[elem])
			DFS(elem);
	}
}
int main() {
	int v, e, ans = 0;
	cin >> v >> e;
	for (int i = 0; i < e; i++) {
		int tmp1, tmp2;
		cin >> tmp1 >> tmp2;
		adj[tmp1].push_back(tmp2);
		adj[tmp2].push_back(tmp1);
	}
	for (int i = 1; i <= v; i++) {
		if (!visited[i]) {
			DFS(i);
			ans++;
		}
	}
	cout << ans;
	return 0;
}