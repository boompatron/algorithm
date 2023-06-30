import sys
sys.setrecursionlimit(10 ** 9)

n = int(sys.stdin.readline().rstrip())
adj = [[] for _ in range(n + 1)]
depth = [0 for _ in range(n + 1)]
parent = [i for i in range(n + 1)]
visited = [False for _ in range(n + 1)]
for i in range(n - 1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    adj[a].append(b)
    adj[b].append(a)


def set_tree(node, dep):
    visited[node] = True
    depth[node] = dep

    for child in adj[node]:
        if visited[child]:
            continue
        parent[child] = node
        set_tree(child, dep + 1)


set_tree(1, 0)
for i in range(2, n + 1):
    print(parent[i])
