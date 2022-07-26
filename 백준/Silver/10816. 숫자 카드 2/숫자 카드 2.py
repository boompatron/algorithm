import sys
from collections import Counter


def solution():
    n = int(sys.stdin.readline().rstrip())
    c = Counter(map(int, sys.stdin.readline().rstrip().split()))
    m = int(sys.stdin.readline().rstrip())
    g = list(map(int, sys.stdin.readline().rstrip().split()))
    ans = []
    for i in enumerate(g):
        ans.append(c[i[1]] if i[1] in c else 0)
    print(' '.join(map(str, ans)))


if __name__ == "__main__":
    solution()
