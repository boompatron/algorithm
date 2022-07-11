#include <iostream>
#include <set>
using namespace std;
int n, m, tmp;
set<int> s;
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0); cout.tie(0);
	cin >> n;
	while (n--) {
		cin >> tmp;
		s.insert(tmp);
	}
	cin >> m;
	while (m--){
		cin >> tmp;
		cout << (s.find(tmp) != s.end()) ? 1 : 0;
		cout << " ";
	}
	return 0;
}