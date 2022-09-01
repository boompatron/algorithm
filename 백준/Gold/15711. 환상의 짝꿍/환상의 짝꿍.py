import sys


def erasto(n):
    is_prime = [True for _ in range(n + 1)]
    is_prime[1] = False
    for i in range(2, int(n ** 1 / 2) + 1):
        j = 2
        while i * j <= n:
            is_prime[i * j] = False
            j += 1
    return {i for i, e in enumerate(is_prime[2:], start=2) if e}


def solution():
    n = int(sys.stdin.readline().rstrip())
    g = []
    for i in range(n):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        g.append(a + b)
    # primes = erasto(int(max(g) ** 1/2))
    primes = erasto(10 ** 6 * 2)
    for num in g:
        ans = 'NO'
        if num > 3 and num % 2 == 0:
            ans = 'YES'
        elif num % 2:
            if num - 2 < 10 ** 6 * 2 and num - 2 in primes:
                ans = 'YES'
            elif num - 2 > 10 ** 6 * 2:
                flag = False
                for p in primes:
                    if (num - 2) % p == 0:
                        flag = True
                ans = 'NO' if flag else 'YES'
        print(ans)


if __name__ == "__main__":
    solution()
