import sys
from itertools import product

n, m = map(int, sys.stdin.readline().rstrip().split())
g = list(map(int, sys.stdin.readline().rstrip().split()))
for prod in product(sorted(g), repeat=m):
    print(*prod)
