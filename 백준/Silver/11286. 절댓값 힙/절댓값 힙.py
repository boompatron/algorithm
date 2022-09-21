import sys
import heapq


def solution():
    n = int(sys.stdin.readline().rstrip())
    hq = []
    while n:
        a = int(sys.stdin.readline().rstrip())
        if a:
            heapq.heappush(hq, [abs(a), False if a < 0 else True])
        else:
            if hq:
                num, is_positive = heapq.heappop(hq)
                print(num if is_positive else num * -1)
            else:
                print(0)
        n -= 1


if __name__ == "__main__":
    solution()


