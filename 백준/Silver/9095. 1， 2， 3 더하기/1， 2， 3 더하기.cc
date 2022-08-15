#include <iostream>
using namespace std;
int f(int n) {
	if (n == 1)
		return 1;
	else if (n == 2)
		return 2;
	else if (n == 3)
		return 4;
	else
		return f(n - 1) + f(n - 2) + f(n - 3);
}
int main() {
	int cnt, tmp;
	cin >> cnt;
	while (cnt > 0) {
		cin >> tmp;
		cout << f(tmp) << endl;
		cnt--;
	}
	return 0;
}