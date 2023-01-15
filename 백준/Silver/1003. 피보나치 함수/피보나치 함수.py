import sys


def solution():
    tc = int(sys.stdin.readline().rstrip())
    g = []
    for _ in range(tc):
        n = int(sys.stdin.readline().rstrip())
        g.append(n)
    dp = [[0 for _ in range(max(max(g) + 1, 2))] for __ in range(2)]
    dp[0][0] = dp[1][1] = 1
    dp[0][1] = dp[1][0] = 0
    for i in range(2, max(g) + 1):
        dp[0][i] = dp[0][i - 1] + dp[0][i - 2]
        dp[1][i] = dp[1][i - 1] + dp[1][i - 2]
    for i in g:
        print(f'{dp[0][i]} {dp[1][i]}')


if __name__ == '__main__':
    solution()
