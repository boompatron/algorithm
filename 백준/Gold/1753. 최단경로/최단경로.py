import sys
import heapq
INF = sys.maxsize


def dijkstra(start, adj, ans):
    ans[start] = 0
    hq = []
    heapq.heappush(hq, [0, start])
    while hq:
        dis, idx = heapq.heappop(hq)
        if ans[idx] < dis:
            continue
        for a in adj[idx]:
            next_idx, next_dis = a[0], a[1] + dis
            if ans[next_idx] > next_dis:
                ans[next_idx] = next_dis
                heapq.heappush(hq, [next_dis, next_idx])
    return ans[1:]


def solution():
    v, e = map(int, sys.stdin.readline().rstrip().split())
    k = int(sys.stdin.readline().rstrip())
    adj, ans = [[] for _ in range(v + 1)], [INF for _ in range(v + 1)]
    while e:
        a, b, c = map(int, sys.stdin.readline().rstrip().split())
        adj[a].append([b, c])
        e -= 1
    for d in dijkstra(k, adj, ans):
        print(d if d != INF else 'INF')


if __name__ == "__main__":
    solution()
