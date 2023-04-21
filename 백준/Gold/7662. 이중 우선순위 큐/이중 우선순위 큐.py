import sys
import heapq
tc = int(sys.stdin.readline().rstrip())
while tc:
    k = int(sys.stdin.readline().rstrip())
    deleted = [False for _ in range(k)]
    max_hq, min_hq = [], []
    for i in range(k):
        inst, num = sys.stdin.readline().rstrip().split()
        num = int(num)
        if inst == 'I':
            heapq.heappush(min_hq, (num, i))
            heapq.heappush(max_hq, (-num, i))
            deleted[i] = True
        else:
            if num == 1:  # 최댓값 삭제
                while max_hq and not deleted[max_hq[0][1]]:
                    heapq.heappop(max_hq)
                if max_hq:
                    deleted[max_hq[0][1]] = False
                    heapq.heappop(max_hq)
            else:  # 최솟값 삭제
                while min_hq and not deleted[min_hq[0][1]]:
                    heapq.heappop(min_hq)
                if min_hq:
                    deleted[min_hq[0][1]] = False
                    heapq.heappop(min_hq)
    while max_hq and not deleted[max_hq[0][1]]:
        heapq.heappop(max_hq)
    while min_hq and not deleted[min_hq[0][1]]:
        heapq.heappop(min_hq)
    print('EMPTY' if not max_hq or not min_hq else f'{-max_hq[0][0]} {min_hq[0][0]}')
    tc -= 1
