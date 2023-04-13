import sys
INF = sys.maxsize


def bellman_ford(adj, ans, start, v, e):
    ans[start] = 0
    for i in range(1, v + 1):
        for j in range(e):
            cur_idx, next_idx, cost = adj[j]
            if ans[cur_idx] != INF and ans[next_idx] > ans[cur_idx] + cost:
                ans[next_idx] = ans[cur_idx] + cost
                if i == v:
                    return True
    return False


def solution():
    v, e = map(int, sys.stdin.readline().rstrip().split())
    adj, ans = [], [INF for _ in range(v + 1)]
    for i in range(e):
        a, b, c = map(int, sys.stdin.readline().rstrip().split())
        adj.append([a, b, c])
    if bellman_ford(adj, ans, 1, v, e):
        print(-1)
    else:
        for a in ans[2:]:
            if a == INF:
                print(-1)
            else:
                print(a)


if __name__ == "__main__":
    solution()
    