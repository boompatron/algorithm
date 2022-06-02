#include <iostream>
#include <set>
using namespace std;
int n, m;
int parent[1000002];
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
	for (int i = 0; i < n + 1; i++)
		parent[i] = i;
	for (int i = 1; i < m + 1; i++) {
		bool b;
		int v1, v2;
		cin >> b >>v1 >> v2;
		if (b) {
			if (get_parent(parent, v1) == get_parent(parent, v2))
				cout << "YES\n";
			else
				cout << "NO\n";
		}
		else
			union_parent(parent, v1, v2);
	}	
	return 0;
}