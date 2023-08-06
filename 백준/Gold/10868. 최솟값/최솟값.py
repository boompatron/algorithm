import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
g = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
tree = [0 for _ in range(len(g) * 4)]


def init_tree(start: int, end: int, node: int):
    if start == end:
        tree[node] = g[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = min(init_tree(start, mid, node * 2), init_tree(mid + 1, end, node * 2 + 1))
    return tree[node]


def get_min(start: int, end: int, node: int, left: int, right: int):
    if left > end or right < start:
        return sys.maxsize

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return min(get_min(start, mid, node * 2, left, right), get_min(mid + 1, end, node * 2 + 1, left, right))


init_tree(0, n - 1, 1)
for i in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(get_min(0, n - 1, 1, a - 1, b - 1))
