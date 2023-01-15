import sys

dxs, dys = (1, -1, 0, 0), (0, 0, 1, -1)
n, m = map(int, sys.stdin.readline().rstrip().split())
g = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(n)]
visited = [False for _ in range(26)]
visited[ord(g[0][0]) - 65] = True
ans = 0


def dfs(x, y, cnt):
    global ans
    ans = max(cnt, ans)
    for i in range(4):
        nx, ny = x + dxs[i], y + dys[i]
        if 0 <= nx < m and 0 <= ny < n and not visited[ord(g[ny][nx]) - 65]:
            visited[ord(g[ny][nx]) - 65] = True
            dfs(nx, ny, cnt + 1)
            visited[ord(g[ny][nx]) - 65] = False


dfs(0, 0, 1)
print(ans)
