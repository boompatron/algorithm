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
    return ans


def solution():
    v = int(sys.stdin.readline().rstrip())
    e = int(sys.stdin.readline().rstrip())
    adj, ans = [[] for _ in range(v + 1)], [INF for _ in range(v + 1)]
    while e:
        a, b, c = map(int, sys.stdin.readline().rstrip().split())
        adj[a].append([b, c])
        e -= 1
    start, end = map(int, sys.stdin.readline().rstrip().split())
    print(dijkstra(start, adj, ans)[end])


if __name__ == "__main__":
    solution()
