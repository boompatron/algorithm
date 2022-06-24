#include <cstdio>
int main() {
	int size, answer;
	scanf("%d", &size);
	answer = size;
	while (size--) {
		int num;
		bool isPrimeNum = true;
		scanf("%d", &num);
		if (num == 1)
			answer--;
		for(int i = 2; i <num; i++)
			if (num % i == 0) {
				answer--;
				break;
			}
	}
	printf("%d\n", answer);
	return 0;
}