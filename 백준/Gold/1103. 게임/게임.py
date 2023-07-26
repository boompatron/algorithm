import sys
sys.setrecursionlimit(10 ** 5)
dxs, dys = (1, -1, 0, 0), (0, 0, 1, -1)

n, m = map(int, sys.stdin.readline().rstrip().split())
g = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(n)]
visited = [[False for _ in range(m)] for __ in range(n)]
dp = [[0 for _ in range(m)] for __ in range(n)]
ans = 0


def in_range(a, b):
    return 0 <= a < m and 0 <= b < n


def dfs(a, b, depth):
    global ans
    ans = max(ans, depth)
    step = int(g[b][a])
    for dx, dy in zip(dxs, dys):
        nx, ny = a + dx * step, b + dy * step
        if in_range(nx, ny) and g[ny][nx] != 'H' and depth + 1 > dp[ny][nx]:
            if visited[ny][nx]:
                print(-1)
                exit()
            else:
                dp[ny][nx] = depth + 1
                visited[ny][nx] = True
                dfs(nx, ny, depth + 1)
                visited[ny][nx] = False


visited[0][0] = True
dfs(0, 0, 1)
print(ans)
