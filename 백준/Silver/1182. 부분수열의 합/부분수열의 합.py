import sys
from itertools import combinations


def solution():
    n, s = map(int, sys.stdin.readline().rstrip().split())
    g = list(map(int, sys.stdin.readline().rstrip().split()))
    cnt = 0
    for i in range(1, n + 1):
        for c in combinations(g, i):
            if sum(c) == s:
                cnt += 1
    print(cnt)


if __name__ == "__main__":
    solution()
