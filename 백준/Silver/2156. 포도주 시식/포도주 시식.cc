#include <iostream>
using namespace std;
int dp[10002], wine[10002];
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++)
		cin >> wine[i];
	dp[1] = wine[1];
	dp[2] = wine[1] + wine[2];
	dp[3] = max(max(dp[2], wine[2] + wine[3]), wine[1] + wine[3]);
	for (int i = 4; i <= n; i++)
		dp[i] = max(max(dp[i - 2] + wine[i], dp[i - 3] + wine[i] + wine[i - 1]), dp[i - 1]);
	cout << dp[n] << endl;
	return 0;
}