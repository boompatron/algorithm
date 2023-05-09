from itertools import product
import heapq


def solution(word):
    l, cnt = [], 1
    for i in range(1, 6):
        for p in product(['A', 'E', 'I', 'O', 'U'], repeat=i):
            heapq.heappush(l, ''.join(p))

    while heapq.heappop(l) != word:
        cnt += 1
    return cnt