import sys
div_num = 1000000007


n, m, k = map(int, sys.stdin.readline().rstrip().split())
tree = [0 for _ in range((n + 1) * 4)]
g = [int(sys.stdin.readline().rstrip()) for _ in range(n)]


def init_tree(start: int, end: int, node: int):
    if start == end:
        tree[node] = g[start]
    else:
        mid = (start + end) // 2
        tree[node] = (init_tree(start, mid, node * 2) * init_tree(mid + 1, end, node * 2 + 1)) % div_num
    return tree[node]


def prefix_sum(start: int, end: int, node: int, left: int, right: int):
    if left > end or right < start:
        return 1

    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    return (prefix_sum(start, mid, node * 2, left, right) * prefix_sum(mid + 1, end, node * 2 + 1, left, right)) % div_num


def update_tree(start: int, end: int, node: int, index: int, diff: int):
    if index > end or index < start:
        return

    # tree[node] += diff
    # tree[node] = int(tree[node] * diff % div_num)

    if start == end:
        tree[node] = g[start]
        return

    mid = (start + end) // 2
    update_tree(start, mid, node * 2, index, diff)
    update_tree(mid + 1, end, node * 2 + 1, index, diff)

    tree[node] = tree[node * 2] * tree[node * 2 + 1] % div_num


init_tree(0, n - 1, 1)
for i in range(m + k):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    if a == 2:
        print(prefix_sum(0, n - 1, 1, b - 1, c - 1))
    else:
        # diff = c / g[b - 1]
        # g[b - 1] = c
        if g[b - 1]:
            diff = c / g[b - 1]
            g[b - 1] = c
        else:
            diff = c
            g[b - 1] = c
        update_tree(0, n - 1, 1, b - 1, diff)
