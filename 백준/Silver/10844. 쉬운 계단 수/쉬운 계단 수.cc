#include <cstdio>
using namespace std;
int main() {
	const int mod = 1000000000;
	int size, num[11][101] = {0};
	num[0][1] = 0;
	for (int i = 1; i < 10; i++)
		num[i][1] = 1;
	scanf("%d", &size);
	for (int i = 2; i <= size; i++) {
          num[0][i] = num[1][i - 1];
          num[9][i] = num[8][i - 1];
		for (int j = 1; j < 9; j++) {
			num[j][i] = (num[j - 1][i - 1] + num[j + 1][i - 1]) % mod;
		}
	}
	int ans = 0;
	for (int h = 0; h < 10; h++)
		ans = (ans + num[h][size]) % mod;
	printf("%d\n", ans);
	return 0;
}