#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int n, k, s;
int in_degree[402], adj[402][402];
vector<int> g[402];
// 위상정렬을 이용한 풀이
// 나중에 더 자세히 보고 최적화 해야할 듯
// 이해가 급선무
// 1. 다양한 갈래가 있을 수 있는데 왜 위상정렬이 성립하는가
void topology_sort()
{
    queue<int> q;
    for(int i = 0; i < n + 1; i++)
    {
        if(in_degree[i] == 0)
            q.push(i);
    }

    while(!q.empty())
    {
        int cur = q.front(); q.pop();

        for(int next: g[cur])
        {
            adj[next][cur] = 1;
            for (int i = 1; i < n + 1; i++)
            {
                if (adj[cur][i] == 1)
                    adj[next][i] = 1;
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
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n >> k;
    int v1, v2;

    while(k--)
    {
        cin >> v1 >> v2;
        g[v1].push_back(v2);
        in_degree[v2]++;
    }

    topology_sort();

    cin >> s;
    while (s--)
    {
        cin >> v1 >> v2;
        if(adj[v1][v2] == 1)
            cout << 1 << '\n';
        else if(adj[v2][v1] == 1)
            cout << -1 << '\n';
        else
            cout << 0 << '\n';
    }

    return 0;
}
