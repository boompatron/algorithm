import sys
from collections import deque
from collections import Counter


def solution(n, edge):
    adj = [[] for _ in range(n + 1)]
    distance = [sys.maxsize for _ in range(n + 1)]
    for a, b in edge:
        adj[a].append(b)
        adj[b].append(a)
    dq = deque()
    dq.appendleft([1, 0])
    distance[1] = 0
    while dq:
        idx, dis = dq.pop()
        for next_idx in adj[idx]:
            if distance[next_idx] > dis + 1:
                dq.appendleft([next_idx, dis + 1])
                distance[next_idx] = dis + 1
    distance = distance[1:]
    return Counter(distance).get(max(distance))