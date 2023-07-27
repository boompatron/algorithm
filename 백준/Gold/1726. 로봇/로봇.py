import sys
from collections import deque
INF = sys.maxsize
change_dir = {1: 0, 2: 2, 3: 1, 4: 3}
dxs, dys = (1, 0, -1, 0), (0, 1, 0, -1)

n, m = map(int, sys.stdin.readline().rstrip().split())
g = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
sy, sx, sd = map(int, sys.stdin.readline().rstrip().split())
ey, ex, ed = map(int, sys.stdin.readline().rstrip().split())

sy -= 1; sx -= 1; sd = change_dir[sd]
ey -= 1; ex -= 1; ed = change_dir[ed]
ans = INF
visited = [[[0 for _ in range(4)] for __ in range(m)] for ___ in range(n)]
visited[sy][sx][sd] = True


def in_range(a, b):
    return 0 <= a < m and 0 <= b < n


dq = deque()
dq.appendleft((sx, sy, sd, 0))

while dq:
    x, y, d, step = dq.pop()

    if x == ex and y == ey and d == ed:
        ans = min(ans, step)
        break

    for i in range(1, 4):
        nx, ny = x + dxs[d] * i, y + dys[d] * i
        if in_range(nx, ny):
            if g[ny][nx]:
                break
            elif not visited[ny][nx][d]:
                visited[ny][nx][d] = True
                dq.appendleft((nx, ny, d, step + 1))

    for i in (1, -1):
        nd = (d + i) % 4
        if not visited[y][x][nd]:
            visited[y][x][nd] = True
            dq.appendleft((x, y, nd, step + 1))
print(ans)
