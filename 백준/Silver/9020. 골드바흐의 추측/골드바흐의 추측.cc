#include <bits/stdc++.h>
using namespace std;
int tc, n;
bool isNotPrime[10001];
int ans[2];
void sieveOfEratosthenes(){
    for (int i = 2; i < 102; i++) {
        int tmp = i * 2;
        while (tmp <= 10000) {
            isNotPrime[tmp] = true;
            tmp += i;
        }
    }
}
void goldbachConjecture(int num){
    for (int a = (int)(num / 2); a >= 2; a--){
        if (!isNotPrime[a] && !isNotPrime[num - a]) {
            ans[0] = a;
            ans[1] = num - a;
            return;
        }
    }
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    isNotPrime[0] = true; isNotPrime[1] = true;
    sieveOfEratosthenes();

    cin >> tc;

    while (tc--) {
        cin >> n;
        goldbachConjecture(n);
        cout << ans[0] << " " << ans[1] << "\n";
    }

    return 0;
}