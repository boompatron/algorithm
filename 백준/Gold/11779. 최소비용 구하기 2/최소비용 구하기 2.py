import sys
import heapq
INF = sys.maxsize

v = int(sys.stdin.readline().rstrip())
e = int(sys.stdin.readline().rstrip())
adj, ans = [[INF for _ in range(v + 1)] for __ in range(v + 1)], [[INF, []] for _ in range(v + 1)]
for i in range(e):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    adj[a][b] = min(c, adj[a][b])
start, end = map(int, sys.stdin.readline().rstrip().split())


def dijkstra(s):
    ans[s][0] = 0
    for j in range(1, v + 1):
        ans[j][1].append(start)
    hq = []
    heapq.heappush(hq, [0, start])
    while hq:
        dis, idx = heapq.heappop(hq)
        if ans[idx][0] < dis:
            continue
        for d in range(1, v + 1):
            if adj[idx][d] != INF:
                next_idx, next_dis = d, adj[idx][d] + dis
                if ans[next_idx][0] > next_dis:
                    ans[next_idx][0] = next_dis
                    ans[next_idx][1] = (ans[idx][1] + [next_idx])
                    heapq.heappush(hq, [next_dis, next_idx])


dijkstra(start)
print(ans[end][0])
print(len(ans[end][1]))
print(' '.join(map(str, ans[end][1])))
