import sys
from collections import deque


def solution():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    in_degree, graph = [[0, 1] for _ in range(n + 1)], [[] for _ in range(n + 1)]
    while m:
        a, b = map(int, sys.stdin.readline().rstrip().split())
        graph[a].append(b)
        in_degree[b][0] += 1
        m -= 1
    ans, dq = [0 for _ in range(n + 1)], deque()
    for node, i_d in enumerate(in_degree[1:], start=1):
        if not i_d[0]:
            dq.appendleft([node, i_d[1]])
    while dq:
        cur, semester = dq.pop()
        ans[cur] = semester
        for g in graph[cur]:
            in_degree[g][0] -= 1
            in_degree[g][1] = semester + 1
            if not in_degree[g][0]:
                dq.appendleft([g, in_degree[g][1]])
    print(' '.join(map(str, ans[1:])))


if __name__ == "__main__":
    solution()
