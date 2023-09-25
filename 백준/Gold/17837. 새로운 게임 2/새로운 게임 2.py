import sys
dxs, dys = (1, 0, -1, 0), (0, 1, 0, -1)
convert_d = {1: 0, 2: 2, 3: 3, 4: 1}

n, k = map(int, sys.stdin.readline().rstrip().split())
g = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
board = [[[] for _ in range(n)] for __ in range(n)]
corrd = {}
for i in range(k):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())  # a - 1 > y, b - 1 > x
    board[a - 1][b - 1].append(i + 1)
    corrd[i + 1] = [b - 1, a - 1, convert_d[c]]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def move():
    for t in range(1, k + 1):
        x, y, d = corrd[t]
        order = board[y][x].index(t)
        moving = board[y][x][order:]
        stay = board[y][x][:order]
        nx, ny = x + dxs[d], y + dys[d]

        if not in_range(nx, ny) or (in_range(nx, ny) and g[ny][nx] == 2):
            d = (d + 2) % 4
            nx, ny = x + dxs[d], y + dys[d]
            corrd[t] = [x, y, d]

        if in_range(nx, ny) and (g[ny][nx] == 1 or g[ny][nx] == 0):
            if g[ny][nx] == 0:
                board[ny][nx].extend(moving)
            else:
                board[ny][nx].extend(list(reversed(moving)))
            board[y][x] = stay
            for m in moving:
                ox, oy, od = corrd[m]
                corrd[m] = [nx, ny, od]
            if len(board[ny][nx]) >= 4:
                return True
    return False


cnt = 1
while cnt < 1001:
    if move():
        break
    cnt += 1
print(cnt if cnt < 1001 else -1)
