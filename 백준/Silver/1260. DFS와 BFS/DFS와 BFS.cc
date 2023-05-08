#include <bits/stdc++.h>
using namespace std;
int v, e, start;
bool visited[1001];
vector<int> adj[1001];
void dfs(int cur){
    visited[cur] = true;
    cout << cur << " ";
    for (int a: adj[cur]){
        if (!visited[a]){
            dfs(a);
        }
    }
}
void bfs(){
    deque<int> dq;

    dq.push_back(start);
    visited[start] = true;
    cout << start << " ";
    while(!dq.empty()){
        int cur = dq.front();
        dq.pop_front();

        for (int a: adj[cur]){
            if (!visited[a]){
                visited[a] = true;
                cout << a << " ";
                dq.push_back(a);
            }
        }
    }
}
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    cin >> v >> e >> start;
    int a, b;
    for (int i = 0; i < e; i++){
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }

    for (int i = 1; i < v + 1; i++){
        sort(adj[i].begin(), adj[i].end());
    }

    dfs(start);
    for (int i = 1; i < v + 1; i++)
        visited[i] = false;
    cout << "\n";
    bfs();

    return 0;
}