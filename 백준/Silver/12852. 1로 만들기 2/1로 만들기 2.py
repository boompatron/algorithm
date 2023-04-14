import sys
from collections import deque
n = int(sys.stdin.readline().rstrip())
dp = [123456789 for _ in range(3 * n + 1)]
dp[n] = 0
for i in range(n - 1, 0, -1):
    dp[i] = min(dp[i * 3] + 1, dp[i * 2] + 1, dp[i + 1] + 1)
print(dp[1])
dq = deque()
num = 1
while num <= n:
    dq.append(num)
    if dp[num] - 1 == dp[num * 3]:
        num *= 3
    elif dp[num] - 1 == dp[num * 2]:
        num *= 2
    else:
        num += 1
while dq:
    print(dq.pop(), end=" ")
