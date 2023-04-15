import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().rstrip().split())
g = list(map(int, sys.stdin.readline().rstrip().split()))
for comb in combinations(sorted(g), m):
    print(*comb)
