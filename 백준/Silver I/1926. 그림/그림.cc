#include <iostream>
#include <deque>
using namespace std;

int dxs[4] = {1, 0, -1, 0}, dys[4] = {0, 1, 0, -1};
int n, m, maxSize = 0, cnt = 0;
bool board[501][501], visited[501][501];

bool inRange(int x, int y)
{
    return 0 <= x && x < m && 0 <= y && y < n;
}

void input()
{
    cin >> n >> m;
    int tmp;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> tmp;
            board[i][j] = (tmp == 1);
        }
    }
}

void bfs(int x, int y)
{
    cnt++;
    deque<pair<int, int>> dq;
    dq.push_back(make_pair(x, y));
    int size = 1;
    visited[y][x] = true;

    while (!dq.empty())
    {
        pair<int, int> cur_pos = dq.back();
        dq.pop_back();

        for (int dir = 0; dir < 4; dir++)
        {
            int nx = cur_pos.first + dxs[dir];
            int ny = cur_pos.second + dys[dir];

            if (board[ny][nx] && !visited[ny][nx] && inRange(nx, ny))
            {
                visited[ny][nx] = true;
                size++;
                dq.push_back(make_pair(nx, ny));
            }
        }
    }

    maxSize = maxSize > size ? maxSize : size;
}

void solve()
{
    deque<pair<int, int>> dq;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            if (board[i][j] && !visited[i][j]) bfs(j, i);
        }
    }

    cout << cnt << "\n" << maxSize << "\n";
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    input();
    solve();

    return 0;
}
