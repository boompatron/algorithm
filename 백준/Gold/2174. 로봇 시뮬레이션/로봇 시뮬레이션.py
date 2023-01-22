import sys
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
direction = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
a, b = map(int, sys.stdin.readline().rstrip().split())
n, m = map(int, sys.stdin.readline().rstrip().split())
g = [[0 for _ in range(a)] for __ in range(b)]
robots = {}


def in_range(aa, bb):
    return 0 <= aa < a and 0 <= bb < b


for _ in range(n):
    x, y, d = map(str, sys.stdin.readline().rstrip().split())
    g[int(y) - 1][int(x) - 1] = _ + 1
    robots[_ + 1] = [int(x) - 1, int(y) - 1, direction[d]]
for _ in range(m):
    robot, inst, repeat = map(str, sys.stdin.readline().rstrip().split())
    for i in range(int(repeat)):
        if inst == 'L':
            robots[int(robot)][2] -= 1
        elif inst == 'R':
            robots[int(robot)][2] += 1
        else:   # inst == 'F'
            x, y, dir = robots[int(robot)][0], robots[int(robot)][1], robots[int(robot)][2]
            nx, ny = x + dxs[dir % 4], y + dys[dir % 4]
            if not in_range(nx, ny):
                print(f"Robot {g[y][x]} crashes into the wall")
                exit(0)
            elif g[ny][nx] != 0:
                print(f"Robot {g[y][x]} crashes into robot {g[ny][nx]}")
                exit(0)
            else:
                g[ny][nx] = g[y][x]
                g[y][x] = 0
                robots[int(robot)] = [nx, ny, dir]
print("OK")
