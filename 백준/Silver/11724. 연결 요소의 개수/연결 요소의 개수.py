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


v, e = map(int, sys.stdin.readline().rstrip().split())
parent = [i for i in range(v + 1)]
while e:
    v1, v2 = map(int, sys.stdin.readline().rstrip().split())
    union_parent(parent, v1, v2)
    e -= 1
for i in range(1, v + 1):
    parent[i] = get_parent(parent, i)
print(len(set(parent[1:])))
