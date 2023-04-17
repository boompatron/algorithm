import sys
from collections import deque
INF = sys.maxsize

v = int(sys.stdin.readline().rstrip())
adj, dq = [{} for _ in range(v + 1)], deque()
y = 0
distance = [INF for _ in range(v + 1)]
for i in range(v):
    g = list(map(int, sys.stdin.readline().rstrip().split()))[:-1]
    pos = g[0]
    for j in range(len(g) // 2):
        adj[pos][g[j * 2 + 1]] = g[j * 2 + 2]


def bfs(init):
    global distance
    for a in range(1, v + 1):
        distance[a] = INF if a != init else 0
    dq.appendleft((init, 0))
    while dq:
        cur, dis = dq.pop()
        for next_idx in adj[cur].keys():
            next_dis = dis + adj[cur][next_idx]
            if distance[next_idx] > next_dis:
                distance[next_idx] = next_dis
                dq.appendleft((next_idx, next_dis))


bfs(1)
tmp = 0
for i in range(1, v + 1):
    if distance[i] > tmp:
        tmp = distance[i]
        y = i
bfs(y)
print(max(distance[1:]))
