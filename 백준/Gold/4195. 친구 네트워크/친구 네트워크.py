import sys


def get_parent(p, x):
    if p[x] != x:
        p[x] = get_parent(p, p[x])
    return p[x]


def union_parent(p, n, a, b):
    a = get_parent(p, a)
    b = get_parent(p, b)
    if a != b:
        p[b] = a
        n[a] += n[b]


def solution():
    tc = int(sys.stdin.readline().rstrip())
    while tc:
        f = int(sys.stdin.readline().rstrip())
        parent = {}
        friend_num = {}
        while f:
            friends = list(map(str, sys.stdin.readline().rstrip().split()))
            for fs in friends:
                if fs not in parent:
                    parent[fs] = fs
                    friend_num[fs] = 1
            union_parent(parent, friend_num, *friends)
            print(friend_num[get_parent(parent, friends[0])])
            f -= 1
        tc -= 1


if __name__ == "__main__":
    solution()
