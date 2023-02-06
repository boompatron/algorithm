#include <iostream>
using namespace std;
int main() {
	int N, x[51], y[51], rank[51];
	cin >> N;
	for (int i = 0; i < N; i++)
		cin >> x[i] >> y[i];

	for (int i = 0; i < N; i++) {
		rank[i] = 1;
		for (int j = 0; j < N; j++) {
			if (i == j)
				continue;
			else {
				if (x[i] < x[j] && y[i] < y[j])
					rank[i]++;
			}
		}
	}
	for (int i = 0; i < N; i++)
		cout << rank[i] << " ";
	return 0;
}