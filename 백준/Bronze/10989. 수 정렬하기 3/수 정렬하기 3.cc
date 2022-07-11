#include <iostream>
using namespace std;
int n, i, tmp, g[10002];
int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(0);	cout.tie(0);
	cin >> n;
	while(n--){
		cin >> tmp;
		g[tmp]++;
	}
	for (i = 1; i < 10001; i++)
		while (g[i]--)
			cout << i << "\n";
	return 0;
}