import sys, heapq
from collections import deque
dxs, dys = (1, -1, 0, 0), (0, 0, 1, -1)

n = int(sys.stdin.readline().rstrip())
g = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
# shark = [0, 0, 2]
shark_pos = [0, 0]
shark_size = 2
eaten_fish_num = 0
dq = deque()
for i in range(n):
    for j in range(n):
        if g[i][j]:
            if g[i][j] == 9:
                shark_pos = [j, i]


def in_range(a, b):
    return 0 <= a < n and 0 <= b < n


def find_next_fish():
    visited = [[False for _ in range(n)] for __ in range(n)]
    dq.appendleft((*shark_pos, 0))
    visited[shark_pos[1]][shark_pos[0]] = True
    pos = [n, n, n * n + 1]
    while dq:
        x, y, d = dq.pop()
        if g[y][x] and g[y][x] < shark_size:
            if d < pos[2] or (d == pos[2] and y < pos[1] or (d == pos[2] and y == pos[1] and x < pos[0])):
                pos = [x, y, d]
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[ny][nx] and g[ny][nx] <= shark_size:
                dq.appendleft((nx, ny, d + 1))
                visited[ny][nx] = True
    return pos


cnt = 0
while True:
    g[shark_pos[1]][shark_pos[0]] = 0
    xx, yy, dd = find_next_fish()
    eaten_fish_num += 1
    if dd == n * n + 1:
        break
    cnt += dd
    if eaten_fish_num == shark_size:
        shark_size += 1
        eaten_fish_num = 0
    shark_pos = [xx, yy]
    g[yy][xx] = 9
print(cnt)
