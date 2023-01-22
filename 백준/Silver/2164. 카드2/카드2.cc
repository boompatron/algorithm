#include <iostream>
#include <queue>
using namespace std;
int main() {
	int N;
	queue<int> q;
	cin >> N;
	for (int i = 1; i <= N; i++)
		q.push(i);

	if (q.size() == 1) {
		cout << q.front();
		exit(0);
	}
	else if (q.size() == 2) {
		q.pop();
		cout << q.front();
		exit(0);
	}

	while (q.size() > 2) {
		q.pop();
		q.push(q.front());
		q.pop();
	}
	q.pop();
	cout << q.front();
	return 0;
}