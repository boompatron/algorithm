import sys


def get_parent(p, x):
    if p[x] != x:
        p[x] = get_parent(p, p[x])
    return p[x]


def union_parent(p, f, a, b):
    a = get_parent(p, a)
    b = get_parent(p, b)
    if a < b:
        p[b] = a
        f[a] = min(f[a], f[b])
    elif a > b:
        p[a] = b
        f[b] = min(f[a], f[b])
    else:
        return


def solution():
    v, e, k = map(int, sys.stdin.readline().rstrip().split())
    friend_fee = list(map(int, sys.stdin.readline().rstrip().split()))
    friend_fee.insert(0, 0)
    parent = [i for i in range(v + 1)]
    while e:
        friend = list(map(int, sys.stdin.readline().rstrip().split()))
        union_parent(parent, friend_fee, *sorted(friend))
        e -= 1
    for i in range(1, v + 1):
        get_parent(parent, i)
    total_fee = sum([friend_fee[s] for s in set(parent)])
    print(total_fee if total_fee <= k else "Oh no")


if __name__ == "__main__":
    solution()
