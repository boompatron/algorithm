import sys


def solution():
    n = int(sys.stdin.readline().rstrip())
    g = list(map(int, sys.stdin.readline().rstrip().split()))
    g.insert(0, 0)
    dp = [0 for _ in range(n + 1)]
    for i in range(n + 1):
        tmp = 0
        for j in range(i):
            if g[i] < g[j] and dp[j] + 1 > tmp:
                tmp = dp[j] + 1
        dp[i] = tmp
    print(max(dp) + 1)


if __name__ == "__main__":
    solution()