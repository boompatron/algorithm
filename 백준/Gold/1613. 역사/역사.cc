#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int n, k, s, a, b;
int in_degree[402], adj[402][402];
vector<int> g[402];

void topology_sort()
{
    queue<int> q;
    for (int i = 0; i < n + 1; i++)
    {
        if (in_degree[i] == 0)
            q.push(i);
    }

    while(!q.empty())
    {
        int cur = q.front(); q.pop();

        for (int next: g[cur])
        {
            adj[next][cur] = 1;
            for  (int i = 1; i < n + 1; i++)
            {
                if (adj[cur][i] == 1)
                {
                    adj[next][i] = 1;
                }
            }
            in_degree[next]--;

            if (in_degree[next] == 0)
                q.push(next);
        }
    }
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    cin >> n >> k;
    while(k--)
    {
        cin >> a >> b;
        g[a].push_back(b);
        in_degree[b]++;
    }

    topology_sort();

    cin >> s;
    while(s--)
    {
        cin >> a >> b;
        if      (adj[a][b] == 1)    cout << "1\n";
        else if (adj[b][a] == 1)    cout << "-1\n";
        else                        cout << "0\n";
    }
}