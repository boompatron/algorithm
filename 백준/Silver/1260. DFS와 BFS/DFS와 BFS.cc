#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <queue>
using namespace std;
const int MAX = 1001;
bool visited[MAX];
vector<int> adj[MAX];
queue<int > q;

void DFS(int num) {
	visited[num] = true;
	cout << num << " ";
	for (int elem : adj[num]) {
		if (!visited[elem])
			DFS(elem);
	}
}

void BFS(int num) {
	q.push(num);
	visited[num] = true;
	while(!q.empty()) {
		int tmp = q.front();
		q.pop();
		cout << tmp << " ";
		for (int elem : adj[tmp]) {
			if (!visited[elem]) {
				q.push(elem);
				visited[elem] = true;
			}
		}
	}
}

int main() {
	int v, e, r;
	cin >> v >> e >> r;
	
	for (int i = 0; i < e; i++) {
		int tmp1, tmp2;
		cin >> tmp1 >> tmp2;
		adj[tmp1].push_back(tmp2);
		adj[tmp2].push_back(tmp1);
	}
	
	for (int i = 1; i <= v; i++)
		sort(adj[i].begin(), adj[i].end());

	DFS(r);
	cout << endl;
	memset(visited, 0, sizeof(visited));
	BFS(r);
	return 0;
}