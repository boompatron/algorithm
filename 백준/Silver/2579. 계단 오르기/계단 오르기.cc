#include <iostream>
using namespace std;
int dp[302], stair[302];
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++)
		cin >> stair[i];
	dp[1] = stair[1];
	dp[2] = stair[1] + stair[2];
	dp[3] = max(stair[1] + stair[3], stair[2] + stair[3]);

	for (int i = 4; i <= n; i++)
		dp[i] = max(dp[i - 2] + stair[i], dp[i - 3] + stair[i] + stair[i - 1]);
	cout << dp[n] << endl;
	return 0;
}