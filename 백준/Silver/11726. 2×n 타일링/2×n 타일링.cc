#include <iostream>
using namespace std;
int dp[1001];
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);
	
	dp[1] = 1;
	dp[2] = 2;
	int n;
	cin >> n;
	for (int i = 3; i <= n; i++)
		dp[i] = (dp[i - 1] + dp[i - 2]) % 10007;
	cout << dp[n] % 10007;
	return 0;
}