#include <cstdio>
int main() {
	int k, dp_A[45] = { 1 }, dp_B[45] = {0};
	scanf("%d", &k);
	for (int i = 1; i <= k; i++) {
		dp_A[i] = dp_B[i - 1];
		dp_B[i] = dp_A[i - 1] + dp_B[i - 1];
	}
	printf("%d %d\n", dp_A[k], dp_B[k]);
	return 0;
}