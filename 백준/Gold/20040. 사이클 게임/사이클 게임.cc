#include <iostream>
#include <set>
using namespace std;
int n, m;
int parent[500001];
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
	cin >> n >> m;
	for (int i = 0; i < n; i++)
		parent[i] = i;
	for (int i = 1; i < m + 1; i++) {
		int v1, v2;
		cin >> v1 >> v2;
		if (get_parent(parent, v1) == v2 || get_parent(parent, v2) == v1 || get_parent(parent, v1) == get_parent(parent, v2)) {
			cout << i;
			exit(0);
		}
		union_parent(parent, v1, v2);
	}
	cout << 0;
		
	return 0;
}