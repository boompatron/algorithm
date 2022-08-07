import sys
from collections import Counter


def solution():
    n = int(sys.stdin.readline().rstrip())
    g = Counter(map(int, sys.stdin.readline().rstrip().split()))
    v = int(sys.stdin.readline().rstrip())
    print(g[v])


if __name__ == "__main__":
    solution()
