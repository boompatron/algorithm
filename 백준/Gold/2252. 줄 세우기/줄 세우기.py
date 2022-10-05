import sys
from collections import deque


def solution():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    adj, degree = [[] for _ in range(n + 1)], [0 for _ in range(n + 1)]
    while m:
        a, b = map(int, sys.stdin.readline().rstrip().split())
        adj[a].append(b)
        degree[b] += 1
        m -= 1
    dq, ans = deque(), deque()
    for i, e in enumerate(degree[1:], start=1):
        if not e:
            dq.appendleft(i)
    while dq:
        cur = dq.pop()
        ans.append(cur)
        for a in adj[cur]:
            degree[a] -= 1
            if not degree[a]:
                dq.appendleft(a)
    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    solution()
