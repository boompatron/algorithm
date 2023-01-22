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


def get_distance(a, b):
    x_diff = (a[0] - b[0]) ** 2
    y_diff = (a[1] - b[1]) ** 2
    return (x_diff + y_diff) ** 0.5


def solution():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    space_gods, adj, parent = [], [], [i for i in range(n)]
    ans = 0
    for i in range(n):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        space_gods.append([x, y])
    for i in range(m):
        v1, v2 = map(int, sys.stdin.readline().rstrip().split())
        if get_parent(parent, v1 - 1) != get_parent(parent, v2 - 1):
            union_parent(parent, v1 - 1, v2 - 1)
    for i in range(n):
        for j in range(i + 1, n):
            adj.append([i, j, get_distance(space_gods[i], space_gods[j])])
    adj.sort(key=lambda a: a[2])
    for v1, v2, dis in adj:
        if get_parent(parent, v1) != get_parent(parent, v2):
            union_parent(parent, v1, v2)
            ans += dis
    print("{:.2f}".format(ans))


if __name__ == "__main__":
    solution()
