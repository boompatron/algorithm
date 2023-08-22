#include <bits/stdc++.h>
#define ft first
#define sd second
#define all(x) (x).begin(), (x).end()
#define mem(v, e) memset((v), (e), sizeof((v)))
using namespace std;
using ll = long long;
using pii = pair<int, int>;
 
int n, mod;
int tenPow[55];
string nums[22];
pii p[22];
ll d[1 << 15][111];
 
ll go(int s, int num) {
    if (s == (1 << n) - 1) return (num % mod == 0);
 
    ll &ret = d[s][num];
    if (ret != -1) return ret;
    ret = 0;
    for (int k = 0; k < n; k++) {
        if (s & (1 << k)) continue;
        auto[next, cnt] = p[k];
        ll nextNum = num * tenPow[cnt] + next;
        nextNum %= mod;
        ret += go(s | (1 << k), nextNum);
    }
    return ret;
}
 
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
 
    cin >> n;
    ll all = 1;
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
        all *= (i + 1);
    }
    cin >> mod;
    tenPow[0] = 1 % mod;
    for (int i = 1; i < 55; i++) {
        tenPow[i] = (tenPow[i - 1] * 10) % mod;
    }
    for (int i = 0; i < n; i++) {
        reverse(all(nums[i]));
        p[i].sd = nums[i].size();
        for (int j = 0; j < nums[i].size(); j++) {
            p[i].ft += (nums[i][j] - '0') * tenPow[j] % mod;
 
        }
        p[i].ft %= mod;
    }
    mem(d, -1);
    ll cnt = go(0, 0);
    ll g = gcd(all, cnt);
    cout << cnt / g << "/" << all / g;
}