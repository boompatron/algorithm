import sys


def solution():
    dxs, dys = [0, 1, 0, -1], [-1, 0, 1, 0]
    n, m = map(int, sys.stdin.readline().rstrip().split())
    y, x, direction = map(int, sys.stdin.readline().rstrip().split())
    g = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
    is_cleaned = [[False for _ in range(m)] for _ in range(n)]
    is_cleaned[y][x] = True

    while True:
        cnt = 0
        left_x, left_y = x + dxs[(direction - 1) % 4], y + dys[(direction - 1) % 4]
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if g[ny][nx] or not g[ny][nx] and is_cleaned[ny][nx]:
                cnt += 1
        if cnt == 4:
            back_x, back_y = x + dxs[(direction + 2) % 4], y + dys[(direction + 2) % 4]
            if g[back_y][back_x]:
                print(sum([1 for i in range(n) for j in range(m) if is_cleaned[i][j]]))
                break
            else:
                x, y = back_x, back_y
        elif not g[left_y][left_x] and not is_cleaned[left_y][left_x]:
            x, y = left_x, left_y
            is_cleaned[y][x] = True
            direction -= 1
        elif g[left_y][left_x] or not g[left_y][left_x] and is_cleaned[left_y][left_x]:
            # x, y = left_x, left_x
            direction -= 1


if __name__ == '__main__':
    solution()
