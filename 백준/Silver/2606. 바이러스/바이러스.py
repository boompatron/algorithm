import sys


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


def solution():
    v = int(sys.stdin.readline().rstrip())
    e = int(sys.stdin.readline().rstrip())
    parent = list(range(v + 1))
    while e:
        a, b = map(int, sys.stdin.readline().rstrip().split())
        union_parent(parent, a, b)
        e -= 1
    print(sum([1 for i in range(2, v + 1) if get_parent(parent, i) == 1]))


if __name__ == "__main__":
    solution()
