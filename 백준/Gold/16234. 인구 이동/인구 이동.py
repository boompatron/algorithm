import sys
from collections import deque
from collections import defaultdict
dxs, dys = (1, -1, 0, 0), (0, 0, 1, -1)


n, l, r = map(int, sys.stdin.readline().rstrip().split())
g = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
cnt = -1
dq = deque()


def in_range(a, b):
    return 0 <= a < n and 0 <= b < n


def check(a, b):
    for dx, dy in zip(dxs, dys):
        nx, ny = a + dx, b + dy
        if in_range(nx, ny) and l <= abs(g[b][a] - g[ny][nx]) <= r:
            return True
    return False


def bfs(a, b, dd):
    visited = set()
    population = g[b][a]
    dq.appendleft((a, b))
    visited.add((a, b))
    while dq:
        x, y = dq.pop()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and l <= abs(g[ny][nx] - g[y][x]) <= r and (nx, ny) not in visited:
                dq.appendleft((nx, ny))
                population += g[ny][nx]
                visited.add((nx, ny))
    total_population = population // len(visited)
    for v in visited:
        dd[(a, b, total_population)].add(v)


flag = True
while flag:
    cnt += 1
    d = defaultdict(set)
    flag = False
    for i in range(n):
        for j in range(n):
            if check(j, i):
                bfs(j, i, d)
                flag = True
    for key in d.keys():
        x, y, t = key
        for j, i in d[key]:
            g[i][j] = t
print(cnt)
