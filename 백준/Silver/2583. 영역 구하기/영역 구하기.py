import sys
from collections import deque
dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
n, m, k = map(int, sys.stdin.readline().rstrip().split())
g, visited = [[True for _ in range(m)] for __ in range(n)], [[False for _ in range(m)] for __ in range(n)]
ans = []
for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            g[i][j] = False


def in_range(a, b):
    return 0 <= a < m and 0 <= b < n


def bfs(a, b):
    cnt = 1
    visited[b][a] = True
    dq = deque()
    dq.appendleft([a, b])
    while dq:
        x, y = dq.pop()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[ny][nx] and g[ny][nx]:
                dq.appendleft([nx, ny])
                visited[ny][nx] = True
                cnt += 1
    return cnt


for i in range(n):
    for j in range(m):
        if g[i][j] and not visited[i][j]:
            ans.append(bfs(j, i))
print(len(ans))
for i in sorted(ans):
    print(i)
