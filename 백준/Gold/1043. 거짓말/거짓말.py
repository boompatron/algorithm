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
    n, m = map(int, sys.stdin.readline().rstrip().split())
    parent = [i for i in range(n + 1)]
    party = [[] for _ in range(m)]
    cnt = 0
    know = list(map(int, sys.stdin.readline().rstrip().split()))[1:]
    for i in range(m):
        party[i] = list(map(int, sys.stdin.readline().rstrip().split()))[1:]
        p_parent = min(party[i])
        for p in party[i]:
            union_parent(parent, p, p_parent)
    know_parent = []
    for k in know:
        know_parent.append(get_parent(parent, k))
    for i in range(m):
        is_know = False
        for p in party[i]:
            if get_parent(parent, p) in know_parent:
                is_know = True
        if not is_know:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    solution()
