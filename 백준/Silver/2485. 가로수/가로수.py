import sys
import math
from functools import reduce


def solution():
    n = int(sys.stdin.readline().rstrip())
    g = []
    pre_pos = 0
    for i in range(n):
        cur = int(sys.stdin.readline().rstrip())
        if pre_pos:
            g.append(abs(cur - pre_pos))
        pre_pos = cur
    gcd = reduce(lambda a, b: math.gcd(a, b), g)
    print(sum([a // gcd for a in g]) - len(g))


if __name__ == "__main__":
    solution()
