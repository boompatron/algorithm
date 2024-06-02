#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
const int INF = 1e7;

int n, e, v1, v2, ans[1005];
vector<pair<int, int>> adj[1005];
priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

int dijkstra(int start, int end)
{
    fill(ans, ans + n + 1, INF);
    ans[start] = 0;

    pq.emplace(0, start);
    while (!pq.empty())
    {
        pair cur = pq.top();
        pq.pop();

        if (ans[cur.second] < cur.first)
            continue;

        for (pair nnode : adj[cur.second]) {
            int ncost = cur.first + nnode.second;

            if (ncost >= ans[nnode.first])
                continue;

            ans[nnode.first] = ncost;
            pq.emplace(ncost, nnode.first);
        }
    }

    return ans[end];
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);


    cin >> n >> e;
    int a, b, c;
    while (e--) {
        cin >> a >> b >> c;
        adj[a].emplace_back(b, c);
        adj[b].emplace_back(a, c);
    }
    cin >> v1 >> v2;

    int aa = min(dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, n), dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, n));
    if (aa >= INF) aa = -1;

    cout << aa;

    return 0;
}
