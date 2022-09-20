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


def solution():
    v, e, x = map(int, sys.stdin.readline().rstrip().split())
    adj, ans = [[] for _ in range(v + 1)], [[INF for _ in range(v + 1)] for __ in range(v + 1)]
    while e:
        a, b, c = map(int, sys.stdin.readline().rstrip().split())
        adj[a].append([b, c])
        e -= 1
    for i in range(1, v + 1):
        dijkstra(i, adj, ans[i])
    answer = 0
    for i in range(1, v + 1):
        if i == x:
            continue
        answer = max(answer, ans[i][x] + ans[x][i])
    print(answer)


if __name__ == "__main__":
    solution()
