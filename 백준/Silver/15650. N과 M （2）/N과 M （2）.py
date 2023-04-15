import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().rstrip().split())
for comb in combinations([i for i in range(1, n + 1)], m):
    print(*comb)
    