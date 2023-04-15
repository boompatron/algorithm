import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().rstrip().split())
g = list(map(int, sys.stdin.readline().rstrip().split()))
for perm in permutations(sorted(g), m):
    print(*perm)
