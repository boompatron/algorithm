import sys


def solution():
    n, k = map(int, sys.stdin.readline().rstrip().split())
    dp = [0 for _ in range(k + 1)]
    coins = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
    dp[0] = 1
    for coin in coins:
        for i in range(coin, k + 1):
            if i >= coin:
                dp[i] += dp[i - coin]
    print(dp[k])


if __name__ == '__main__':
    solution()
