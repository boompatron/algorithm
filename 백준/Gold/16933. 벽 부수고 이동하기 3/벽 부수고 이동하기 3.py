import sys
from collections import deque
dxs, dys = (1, 0, -1, 0), (0, 1, 0, -1)
INF = sys.maxsize

n, m, k = map(int, sys.stdin.readline().rstrip().split())
g = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(n)]
dp = [[[INF for _ in range(k + 1)] for __ in range(m)] for ___ in range(n)]
dp[0][0][k] = 1
dq = deque()
dq.appendleft((1, k, 0, 0))
while dq:
    dis, wall, x, y = dq.pop()
    if x == m - 1 and y == n - 1:
        dp[y][x][wall] = min(dp[y][x][wall], dis)
        continue

    for d in range(4):
        nx, ny = x + dxs[d], y + dys[d]
        if 0 <= nx < m and 0 <= ny < n:
            if g[ny][nx] == '0' and dp[ny][nx][wall] > dis + 1:
                dq.appendleft((dis + 1, wall, nx, ny))
                dp[ny][nx][wall] = dis + 1
            elif g[ny][nx] == '1' and wall and dp[ny][nx][wall - 1] > dis + 1:
                if dis % 2:
                    dq.appendleft((dis + 1, wall - 1, nx, ny))
                    dp[ny][nx][wall - 1] = dis + 1
                else:
                    dq.appendleft((dis + 1, wall, x, y))

ans = min([dp[n - 1][m - 1][i] for i in range(k + 1)])
print(ans if ans != INF else -1)

