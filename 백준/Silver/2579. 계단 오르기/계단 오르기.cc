#include <iostream>
#include <algorithm>
using namespace std;
int main() {
	int size, stair[300], dp[300];
	cin >> size;
	for (int i = 0; i < size; i++)
		cin >> stair[i];
	dp[0] = stair[0];
	dp[1] = max(stair[0] + stair[1], stair[1]);
	dp[2] = max(stair[0] + stair[2], stair[1] + stair[2]);
	//dp[2] = max(stair[0] + stair[2], stair[1] + stair[2]);
	for (int i = 3; i < size; i++)
		dp[i] = max(dp[i - 2] + stair[i], dp[i - 3] + stair[i - 1] + stair[i]);
	cout << dp[size - 1];
	return 0;
}