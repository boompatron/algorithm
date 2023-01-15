import sys

dxs, dys = (1, -1, 0, 0), (0, 0, 1, -1)
n, m = map(int, sys.stdin.readline().rstrip().split())
g = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(n)]
visited = 0
visited |= (1 << (ord(g[0][0]) - 65))
ans = 0


def dfs(x, y, cnt):
    global ans, visited
    ans = max(cnt, ans)
    for i in range(4):
        nx, ny = x + dxs[i], y + dys[i]
        if 0 <= nx < m and 0 <= ny < n and not (visited & (1 << (ord(g[ny][nx]) - 65))):
            visited |= (1 << (ord(g[ny][nx]) - 65))
            dfs(nx, ny, cnt + 1)
            visited &= ~(1 << (ord(g[ny][nx]) - 65))


dfs(0, 0, 1)
print(ans)
