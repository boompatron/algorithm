import sys
from collections import deque
v = int(sys.stdin.readline().rstrip())
adj = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(v)]
for num in range(v):
    adj[num].insert(0, 0)
adj.insert(0, [])
visited = [False for _ in range(v + 1)]
ans = [[0 for _ in range(v)] for __ in range(v)]


def clear_visited():
    for a in range(v + 1):
        visited[a] = False


def find(start):
    clear_visited()
    dq = deque()
    dq.appendleft(start)
    while dq:
        cur = dq.pop()
        for i in range(1, v + 1):
            if adj[cur][i] and not visited[i]:
                dq.appendleft(i)
                visited[i] = True
    for i in range(1, v + 1):
        print(int(visited[i]), end=" ")
    print()


for num in range(1, v + 1):
    find(num)
