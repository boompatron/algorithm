import sys
from collections import deque
dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
T = int(sys.stdin.readline().rstrip())
g = [[0 for _ in range(51)] for __ in range(51)]
visited = [[False for _ in range(51)] for __ in range(51)]


def clearList(n, m):
    for i in range(n):
        for j in range(m):
            visited[i][j] = False
            g[i][j] = 0


def inRange(x, y, width, height):
    return 0 <= x < width and 0 <= y < height


def BFS(x, y, width, height):
    dq = deque()
    dq.appendleft([x, y])
    while dq:
        tmp_x, tmp_y = dq.pop()
        for dx, dy in zip(dxs, dys):
            nx, ny = tmp_x + dx, tmp_y + dy
            if inRange(nx, ny, width, height) and not visited[ny][nx] and g[ny][nx]:
                dq.appendleft([nx, ny])
                visited[ny][nx] = True


for ___ in range(T):
    M, N, K = map(int, sys.stdin.readline().rstrip().split())
    clearList(N, M)
    for _ in range(K):
        xx, yy = map(int, sys.stdin.readline().rstrip().split())
        g[yy][xx] = 1
    ans = 0
    for i in range(N):
        for j in range(M):
            if g[i][j] and not visited[i][j]:
                BFS(j, i, M, N)
                ans += 1
    print(ans)
