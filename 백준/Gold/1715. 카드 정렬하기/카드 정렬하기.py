import sys
import heapq

n = int(sys.stdin.readline().rstrip())
ans = 0
hq = []
for i in range(n):
    heapq.heappush(hq, int(sys.stdin.readline().rstrip()))
while len(hq) > 1:
    a1, a2 = heapq.heappop(hq), heapq.heappop(hq)
    ans += a1 + a2
    heapq.heappush(hq, a1 + a2)
print(ans)
