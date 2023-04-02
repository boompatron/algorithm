#include <bits/stdc++.h>
using namespace std;
int n, g[16], ans;
bool isPromising(int x) {
    for (int i = 0; i < x; i++) {
        if (g[x] == g[i] || abs(g[x] - g[i]) == abs(x - i)){
            return false;
        }
    }
    return true;
}

void nQueen(int x) {
    if (x == n) {
        ans += 1;
        return;
    }
    for (int i = 0; i < n; i++) {
        g[x] = i;
        if (isPromising(x)) {
            nQueen(x + 1);
        }
    }
}

int main() {
    cin >> n;
    nQueen(0);
    cout << ans;
    return 0;
}