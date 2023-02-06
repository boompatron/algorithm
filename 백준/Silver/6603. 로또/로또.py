import sys
from itertools import combinations


def solution():
    while True:
        g = list(map(int, sys.stdin.readline().rstrip().split()))
        if len(g) == 1:
            exit(0)
        for c in combinations(g[1:], 6):
            print(*c)
        print()


if __name__ == "__main__":
    solution()
