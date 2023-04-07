import sys
from collections import deque
T = int(sys.stdin.readline().rstrip())
visited = [False for _ in range(1001)]
#l = [0 for _ in range(1001)]

def clearList():
    for i in range(1001):
        visited[i] = False
        #l[i] = 0


def BFS(num, l_list):
    dq = deque()
    dq.appendleft(num)
    visited[num] = True
    while dq:
        tmp = dq.pop()
        if not visited[l_list[tmp]]:
            dq.appendleft(l_list[tmp])
            visited[l_list[tmp]] = True


for _ in range(T):
    clearList()
    N = int(sys.stdin.readline().rstrip())
    l = list(map(int, sys.stdin.readline().rstrip().split()))
    l.insert(0, 0)
    cnt = 0
    for i in range(1, N + 1):
        if not visited[i]:
            BFS(i, l)
            cnt += 1
    print(cnt)

