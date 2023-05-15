from collections import deque
dxs, dys = (1, -1, 0, 0), (0, 0, 1, -1)
INF = 10 ** 8


def solve(test_case):
    n = int(input().rstrip())
    g = [list(map(int, input().rstrip())) for _ in range(n)]
    distance = [[INF for _ in range(n)] for __ in range(n)]
    distance[0][0] = 0

    def in_range(a, b):
        return 0 <= a < n and 0 <= b < n

    dq = deque()
    dq.appendleft((0, 0, 0))
    while dq:
        x, y, dis = dq.pop()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and distance[ny][nx] > dis + g[ny][nx]:
                dq.appendleft((nx, ny, dis + g[ny][nx]))
                distance[ny][nx] = dis + g[ny][nx]
    print(f'#{test_case} {distance[n - 1][n - 1]}')


tc = int(input().rstrip())
for t in range(1, tc + 1):
    solve(t)
