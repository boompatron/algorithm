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
    parent, ans = [i for i in range(n)], 0
    for i in range(m):
        v1, v2 = map(int, sys.stdin.readline().rstrip().split())
        if get_parent(parent, v1) != get_parent(parent, v2):
            union_parent(parent, v1, v2)
        elif get_parent(parent, v1) == get_parent(parent, v2) and not ans:
            ans = i + 1
            break
    print(ans)


if __name__ == "__main__":
    solution()
