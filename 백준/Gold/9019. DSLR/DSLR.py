import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
dq = deque()
while n:
    ans = '0' * 10001
    visited = [123456 for _ in range(10001)]
    dq.clear()
    a, b = map(int, sys.stdin.readline().rstrip().split())
    dq.appendleft((a, ''))
    while dq:
        cur, inst = dq.pop()
        if cur == b and len(ans) > len(inst):
            ans = inst
            continue
        d = (cur * 2) % 10000
        if visited[d] > len(inst):
            visited[d] = len(inst)
            dq.appendleft((d, inst + 'D'))
        s = (cur - 1) % 10000
        if visited[s] > len(inst):
            visited[s] = len(inst)
            dq.appendleft((s, inst + 'S'))
        l = cur // 1000 + (cur % 1000) * 10
        if visited[l] > len(inst):
            visited[l] = len(inst)
            dq.appendleft((l, inst + 'L'))
        r = (cur % 10) * 1000 + cur // 10
        if visited[r] > len(inst):
            visited[r] = len(inst)
            dq.appendleft((r, inst + 'R'))
    print(ans)
    n -= 1
