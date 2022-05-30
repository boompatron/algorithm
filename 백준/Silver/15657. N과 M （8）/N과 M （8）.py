import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
l = list(map(int, sys.stdin.readline().rstrip().split()))
l.sort()


def f(s):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in l:
        if len(s) and i < s[-1]:
            continue
        f(s + [i])


f([])
