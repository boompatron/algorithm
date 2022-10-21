import sys
from collections import deque
dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]


def main():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    g = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
    dq = deque()

    def in_range(a, b):
        return 0 <= a < m and 0 <= b < n

    def check_glacier_num():
        cnt = 0
        visited = [[False for _ in range(m)] for __ in range(n)]
        for a in range(1, n - 1):
            for b in range(1, m - 1):
                if g[a][b] and not visited[a][b]:
                    visited[a][b] = True
                    cnt += 1
                    dq.appendleft((b, a))
                    while dq:
                        x, y = dq.pop()
                        for dx, dy in zip(dxs, dys):
                            nx, ny = x + dx, y + dy
                            if in_range(nx, ny) and not visited[ny][nx] and g[ny][nx]:
                                dq.appendleft((nx, ny))
                                visited[ny][nx] = True
        return cnt

    def melt():
        add = [[0 for _ in range(m)] for __ in range(n)]
        for a in range(1, n - 1):
            for b in range(1, m - 1):
                if g[a][b]:
                    for dx, dy in zip(dxs, dys):
                        nx, ny = b + dx, a + dy
                        if not g[ny][nx]:
                            add[a][b] += 1
        for a in range(n):
            for b in range(m):
                g[a][b] -= add[a][b] if g[a][b] >= add[a][b] else g[a][b]

    ans = 0
    while 1:
        num = check_glacier_num()
        if num > 1:
            break
        elif num == 0:
            ans = 0
            break
        melt()
        ans += 1
    print(ans)


if __name__ == '__main__':
    main()
