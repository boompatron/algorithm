import sys
from collections import deque


def solution():
    t = int(sys.stdin.readline().rstrip())
    while t:
        ans = ''
        p = sys.stdin.readline().rstrip()
        n = int(sys.stdin.readline().rstrip())
        d = deque(sys.stdin.readline().rstrip().strip('[').strip(']').strip('').split(','))
        if n == 0:
            d = deque()
        is_reversed = False
        # print(d, len(d))
        for i in p:
            if i == 'R':
                is_reversed = not is_reversed
            elif i == 'D':
                if len(d):
                    if is_reversed:
                        d.pop()
                    else:
                        d.popleft()
                else:
                    ans = 'error'

        if ans != 'error':
            ans += '['
            if is_reversed:
                while len(d):
                    ans += d.pop() + ','
            else:
                while len(d):
                    ans += d.popleft() + ','
            ans = ans[:-1]
            ans += ']'
        if ans == ']':
            ans = '[]'
        print(ans, end='\n')
        t -= 1


if __name__ == "__main__":
    solution()

