import sys
from collections import deque
dice = [[0, 2, 0],
        [4, 1, 3],
        [0, 5, 0],
        [0, 6, 0]]
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]


def roll_dice(direction):
    if direction == 0: # East
        tmp = dice[1][2]
        for i in range(2, 0, -1):
            dice[1][i] = dice[1][i - 1]
        dice[1][0] = dice[3][1]
        dice[3][1] = tmp
    elif direction == 1: # South
        tmp = dice[3][1]
        for i in range(3, 0, -1):
            dice[i][1] = dice[i - 1][1]
        dice[0][1] = tmp
    elif direction == 2: # West
        tmp = dice[1][0]
        for i in range(2):
            dice[1][i] = dice[1][i + 1]
        dice[1][2] = dice[3][1]
        dice[3][1] = tmp
    elif direction == 3: # North
        tmp = dice[0][1]
        for i in range(3):
            dice[i][1] = dice[i + 1][1]
        dice[3][1] = tmp


def print_dice():
    print("----------dice------------")
    for i in dice:
        for j in i:
            if j == 0:
                print(" ", end=" ")
            else:
                print(j, end=" ")
        print()


def in_range(x, y, n, m):
    return 0 <= x < m and 0 <= y < n


def get_dice_bottom():
    return dice[3][1]


def clear_visited(v, n, m):
    for i in range(n):
        for j in range(m):
            v[i][j] = False


def get_score(g, visited, a, b, n, m):
    clear_visited(visited, n, m)
    dq, cnt, cur = deque(), 1, g[b][a]
    dq.appendleft([a, b])
    visited[b][a] = True
    while len(dq):
        x, y = dq.pop()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny, n, m) and g[ny][nx] == cur and not visited[ny][nx]:
                dq.appendleft([nx, ny])
                visited[ny][nx] = True
                cnt += 1
    return cnt * cur


dk = {0: "동", 1: "남", 2: "서", 3: "북"}


def solution():
    n, m, k = map(int, sys.stdin.readline().rstrip().split())
    visited = [[False for _ in range(m)] for __ in range(n)]
    g = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
    x, y, score = 0, 0, 0
    direction = 0
    # print("init dice")
    # print_dice()
    for i in range(k):
        # print("======================================================")
        # print(f"{i + 1}\t|이동 전 : y: {y + 1}, x : {x + 1}", end="\t|")
        # 우선 이동
        nx, ny = x + dxs[direction % 4], y + dys[direction % 4]
        if in_range(nx, ny, n, m):
            x, y = nx, ny
        else:
            direction += 2
            x, y = x + dxs[direction % 4], y + dys[direction % 4]
        # print(f"이동 후 : y : {y + 1},  x  :{x + 1}", end="\t|")
        # 점수 계산
        tmp = get_score(g, visited, x, y, n, m)
        score += tmp
        roll_dice(direction % 4)
        # 방향 전환
        if get_dice_bottom() > g[y][x]:
            direction += 1
        elif get_dice_bottom() < g[y][x]:
            direction -= 1
        # print(f"score : {tmp}\t| 방향 : {dk[direction % 4]}")
        # print_dice()
    print(score)


if __name__ == "__main__":
    solution()
