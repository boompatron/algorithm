#include <iostream>
using namespace std;
int n, m;
int g[10001];
int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);	cout.tie(0);
	cin >> n >> m;
	for (int i = 0; i < n; i++)
		cin >> g[i];
	int end = 0, partial_sum = 0, cnt = 0;
	for (int start = 0; start < n; start++) {
		while (partial_sum < m && end < n) {
			partial_sum += g[end++];
		}
		if (partial_sum == m)
			cnt++;
		partial_sum -= g[start];
	}
	cout << cnt;
	return 0;
}