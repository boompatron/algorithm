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


n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
parent = [i for i in range(n + 1)]
adj = []
for i in range(m):
    v1, v2, dis = map(int, sys.stdin.readline().rstrip().split())
    adj.append([v1, v2, dis])
adj.sort(key=lambda x: x[2])
ans = 0
for v1, v2, dis in adj:
    if get_parent(parent, v1) != get_parent(parent, v2):
        union_parent(parent, v1, v2)
        ans += dis
print(ans)
