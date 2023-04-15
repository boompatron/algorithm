import sys
from itertools import combinations_with_replacement

n, m = map(int, sys.stdin.readline().rstrip().split())
for comb_with_rep in combinations_with_replacement([i for i in range(1, n + 1)], m):
    print(*comb_with_rep)
