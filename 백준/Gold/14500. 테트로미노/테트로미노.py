import sys
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
ans, max_val, n, m = 0, 0, 0, 0
g = [[]]


def in_range(a, b):
    global n, m
    return 0 <= a < m and 0 <= b < n


def get_max_score(x, y, visited, val, depth):
    global ans, max_val, n, m, g
    if not depth:
        ans = max(ans, val)
        return
    if ans >= val + depth * max_val:
        return
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and not visited[ny][nx]:
            nval = val + g[ny][nx]
            if depth == 2:
                visited[ny][nx] = True
                get_max_score(x, y, visited, nval, depth - 1)
                visited[ny][nx] = False
            visited[ny][nx] = True
            get_max_score(nx, ny, visited, nval, depth - 1)
            visited[ny][nx] = False


def solution():
    global max_val, g, n, m
    n, m = map(int, sys.stdin.readline().rstrip().split())
    g = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
    visited = [[False for _ in range(m)] for __ in range(n)]
    max_val = max(map(max, g))

    for i in range(n):
        for j in range(m):
            visited[i][j] = True
            get_max_score(j, i, visited, g[i][j], 3)
            visited[i][j] = False
    print(ans)


if __name__ == '__main__':
    solution()
