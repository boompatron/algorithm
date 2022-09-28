import sys


def solution():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    g = list(map(int, sys.stdin.readline().rstrip().split()))
    for i in range(1, n):
        g[i] += g[i - 1]
    g.insert(0, 0)
    while m:
        a, b = map(int, sys.stdin.readline().rstrip().split())
        print(g[b] - g[a - 1])
        m -= 1


if __name__ == '__main__':
    solution()