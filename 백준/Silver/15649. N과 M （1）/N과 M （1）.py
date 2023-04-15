import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().rstrip().split())
for perm in permutations([i for i in range(1, n + 1)], m):
    print(*perm)
