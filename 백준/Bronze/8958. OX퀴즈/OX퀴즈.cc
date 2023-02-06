#include <iostream>
using namespace std;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);
	int size, cnt = 0, score = 0;
	string str;
	cin >> size;
	while (size--) {
		cin >> str;
		for (int i = 0; i < str.size(); i++) {
			if (str[i] == 'O') {
				cnt++;
				score += cnt;
			}
			else if (str[i] == 'X') {
				cnt = 0;
			}
		}
		cout << score << endl;
		score = 0;
		cnt = 0;
	}
	return 0;
}