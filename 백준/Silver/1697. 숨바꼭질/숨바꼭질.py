import sys
from collections import deque
dxs = [1, -1, 0]


def in_range(x):
    return 0 <= x < 10 ** 5 + 1


def bfs(n, k):
    g = [sys.maxsize for _ in range(10 ** 5 + 1)]
    dq = deque()
    dq.appendleft([n, 0])
    g[n] = 0
    while dq:
        pos, cnt = dq.pop()
        for dx in dxs:
            nx = pos + (dx if dx else pos)
            if in_range(nx) and g[nx] > cnt + 1:
                g[nx] = cnt + 1
                dq.appendleft([nx, cnt + 1])
    print(g[k])


def solition():
    n, k = map(int, sys.stdin.readline().rstrip().split())
    bfs(n, k)


if __name__ == "__main__":
    solition()