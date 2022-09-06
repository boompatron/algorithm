#include <iostream>
using namespace std;
int main() {
	int num, dp[1000001];
	cin >> num;
	dp[1] = 0;
	dp[2] = 1;
	dp[3] = 1;
	for (int i = 4; i <= num; i++) {
		if (i % 3 == 0 && i % 2 == 0)
			dp[i] = min(min(dp[i - 1], dp[i / 3]), dp[i / 2]) + 1;
		else if (i % 3 == 0)
			dp[i] = min(dp[i - 1], dp[i / 3]) + 1;
        else if (i % 2 == 0)
			dp[i] = min(dp[i - 1], dp[i / 2]) + 1;
		else
			dp[i] = dp[i - 1] + 1;
	}
	cout << dp[num];
	return 0;
}