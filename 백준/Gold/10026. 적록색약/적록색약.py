import sys
from collections import deque
dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
color = {'R':0, 'B':1, 'G':2}
n = int(sys.stdin.readline().rstrip())
g = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(n)]
visited_normal = [[False for _ in range(n)] for __ in range(n)]
visited_rg_weakness = [[False for _ in range(n)] for __ in range(n)]
normal_ans, rg_weakness_ans = 0, 0


def in_range(a, b):
    return 0 <= a < n and 0 <= b < n


def count_area(a, b, c, isNormal):
    dq = deque()
    dq.appendleft([a, b])
    #visited = [[]]
    if isNormal:
        visited_normal[b][a] = True
        visited = visited_normal
    else:
        visited_rg_weakness[b][a] = True
        visited = visited_rg_weakness
    while dq:
        x, y = dq.pop()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[ny][nx]:
                if (isNormal and c == g[ny][nx]) or (not isNormal and color[c] % 2 == color[g[ny][nx]] % 2):
                    dq.appendleft([nx, ny])
                    visited[ny][nx] = True


for i in range(n):
    for j in range(n):
        if not visited_normal[i][j]:
            count_area(j, i, g[i][j], True)
            normal_ans += 1
        if not visited_rg_weakness[i][j]:
            count_area(j, i, g[i][j], False)
            rg_weakness_ans += 1
print(normal_ans, rg_weakness_ans)

