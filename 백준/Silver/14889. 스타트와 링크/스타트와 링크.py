import sys
from itertools import combinations


def solution():
    n = int(sys.stdin.readline().rstrip())
    g = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
    ans = sys.maxsize
    p = list(range(n))
    for team1 in combinations(p, n // 2):
        team2 = [i for i in p if i not in team1]
        team1_power = sum([g[a][b] + g[b][a] for a, b in combinations(team1, 2)])
        team2_power = sum([g[a][b] + g[b][a] for a, b in combinations(team2, 2)])
        if ans > abs(team1_power - team2_power):
            ans = abs(team1_power - team2_power)
    print(ans)


if __name__ == "__main__":
    solution()

