from collections import defaultdict


def solution(info, edges):
    adj = defaultdict(set)
    for u, v in edges:
        adj[u].add(v)
    ans = [0 for _ in range(len(info))]

    def dfs(cur: int, sheep: int, wolf: int, next_nums: set):
        if info[cur]:
            wolf += 1
        else:
            sheep += 1
        ans[cur] = max(ans[cur], sheep)
        if sheep <= wolf:
            return
        next_nums |= adj[cur]
        if not next_nums:
            return
        for n in list(next_nums):
            dfs(n, sheep, wolf, {i for i in next_nums if i != n})
    dfs(0, 0, 0, set())
    return max(ans)