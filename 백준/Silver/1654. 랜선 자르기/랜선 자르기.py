import sys


k, n = map(int, sys.stdin.readline().rstrip().split())
g = [int(sys.stdin.readline().rstrip()) for _ in range(k)]

left, right = 1, max(g)

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for i in g:
        cnt += i // mid
    if cnt >= n:
        left = mid + 1
    else:
        right = mid - 1
print(right)

