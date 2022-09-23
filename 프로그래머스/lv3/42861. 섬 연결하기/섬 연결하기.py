import heapq


def get_parent(p, x):
    if p[x] != x:
        p[x] = get_parent(p, p[x])
    return p[x]


def union_parent(p, a, b):
    a = get_parent(p, a)
    b = get_parent(p, b)
    if a < b:
        p[a] = b
    elif a > b:
        p[b] = a
    else:
        return


def solution(n, costs):
    hq, parent = [], list(range(n + 1))
    ans = 0
    for a, b, cost in costs:
        heapq.heappush(hq, [cost, a, b])
    while hq:
        cost, a, b = heapq.heappop(hq)
        if get_parent(parent, a) != get_parent(parent, b):
            union_parent(parent, a, b)
            ans += cost
    return ans