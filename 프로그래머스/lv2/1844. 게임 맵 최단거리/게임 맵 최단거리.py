from collections import deque
dxs, dys = (1, -1, 0, 0), (0, 0, 1, -1)


def solution(maps):
    dq = deque()
    n, m = len(maps), len(maps[0])
    distance = [[n * m + 1 for _ in range(m)] for __ in range(n)]
    distance[0][0] = 1
    dq.appendleft((0, 0, 1))
    while dq:
        x, y, dis = dq.pop()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] and distance[ny][nx] > dis + 1:
                distance[ny][nx] = dis + 1
                dq.appendleft((nx, ny, dis + 1))
    return distance[n - 1][m - 1] if distance[n - 1][m - 1] != n * m + 1 else -1