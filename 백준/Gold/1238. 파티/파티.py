import sys
import heapq
INF = sys.maxsize / 2


def dijkstra(adj, ans, start):
    ans[start] = 0
    hq = []
    heapq.heappush(hq, [0, start])
    while len(hq):
        dis, idx = heapq.heappop(hq)
        if ans[idx] < dis:
            continue
        for a in adj[idx]:
            next_idx, next_dis = a[0], a[1] + dis
            if ans[next_idx] > next_dis:
                ans[next_idx] = next_dis
                heapq.heappush(hq, [next_dis, next_idx])


def solution():
    v, e, x = map(int, sys.stdin.readline().rstrip().split())
    adj, ans = [[] for _ in range(v + 1)], [[INF for _ in range(v + 1)] for __ in range(v + 1)]
    while e:
        v1, v2, d = map(int, sys.stdin.readline().rstrip().split())
        adj[v1].append([v2, d])
        e -= 1
    for i in range(1, v + 1):
        dijkstra(adj, ans[i], i)
    t = 0
    for s in range(1, v + 1):
        if s == x:
            continue
        t = max(t, ans[x][s] + ans[s][x])
    print(t)


if __name__ == "__main__":
    solution()
