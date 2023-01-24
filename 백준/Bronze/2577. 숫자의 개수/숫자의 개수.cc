#include <iostream>
using namespace std;
int main() {
	int a, b, c, mul;
	int num[10] = {0,0,0,0,0,0,0,0,0,0};
	cin >> a >> b >> c;
	mul = a * b * c;
	while (mul > 0) {
		int tmp = mul % 10;
		for (int i = 0; i < 10; i++) {
			if (i == tmp)
				num[i]++;
		}
		mul /= 10;
	}
	for (int i = 0; i < 10; i++)
		cout << num[i] << endl;
	return 0;
}