import sys


def solution():
    n = int(sys.stdin.readline().rstrip())
    g = ['' for _ in range(n)]
    for _ in range(n):
        g[_] = sys.stdin.readline().rstrip()
    print('\n'.join(sorted(set(g), key=lambda x: (len(x), x))))


if __name__ == "__main__":
    solution()
