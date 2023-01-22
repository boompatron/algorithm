import sys
from copy import deepcopy


def solution():
    t = int(sys.stdin.readline().rstrip())
    while t:
        n, m = map(int, sys.stdin.readline().rstrip().split())
        g = map(int, sys.stdin.readline().rstrip().split())
        g1 = deepcopy(g)
        priority = sorted(g)
        printer_queue = list(enumerate(g1))
        cnt = 0
        while True:
            if printer_queue[0][1] == priority[-1]:
                cnt += 1
                if printer_queue[0][0] == m:
                    break
                printer_queue.pop(0)
                priority.pop()
            else:
                printer_queue.append(printer_queue.pop(0))
        print(cnt)
        t -= 1


if __name__ == "__main__":
    solution()
