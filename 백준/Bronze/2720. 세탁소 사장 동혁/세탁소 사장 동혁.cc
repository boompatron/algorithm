#include <iostream>
using namespace std;
int main() {
	int size;
	cin >> size;
	while (size--) {
		int money;
		cin >> money;
		cout << money / 25 << " ";
		money %= 25;
		cout << money / 10 << " ";
		money %= 10;
		cout << money / 5 << " ";
		money %= 5;
		cout << money << endl;
	}
	return 0;
}