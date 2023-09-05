import sys
from heapq import heappop, heappush
INF = sys.maxsize


def dijkstra(ans: list, num: int, adj):
    ans[num] = 0
    hq = []
    heappush(hq, [0, num])
    while hq:
        dis, idx = heappop(hq)
        if ans[idx] < dis:
            continue
        for a in adj[idx]:
            n_idx, n_dis = a[0], a[1] + dis
            if ans[n_idx] > n_dis:
                ans[n_idx] = n_dis
                heappush(hq, [n_dis, n_idx])


def solution(n, s, a, b, fares):
    adj = [[] for _ in range(n + 1)]
    ans = [[INF for _ in range(n + 1)] for __ in range(n + 1)]
    for v1, v2, fare in fares:
        adj[v1].append([v2, fare])
        adj[v2].append([v1, fare])
    for i in range(1, n + 1):
        dijkstra(ans[i], i, adj)

    return min([ans[s][i] + ans[i][a] + ans[i][b] for i in range(1, n + 1)])