import sys
from collections import deque
dxs, dys = (1, -1, 0, 0), (0, 0, 1, -1)
INF = sys.maxsize
n = 0
cnt = 1


def in_range(a, b):
    return 0 <= a < n and 0 <= b < n


while True:
    n = int(sys.stdin.readline().rstrip())
    if not n:
        exit(0)
    g = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
    dp = [[INF for _ in range(n)] for __ in range(n)]
    visited = [[False for _ in range(n)] for __ in range(n)]
    visited[0][0] = True
    dq = deque()
    dq.appendleft((0, 0, g[0][0]))
    while dq:
        x, y, dis = dq.pop()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and dis + g[ny][nx] < dp[ny][nx]:
                dq.appendleft((nx, ny, dis + g[ny][nx]))
                dp[ny][nx] = dis + g[ny][nx]
    print(f'Problem {cnt}: {dp[n - 1][n - 1]}')
    cnt += 1

