import sys
sys.setrecursionlimit(10 ** 5)

n = int(sys.stdin.readline().rstrip())
adj = [[] for _ in range(n + 1)]
parent = [i for i in range(n + 1)]
depth = [0 for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(n - 1):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    adj[x].append(y)
    adj[y].append(x)


def set_tree(node: int, dep: int):
    # dfs 방식으로 트리를 구성한다
    visited[node] = True
    depth[node] = dep

    for child in adj[node]:
        if visited[child]:
            continue
        parent[child] = node
        set_tree(child, dep + 1)


def lca(a: int, b: int):
    # 먼저 깊이(depth)가 동일하도록
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = parent[a]
        else:
            b = parent[b]
    # 노드가 같아지도록
    while a != b:
        a = parent[a]
        b = parent[b]
    return a


set_tree(1, 0)

m = int(sys.stdin.readline().rstrip())
for _ in range(m):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    print(lca(x, y))
