#include <iostream>
using namespace std;
int d(int n) {
	int tmp = n, sum = n;
	while (tmp > 0) {
		sum += tmp % 10;
		tmp /= 10;
	}
	return sum;
}
int main() {
	int i = 1;
	while (i <= 10000) {
		bool is_selfNum = true;
		for (int j = i; j > 0; j--) {
			if (i == d(j)) {
				is_selfNum = false;
				break;
			}
		}
		if (is_selfNum)
			cout << i << endl;
		i++;
	}
	return 0;
}