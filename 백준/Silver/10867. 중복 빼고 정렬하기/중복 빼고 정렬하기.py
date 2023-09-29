import sys


def solution():
    n = int(sys.stdin.readline().rstrip())
    g = set(map(int, sys.stdin.readline().rstrip().split()))
    print(' '.join(map(str, sorted(g))))


if __name__ == "__main__":
    solution()
