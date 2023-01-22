#include <iostream>
using namespace std;
int n, s;
int g[100001];
int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);	cout.tie(0);
	cin >> n >> s;
	for (int i = 0; i < n; i++)
		cin >> g[i];
	int end = 0, partial_sum = 0, ans = 123456789;
	for (int start = 0; start < n; start++) {
		while (partial_sum < s && end < n) {
			partial_sum += g[end++];
		}
		if (ans > end - start && partial_sum >= s)
			ans = end - start;
		partial_sum -= g[start];
	}
	if (ans == 123456789)
		cout << 0;
	else
		cout << ans;
	return 0;
}