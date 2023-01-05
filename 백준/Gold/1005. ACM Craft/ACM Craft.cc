#include <bits/stdc++.h>
using namespace std;
int n, k, w;
int building_time[1002], degree[1002], complete_time[1002];
vector<int> adj[1002];
struct comp{
    bool operator()(pair<int, int> a, pair<int, int> b){
        return a.first > b.first;
    }
};
priority_queue<pair<int, int>, vector<pair<int, int>>, comp> pq;
int solve(){
    cin >> n >> k;
    for(int i = 1; i <= n; i++) {
        cin >> building_time[i];
        complete_time[i] = INT_MAX;
        adj[i].clear();
        degree[i] = 0;
    }
    int a, b;
    for(int i = 1; i <= k; i++){
        cin >> a >> b;
        degree[b] += 1;
        adj[a].push_back(b);
    }
    cin >> w;
    for(int i = 1; i <= n; i++){
        if(degree[i] == 0)
            pq.emplace(building_time[i], i);
    }
    while(!pq.empty()){
        pair<int, int> cur = pq.top();
        pq.pop();

        if(complete_time[cur.second] > cur.first)   complete_time[cur.second] = cur.first;
        for(int ad: adj[cur.second]){
            degree[ad] -= 1;
            if(degree[ad] == 0)  pq.emplace(cur.first + building_time[ad], ad);
        }
    }
     return complete_time[w];
}
int main(){
    int tc;
    cin >> tc;
    while(tc--){
        cout << solve() << "\n";
    }
    return 0;
}