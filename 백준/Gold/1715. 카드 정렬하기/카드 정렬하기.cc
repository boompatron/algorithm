#include <bits/stdc++.h>
using namespace std;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    priority_queue<int> pq;
    int n, tmp, ans = 0;
    cin >> n;
    while (n--){
        cin >> tmp;
        pq.push(-tmp);
    }
    while(pq.size() > 1){
        int a1 = -pq.top();
        pq.pop();
        int a2 = -pq.top();
        pq.pop();
        ans += a1 + a2;
        pq.push(-(a1 + a2));
    }
    cout << ans << "\n";

    return 0;
}