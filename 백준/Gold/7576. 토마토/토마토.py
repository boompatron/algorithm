import sys
from collections import deque
INF = sys.maxsize
dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]


def in_range(x, y, n, m):
    return 0 <= x < m and 0 <= y < n


def bfs(g, n, m, tomatoes):
    ripe_day = [[INF for _ in range(m)] for __ in range(n)]
    for t in tomatoes:
        ripe_day[t[1]][t[0]] = 0
    while tomatoes:
        x, y, day = tomatoes.pop()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny, n, m) and g[ny][nx] == 0 and ripe_day[ny][nx] > day + 1:
                tomatoes.appendleft([nx, ny, day + 1])
                ripe_day[ny][nx] = day + 1
    ans = 0
    for y, e1 in enumerate(ripe_day):
        for x, e2 in enumerate(e1):
            if g[y][x] == 0:
                ans = max(ans, e2)
    return ans if ans != INF else -1


def solution():
    m, n = map(int, sys.stdin.readline().rstrip().split())
    g = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
    tomatoes = deque()
    for y, e1 in enumerate(g):
        for x, e2 in enumerate(e1):
            if e2 == 1:
                tomatoes.appendleft([x, y, 0])
    print(bfs(g, n, m, tomatoes))


if __name__ == "__main__":
    solution()
