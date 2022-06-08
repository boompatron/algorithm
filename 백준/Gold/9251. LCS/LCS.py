import sys
from collections import deque
dxs, dys = [-1, 0], [0, -1]
l1 = sys.stdin.readline().rstrip()
l2 = sys.stdin.readline().rstrip()
g = [[0 for i in range(len(l2) + 1)] for j in range(len(l1) + 1)]
ans = ""


def print_g():
    print(end="\tl2\t")
    for i in range(len(l2)):
        print(l2[i], end="\t")
    print()
    for i in range(len(l2) + 1):
        if i:
            print(l1[i - 1], end="\t")
        else:
            print("l1", end="\t")
        for j in range(len(l1) + 1):
            print(g[i][j], end="\t")
        print()


for i in range(1, len(l1) + 1):
    for j in range(1, len(l2) + 1):
        if l1[i - 1] == l2[j - 1]:
            g[i][j] = g[i - 1][j - 1] + 1
        else:
            g[i][j] = max(g[i - 1][j], g[i][j - 1])
print(g[len(l1)][len(l2)])
