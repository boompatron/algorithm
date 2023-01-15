import sys
from itertools import combinations


def solution():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    g = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
    ans = sys.maxsize
    houses, chickens = [], []
    for i in range(n):
        for j in range(n):
            if g[i][j] == 1:
                houses.append([j, i])
            elif g[i][j] == 2:
                chickens.append([j, i])
    for c in combinations(chickens, m):
        tmp = 0
        for house in houses:
            indi_dis = sys.maxsize
            for x, y in c:
                indi_dis = min(indi_dis, abs(x - house[0]) + abs(y - house[1]))
            tmp += indi_dis
        ans = min(ans, tmp)
    print(ans)


if __name__ == '__main__':
    solution()
