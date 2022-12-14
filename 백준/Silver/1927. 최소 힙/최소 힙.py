import sys
import heapq

n = int(sys.stdin.readline().rstrip())
hq = []
while n:
    a = int(sys.stdin.readline().rstrip())
    if a:
        heapq.heappush(hq, a)
    else:
        print(0 if not hq else heapq.heappop(hq))
    n -= 1
