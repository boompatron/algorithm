import sys
dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1] # 동 서 남 북
upper_dir, lower_dir = [3, 0, 2, 1], [2, 0, 3, 1]


def in_range(x, x_lowest, x_highest, y, y_lowest, y_highest):
    return x_lowest <= x < x_highest and y_lowest <= y < y_highest


def spread_dust(g, r, c):
    next_g = [[0 for _ in range(c)] for __ in range(r)]
    for i in range(r):
        for j in range(c):
            if g[i][j] > 0:
                cnt = 0
                for dx, dy in zip(dxs, dys):
                    nx, ny = j + dx, i + dy
                    if in_range(nx, 0, c, ny, 0, r) and g[ny][nx] >= 0:
                        cnt += 1
                        next_g[ny][nx] += g[i][j] // 5
                next_g[i][j] += g[i][j] - cnt * (g[i][j] // 5)
            elif g[i][j] == -1:
                next_g[i][j] = -1
    return next_g


def air_flow(g, r, c, air_cleaner):
    dir = 0
    x, y = air_cleaner[0]
    y -= 1
    while dir < 4:
        nx, ny = x + dxs[upper_dir[dir]], y + dys[upper_dir[dir]]
        if not in_range(nx, 0, c, ny, 0, air_cleaner[0][1] + 1):
            dir += 1
        else:
            g[y][x] = g[ny][nx]
            x, y = nx, ny
    g[air_cleaner[0][1]][air_cleaner[0][0] + 1] = 0
    dir = 0
    x, y = air_cleaner[1]
    y += 1
    while dir < 4:
        nx, ny = x + dxs[lower_dir[dir]], y + dys[lower_dir[dir]]
        if not in_range(nx, 0, c, ny, air_cleaner[1][1], r):
            dir += 1
        else:
            g[y][x] = g[ny][nx]
            x, y = nx, ny
    g[air_cleaner[1][1]][air_cleaner[1][0] + 1] = 0


def solution():
    r, c, t = map(int, sys.stdin.readline().rstrip().split())
    g = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(r)]
    air_cleaner = []
    for i in range(r):
        for j in range(c):
            if g[i][j] == -1 and not air_cleaner:
                air_cleaner.append([j, i])
                air_cleaner.append([j, i + 1])
    while t:
        g = spread_dust(g, r, c)
        air_flow(g, r, c, air_cleaner)
        t -= 1
    print(sum(g[i][j] for i in range(r) for j in range(c)) + 2)


if __name__ == "__main__":
    solution()
