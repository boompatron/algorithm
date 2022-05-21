import sys
from collections import deque
h, w = map(int, sys.stdin.readline().rstrip().split())
block = list(map(int, sys.stdin.readline().rstrip().split()))
g = [[0 for _ in range(w)] for __ in range(h)]
for i in range(h):
    for j in range(w):
        if block[j] > i:
            g[i][j] = 1
for i in range(h):
    do_count = False
    dq = deque()
    for j in range(w):
        if g[i][j] == 1:
            if do_count and len(dq):
                while dq:
                    x, y = dq.pop()
                    g[y][x] = 2
            if (j > 0 and g[i][j - 1] == 0) or j == 0:
                do_count = not do_count
        elif g[i][j] == 0 and do_count:
            dq.append([j, i])
ans = sum([1 for i in range(h) for j in range(w) if g[i][j] == 2])
print(ans)
