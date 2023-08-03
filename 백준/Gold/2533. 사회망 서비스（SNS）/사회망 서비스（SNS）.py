import sys
sys.setrecursionlimit(10 ** 7)


n = int(sys.stdin.readline().rstrip())
adj = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
dp = [[0 for _ in range(2)] for __ in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    adj[a].append(b)
    adj[b].append(a)


def find(cur):
    visited[cur] = True
    dp[cur][0] = 1
    for child in adj[cur]:
        if visited[child]:
            continue
        find(child)
        dp[cur][1] += dp[child][0]
        dp[cur][0] += min(dp[child][0], dp[child][1])


find(1)
print(min(dp[1][0], dp[1][1]))
