import sys
from itertools import combinations

n, m, h = map(int, sys.stdin.readline().rstrip().split())
ladder = [[False for _ in range(n)] for __ in range(h)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    ladder[a - 1][b - 1] = True


def go_down():
    for cur in range(n):
        pos = cur
        for i in range(h):
            if ladder[i][pos]:
                if pos == n - 1:
                    pos -= 1
                else:
                    pos += 1
            elif pos > 0 and ladder[i][pos - 1]:
                pos -= 1
        if pos != cur:
            return False
    return True


if go_down():
    print(0)
    exit(0)
else:
    ans = 1
    while ans < 4:
        for c in combinations(range(n * h), ans):
            tmp = []
            is_go = True
            for num in c:
                x, y = num % n, num // n
                if ladder[y][x] or (x < n - 1 and ladder[y][x + 1]):
                    is_go = False
                    continue
                tmp.append([x, y])

            if is_go:
                for x, y in tmp:
                    ladder[y][x] = True
                if go_down():
                    print(ans)
                    exit(0)
                for x, y in tmp:
                    ladder[y][x] = False
        ans += 1
print(-1)
