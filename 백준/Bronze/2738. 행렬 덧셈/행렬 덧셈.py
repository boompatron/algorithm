import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
g1 = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
g2 = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        print(g1[i][j] + g2[i][j], end=' ')
    print()
