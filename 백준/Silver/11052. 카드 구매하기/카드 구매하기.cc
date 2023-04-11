#include <iostream>
using namespace std;
int main() {
	long long size, arr[1001], dp[1001] = {0,}, answer = 0;
	cin >> size;
	for (int i = 1; i <= size; i++)
		cin >> arr[i];
	for (int i = 1; i <= size; i++) {
		for (int j = i; j > 0; j--) {
			dp[i] = max(dp[i-j] + arr[j] , dp[i]);
			answer = max(answer, dp[i]);
		}
	}
	cout << answer;
	return 0;
}