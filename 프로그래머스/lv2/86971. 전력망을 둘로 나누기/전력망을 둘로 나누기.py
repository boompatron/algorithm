import sys
from itertools import combinations
from collections import Counter


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


def solution(n, wires):
    ans = sys.maxsize
    for c in combinations(wires, n - 2):
        parent = [i for i in range(n + 1)]
        for a, b in c:
            if get_parent(parent, a) != get_parent(parent, b):
                union_parent(parent, a, b)
        for i in range(1, n + 1):
            get_parent(parent, i)
        c = Counter(parent[1:])
        ans = min(abs(list(c.values())[0] - list(c.values())[1]), ans)
    return ans