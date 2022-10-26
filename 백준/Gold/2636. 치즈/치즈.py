import sys
from collections import deque
dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
n, m = map(int, sys.stdin.readline().rstrip().split())
g = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for __ in range(n)]


def in_range(a, b):
    return 0 <= a < m and 0 <= b < n


def clear_visited():
    for a in range(n):
        for b in range(m):
            visited[a][b] = False


def spread_air():
    dq = deque()
    dq.appendleft([0, 0])
    while dq:
        x, y = dq.pop()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and (g[ny][nx] == 0 or g[ny][nx] == 2) and not visited[ny][nx]:
                g[ny][nx] = 2
                dq.appendleft([nx, ny])
                visited[ny][nx] = True


def check(x, y):
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and g[ny][nx] == 2:
            g[y][x] = 3
            return


def melt():
    melted_cheese = 0
    for a in range(n):
        for b in range(m):
            if g[a][b] == 3:
                g[a][b] = 2
                melted_cheese += 1
    return melted_cheese



ans, time = 0, 0
while True:
    clear_visited()
    time += 1
    spread_air()
    for i in range(n):
        for j in range(m):
            if g[i][j] == 1:
                check(j, i)
    tmp = melt()
    if tmp == 0:
        break
    ans = tmp
print(time - 1)
print(ans)
