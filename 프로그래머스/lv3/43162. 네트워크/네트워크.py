from collections import Counter


def get_parent(p, x):
    if p[x] != x:
        p[x] = get_parent(p, p[x])
    return p[x]


def union_parent(p, a, b):
    a = get_parent(p, a)
    b = get_parent(p, b)
    if a < b:
        p[b] = a
    elif a > b:
        p[a] = b
    else:
        return


def solution(n, computers):
    parent = [i for i in range(n + 1)]
    for i, a in enumerate(computers, start=1):
        for j, b in enumerate(a, start=1):
            if b:
                union_parent(parent, i, j)
    for i, e in enumerate(parent):
        parent[i] = get_parent(parent, i)
    return len(Counter(parent[1:]))