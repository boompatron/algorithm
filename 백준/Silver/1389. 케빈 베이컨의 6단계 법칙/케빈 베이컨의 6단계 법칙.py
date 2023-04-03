import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
adj = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    adj[a].append(b)
    adj[b].append(a)
ans, cnt = n + 1, (n + 1) * (n + 1)
for i in range(1, n + 1):
    distance, dq = [n + 1 for _ in range(n + 1)], deque()
    distance[i] = 0
    dq.appendleft((i, 0))
    while dq:
        cur, dis = dq.pop()
        for a in adj[cur]:
            if distance[a] > dis + 1:
                distance[a] = dis + 1
                dq.appendleft((a, dis + 1))
    if sum(distance[1:]) < cnt:
        cnt = sum(distance[1:])
        ans = i

print(ans)
