import sys
sys.setrecursionlimit(10 ** 9)


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


def solution():
    v, e = map(int, sys.stdin.readline().rstrip().split())
    parent = [i for i in range(v + 1)]
    for i in range(e):
        c, a, b = map(int, sys.stdin.readline().rstrip().split())
        if c:
            if get_parent(parent, a) == get_parent(parent, b):
                print("YES")
            else:
                print("NO")
        else:
            union_parent(parent, a, b)


if __name__ == "__main__":
    solution()
