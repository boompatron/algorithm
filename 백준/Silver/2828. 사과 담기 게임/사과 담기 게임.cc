#include <iostream>
using namespace std;
int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	int n, m, cnt, distance = 0;
	cin >> n >> m >> cnt;
	int left_side = 1, right_side = m;
	while (cnt--) {
		int pos;
		cin >> pos;
		if (pos < left_side) {
			int tmp = left_side - pos;
			left_side -= tmp;
			right_side -= tmp;
			distance += tmp;
		}
		else if (pos > right_side) {
			int tmp = pos - right_side;
			left_side += tmp;
			right_side += tmp;
			distance += tmp;
		}
	}
	cout << distance;
	return 0;
}