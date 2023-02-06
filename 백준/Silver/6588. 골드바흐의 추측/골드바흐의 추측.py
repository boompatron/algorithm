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
    g = []
    while True:
        n = int(sys.stdin.readline().rstrip())
        if n == 0:
            primes = erasto(max(g))
            for num in g:
                ans = ""
                for i in range(3, num // 2 + 1, 2):
                    if i in primes and num - i in primes:
                        ans = f"{num} = {i} + {num - i}"
                        break
                print(ans if ans else "Goldbach's conjecture is wrong.")
            break
        else:
            g.append(n)


if __name__ == "__main__":
    solution()
