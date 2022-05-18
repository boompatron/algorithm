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
    adj = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(m)]
    ans = 0
    visited = [False for _ in range(n + 1)]
    parent = [i for i in range(n + 1)]
    total_price = sum([adj[i][2] for i in range(m)])
    adj.sort(key=lambda x: x[2])
    for v1, v2, dis in adj:
        if get_parent(parent, v1) != get_parent(parent, v2):
            union_parent(parent, v1, v2)
            visited[v1] = True
            visited[v2] = True
            ans += dis
    is_connected_all = True
    for i in range(2, n + 1):
        if get_parent(parent, i) != get_parent(parent, 1):
            is_connected_all = False
    if is_connected_all:
        print(total_price - ans)
    else:
        print(-1)


if __name__ == "__main__":
    solution()
