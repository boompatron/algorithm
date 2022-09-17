import sys
from collections import deque
INF = sys.maxsize
dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]


def in_range(x, y, n, m):
    return 0 <= x < m and 0 <= y < n


def bfs(g, n, m):
    dq1, dq2 = deque(), deque()
    distance = [[INF for _ in range(m)] for __ in range(n)]
    distance[0][0] = 1
    dq1.appendleft([0, 0, 1])
    while dq1:
        x, y, dis = dq1.pop()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny, n, m) and distance[ny][nx] > dis + 1:
                if g[ny][nx] == '1':
                    dq2.appendleft([nx, ny, dis + 1])
                else:
                    dq1.appendleft([nx, ny, dis + 1])
                distance[ny][nx] = dis + 1
    while dq2:
        x, y, dis = dq2.pop()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny, n, m) and distance[ny][nx] > dis + 1 and g[ny][nx] == '0':
                distance[ny][nx] = dis + 1
                dq2.appendleft([nx, ny, dis + 1])
    return distance[n - 1][m - 1] if distance[n - 1][m - 1] != INF else -1


def solution():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    g = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(n)]
    print(bfs(g, n, m))


if __name__ == "__main__":
    solution()
