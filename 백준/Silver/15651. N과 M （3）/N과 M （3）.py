import sys


def recursive(n, m, s):
    if len(s) == m:
        print(' '.join(map(str, s)))
    else:
        for i in range(1, n + 1):
            recursive(n, m, s + [i])


def solution():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    recursive(n, m, [])


if __name__ == "__main__":
    solution()
