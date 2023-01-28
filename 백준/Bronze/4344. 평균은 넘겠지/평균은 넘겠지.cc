#include <iostream>
using namespace std;
int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	int TC_size;
	cin >> TC_size;
	while (TC_size--) {
		int cnt, score[1000], aver = 0, over = 0;
		double answer;
		cin >> cnt;
		for (int i = 0; i < cnt; i++) {
			cin >> score[i];
			aver += score[i];
		}
		aver /= cnt;
		for (int i = 0; i < cnt; i++) {
			if (score[i] > aver)
				over++; 
		}
		over *= 1000000;
		int integer = over / cnt / 10000;
		int decimal_point = over / cnt % 10000;
		int dec[3] = {0, 0, 0};

		cout << integer << ".";
		int j = 1000;
		for (int i = 0; i < 3; i++) {
			dec[i] = decimal_point  / j;
			decimal_point -= dec[i] * j;
			j /= 10;
		}
		if (decimal_point % 10 > 4)
			dec[2]++;
		cout << dec[0] << dec[1] << dec[2];
		cout << "%" << endl;
	}
	return 0;
}