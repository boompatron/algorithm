from copy import deepcopy

dxs, dys = (1, -1, 0, 0), (0, 0, 1, -1)
visited = [[False for _ in range(5)]for __ in range(5)]
g = [[0 for _ in range(5)] for _ in range(5)]
n, m = 0, 0


def in_range(a, b):
    return 0 <= a < m and 0 <= b < n


def dfs(cx, cy, ox, oy):
    global visited
    if visited[cy][cx]:
        return 0
    # 현재는 지는 상태 winnable % 2 == 0 > 패배, 1 > 승리
    winnable = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = cx + dx, cy + dy
        if not in_range(nx, ny) or visited[ny][nx] or g[ny][nx] == 0:
            continue
        visited[cy][cx] = True
        # 상대방의 결과 가져오기
        op_result = dfs(ox, oy, nx, ny) + 1
        visited[cy][cx] = False

        # 나는 지고 상대방도 진다? -> 이기는 경우로 저장
        if winnable % 2 == 0 and op_result % 2 == 1:
            winnable = op_result

        # 나는 지는데 상대방이 이긴다 -> 최대한 늦게 까지 끌기
        elif winnable % 2 == 0 and op_result % 2 == 0:
            winnable = max(winnable, op_result)

        # 나는 이기고 상대는 진다 -> 최소 턴으로 기록
        elif winnable % 2 == 1 and op_result % 2 == 1:
            winnable = min(winnable, op_result)
    return winnable


def solution(board, aloc, bloc):
    global n, m, g
    n, m = len(board), len(board[0])
    g = deepcopy(board)
    return dfs(*reversed(aloc), *reversed(bloc))
