import sys
from collections import defaultdict

n = int(sys.stdin.readline().rstrip())
g = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
election = [[]]
ans = sys.maxsize


def divide_area(a, b, e1, e2):
    global election
    election = [[0 for _ in range(n + 1)] for __ in range(n + 1)]
    for r in range(1, b + e1):
        for c in range(1, a + 1):
            election[r][c] = 1
    for r in range(1, b + e2 + 1):
        for c in range(a + 1, n + 1):
            election[r][c] = 2
    for r in range(b + e1, n + 1):
        for c in range(1, a - e1 + e2):
            election[r][c] = 3
    for r in range(b + e2 + 1, n + 1):
        for c in range(a - e1 + e2, n + 1):
            election[r][c] = 4

    for i in range(e1 + 1):
        election[b + i][a - i] = 5
    for i in range(e2 + 1):
        election[b + i][a + i] = 5
    for i in range(e2 + 1):
        election[b + e1 + i][a - e1 + i] = 5
    for i in range(e1 + 1):
        election[b + e2 + i][a + e2 - i] = 5

    for i in range(b + 1, b + e1 + e2):
        is_five = False
        for j in range(1, n + 1):
            if election[i][j] == 5:
                is_five = not is_five
            else:
                if is_five:
                    election[i][j] = 5


def calculate_population():
    global ans
    d = defaultdict(int)
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            d[election[a][b]] += g[a - 1][b - 1]
    ans = min(max(d.values()) - min(d.values()), ans)


def in_range(a, b, e1, e2):
    if a - e1 <= 0 or a + e1 > n + 1:
        return False
    if b + e1 + e1 > n + 1:
        return False
    return True


for x in range(1, n + 1):
    for y in range(1, n + 1):
        for d1 in range(1, x):
            for d2 in range(1, n - x + 1):
                if d1 + d2 <= n - y and in_range(x, y, d1, d2):
                    divide_area(x, y, d1, d2)
                    calculate_population()

print(ans)
