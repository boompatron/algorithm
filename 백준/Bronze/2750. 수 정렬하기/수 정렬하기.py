import sys
import heapq


def solution():
    n = int(sys.stdin.readline().rstrip())
    hq = []
    while n:
        num = int(sys.stdin.readline().rstrip())
        heapq.heappush(hq, num)
        n -= 1
    while hq:
        print(heapq.heappop(hq))


if __name__ == "__main__":
    solution()
