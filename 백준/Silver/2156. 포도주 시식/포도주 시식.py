import sys
n = int(sys.stdin.readline().rstrip())
wine, dp = [0, 0], [0 for _ in range(n + 2)]
for i in range(n):
    w = int(sys.stdin.readline().rstrip())
    wine.append(w)
for i in range(2, n + 2):
    dp[i] = max(dp[i - 2] + wine[i], dp[i - 3] + wine[i] + wine[i - 1], dp[i - 1])
print(max(dp))
