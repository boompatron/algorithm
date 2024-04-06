import sys
from collections import deque
dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
n, m = map(int, sys.stdin.readline().rstrip().split())
g = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
d = [[123456789 for _ in range(m)] for __ in range(n)]
visited = [[False for _ in range(m)] for __ in range(n)]


def clear_visited():
    for a in range(n):
        for b in range(m):
            visited[a][b] = False


def in_range(a, b):
    return 0 <= a < m and 0 <= b < n


def virus_spread(a, b):
    size = 1
    dq = deque()
    dq.appendleft([a, b])
    while dq:
        x, y = dq.pop()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and g[ny][nx] == 0 and not visited[ny][nx]:
                dq.appendleft([nx, ny])
                visited[ny][nx] = True
                size += 1
    #print(size)
    return size


wall, vacant, virus = 0, 0, 0
for i in range(n):
    for j in range(m):
        if g[i][j] == 0:
            vacant += 1
        elif g[i][j] == 1:
            wall += 1
        else:
            virus += 1
ans = 123456789
for first in range(n * m):
    if g[first // m][first % m] == 0:
        first_y, first_x = first // m, first % m
    else:
        continue
    for second in range(first + 1, n * m):
        if g[second // m][second % m] == 0:
            second_y, second_x = second // m, second % m
        else:
            continue
        for third in range(second + 1, n * m):
            if g[third // m][third % m] == 0:
                third_y, third_x = third // m, third % m
            else:
                continue
            g[first_y][first_x] = 1
            g[second_y][second_x] = 1
            g[third_y][third_x] = 1
            clear_visited()
            tmp = 0
            for i in range(n):
                for j in range(m):
                    if g[i][j] == 2 and not visited[i][j]:
                        tmp += virus_spread(j, i)
            ans = min(tmp, ans)
            g[first_y][first_x] = 0
            g[second_y][second_x] = 0
            g[third_y][third_x] = 0
            # print("first x, y : ", first_x, first_y, end="|")
            # print("second x, y : ", second_x, second_y, end="|")
            # print("third x, y : ", third_x, third_y, end="|")
            # print("tmp : ", tmp)
print(n * m - (wall + 3) - ans)
