import sys
from collections import deque
INF = sys.maxsize

v, e = map(int, sys.stdin.readline().rstrip().split())
adj = [[] for _ in range(v + 1)]
for i in range(v - 1):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    adj[a].append([b, c])
    adj[b].append([a, c])
usado = [[INF for _ in range(v + 1)] for __ in range(v + 1)]
dq = deque()

for i in range(1, v + 1):
    visited = [False for _ in range(v + 1)]
    visited[i] = True
    usado[i][i] = 0
    dq.appendleft((i, INF))
    while dq:
        pos, cur = dq.pop()
        for n, d in adj[pos]:
            if not visited[n]:
                visited[n] = True
                next_dis = cur if cur < d else d
                usado[i][n] = next_dis
                dq.appendleft((n, next_dis))

for i in range(e):
    k, v = map(int, sys.stdin.readline().rstrip().split())
    print(sum([1 for j in usado[v][1:] if j >= k]))

