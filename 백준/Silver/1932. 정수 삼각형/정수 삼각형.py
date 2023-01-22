import sys


def solution():
    n = int(sys.stdin.readline().rstrip())
    # g = [[0 for _ in range(__ + 1)] for __ in range(n)]
    g = [[] for _ in range(n)]
    for i in range(n):
        g[i] = list(map(int, sys.stdin.readline().rstrip().split()))
    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            g[i][j] += max(g[i + 1][j], g[i + 1][j + 1])
    print(g[0][0])


if __name__ == "__main__":
    solution()
