dxs, dys = (1, -1, 0, 0), (0, 0, 1, -1)
visited = [[False for _ in range(5)]for __ in range(5)]
n, m = 0, 0


def in_range(a, b):
    return 0 <= a < m and 0 <= b < n


def dfs(board, cx, cy, ox, oy):
    global visited
    if visited[cy][cx]:
        return 0
    winnable = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = cx + dx, cy + dy
        if not in_range(nx, ny) or visited[ny][nx] or board[ny][nx] == 0:
            continue
        visited[cy][cx] = True
        op_result = dfs(board, ox, oy, nx, ny) + 1
        visited[cy][cx] = False

        if winnable % 2 == 0 and op_result % 2 == 1:
            winnable = op_result
        elif winnable % 2 == 0 and op_result % 2 == 0:
            winnable = max(winnable, op_result)
        elif winnable % 2 == 1 and op_result % 2 == 1:
            winnable = min(winnable, op_result)
    return winnable


def solution(board, aloc, bloc):
    global n, m
    n, m = len(board), len(board[0])
    return dfs(board, *reversed(aloc), *reversed(bloc))