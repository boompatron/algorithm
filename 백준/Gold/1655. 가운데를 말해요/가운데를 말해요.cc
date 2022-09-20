#include <iostream>
#include <queue>
using namespace std;
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0); cout.tie(0);

	priority_queue<int, vector<int>, greater<int>> pq_right;
	priority_queue<int> pq_left;
	int n;
	cin >> n;
	for (int i = 0; i < n; i++) {
		int cur;
		cin >> cur;
		if (pq_left.size() == pq_right.size())
			pq_left.push(cur);
		else
			pq_right.push(cur);
		if (!pq_left.empty() && !pq_right.empty() && pq_left.top() > pq_right.top()) {
			int tmp1 = pq_left.top(), tmp2 = pq_right.top();
			pq_left.pop();
			pq_right.pop();
			pq_left.push(tmp2);
			pq_right.push(tmp1);
		}
		cout << pq_left.top() << "\n";
	}
	return 0;
}