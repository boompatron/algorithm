import sys
from collections import deque
from itertools import combinations
from copy import deepcopy
dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]


def solution():
    n, m = map(int, sys.stdin.readline().rstrip().split())

    def in_range(a, b):
        return 0 <= a < n and 0 <= b < n

    g = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
    virus = deque()
    for i in range(n):
        for j in range(n):
            if g[i][j] == 1:
                g[i][j] = -1
            elif g[i][j] == 2:
                virus.append([j, i, 0])
                g[i][j] = 1e7
            else:
                g[i][j] = 1e7
    ans_list = []
    for cur in combinations(virus, m):
        tmpG = deepcopy(g)
        dq = deque()
        for c in cur:
            dq.appendleft(c)
            tmpG[c[1]][c[0]] = 0
        while dq:
            x, y, t = dq.pop()
            nt = t + 1
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if in_range(nx, ny) and tmpG[ny][nx] > nt:
                    dq.appendleft([nx, ny, nt])
                    tmpG[ny][nx] = nt
        max_val = max(map(max, tmpG))
        if max_val != 1e7:
            ans_list.append(max_val)
    print(min(ans_list) if ans_list else -1)


if __name__ == '__main__':
    solution()
