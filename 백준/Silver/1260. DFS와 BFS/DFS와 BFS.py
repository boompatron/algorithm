import sys
from collections import deque


def solution():
    v, e, start = map(int, sys.stdin.readline().rstrip().split())
    adj = [[] for _ in range(v + 1)]
    while e:
        v1, v2 = map(int, sys.stdin.readline().rstrip().split())
        adj[v1].append(v2)
        adj[v2].append(v1)
        e -= 1
    visited = [False for _ in range(v + 1)]
    for i in range(1, v + 1):
        adj[i].sort()

    def clear_visited():
        for i in range(v + 1):
            visited[i] = False

    def dfs(num: int):
        print(num, end=" ")
        visited[num] = True
        for a in adj[num]:
            if not visited[a]:
                dfs(a)

    def bfs(num: int):
        visited[num] = True
        dq = deque()
        dq.appendleft(num)
        while dq:
            cur = dq.pop()
            print(cur, end=" ")
            for a in adj[cur]:
                if not visited[a]:
                    dq.appendleft(a)
                    visited[a] = True

    dfs(start)
    print()
    clear_visited()
    bfs(start)


if __name__ == '__main__':
    solution()
