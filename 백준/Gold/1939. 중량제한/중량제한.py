import sys
from collections import deque

v, e = map(int, sys.stdin.readline().rstrip().split())
adj = [[] for _ in range(v + 1)]
for i in range(e):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    adj[a].append([b, c])
    adj[b].append([a, c])
start, end = map(int, sys.stdin.readline().rstrip().split())
left, right = 0, 1000000001
for i in range(1, v + 1):
    adj[i].sort(reverse=True)


def bfs(cost):
    dq = deque()
    dq.append(start)
    visited[start] = True
    while dq:
        cur = dq.pop()
        if cur == end:
            return True
        for nv, nc in adj[cur]:
            if not visited[nv] and nc >= cost:
                dq.appendleft(nv)
                visited[nv] = True
    return False


while left <= right:
    visited = [False for _ in range(v + 1)]
    mid = (left + right) // 2
    if bfs(mid):
        left = mid + 1
    else:
        right = mid - 1
print(right)
