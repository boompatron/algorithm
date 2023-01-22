import sys
import heapq

n = int(sys.stdin.readline().rstrip())
min_hq, max_hq = [], []
while n:
    a = int(sys.stdin.readline().rstrip())
    if len(min_hq) > len(max_hq):
        heapq.heappush(max_hq, a)
    else:
        heapq.heappush(min_hq, -a)
    if min_hq and max_hq and -min_hq[0] > max_hq[0]:
        min_val, max_val = -heapq.heappop(min_hq), heapq.heappop(max_hq)
        heapq.heappush(min_hq, -max_val)
        heapq.heappush(max_hq, min_val)
    print(-min_hq[0])
    n -= 1
