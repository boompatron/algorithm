import sys
from collections import deque
dxs, dys = (1, -1, 0, 0), (0, 0, 1, -1)

n, m, t = map(int, sys.stdin.readline().rstrip().split())
g = [deque(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
inst = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(t)]
zero_num = 0


def in_range(a, b):
    return 0 <= a < m and 0 <= b < n


def work():
    visited = [[False for _ in range(m)] for __ in range(n)]
    get_avg = True
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and g[i][j]:
                if bfs(j, i, g[i][j], visited):
                    get_avg = False
    global zero_num
    zero_num = sum([g[i].count(0) for i in range(n)])
    if get_avg and zero_num < n * m:
        avg = sum([sum([i for i in j]) for j in g]) / sum([sum([1 for i in j if i]) for j in g])
        for i in range(n):
            for j in range(m):
                if g[i][j]:
                    if g[i][j] > avg:
                        g[i][j] -= 1
                    elif g[i][j] < avg:
                        g[i][j] += 1


def bfs(a, b, c, v):
    dq = deque()
    dq.appendleft([a, b])
    flag = False
    while dq:
        j, i = dq.pop()
        for dx, dy in zip(dxs, dys):
            nx, ny = (j + dx) % m, i + dy
            if in_range(nx, ny) and g[ny][nx] == c and not v[ny][nx]:
                v[ny][nx] = True
                flag = True
                g[ny][nx] = 0
                dq.appendleft([nx, ny])
    return flag


for x, d, k in inst:
    if zero_num == n * m:
        continue
    tmp = 1
    while tmp * x < n + 1:
        g[tmp * x - 1].rotate(-k if d else k)
        tmp += 1
    work()
print(sum([sum([i for i in j]) for j in g]))
