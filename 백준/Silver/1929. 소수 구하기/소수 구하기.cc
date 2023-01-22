#include <iostream>
using namespace std;
int n, m;
int erasto[1000002];
int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);	cout.tie(0);
	erasto[1] = true;
	cin >> m >> n;
	int pos = 2;
	while (pos <= n) {
		if (!erasto[pos]) {
			int num = pos * 2;
			while (num <= n) {
				erasto[num] = true;
				num += pos;
			}
		}
		pos += 1;
	}
	for (int i = m; i < n + 1; i++)
		if (!erasto[i])
			cout << i << "\n";
	return 0;
}