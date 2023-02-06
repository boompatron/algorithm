import sys


def solution():
    t = int(sys.stdin.readline().rstrip())
    dp = [0, 1, 2, 4]
    while t:
        n = int(sys.stdin.readline().rstrip())
        if len(dp) <= n:
            while len(dp) <= n:
                dp.append(sum(dp[-3:]))
        print(dp[n])
        t -= 1


if __name__ == "__main__":
    solution()
