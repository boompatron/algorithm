from collections import deque
import heapq


def solution(priorities, location):
    dq = deque(enumerate(priorities))
    hq = []
    for p in priorities:
        heapq.heappush(hq, -p)
    cnt = 0
    while dq:
        if dq[0][1] == -hq[0]:
            cnt += 1
            heapq.heappop(hq)
            if dq[0][0] == location:
                break
            dq.popleft()
        else:
            dq.append(dq.popleft())
    return cnt