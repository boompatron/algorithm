#include <iostream>
#include <algorithm>
using namespace std;
int main() {
	int size, arr[1000], dp[1000] = {1}, answer = 0;
	cin >> size;
	for (int i = 0; i < size; i++) {
		cin >> arr[i];
		dp[i] = 1;
	}
	for (int i = 0; i < size; i++) {
		for (int j = 0; j < i; j++) {
			if (arr[i] > arr[j] && dp[i] < dp[j] + 1) {
				dp[i] = dp[j] + 1;
			}
		}
		answer = max(answer, dp[i]);
	}
	cout << answer;
	return 0;
}
