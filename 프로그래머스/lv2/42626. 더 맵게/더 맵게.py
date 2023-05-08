import heapq


def solution(scoville, k):
    hq = []
    cnt = 0
    for s in scoville:
        heapq.heappush(hq, s)
    while len(hq) >= 2 and hq[0] < k:
        cnt += 1
        heapq.heappush(hq, heapq.heappop(hq) + heapq.heappop(hq) * 2)
    if hq[0] < k:
        return -1
    else: 
        return cnt
