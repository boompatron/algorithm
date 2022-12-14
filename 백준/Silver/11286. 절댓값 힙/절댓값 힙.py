import sys
import heapq

n = int(sys.stdin.readline().rstrip())
hq = []
while n:
    a = int(sys.stdin.readline().rstrip())
    if a:
        heapq.heappush(hq, [abs(a), a > 0])
    else:
        if not hq:
            print(0)
        else:
            val, isPositive = heapq.heappop(hq)
            print(val if isPositive else -val)
    n -= 1
