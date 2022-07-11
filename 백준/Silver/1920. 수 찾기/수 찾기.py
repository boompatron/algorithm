import sys


def solution():
    n = int(sys.stdin.readline().rstrip())
    g1 = list(map(int, sys.stdin.readline().rstrip().split()))
    d = dict.fromkeys(g1)
    m = int(sys.stdin.readline().rstrip())
    g2 = list(map(int, sys.stdin.readline().rstrip().split()))
    for g in g2:
        print(1 if g in d else 0)


if __name__ == "__main__":
    solution()
