import sys


def is_promising(g):
    for i in range(1, len(g) // 2 + 2):
        for j in range(len(g) - i):
            if g[j - i: j] == g[j:j + i] or g[j:j + i] == g[j + i: j + i * 2]:
                return False
    return True


def good_sequence(g, n):
    if is_promising(g):
        if len(g) == n:
            print(g)
            exit(0)
        else:
            for i in ('1', '2', '3'):
                good_sequence(g + i, n)


def solution():
    n = int(sys.stdin.readline().rstrip())
    good_sequence('', n)


if __name__ == "__main__":
    solution()
