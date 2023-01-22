#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int n, m;
int parent[100001];
int get_parent(int parent[], int x) {
	if (parent[x] == x) return x;
	return parent[x] = get_parent(parent, parent[x]);
}
void union_parent(int parent[], int a, int b) {
	a = get_parent(parent, a);
	b = get_parent(parent, b);
	if (a < b)		parent[b] = a;
	else if (a > b) parent[a] = b;
	else			return;
}

int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);
	vector<vector<int>> adj;
	int ans = 0, biggest = 0;
	cin >> n >> m;
	for (int i = 1; i < n + 1; i++)
		parent[i] = i;
	for (int i = 0; i < m; i++) {
		int v1, v2, dis;
		vector<int> tmp;
		cin >> v1 >> v2 >> dis;
		tmp.push_back(dis);
		tmp.push_back(v1);
		tmp.push_back(v2);
		adj.push_back(tmp);
	}
	sort(adj.begin(), adj.end());
	for (auto elem : adj) {
		if (get_parent(parent, elem[1]) != get_parent(parent, elem[2])) {
			union_parent(parent, elem[1], elem[2]);
			ans += elem[0];
			if (elem[0] > biggest)	biggest = elem[0];
		}
	}
	cout << ans - biggest;
	return 0;
}