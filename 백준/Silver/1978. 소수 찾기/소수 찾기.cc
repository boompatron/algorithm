#include <iostream>
using namespace std;
int main() {
	int size, answer;
	cin >> size;
	answer = size;
	while (size--) {
		int num;
		bool isPrimeNum = true;
		cin >> num;
		if (num == 1)
			answer--;
		for(int i = 2; i <num; i++)
			if (num % i == 0) {
				answer--;
				break;
			}
	}
	cout << answer;
	return 0;
}