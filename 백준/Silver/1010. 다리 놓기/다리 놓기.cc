#include <iostream>
using namespace std;
int main() {
	int size;
	cin >> size;
	while (size--) {
		long long n, m, dp[30];
		cin >> n >> m;
		dp[0] = 1;
		dp[1] = n + 1;
		for (long long i = 2; i <= m - n; i++) {
			dp[i] = dp[i - 1] * (i + n) / (i);
		}
		cout << dp[m - n] << endl;
	}
	return 0;
}