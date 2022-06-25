import sys
INF = sys.maxsize


def bellman_ford(adj, ans, start, v, e):
    ans[start] = 0
    for i in range(v):
        for j in range(e):
            cur_idx, next_idx, cost = adj[j]
            if ans[cur_idx] != INF and ans[next_idx] > ans[cur_idx] + cost:
                ans[next_idx] = ans[cur_idx] + cost
                if i == v - 1:
                    return True
    return False


def solution():
    v, e = map(int, sys.stdin.readline().rstrip().split())
    adj, ans = [], [INF for _ in range(v + 1)]
    for _ in range(e):
        a, b, c = map(int, sys.stdin.readline().rstrip().split())
        adj.append([a, b, c])
    if bellman_ford(adj, ans, 1, v, e):
        print(-1)
    else:
        for i in range(2, v + 1):
            if ans[i] == INF:
                print(-1)
            else:
                print(ans[i])


if __name__ == "__main__":
    solution()
