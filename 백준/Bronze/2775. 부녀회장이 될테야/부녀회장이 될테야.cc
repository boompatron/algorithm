#include <iostream>
using namespace std;
int main() {
	int T, k, n, people[14][15];
	for (int i = 0; i < 14; i++) {
		people[0][i] = 1;
		people[i][0] = i + 1;
	}
	people[0][14] = 1;;
	for (int i = 1; i < 15; i++) {
		for (int j = 1; j < 14; j++) {
			people[j][i] = people[j - 1][i] + people[j][i - 1];
		}
	}
	cin >> T;
	while (T > 0) {
		cin >> k; cin >> n;
		cout << people[n-1][k] << endl;
		T--;
	}
	return 0;
}