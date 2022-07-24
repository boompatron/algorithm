import sys
import heapq
from collections import deque


def solution():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    in_degree, graph = [0 for _ in range(n + 1)], [[] for _ in range(n + 1)]
    while m:
        a, b = map(int, sys.stdin.readline().rstrip().split())
        graph[a].append(b)
        in_degree[b] += 1
        m -= 1
    hq, ans = [], deque()
    for vertex in range(1, n + 1):
        if not in_degree[vertex]:
            heapq.heappush(hq, vertex)
    while hq:
        cur = heapq.heappop(hq)
        ans.append(cur)
        for g in graph[cur]:
            in_degree[g] -= 1
            if not in_degree[g]:
                heapq.heappush(hq, g)
    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    solution()
