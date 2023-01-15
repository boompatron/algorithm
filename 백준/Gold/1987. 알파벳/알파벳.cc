#include <bits/stdc++.h>
using namespace std;
char g[21][21];
int ans = 0, n, m, dxs[4] = {1, -1, 0, 0}, dys[4] = {0, 0, 1, -1};
bool visited[26];
void dfs(int x, int y, int cnt){
    ans = max(ans, cnt);
    for (int i = 0; i < 4; i++){
        int nx = x + dxs[i], ny = y + dys[i];
        if (0 <= nx && nx < m && 0 <= ny && ny < n && !visited[(int)g[ny][nx] - 65]){
            visited[(int)g[ny][nx] - 65] = true;
            dfs(nx, ny, cnt + 1);
            visited[(int)g[ny][nx] - 65] = false;
        }
    }
}

int main(){
    cin >> n >> m;
    for(int i = 0; i < n; i++)
        for(int j = 0; j < m; j++)
            cin >> g[i][j];
    visited[(int)g[0][0] - 65] = true;
    dfs(0, 0, 1);
    cout << ans << '\n';
    return 0;
}