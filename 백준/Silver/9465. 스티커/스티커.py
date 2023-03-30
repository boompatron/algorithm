import sys
t = int(sys.stdin.readline().rstrip())
while t:
    n = int(sys.stdin.readline().rstrip())
    dp = [[0 for _ in range(n + 22)] for __ in range(2)]
    sticker = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(2)]
    sticker[0].insert(0, 0)
    sticker[0].insert(0, 0)
    sticker[1].insert(0, 0)
    sticker[1].insert(0, 0)
    for i in range(2, n + 2):
        dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + sticker[0][i]
        dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + sticker[1][i]
    print(max(dp[0][n + 1], dp[1][n + 1]))
    t -= 1
