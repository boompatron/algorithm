import sys, heapq
INF = sys.maxsize


n, m, x = map(int, sys.stdin.readline().rstrip().split())
adj, ans = [[] for _ in range(n + 1)], [[INF for _ in range(n + 1)] for __ in range(n + 1)]
for i in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    adj[a].append([b, c])


def dijkstra(num):
    ans[num][num] = 0
    hq = []
    heapq.heappush(hq, [0, num])
    while hq:
        dis, idx = heapq.heappop(hq)
        if ans[num][idx] < dis:
            continue
        for aa in adj[idx]:
            nidx, ndis = aa[0], aa[1] + dis
            if ans[num][nidx] > ndis:
                ans[num][nidx] = ndis
                heapq.heappush(hq, [ndis, nidx])


for i in range(1, n + 1):
    dijkstra(i)
longest = -INF
for i in range(1, n + 1):
    longest = max(ans[i][x] + ans[x][i], longest)
print(longest)
