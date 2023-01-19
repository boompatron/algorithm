#include <iostream>
using namespace std;
int main(void)
{
	int size, line[11], answer[11];
	int cur;
	cin >> size;
	for (int i = 0; i < size; i++) {
		cin >> line[i];
		answer[i] = NULL;
	}
	for (int i = 0; i < size; i++) {
		cur = 0;
		while (1) {
			if (answer[cur] == NULL) {
				if (line[i] == 0) {
					answer[cur] = i + 1;
					break;
				}
				else{						// line[i] != 0
					cur++;
					line[i]--;
				}
			}
			else
				cur++;
		}
	}
	for (int i = 0; i < size; i++)
		cout << answer[i] << " ";
	return 0;
}