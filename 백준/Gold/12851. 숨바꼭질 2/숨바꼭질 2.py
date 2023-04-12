import sys
from collections import deque

visited = [123456789 for _ in range(100001)]
fastest, ans = 123456789, 0
n, k = map(int, sys.stdin.readline().rstrip().split())
dq = deque()
dq.appendleft((n, 0))
while dq:
    cur, cnt = dq.pop()
    if cur == k:
        ans += 1
        fastest = min(fastest, cnt)
    else:
        for dx in (-1, 1, cur):
            nx = cur + dx
            if 0 <= nx <= 100000 and visited[nx] >= cnt:
                visited[nx] = cnt
                dq.appendleft((nx, cnt + 1))
print(f'{fastest}\n{ans}')
