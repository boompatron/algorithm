#include <iostream>
using namespace std;
int main(void) {
	int point, tape_length, tape_num; tape_num = 1;
	int fix_point[1001];
	int first_point, tmp;
	cin >> point; cin >> tape_length;

	for (int i = 0; i < point; i++)
		cin >> fix_point[i];

	for (int i = 0; i < point; i++) {
		for (int j = 0; j < point - 1; j++) {
			if (fix_point[j] > fix_point[j + 1]) {
				tmp = fix_point[j + 1];
				fix_point[j + 1] = fix_point[j];
				fix_point[j] = tmp;
			}
		}
	}
	first_point = fix_point[0];

	for (int i = 0; i < point; i++) {
		if ((first_point + tape_length - 1) < fix_point[i + 1]) {
			first_point = fix_point[i + 1];
			tape_num++;
		}
	}
	cout << tape_num;
	return 0;
}