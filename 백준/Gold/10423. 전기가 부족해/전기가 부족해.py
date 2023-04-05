import sys


def get_parent(p, x):
    if p[x] != x:
        p[x] = get_parent(p, p[x])
    return p[x]


def union_parent(p, a, b, p_p):
    a = get_parent(p, a)
    b = get_parent(p, b)
    if a in p_p:
        p[b] = a
    elif b in p_p:
        p[a] = b
    elif a > b:
        p[a] = b
    elif a < b:
        p[b] = a
    else:
        return


def solution():
    n, m, k = map(int, sys.stdin.readline().rstrip().split())
    power_plant = list(map(int, sys.stdin.readline().rstrip().split()))
    power_plant_d = {}
    for i in power_plant:
        power_plant_d[i] = 1
    adj, parent = [], [i for i in range(n + 1)]
    ans = 0
    for i in range(m):
        u, v, w = map(int, sys.stdin.readline().rstrip().split())
        adj.append([u, v, w])
    adj.sort(key=lambda x: x[2])
    for v1, v2, dis in adj:
        if get_parent(parent, v1) != get_parent(parent, v2) and not ((get_parent(parent, v1) in power_plant_d) & (get_parent(parent, v2) in power_plant_d)):
            union_parent(parent, v1, v2, power_plant_d)
            ans += dis
    print(ans)


if __name__ == "__main__":
    solution()
