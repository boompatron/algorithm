def solution(m, n, puddles):
    g = [[1 for _ in range(m)] for __ in range(n)]
    for x, y in puddles:
        g[y - 1][x - 1] = 0
    dp = [[0 for _ in range(m)] for __ in range(n)]
    for i in range(n):
        if not g[i][0]:
            break
        dp[i][0] = 1
    for i in range(m):
        if not g[0][i]:
            break
        dp[0][i] = 1
    for i in range(1, n):
        for j in range(1, m):
            if g[i][j]:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000007
    return dp[n - 1][m - 1] % 1000000007