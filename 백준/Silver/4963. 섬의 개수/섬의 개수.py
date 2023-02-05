import sys
from collections import deque
dxs, dys = [1, 1, 1, 0, 0, -1, -1, -1], [1, 0, -1, 1, -1, 1, 0, -1]


def inRange(x, y, width, height):
    return 0 <= x < width and 0 <= y < height


def BFS(x, y, width, height):
    dq = deque()
    dq.appendleft([x, y])
    visited[y][x] = True
    while dq:
        tmp_x, tmp_y = dq.pop()
        for dx, dy in zip(dxs, dys):
            nx, ny = tmp_x + dx, tmp_y + dy
            if inRange(nx, ny, width, height) and not visited[ny][nx] and g[ny][nx]:
                dq.appendleft([nx, ny])
                visited[ny][nx] = True


while True:
    w, h = map(int, sys.stdin.readline().rstrip().split())
    if w == 0 and h == 0:
        break
    g = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(h)]
    visited = [[False for _ in range(w)] for __ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if g[i][j] and not visited[i][j]:
                BFS(j, i, w, h)
                ans += 1
    print(ans)
    