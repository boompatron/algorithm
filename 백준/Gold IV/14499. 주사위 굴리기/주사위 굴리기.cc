#include <iostream>
using namespace std;

int dxs[4] = {1, 0, -1, 0}, dys[4] = {0, 1, 0, -1};
int n, m, x, y, k;

bool inRange(int a, int b)
{
    return a >= 0 && a < m && b >= 0 && b < n;
}
int dice[4][3], board[21][21];

int changeDir(int ori)
{
    if (ori == 1) return 0;
    else if (ori == 4) return 1;
    else return ori;
}

void rollUp()
{
    int tmp = dice[0][1];
    for (int i = 0; i < 3; i++)
    {
        dice[i][1] = dice[i + 1][1];
    }
    dice[3][1] = tmp;
}

void rollDown()
{
    int tmp = dice[3][1];
    for (int i = 3; i > 0 ; i--)
    {
        dice[i][1] = dice[i - 1][1];
    }
    dice[0][1] = tmp;
}

void rollRight()
{
    int tmp = dice[1][0];
    for (int i = 0; i < 2; i++)
    {
        dice[1][i] = dice[1][i + 1];
    }
    dice[1][2] = dice[3][1];
    dice[3][1] = tmp;
}

void rollLeft()
{
    int tmp = dice[1][2];
    for (int i = 2; i > 0; i--)
    {
        dice[1][i] = dice[1][i - 1];
    }
    dice[1][0] = dice[3][1];
    dice[3][1] = tmp;
}

void rollDice(int dir)
{
    if (dir == 0) rollRight();
    else if (dir == 1) rollDown();
    else if (dir == 2) rollLeft();
    else rollUp();
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    cin >> n >> m >> y >> x >> k;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < m; j++)
        {
            cin >> board[i][j];
        }
    }

    int dir;
    for (int i = 0; i < k; i++)
    {
        cin >> dir;
        dir = changeDir(dir);
        int nx = x + dxs[dir], ny = y + dys[dir];

        if (inRange(nx, ny))
        {
            x = nx, y = ny;
            rollDice(dir);

            if (board[y][x] == 0)   board[y][x] = dice[3][1];
            else {
                dice[3][1] = board[y][x];
                board[y][x] = 0;
            }

            cout << dice[1][1] << "\n";
        }
    }


    return 0;
}
