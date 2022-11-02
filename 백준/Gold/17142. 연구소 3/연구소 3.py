import sys
from collections import deque
from itertools import combinations
from copy import deepcopy
dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
MAX_SIZE = 1e7


def solution():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    g = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
    dq = deque()

    def in_range(a, b):
        return 0 <= a < n and 0 <= b < n

    for i in range(n):
        for j in range(n):
            if g[i][j] == 1:
                g[i][j] = -1
            else:
                if g[i][j] == 2:
                    dq.appendleft((j, i, 0))
                g[i][j] = MAX_SIZE
    ans_list = []
    for cur in combinations(dq, m):
        tmpG = deepcopy(g)
        active_virus = deque()
        for c in cur:
            tmpG[c[1]][c[0]] = 0
            active_virus.appendleft(c)
        for d in [v for v in dq if v not in cur]:
            tmpG[d[1]][d[0]] = -2
        while active_virus:
            x, y, t = active_virus.pop()
            nt = t + 1
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if in_range(nx, ny):
                    if tmpG[ny][nx] == -2:
                        active_virus.appendleft((nx, ny, nt))
                        tmpG[ny][nx] = 0
                    elif nt < tmpG[ny][nx]:
                        active_virus.appendleft((nx, ny, nt))
                        tmpG[ny][nx] = nt
        if max(map(max, tmpG)) != MAX_SIZE:
            ans_list.append(max(map(max, tmpG)))
    print(min(ans_list) if ans_list else -1)


if __name__ == '__main__':
    solution()
