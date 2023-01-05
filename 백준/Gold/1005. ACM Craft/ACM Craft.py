import sys
import heapq
from collections import deque


def solution():
    n, k = map(int, sys.stdin.readline().rstrip().split())
    adj, degree = [[] for _ in range(n + 1)], [0 for _ in range(n + 1)]
    complete_time = [sys.maxsize for _ in range(n + 1)]
    hq, ans = [], deque()
    building_time = list(map(int, sys.stdin.readline().rstrip().split()))
    building_time.insert(0, 0)
    for _ in range(k):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        adj[a].append(b)
        degree[b] += 1
    w = int(sys.stdin.readline().rstrip())
    for _ in range(1, n + 1):
        if degree[_] == 0:
            heapq.heappush(hq, [building_time[_], _])
    while hq:
        acc_time, cur = heapq.heappop(hq)
        if complete_time[cur] > acc_time:
            complete_time[cur] = acc_time
        for a in adj[cur]:
            degree[a] -= 1
            if degree[a] == 0:
                heapq.heappush(hq, [acc_time + building_time[a], a])
    print(complete_time[w])



if __name__ == '__main__':
    tc = int(sys.stdin.readline().rstrip())
    while tc:
        solution()
        tc -= 1
