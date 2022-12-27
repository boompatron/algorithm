import sys
from collections import deque
dxs, dys = [1, 2, 2, 1, -1, -2, -2, -1], [-2, -1, 1, 2, 2, 1, -1, -2]


def in_range(a, b, n):
    return 0 <= a < n and 0 <= b < n


def bfs(start, end, n):
    g = [[sys.maxsize for _ in range(n)] for __ in range(n)]
    dq = deque()
    dq.appendleft([0, *start])
    while dq:
        d, x ,y = dq.pop()
        if x == end[0] and y == end[1]:
            return d
        nd = d + 1
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny, n) and g[ny][nx] > nd:
                g[ny][nx] = nd
                dq.appendleft([nd, nx, ny])
    return g[end[1]][end[0]]

def solution():
    n = int(sys.stdin.readline().rstrip())
    start = list(map(int, sys.stdin.readline().rstrip().split()))
    end = list(map(int, sys.stdin.readline().rstrip().split()))
    print(bfs(start, end, n))


if __name__ == '__main__':
    tc = int(sys.stdin.readline().rstrip())
    while tc:
        solution()
        tc -= 1