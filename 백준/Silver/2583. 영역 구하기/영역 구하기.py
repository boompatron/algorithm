import sys
from collections import deque
visited, g = [[]], [[]]
n, m = 0, 0
dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]


def in_range(x, y):
    global n, m
    return 0 <= x < m and 0 <= y < n


def bfs(xx, yy):
    global g, visited, n, m
    dq = deque()
    dq.appendleft([xx, yy])
    cnt = 1
    visited[yy][xx] = True
    while dq:
        x, y = dq.pop()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not g[ny][nx] and not visited[ny][nx]:
                dq.appendleft([nx, ny])
                visited[ny][nx] = True
                cnt += 1
    return cnt


def solution():
    global n, m, g, visited
    n, m, k = map(int, sys.stdin.readline().rstrip().split())
    g, visited = [[False for _ in range(m)] for __ in range(n)], [[False for _ in range(m)] for __ in range(n)]
    while k:
        x1, y1, x2, y2 = map(int, sys.stdin.readline().rstrip().split())
        for y in range(y1, y2):
            for x in range(x1, x2):
                g[y][x] = True
        k -= 1
    ans = []
    for y, e1 in enumerate(g):
        for x, e2 in enumerate(e1):
            if not e2 and not visited[y][x]:
                ans.append(bfs(x, y))
    print(len(ans))
    for i in sorted(ans):
        print(i, end=" ")


if __name__ == "__main__":
    solution()
