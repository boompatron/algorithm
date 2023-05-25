import sys
from copy import deepcopy
dxs, dys = (1, 0, -1, 0), (0, 1, 0, -1)
cctv_direction_range = {1: 4, 2: 2, 3: 4, 4: 4, 5: 1}


n, m = map(int, sys.stdin.readline().rstrip().split())
g = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
cctv = []
for i in range(n):
    for j in range(m):
        if 0 < g[i][j] < 6:
            cctv.append((j, i, g[i][j]))
k = len(cctv)
ans = n * m + 1


def in_range(a, b):
    return 0 <= a < m and  0 <= b < n


def proceed(a, b, office, direction):
    dx, dy = dxs[direction], dys[direction]
    nx, ny = a, b
    while in_range(nx, ny) and g[ny][nx] != 6:
        office[ny][nx] = 7
        nx += dx
        ny += dy


def watch(a, b, office, cctv_num, direction):
    proceed(a, b, office, direction)
    if cctv_num == 2:
        proceed(a, b, office, (direction + 2) % 4)
    elif cctv_num == 3:
        proceed(a, b, office, (direction + 1) % 4)
    elif cctv_num == 4:
        proceed(a, b, office, (direction + 1) % 4)
        proceed(a, b, office, (direction - 1) % 4)
    elif cctv_num == 5:
        for d in range(1, 4):
            proceed(a, b, office, (direction + d) % 4)


def dfs(depth, office):
    if depth == k:
        global ans
        s = sum([1 for a in range(m) for b in range(n) if office[b][a] == 0])
        ans = min(ans, s)
        return
    a, b, num = cctv[depth]
    for d in range(cctv_direction_range[g[b][a]]):
        tmp_office = deepcopy(office)
        watch(a, b, tmp_office, num, d)
        dfs(depth + 1, tmp_office)


dfs(0, g)
print(ans)