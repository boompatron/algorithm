#include <iostream>
#include <string>
using namespace std;
int main() {
	int tc_size;
	cin >> tc_size;
	while (tc_size--) {
		string str, ans = "YES";
		int num = 0;
		cin >> str;
		for (int i = 0; i < str.size(); i++) {
			if (str[i] == '(')
				num++;
			else if (str[i] == ')')
				num--;

			if (num < 0)
				ans = "NO";
		}
		if (num != 0)
			ans = "NO";
		cout << ans << endl;
	}
	return 0;
}