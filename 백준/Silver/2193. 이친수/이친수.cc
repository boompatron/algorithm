#include <iostream>
using namespace std;
long long dp[92];
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);
	int n;
	cin >> n;
	dp[0] = 0; dp[1] = 1;	dp[2] = 1;
	for (int i = 3; i <= n; i++) {
		dp[i] = dp[i - 2] + dp[i - 1];
	}
	cout << dp[n];
	return 0;
}