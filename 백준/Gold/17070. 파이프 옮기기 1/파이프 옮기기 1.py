import sys
ans = 0
n = int(sys.stdin.readline().rstrip())
g = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]


def dfs(a, b, direction):
    global ans
    if a == n - 1 and b == n - 1:
        ans += 1
        return
    if direction == 0 or direction == 1:  # 오른쪽으로 이동할 때
        if a + 1 < n:
            if g[b][a + 1] == 0:
                dfs(a + 1, b, 0)
    if direction == 2 or direction == 1:  # 아래쪽으로 이동
        if b + 1 < n:
            if not g[b + 1][a]:
                dfs(a, b + 1, 2)
    if a + 1 < n and b + 1 < n:
        if g[b][a + 1] == 0 and g[b + 1][a] == 0 and g[b + 1][a + 1] == 0:
            dfs(a + 1, b + 1, 1)


dfs(1, 0, 0)
print(ans)
