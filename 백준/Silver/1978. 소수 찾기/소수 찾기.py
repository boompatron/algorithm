import sys


def erasto(g, n):
    for i in range(2, n // 2 + 2):
        pos = 2 * i
        while pos <= n:
            g[pos] = False
            pos += i


def solution():
    n = int(sys.stdin.readline().rstrip())
    g = list(map(int, sys.stdin.readline().rstrip().split()))
    is_prime = [True for _ in range(max(g) + 1)]
    is_prime[0], is_prime[1] = False, False
    erasto(is_prime, max(g))
    print(sum([1 for i in g if is_prime[i]]))


if __name__ == "__main__":
    solution()
