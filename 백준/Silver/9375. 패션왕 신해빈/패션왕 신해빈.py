import sys
from collections import defaultdict
from functools import reduce

testcase = int(sys.stdin.readline().rstrip())
for tc in range(testcase):
    n = int(sys.stdin.readline().rstrip())
    dd = defaultdict(int)
    for i in range(n):
        a, b = sys.stdin.readline().rstrip().split()
        dd[b] += 1
    tmp = map(lambda x: x + 1, dd.values())
    ans = 1
    for t in tmp:
        ans *= t
    print(ans - 1)
