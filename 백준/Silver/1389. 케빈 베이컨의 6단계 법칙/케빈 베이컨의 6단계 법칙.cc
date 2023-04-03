#include <bits/stdc++.h>
using namespace std;
int n, m, a, b, ans, cnt, dis[101];
vector<int> adj[101];
int main(){
    cin >> n >> m;
    for (int i = 0; i < m; i++) {
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    ans = n + 1, cnt = (n + 1) * (n + 1);
    for (int i = 1; i < n + 1; i++) {
        deque< pair<int, int> > dq;
        for(int j = 0; j < n + 1; j++)
            dis[j] = n + 1;
        dq.push_back(make_pair(i, 0));
        while (!dq.empty()){
            pair<int, int> cur = dq.front();
            dq.pop_front();
            for(int pos : adj[cur.first]){
                if (dis[pos] > cur.second + 1){
                    dq.push_back(make_pair(pos, cur.second + 1));
                    dis[pos] = cur.second + 1;
                }
            }
        }
        if (accumulate(dis + 1, dis + n + 1, 0) < cnt){
            cnt = accumulate(dis + 1, dis + n + 1, 0);
            ans = i;
        }
    }
    cout << ans;
    return 0;
}