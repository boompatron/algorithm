import sys
from itertools import combinations_with_replacement

n, m = map(int, sys.stdin.readline().rstrip().split())
g = list(map(int, sys.stdin.readline().rstrip().split()))
for comb_with_rep in combinations_with_replacement(sorted(g), m):
    print(*comb_with_rep)
