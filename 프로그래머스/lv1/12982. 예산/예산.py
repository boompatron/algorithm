import heapq


def solution(d, budget):
    answer = 0
    hq = []
    for money in d:
        heapq.heappush(hq, money)
    while hq:
        cur = heapq.heappop(hq)
        budget -= cur
        if budget >= 0:
            answer += 1
    return answer