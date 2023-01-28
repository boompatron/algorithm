import sys


def get_parent(p, x):
    if p[x] != x:
        p[x] = get_parent(p, p[x])
    return p[x]


def union_parent(p, a, b):
    a = get_parent(p, a)
    b = get_parent(p, b)
    if a > b:
        p[a] = b
    elif a < b:
        p[b] = a
    else:
        return


def solution():
    n = int(sys.stdin.readline().rstrip())
    g = []
    parent = [i for i in range(n)]
    star = [[0, 0] for _ in range(n)]
    for i in range(n):
        star[i][0], star[i][1] = map(float, sys.stdin.readline().rstrip().split())
    for i in range(n):
        for j in range(i + 1, n):
            dis = ((star[i][0] - star[j][0]) ** 2 + (star[i][1] - star[j][1]) ** 2) ** 0.5
            g.append([i, j, dis])
    g.sort(key=lambda x: x[2])
    ans = 0
    for v1, v2, d in g:
        if get_parent(parent, v1) != get_parent(parent, v2):
            union_parent(parent, v1, v2)
            ans += d
    print(round(ans, 2))


if __name__ == "__main__":
    solution()
