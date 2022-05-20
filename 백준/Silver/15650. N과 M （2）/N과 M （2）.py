import sys
n, m = map(int, sys.stdin.readline().rstrip().split())


def f(s):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(1, n + 1):
        if i in s or (len(s) and i < s[-1]):
            continue
        f(s + [i])


f([])
