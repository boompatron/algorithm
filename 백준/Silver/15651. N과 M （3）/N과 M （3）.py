import sys
from itertools import product

n, m = map(int, sys.stdin.readline().rstrip().split())
for prod in product([i for i in range(1, n + 1)], repeat=m):
    print(*prod)
