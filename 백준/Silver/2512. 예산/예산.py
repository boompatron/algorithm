import sys


n = int(sys.stdin.readline().rstrip())
g = list(map(int, sys.stdin.readline().rstrip().split()))
b = int(sys.stdin.readline().rstrip())
left, right = 1, max(g)
while left <= right:
    mid = (left + right) // 2
    b_sum = 0
    for i in g:
        b_sum += i if i < mid else mid
    if b_sum <= b:
        left = mid + 1
    else:
        right = mid - 1
print(right)
