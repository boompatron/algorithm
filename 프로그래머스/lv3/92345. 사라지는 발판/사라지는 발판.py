# minimax tree 알고리즘...
# 나는 내 턴에서 최선을 다하고
# 상대방도 최선을 다한다

from copy import deepcopy

dxs, dys = (1, -1, 0, 0), (0, 0, 1, -1)
visited = [[False for _ in range(5)]for __ in range(5)]
g = [[0 for _ in range(5)] for _ in range(5)]
n, m = 0, 0


def in_range(a, b):
    return 0 <= a < m and 0 <= b < n


# 반환값 : 현재 상태에서 둘 다 최적의 플레이를 할 때 남은 이동 횟수 이자 두 플레이어의 이동 횟수의 합
# 나 > 상대 > 나 > 상대 > ...
# 반환 값이 짝수 : 앞으로 짝수번 이동을 더 한다 -> 플레이어가 패배함을 의미,
# 홀수 : 앞으로 홀수 번 이동을 더한다 -> 플레이어가 승리함을 의미
# cx, cy : 현재 플레이어의 좌표, ox, oy : 상대 플레이어의 좌표
def dfs(cx, cy, ox, oy):
    global visited
    if visited[cy][cx]:
        return 0
    ret = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = cx + dx, cy + dy
        # 범위를 벗어나거나, 이미 방문을 해 발판이 없거나, 애초에 발판이 없는 곳인 경우
        if not in_range(nx, ny) or visited[ny][nx] or g[ny][nx] == 0:
            # 무시
            continue

        # 일단 현재 위치는 방문 표시를 하고
        visited[cy][cx] = True
        # 현재 플레이어를 이동시켰을 때의 새로 계산
        # val 은 플레이어가 4방향으로 각각 이동했을 때, 남은 이동 횟수
        # val 짝수이면 플레이어의 패배, 홀수이면 플레이어의 승리
        val = dfs(ox, oy, nx, ny) + 1
        # 방문 표시 해제
        visited[cy][cx] = False

        # 현재 저장된 턴은 패배인데 새로 계산된 턴은 승리인 경우
        if ret % 2 == 0 and val % 2 == 1:
            # 남은 턴 갱신
            ret = val

        # 현재 저장된 턴과 새로 계산된 턴 모두 패배인 경우
        elif ret % 2 == 0 and val % 2 == 0:
            # 최대한 늦게까지 끌고 져야 함
            ret = max(ret, val)

        # 현재 저장된 턴과 새로 계산된 턴 모두 승리인 경우
        elif ret % 2 == 1 and val % 2 == 1:
            # 최대한 빠르게 마무리 해야 함
            ret = min(ret, val)
    return ret


def solution(board, aloc, bloc):
    global n, m, g
    n, m = len(board), len(board[0])
    g = deepcopy(board)
    return dfs(*reversed(aloc), *reversed(bloc))
