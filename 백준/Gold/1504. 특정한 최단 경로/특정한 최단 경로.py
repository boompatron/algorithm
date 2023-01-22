import sys
import heapq


def dijkstra(_start, _ans, _adj):
    _ans[_start] = 0
    hq = []
    heapq.heappush(hq, [0, _start])
    while len(hq):
        dis, cur = heapq.heappop(hq)
        if _ans[cur] < dis:
            continue
        for a in _adj[cur]:
            n, n_dis = a[0], a[1] + dis
            if _ans[n] > n_dis:
                _ans[n] = n_dis
                heapq.heappush(hq, [n_dis, n])


def solution():
    v, e = map(int, sys.stdin.readline().rstrip().split())
    adj = [[] for _ in range(v + 1)]
    ans_one = [123456789 for _ in range(v + 1)]
    ans_n, ans_v1 = [123456789 for _ in range(v + 1)], [123456789 for _ in range(v + 1)]
    for i in range(e):
        a, b, c = map(int, sys.stdin.readline().rstrip().split())
        adj[a].append([b, c])
        adj[b].append([a, c])
    v1, v2 = map(int, sys.stdin.readline().rstrip().split())
    dijkstra(1, ans_one, adj)
    dijkstra(v, ans_n, adj)
    dijkstra(v1, ans_v1, adj)
    one_to_v1, one_to_v2 = ans_one[v1], ans_one[v2]
    v1_to_v2 = ans_v1[v2]
    n_to_v1, n_to_v2 = ans_n[v1], ans_n[v2]
    ans = min(one_to_v1 + v1_to_v2 + n_to_v2, one_to_v2 + v1_to_v2 + n_to_v1)
    if ans >= 123456789:
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    solution()
