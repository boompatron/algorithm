import sys
INF = 1e7


def main():
    v, e = map(int, sys.stdin.readline().rstrip().split())
    adj = [[INF for _ in range(v + 1)] for _ in range(v + 1)]
    for _ in range(e):
        v1, v2, distance = map(int, sys.stdin.readline().rstrip().split())
        adj[v1][v2] = distance

    for i in range(1, v + 1):
        for j in range(1, v + 1):
            for k in range(1, v + 1):
                if adj[i][k] + adj[k][j] < adj[i][j]:
                    adj[i][j] = adj[i][k] + adj[k][j]
    ans = INF
    for i in range(1, v + 1):
        ans = min(ans, adj[i][i])
    print(ans if ans != INF else -1)


if __name__ == '__main__':
    main()
