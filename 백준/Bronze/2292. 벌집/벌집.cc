#include <iostream>
using namespace std;
int main() {
	int num, increase_width = 6, start = 2, answer = 1;
	cin >> num;
	if (num == 1) {
		cout << 1 << endl;
		exit(0);
	}
	while (1) {
		if (num < start) {
			break;
		}
		else {
			start += increase_width;
			increase_width += 6;
			answer++;
		}
	}
	cout << answer;
	return 0;
}