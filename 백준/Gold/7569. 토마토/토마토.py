import sys
from collections import deque
dxs, dys, dzs = [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]
m, n, h = map(int, sys.stdin.readline().rstrip().split())
g = [[[0 for _ in range(m)] for __ in range(n)] for ___ in range(h)]
# visited = [[[False for _ in range(m)] for __ in range(n)] for ___ in range(h)]
day = [[[123456789 for _ in range(m)] for __ in range(n)] for ___ in range(h)]
tomato = deque()
ans = 0
for i in range(h):
    for j in range(n):
        g[i][j] = list(map(int, sys.stdin.readline().rstrip().split()))
        for k in range(m):
            if g[i][j][k] == 1:
                tomato.appendleft([k, j, i, 0])
                day[i][j][k] = 0


def in_range(a, b, c):
    return 0 <= a < m and 0 <= b < n and 0 <= c < h


def ripe():
    global ans, day, g
    while tomato:
        x, y, z, d = tomato.pop()
        ans = max(ans, d)
        for dx, dy, dz in zip(dxs, dys, dzs):
            nx, ny, nz = x + dx, y + dy, z + dz
            if in_range(nx, ny, nz) and g[nz][ny][nx] == 0 and day[nz][ny][nx] > d + 1:
                day[nz][ny][nx] = d + 1
                tomato.appendleft([nx, ny, nz, d + 1])


ripe()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if day[i][j][k] == 123456789 and g[i][j][k] == 0:
                print(-1)
                exit(0)
print(ans)
