import sys


def recursive(g, s, n):
    if len(s) == 6:
        print(' '.join(map(str, s)))
    else:
        for i in range(n):
            if g[i] in s or len(s) and max(s) > g[i]:
                continue
            recursive(g, s + [g[i]], n)


def solution():
    while True:
        g = list(map(int, sys.stdin.readline().rstrip().split()))
        # print(g, g[1:])
        exit(0) if len(g) == 1 else recursive(g[1:], [], len(g) - 1)
        print()


if __name__ == "__main__":
    solution()
