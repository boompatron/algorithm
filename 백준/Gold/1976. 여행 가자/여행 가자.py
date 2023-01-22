import sys
n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
parent = [i for i in range(n + 1)]


def find_parent(p, x):
    if p[x] != x:
        p[x] = find_parent(p, p[x])
    return p[x]


def union_parent(p, a, b):
    a = find_parent(p, a)
    b = find_parent(p, b)
    if a < b:
        p[b] = a
    elif a > b:
        p[a] = b
    else:
        return


g = [[0 for _ in range(n + 1)] for __ in range(n + 1)]
for i in range(1, n + 1):
    g[i] = list(map(int, sys.stdin.readline().rstrip().split()))
    g[i].insert(0, 0)
    for j in range(1, n + 1):
        if g[i][j] and find_parent(parent, i) != find_parent(parent, j):
            union_parent(parent, i, j)
travel = list(map(int, sys.stdin.readline().rstrip().split()))
ans_list = []
for t in travel:
    ans_list.append(parent[t])
if len(set(ans_list)) == 1:
    print("YES")
else:
    print("NO")
