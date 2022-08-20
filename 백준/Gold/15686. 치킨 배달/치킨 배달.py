import sys
from itertools import combinations


def solution():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    g = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
    house, chicken = [], []
    ans = sys.maxsize
    for y, e1 in enumerate(g):
        for x, e2 in enumerate(e1):
            if e2 == 1:
                house.append((x, y))
            elif e2 == 2:
                chicken.append((x, y))
    for c in combinations(chicken, m):
        tmp = 0
        for house_x, house_y in house:
            chicken_len = sys.maxsize
            for chicken_x, chicken_y in c:
                chicken_len = min(chicken_len, abs(house_x - chicken_x) + abs(house_y - chicken_y))
            tmp += chicken_len
        ans = min(tmp, ans)
    print(ans)


if __name__ == "__main__":
    solution()
