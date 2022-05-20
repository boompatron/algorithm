import sys
from collections import deque
from copy import deepcopy
dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
n, m = map(int, sys.stdin.readline().rstrip().split())
g = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
g[0][0] = 2
g_next = deepcopy(g)
visited = [[False for _ in range(m)] for __ in range(n)]


def print_g():
    for a in g:
        for b in a:
            print(b, end=" ")
        print()
    print("================")


def in_range(a, b):
    return 0 <= a < m and 0 <= b < n


def clear_visited():
    for a in range(n):
        for b in range(m):
            visited[a][b] = False


def air_spread():
    dq = deque()
    dq.appendleft([0, 0])
    visited[0][0] = True
    while dq:
        x, y = dq.pop()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[ny][nx] and (g[ny][nx] == 0 or g[ny][nx] == 2):
                g[ny][nx] = 2
                visited[ny][nx] = True
                dq.appendleft([nx, ny])


def melt(a, b):
    contact = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = a + dx, b + dy
        if in_range(nx, ny) and g[ny][nx] == 2:
            contact += 1
    if contact >= 2:
        g[b][a] = 0
        return True
    return False


ans = 0
while True:
    melted_cheese = 0
    clear_visited()
    air_spread()
    for i in range(n):
        for j in range(m):
            if g[i][j] == 1:
                melted_cheese += int(melt(j, i))
    if melted_cheese == 0:
        break
    ans += 1
print(ans)
