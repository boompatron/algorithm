#include <iostream>
using namespace std;
int main() {
	long long size;
	cin >> size;
	if (size % 2 == 1)
		cout << "SK";
	else
		cout << "CY";
	return 0;
}