import sys
from collections import deque
k = int(sys.stdin.readline().rstrip())
color = ['' for _ in range(20001)]
adj = [[] for _ in range(20001)]


def BFS(num):
    dq = deque()
    color[num] = 'R'
    dq.appendleft(num)
    while dq:
        tmp = dq.pop()
        for i in adj[tmp]:
            if color[i] == '':
                dq.appendleft(i)
                if color[tmp] == 'R':
                    color[i] = 'B'
                else:
                    color[i] = 'R'


def clearLists():
    for i in range(20001):
        color[i] = ''
        adj[i] = []


for _ in range(k):
    clearLists()
    v, e = map(int, sys.stdin.readline().rstrip().split())
    for i in range(e):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        adj[a].append(b)
        adj[b].append(a)
    for i in range(1, v + 1):
        if color[i] == '':
            BFS(i)
    ans = True
    for i in range(1, v + 1):
        for j in adj[i]:
            if color[i] == color[j]:
              ans = False
    if ans:
        print("YES")
    else:
        print("NO")
