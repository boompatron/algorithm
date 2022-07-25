import sys
import heapq


def solution():
    n = int(sys.stdin.readline().rstrip())
    a_hq, b_hq = [], []
    A = list(map(int, sys.stdin.readline().rstrip().split()))
    B = list(map(int, sys.stdin.readline().rstrip().split()))
    for a, b in zip(A, B):
        heapq.heappush(a_hq, -a)
        heapq.heappush(b_hq, b)
    ans = 0
    while n:
        ans -= heapq.heappop(a_hq) * heapq.heappop(b_hq)
        n -= 1
    print(ans)


if __name__ == "__main__":
    solution()
