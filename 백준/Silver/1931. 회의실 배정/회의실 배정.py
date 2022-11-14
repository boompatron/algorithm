import sys
import heapq


def solution():
    n = int(sys.stdin.readline().rstrip())
    hq, cnt = [], 0
    for _ in range(n):
        start, end = map(int, sys.stdin.readline().rstrip().split())
        heapq.heappush(hq, [end, start])
    cur_time = 0
    while hq:
        end, start = heapq.heappop(hq)
        if start >= cur_time:
            cnt += 1
            cur_time = end
    print(cnt)


if __name__ == '__main__':
    solution()
