#include <iostream>
#include <algorithm>
using namespace std;
int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	int level, answer = 0, tmp = 0;
	int ypos = 0, xpos = 0;
	int num[501][501] = {};
	cin >> level;
	for (int i = 1; i <= level; i++) {
		for (int j = 1; j <= i; j++)
			cin >> num[i][j];
	}
	for (int i = 1; i <= level; i++) {
		for (int j = 1; j <= i; j++) {
			num[i][j] += max(num[i-1][j], num[i-1][j-1]);
		}
	}
	for (int i = 0; i <= level; i++)
		answer = max(answer, num[level][i]);
	cout << answer;
	return 0;
}