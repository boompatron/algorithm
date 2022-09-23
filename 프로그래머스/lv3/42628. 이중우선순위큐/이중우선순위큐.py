import heapq


def solution(operations):
    max_hq, min_hq, removed = [], [], set()
    for operation in operations:
        inst, num = operation.split()
        num = int(num)
        if inst == 'D':
            if num == 1:
                while max_hq and -max_hq[0] in removed:
                    heapq.heappop(max_hq)
                if max_hq:
                    removed.add(-heapq.heappop(max_hq))
            else:
                while min_hq and min_hq[0] in removed:
                    heapq.heappop(min_hq)
                if min_hq:
                    removed.add(heapq.heappop(min_hq))
        else:
            heapq.heappush(min_hq, num)
            heapq.heappush(max_hq, -num)
    while min_hq and min_hq[0] in removed:
        heapq.heappop(min_hq)
    while max_hq and -max_hq[0] in removed:
        heapq.heappop(max_hq)
    return [-heapq.heappop(max_hq) if max_hq else 0, heapq.heappop(min_hq) if min_hq else 0]