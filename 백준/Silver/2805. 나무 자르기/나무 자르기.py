import sys


n, m = map(int, sys.stdin.readline().rstrip().split())
g = list(map(int, sys.stdin.readline().rstrip().split()))
g.sort(reverse=True)
left, right = 0, max(g)

while left <= right:
    mid = (left + right) // 2
    tree_sum = 0
    for tree in g:
        if tree < mid:
            break
        tree_sum += tree - mid
    if tree_sum < m:
        right = mid - 1
    else:
        left = mid + 1
print(right)
