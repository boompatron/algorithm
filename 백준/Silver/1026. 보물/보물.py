import sys


def solution():
    n = int(sys.stdin.readline().rstrip())
    A = sorted(map(int, sys.stdin.readline().rstrip().split()))
    B = sorted(map(int, sys.stdin.readline().rstrip().split()), key=lambda x: -x)
    print(sum([a*b for a, b in zip(A, B)]))


if __name__ == "__main__":
    solution()
