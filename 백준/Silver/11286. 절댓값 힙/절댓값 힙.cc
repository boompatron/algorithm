#include <bits/stdc++.h>
using namespace std;
struct comp{
    bool operator()(pair<int, int> a, pair<int, int> b){
        if (a.first == b.first) return a.second > b.second;
        else                    return a.first > b.first;
    }
};
int n, x;
priority_queue<pair<int, int>, vector<pair<int, int>>, comp> pq;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n;
    while(n--){
        cin >> x;
        if(x == 0){
            if (pq.empty()) cout << "0\n";
            else{
                cout << pq.top().first * pq.top().second << "\n";
                pq.pop();
            }
        }
        else pq.push(make_pair(abs(x), (x > 0) ? 1 : -1));
    }
    return 0;
}