from collections import defaultdict
adj = defaultdict(list)
ans = []


def dfs(cur):
    while adj[cur]:
        dfs(adj[cur].pop(0))
    if not adj[cur]:
        ans.append(cur)
        return


def solution(t):
    for a, b in t:
        adj[a].append(b)
    for value in adj.values():
        value.sort()
    dfs('ICN')
    return ans[::-1]