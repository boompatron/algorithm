#include <iostream>
using namespace std;
int dp[1000001];
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);
	int N;
	cin >> N;
	for (int i = N; i > 0; i--) {
		if (i % 3 == 0)	dp[i / 3] = dp[i] + 1;
		if (i % 2 == 0)	dp[i / 2] = dp[i / 2] ? min(dp[i / 2], dp[i] + 1) : dp[i] + 1;
		dp[i - 1] = dp[i - 1] ? min(dp[i - 1], dp[i] + 1) : dp[i] + 1;
	}
	cout << dp[1] << endl;
	return 0;
}