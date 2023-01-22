import sys


def solution():
    n = int(sys.stdin.readline().rstrip())
    g = list(map(int, sys.stdin.readline().rstrip().split()))
    for i in range(1, n):
        g[i] = max(g[i], g[i - 1] + g[i])
    print(max(g))


if __name__ == '__main__':
    solution()
