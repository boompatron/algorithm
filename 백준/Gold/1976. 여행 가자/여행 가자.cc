#include <iostream>
#include <set>
using namespace std;
int n, m;
int g[202][202];
int parent[202];
int find_parent(int parent[], int x) {
	if (parent[x] == x) return x;
	return parent[x] = find_parent(parent, parent[x]);
}
void union_parent(int parent[], int a, int b) {
	a = find_parent(parent, a);
	b = find_parent(parent, b);
	if (a < b)		parent[b] = a;
	else if (a > b) parent[a] = b;
	else			return;
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);
	cin >> n >> m;
	for (int i = 1; i < n + 1; i++)
		parent[i] = i;
	for (int i = 1; i < n + 1; i++) {
		for (int j = 1; j < n + 1; j++) {
			cin >> g[i][j];
			if (g[i][j] == 1 && find_parent(parent, i) != find_parent(parent, j))
				union_parent(parent, i, j);
		}
	}
	set<int> s;
	int travel;
	for (int i = 0; i < m; i++) {
		cin >> travel;
		s.insert(parent[travel]);
	}
	if (s.size() == 1)	cout << "YES" << endl;
	else				cout << "NO" << endl;
	return 0;
}