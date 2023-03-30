import sys
from collections import deque
l1, l2 = sys.stdin.readline().rstrip(), sys.stdin.readline().rstrip()
g = [[0 for _ in range(len(l2) + 1)] for __ in range(len(l1) + 1)]


def fill_in_g():
    for a in range(1, len(l1) + 1):
        for b in range(1, len(l2) + 1):
            if l1[a - 1] == l2[b - 1]:
                g[a][b] = g[a - 1][b - 1] + 1
            else:
                g[a][b] = max(g[a - 1][b], g[a][b - 1])
    return g[len(l1)][len(l2)]


def make_lcs():
    ans = ""
    dq = deque()
    dq.appendleft([len(l2), len(l1)])
    cur_val = -1
    while dq and cur_val != 0:
        x, y = dq.pop()
        cur_val = g[y][x]
        left_val, up_val = g[y][x - 1], g[y - 1][x]
        if cur_val == up_val or cur_val == left_val:
            if cur_val == left_val:
                dq.appendleft([x - 1, y])
            elif cur_val == up_val:
                dq.appendleft([x, y - 1])
        elif cur_val > left_val and cur_val > up_val:
            ans += l1[y - 1]
            dq.appendleft([x - 1, y - 1])
    return "".join(list(reversed(ans)))


print(fill_in_g())
print(make_lcs())

