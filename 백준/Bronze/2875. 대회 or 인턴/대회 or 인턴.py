import sys
n, m, k = map(int, sys.stdin.readline().rstrip().split())
for i in range(1, (n + m) // 3 + 2):
    if i * 2 > n or i > m or i * 3 + k > n + m:
        print(i - 1)
        break
