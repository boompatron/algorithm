#include <iostream>
using namespace std;
int dp0[42], dp1[42];
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);
	int size;
	cin >> size;
	dp0[0] = 1;	dp1[1] = 1;
	while (size--) {
		int num;
		cin >> num;
		for (int i = 2; i <= num; i++) {
			dp0[i] = dp0[i - 1] + dp0[i - 2];
			dp1[i] = dp1[i - 1] + dp1[i - 2];
		}
		cout << dp0[num] << " " << dp1[num] << endl;
	}
	return 0;
}