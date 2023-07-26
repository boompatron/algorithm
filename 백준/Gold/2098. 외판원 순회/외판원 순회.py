import sys
INF = sys.maxsize

n = int(sys.stdin.readline().rstrip())
g = []
for _ in range(n):
    g.append(list(map(int, sys.stdin.readline().rstrip().split())))
dp = [[-1 for _ in range(1 << n)] for _ in range(n)]
# g.insert(0, [])


def dfs(cur, visited):
    if visited == (1 << n) - 1:     # 모든 도시 방문
        if not g[cur][0]:               # 출발점으로 가는 경로가 존재한다
            return INF
        dp[cur][visited] = g[cur][0]
        return g[cur][0]

    if dp[cur][visited] != -1:     # 이미 최소 비용이 계산되어 있다
        return dp[cur][visited]

    min_dist = INF
    for i in range(n):           # 모든 도시를 탐방한다
        if not visited & (1 << i) and g[cur][i] != 0:
            min_dist = min(min_dist, dfs(i, visited | (1 << i)) + g[cur][i])
    dp[cur][visited] = min_dist
    return min_dist


print(dfs(0, 1))
