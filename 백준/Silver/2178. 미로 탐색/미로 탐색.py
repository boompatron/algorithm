import sys
from collections import deque
dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
n, m = map(int, sys.stdin.readline().rstrip().split())
g = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(n)]
d = [[123456789 for _ in range(m)] for __ in range(n)]


def in_range(a, b):
    return 0 <= a < m and 0 <= b < n


def bfs():
    dq = deque()
    dq.appendleft([0, 0, 0])
    while dq:
        x, y, length = dq.pop()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and g[ny][nx] == '1' and d[ny][nx] > length + 1:
                dq.appendleft([nx, ny, length + 1])
                d[ny][nx] = length + 1


bfs()
print(d[n - 1][m - 1] + 1)
