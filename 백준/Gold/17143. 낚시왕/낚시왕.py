import sys
import heapq
from copy import deepcopy
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
change_direction = {1: 3, 2: 1, 3: 0, 4: 2}


def in_range(x, y, n, m):
    return 0 <= x < m and 0 <= y < n


def catch_shark(hq, pos):
    tmp, y, idx = 0, 123456789, 0
    for i in range(len(hq)):
        if pos == hq[i][2] and y > hq[i][0]:
            tmp = -hq[i][1]
            y = hq[i][0]
            idx = i
    if y != 123456789:
        hq.pop(idx)
    return tmp


def move_shark(hq, n, m):
    tmp_hq, pos_list = [], {}
    while len(hq):
        y, z, x, s, d = heapq.heappop(hq) # -z : 크기, s 속도, d : 방향
        nx, ny = (x + dxs[d % 4] * s) % (2 * (m - 1)), (y + dys[d % 4] * s) % (2 * (n - 1))
        if not in_range(nx, ny, n, m):
            if nx >= m or -m <= nx < 0:
                nx = m - 1 - (nx % (m - 1))
                d += 2
            elif ny >= n or -n <= ny < 0:
                ny = n - 1 - (ny % (n - 1))
                d += 2
        if nx * 101 + ny not in pos_list or pos_list[nx * 101 + ny][0] < -z:
            pos_list[nx * 101 + ny] = [-z, s, d]
    for pk in pos_list.keys():
        x, y = pk // 101, pk % 101
        z, s, d = pos_list[pk]
        heapq.heappush(hq, [y, -z, x, s, d])


def solution():
    n, m, shark = map(int, sys.stdin.readline().rstrip().split())
    shark_hq, ans = [], 0
    for i in range(shark):
        y, x, s, d, z = map(int, sys.stdin.readline().rstrip().split())
        heapq.heappush(shark_hq, [y - 1, -z, x - 1, s, change_direction[d]])
    for i in range(m):
        ans += catch_shark(shark_hq, i)
        move_shark(shark_hq, n, m)
    print(ans)


if __name__ == "__main__":
    solution()

