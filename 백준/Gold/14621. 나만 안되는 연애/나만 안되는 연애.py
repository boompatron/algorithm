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
    n, m = map(int, sys.stdin.readline().rstrip().split())
    univ_sex = list(map(str, sys.stdin.readline().rstrip().split()))
    adj, parent = [], [i for i in range(n)]
    ans = 0
    for i in range(m):
        u, v, d = map(int, sys.stdin.readline().rstrip().split())
        adj.append([u - 1, v - 1, d])
    adj.sort(key=lambda x: x[2])
    for v1, v2, dis in adj:
        if get_parent(parent, v1) != get_parent(parent, v2) and univ_sex[v1] != univ_sex[v2]:
            union_parent(parent, v1, v2)
            ans += dis
    is_all_connected = True
    for i in range(1, n):
        if get_parent(parent, i) != 0:
            is_all_connected = False
    if is_all_connected:
        print(ans)
    else:
        print(-1)


if __name__ == "__main__":
    solution()
