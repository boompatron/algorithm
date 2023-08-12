import sys
from collections import deque
dxs, dys = (1, 0, -1, 0), (0, 1, 0, -1)
INF = sys.maxsize

n, m = map(int, sys.stdin.readline().split())
g = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
distance = [[INF for _ in range(m)] for __ in range(n)]
dq = deque()
for i in range(n):
    for j in range(m):
        if g[i][j] == 2:
            dq.appendleft((j, i, 0))
            distance[i][j] = 0
        elif g[i][j] == 0:
            distance[i][j] = 0


def in_range(a, b):
    return 0 <= a < m and 0 <= b < n


while dq:
    x, y, d = dq.pop()
    for dx, dy in zip(dxs, dys):
        nx, ny, nd = x + dx, y + dy, d + 1
        if in_range(nx, ny) and g[ny][nx] == 1 and distance[ny][nx] > nd:
            dq.appendleft((nx, ny, nd))
            distance[ny][nx] = nd

for i in distance:
    for j in i:
        print(j if j != INF else -1, end=' ')
    print()
