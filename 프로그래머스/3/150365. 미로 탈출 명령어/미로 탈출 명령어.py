import sys
sys.setrecursionlimit(10 ** 4)
dxs, dys, dal = (0, -1, 1, 0), (1, 0, 0, -1), ('d', 'l', 'r', 'u')
ans = ''
is_finished = False


def solution(n, m, x, y, r, c, k):
    global ans, is_finished
    x, y = y - 1, x - 1
    ex, ey = c - 1, r - 1

    def dfs(a: int, b: int, route: str, depth: int):
        global ans, is_finished
        if is_finished:
            return
        if abs(ex - a) + abs(ey - b) > k - depth:
            return
        if not is_finished and depth == k:
            if a == ex and b == ey:
                is_finished = True
                ans = route
            return
        for i in range(4):
            nx, ny = a + dxs[i], b + dys[i]
            if 0 <= nx < m and 0 <= ny < n:
                dfs(nx, ny, route + dal[i], depth + 1)

    dis = abs(ex - x) + abs(ey - y)
    if dis > k or dis % 2 != k % 2:
        return 'impossible'
    dfs(x, y, '', 0)

    return ans if is_finished else 'impossible'
