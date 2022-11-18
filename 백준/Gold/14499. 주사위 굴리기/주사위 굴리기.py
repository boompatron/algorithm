import sys
dxs, dys = [1, -1, 0, 0], [0, 0, -1, 1]
# dice = [[0, 2, 0],
#         [4, 1, 3],
#         [0, 5, 0],
#         [0, 6, 0]]
dice = [[0 for _ in range(3)] for __ in range(4)]


def rollDice(d):
    if d == 1: #East
        tmp = dice[1][0]
        for i in range(2):
            dice[1][i] = dice[1][i + 1]
        dice[1][2] = dice[3][1]
        dice[3][1] = tmp
    elif d == 2:
        tmp = dice[1][2]
        for i in range(2, 0, -1):
            dice[1][i] = dice[1][i - 1]
        dice[1][0] = dice[3][1]
        dice[3][1] = tmp
    elif d == 3:  # North
        tmp = dice[3][1]
        for i in range(3, 0, -1):
            dice[i][1] = dice[i - 1][1]
        dice[0][1] = tmp
    if d == 4:  # South
        tmp = dice[0][1]
        for i in range(3):
            dice[i][1] = dice[i + 1][1]
        dice[3][1] = tmp
    return dice[1][1]


def inRange(a, b, c, d):
    return 0 <= a < d and 0 <= b < c


n, m, y, x, k = map(int, sys.stdin.readline().rstrip().split())
g = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
inst = list(map(int, sys.stdin.readline().rstrip().split()))
for i in range(k):
    nx, ny = x + dxs[inst[i] - 1], y + dys[inst[i] - 1]
    if inRange(nx, ny, n, m):
        if g[ny][nx] == 0:
            g[ny][nx] = rollDice(inst[i])
        else:
            rollDice(inst[i])
            dice[1][1] = g[ny][nx]
            g[ny][nx] = 0
        print(dice[3][1])
        x, y = nx, ny
