import sys
from collections import deque
from itertools import combinations
dxs, dys = (1, -1, 0, 0), (0, 0, 1, -1)

n, m = map(int, sys.stdin.readline().rstrip().split())
g = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
empty, empty_cnt, viruses, ans = set(), 0, set(), 0
for i in range(n):
    for j in range(m):
        if g[i][j] == 0:
            empty.add((j, i))
            empty_cnt += 1
        elif g[i][j] == 2:
            viruses.add((j, i))
for w1, w2, w3 in combinations(empty, 3):
    visited = [[False for _ in range(m)] for __ in range(n)]
    g[w1[1]][w1[0]] = g[w2[1]][w2[0]] = g[w3[1]][w3[0]] = 1
    dq = deque()
    for virus in viruses:
        dq.appendleft(virus)
    cnt = 0
    while dq:
        x, y = dq.pop()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and g[ny][nx] == 0 and not visited[ny][nx]:
                visited[ny][nx] = True
                dq.appendleft((nx, ny))
                cnt += 1
    ans = max(ans, empty_cnt - cnt)
    g[w1[1]][w1[0]] = g[w2[1]][w2[0]] = g[w3[1]][w3[0]] = 0
print(ans - 3)
