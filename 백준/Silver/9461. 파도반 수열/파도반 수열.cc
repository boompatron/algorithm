#include <iostream>
using namespace std;
int main() {
	int size;
    long long int P[100];
	cin >> size;
	P[0] = 1;
	P[1] = 1;
	P[2] = 1;
	P[3] = 2;
	P[4] = 2;
	P[5] = 3;
	P[6] = 4;
	P[7] = 5;
	P[8] = 7;
	P[9] = 9;
	while (size--) {
		int tmp;
		cin >> tmp;
		if (tmp > 9) {
			for (int i = 10; i < tmp; i++)
				P[i] = P[i - 1] + P[i - 5];
		}
		cout << P[tmp-1] << endl;
	}

	return 0;
}