import sys
import heapq


def solution():
    n = int(sys.stdin.readline().rstrip())
    hq = []
    while n:
        a = int(sys.stdin.readline().rstrip())
        if a:
            heapq.heappush(hq, -a)
        else:
            print(-heapq.heappop(hq) if hq else 0)
        n -= 1


if __name__ == "__main__":
    solution()
