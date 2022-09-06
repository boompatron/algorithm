#include <cstdio>
int main() {
	int size;
	scanf("%d", &size);
	int dp_0[41] = { 1, 0, 1}, dp_1[41] = { 0, 1, 1};
	for (int i = 2; i < 41; i++) {
		dp_0[i] = dp_0[i - 1] + dp_0[i - 2];
		dp_1[i] = dp_1[i - 1] + dp_1[i - 2];
	}

	while (size--) {
		int num;
		scanf("%d", &num);
        printf("%d %d\n", dp_0[num], dp_1[num]);
	}
	return 0;
}