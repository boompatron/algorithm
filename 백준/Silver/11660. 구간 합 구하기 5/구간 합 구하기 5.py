import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
g = [[0 for _ in range(n)] for __ in range(n + 1)]
g[0].append(0)
for i in range(n):
    g[i + 1] = list(map(int, sys.stdin.readline().rstrip().split()))
    g[i + 1].insert(0, 0)
for i in range(1, n + 1):
    for j in range(2, n + 1):
        g[i][j] += g[i][j - 1]
for j in range(1, n + 1):
    for i in range(2, n + 1):
        g[i][j] += g[i - 1][j]
for i in range(m):
    y1, x1, y2, x2 = map(int, sys.stdin.readline().rstrip().split())
    ans = g[y2][x2] - g[y2][x1 - 1] - g[y1 - 1][x2] + g[y1 - 1][x1 - 1]
    print(ans)
