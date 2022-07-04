import sys
INF = sys.maxsize


def bellman_ford(adj, ans, start, v):
    ans[start] = 0
    for i in range(v):
        for cur_idx, next_idx, cost in adj:
            if ans[next_idx] > ans[cur_idx] + cost:
                ans[next_idx] = ans[cur_idx] + cost
                if i == v - 1:
                    return True
    return False


def solution():
    tc = int(sys.stdin.readline().rstrip())
    while tc:
        v, e, w = map(int, sys.stdin.readline().rstrip().split())
        adj, ans = [], [INF for _ in range(v + 1)]
        d = {}
        for i in range(e):
            a, b, c = map(int, sys.stdin.readline().rstrip().split())
            if (a, b) not in d or d[(a, b)] > c:
                d[(a, b)] = c
        for k in d.keys():
            adj.append([k[0], k[1], d[k]])
            adj.append([k[1], k[0], d[k]])
        for i in range(w):
            a, b, c = map(int, sys.stdin.readline().rstrip().split())
            adj.append([a, b, -c])
        if bellman_ford(adj, ans, 1, v):
            print("YES")
        else:
            print("NO")
        tc -= 1


if __name__ == "__main__":
    solution()
