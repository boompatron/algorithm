from collections import deque
dxs, dys = (1, 0, -1, 0), (0, 1, 0, -1)
g = [[' ' for _ in range(103)] for __ in range(103)]
visited = [[False for _ in range(103)] for __ in range(103)]


# def print_graph(graph, size):
#     print('==-==--==-=-=--==-=-')
#     print(' ', end='\t')
#     for i in range(size):
#         print(i, end=' ')
#     print()
#     for i in range(size):
#         print(i, end='\t')
#         for j in range(size):
#             print(graph[i][j], end=' ')
#         print()
#     print('==-==--==-=-=--==-=-')


def in_range(a, b):
    return 0 <= a < 103 and 0 <= b < 103


def solution(r, cx, cy, ix, iy):
    for x1, y1, x2, y2 in r:
        for x in range(x1 * 2, x2 * 2 + 1):
            for y in range(y1 * 2, y2 * 2 + 1):
                if x1 * 2 < x < x2 * 2 and y1 * 2 < y < y2 * 2:
                    g[y][x] = '.'  # 내부 채우기
                elif g[y][x] != '.':
                    g[y][x] = '*'  # 테두리
    dq = deque()
    dq.appendleft((cx * 2, cy * 2, 0))
    cnt = 0
    while dq:
        x, y, d = dq.pop()
        if x == ix * 2 and y == iy * 2:
            cnt = d
            break
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and not visited[ny][nx] and g[ny][nx] == '*':
                dq.appendleft((nx, ny, d + 1))
                visited[ny][nx] = True
    # print_graph(g, 22)
    return cnt // 2