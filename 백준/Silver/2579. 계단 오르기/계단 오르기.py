import sys


def solution():
    n = int(sys.stdin.readline().rstrip())
    stairs, dp = [0, 0, 0], [0 for _ in range(n + 3)]
    for i in range(n):
        tmp = int(sys.stdin.readline().rstrip())
        stairs.append(tmp)
    for i in range(3, n + 3):
        dp[i] = max(dp[i - 2], dp[i - 3] + stairs[i - 1]) + stairs[i]
    print(dp[-1])


if __name__ == "__main__":
    solution()
