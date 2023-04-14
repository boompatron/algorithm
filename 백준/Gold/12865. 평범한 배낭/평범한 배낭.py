import sys
import heapq


def solution():
    n, k = map(int, sys.stdin.readline().rstrip().split())
    dp = [[0 for _ in range(k + 1)] for __ in range(n + 1)]
    hq = []
    for i in range(n):
        w, v = map(int, sys.stdin.readline().rstrip().split())
        heapq.heappush(hq, [v, w])
    for i in range(1, n + 1):
        v, w = heapq.heappop(hq)
        for j in range(1, k + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v) if w <= j else dp[i - 1][j]
    print(dp[n][k])


if __name__ == "__main__":
    solution()
