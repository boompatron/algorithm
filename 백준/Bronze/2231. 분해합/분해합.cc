#include <iostream>
using namespace std;
int ans = 0, rValue, N;
void solve(int n) {
	rValue = n;
	//if (n >= 10) {
		int num[8], nCopy = n, i = 0;
		while (nCopy > 0) {
			num[i] = nCopy % 10;
			nCopy /= 10;
			i++;
		}
		for (int j = 0; j < i; j++)
			rValue += num[j];
	//}
	if (rValue > N / 10) {
		if (rValue == N)
			ans = n;
		solve(n - 1);
	}

}
int main() {
	cin >> N;
	//solve(1);
	solve(N);
	cout << ans;
	return 0;
}