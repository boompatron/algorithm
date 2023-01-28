#include <iostream>
using namespace std;
int dp[5002];
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);
	int sugar;
	cin >> sugar;
	dp[3] = dp[5] = 1;
	for (int i = 6; i <= sugar; i++) {
		if (dp[i - 3])	dp[i] = dp[i - 3] + 1;
		if (dp[i - 5])	dp[i] = dp[i] ? min(dp[i], dp[i - 5] + 1) : dp[i - 5] + 1;
	}
	cout << (dp[sugar] == 0 ? -1 : dp[sugar]) << endl;
	return 0;
}