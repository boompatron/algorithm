import sys
from collections import deque
dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
n = int(sys.stdin.readline().rstrip())
g = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
highest = max(max(g))
visited = [[False for _ in range(n)] for __ in range(n)]


def in_range(a, b):
    return 0 <= a < n and 0 <= b < n


def clear_visited():
    for a in range(n):
        for b in range(n):
            visited[a][b] = False


def count_island(h):
    cnt = 0
    for a in range(n):
        for b in range(n):
            if g[a][b] >= h and not visited[a][b]:
                dq = deque()
                dq.appendleft([b, a])
                visited[a][b] = True
                while dq:
                    x, y = dq.pop()
                    for dx, dy in zip(dxs, dys):
                        nx, ny = x + dx, y + dy
                        if in_range(nx, ny) and g[ny][nx] >= h and not visited[ny][nx]:
                            dq.appendleft([nx, ny])
                            visited[ny][nx] = True
                cnt += 1
    return cnt


ans = 0
for i in range(1, highest + 1):
    clear_visited()
    tmp = count_island(i)
    ans = max(ans, tmp)
print(ans)
