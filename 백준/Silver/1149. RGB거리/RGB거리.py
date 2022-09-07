import sys
dxs = [-2, -1, 1, 2]


def in_range(x):
    return 0 <= x < 3


def solution():
    n = int(sys.stdin.readline().rstrip())
    g = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
    for i in range(1, n):
        for x in range(3):
            tmp = sys.maxsize
            for dx in dxs:
                nx = x + dx
                if in_range(nx) and g[i - 1][nx] < tmp:
                    tmp = g[i - 1][nx]
            g[i][x] += tmp
    print(min(g[n - 1]))


if __name__ == "__main__":
    solution()
