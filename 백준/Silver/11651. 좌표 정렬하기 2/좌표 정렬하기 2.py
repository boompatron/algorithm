import sys


def solution():
    n = int(sys.stdin.readline().rstrip())
    g = [[] for _ in range(n)]
    for i in range(n):
        g[i] = list(map(int, sys.stdin.readline().rstrip().split()))
    for i in sorted(g, key=lambda x: (x[1], x[0])):
        print(' '.join(map(str, i)))


if __name__ == "__main__":
    solution()