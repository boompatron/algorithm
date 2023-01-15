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
    v, e = map(int, sys.stdin.readline().rstrip().split())
    adj, parent, ans = [], [i for i in range(v + 1)], 0
    for i in range(e):
        a, b, c = map(int, sys.stdin.readline().rstrip().split())
        adj.append([a, b, c])
    adj.sort(key=lambda x: x[2])
    for v1, v2, dis in adj:
        if get_parent(parent, v1) != get_parent(parent, v2):
            union_parent(parent, v1, v2)
            ans += dis
    print(ans)


if __name__ == "__main__":
    solution()

