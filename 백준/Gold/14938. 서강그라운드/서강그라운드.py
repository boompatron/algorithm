import sys
import heapq
INF = sys.maxsize


def dijkstra(adj, start, v, search_range, items):
    shortest_distance = [INF for _ in range(v + 1)]
    shortest_distance[start] = 0
    hq, ans = [], 0
    heapq.heappush(hq, [0, start])
    while len(hq):
        dis, idx = heapq.heappop(hq)
        if shortest_distance[idx] < dis:
            continue
        for a in adj[idx]:
            next_idx, next_dis = a[0], a[1] + dis
            if shortest_distance[next_idx] > next_dis:
                shortest_distance[next_idx] = next_dis
                heapq.heappush(hq, [next_dis, next_idx])
    for idx, distance in enumerate(shortest_distance):
        if distance <= search_range:
            ans += items[idx]
    return ans


def solution():
    v, search_range, e = map(int, sys.stdin.readline().rstrip().split())
    items = list(map(int, sys.stdin.readline().rstrip().split()))
    items.insert(0, 0)
    adj = [[] for _ in range(v + 1)]
    for i in range(e):
        a, b, c = map(int, sys.stdin.readline().rstrip().split())
        adj[a].append([b, c])
        adj[b].append([a, c])
    ans = 0
    for i in range(1, v + 1):
        ans = max(ans, dijkstra(adj, i, v, search_range, items))
    print(ans)


if __name__ == "__main__":
    solution()
