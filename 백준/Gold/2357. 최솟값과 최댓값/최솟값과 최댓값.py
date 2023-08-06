import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
g = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
min_tree = [0 for _ in range(len(g) * 4)]
max_tree = [0 for _ in range(len(g) * 4)]


def init_tree(start: int, end: int, node: int, tree: list, is_min: bool):
    if start == end:
        tree[node] = g[start]
        return tree[node]
    mid = (start + end) // 2
    if is_min:
        tree[node] = min(init_tree(start, mid, node * 2, tree, is_min),
                         init_tree(mid + 1, end, node * 2 + 1, tree, is_min))
    else:
        tree[node] = max(init_tree(start, mid, node * 2, tree, is_min),
                         init_tree(mid + 1, end, node * 2 + 1, tree, is_min))
    return tree[node]


def get_val(start: int, end: int, node: int, left: int, right: int, tree: list, is_min: bool):
    if left > end or right < start:
        return sys.maxsize if is_min else -sys.maxsize

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    if is_min:
        return min(get_val(start, mid, node * 2, left, right, tree, is_min),
                   get_val(mid + 1, end, node * 2 + 1, left, right, tree, is_min))
    else:
        return max(get_val(start, mid, node * 2, left, right, tree, is_min),
                   get_val(mid + 1, end, node * 2 + 1, left, right, tree, is_min))


init_tree(0, n - 1, 1, min_tree, True)
init_tree(0, n - 1, 1, max_tree, False)
for i in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    print(get_val(0, n - 1, 1, a - 1, b - 1, min_tree, True), get_val(0, n - 1, 1, a - 1, b - 1, max_tree, False))
