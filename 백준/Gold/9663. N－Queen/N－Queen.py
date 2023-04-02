import sys


def is_promising(x):
    global g
    for i in range(x):
        if g[i] == g[x] or abs(g[i] - g[x]) == abs(x - i):
            return False
    return True


def n_queen(x):
    global ans
    if x == n:
        ans += 1
        return
    for i in range(n):
        global g
        g[x] = i
        if is_promising(x):
            n_queen(x + 1)


n = int(sys.stdin.readline().rstrip())
ans = 0
g = [0 for _ in range(n)]
n_queen(0)
print(ans)
