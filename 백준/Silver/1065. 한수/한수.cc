#include <iostream>
using namespace std;
int ans = 0;
void solve(int n) {
	if (n < 10) {
		ans += n;
	}
	else {
		int tmp[5], copy = n, i = 0, common_diff;
		bool isNum = true;
		while (copy > 0) {
			tmp[i] = copy % 10;
			copy /= 10;
			i++;
		}
		common_diff = tmp[0] - tmp[1];
		for (int j = 1; j < i - 1; j++) {
			if (tmp[j] - tmp[j + 1] != common_diff)
				isNum = false;
		}
		if (isNum)
			ans++;
		solve(n - 1);
	}
}
int main() {
	int N;
	cin >> N;
	solve(N);
	cout << ans << endl;
	return 0;
}