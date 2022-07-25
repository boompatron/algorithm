import sys
from collections import deque


def solution():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    in_degree, graph = [0 for _ in range(n + 1)], [[] for _ in range(n + 1)]
    while m:
        g = list(map(int, sys.stdin.readline().rstrip().split()))[1:]
        for i in enumerate(g[:-1]):
            in_degree[g[i[0] + 1]] += 1
            graph[i[1]].append(g[i[0] + 1])
        m -= 1
    dq, ans = deque(), deque()
    for d in enumerate(in_degree[1:], start=1):
        if not in_degree[d[0]]:
            dq.appendleft(d[0])
    while dq:
        cur = dq.pop()
        ans.append(cur)
        for g in graph[cur]:
            in_degree[g] -= 1
            if not in_degree[g]:
                dq.appendleft(g)
    if len(ans) != n:
        print(0)
    else:
        for i in enumerate(ans):
            print(i[1], end="\n")


if __name__ == "__main__":
    solution()
