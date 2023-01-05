#include <iostream>
using namespace std;
int M, a, check_num;
// bool* ans;
void init(int* a) { *a = 0; }
void all(int* a) { *a = -1; }
void drop(int* a, int i) {*a &= ~(1 << i);}
void set(int* a, int i) {*a |= (1 << i);}
bool isSet(int* a, int i) {return *a & (1 << i);}
void toggle(int* a, int i) {*a ^= (1 << i);}
//void show(int* a) {
//	for (int i = 32; i > 0; i--) {
//		cout << ((*a & (1 << i - 1)) ? 1 : 0);
//	}
//	cout << "\n";
//}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL); cout.tie(NULL);
	cin >> M;
	// ans = new bool[M];
	while (M--) {
		string s;
		cin >> s;
		if (s == "all")
			all(&a);
		else if (s == "empty")
			init(&a);
		else {
			int x;
			cin >> x;
			if (s == "add")
				set(&a, x);
			else if (s == "remove")
				drop(&a, x);
			else if (s == "check")
				cout << isSet(&a, x) << "\n";
				// ans[check_num++] = isSet(&a, x);
			else if (s == "toggle")
				toggle(&a, x);
		}
	}
	//for (int i = 0; i < check_num; i++)
	//	cout << ans[i] << "\n";
	//delete ans;
	return 0;
}