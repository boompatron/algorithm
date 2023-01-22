import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
g = list(map(int, sys.stdin.readline().rstrip().split()))
end, partial_sum, cnt = 0, 0, 0
for start in range(n):
    # end, partial_sum = start, 0
    while partial_sum < m and end < n:
        partial_sum += g[end]
        end += 1
    if partial_sum == m:
        cnt += 1
    partial_sum -= g[start]
print(cnt)
