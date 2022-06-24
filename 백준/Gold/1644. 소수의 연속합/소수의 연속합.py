import sys
n = int(sys.stdin.readline().rstrip())
isPrime, primeList = [False for _ in range(n + 1)], []
isPrime[0], isPrime[1] = True, True


def eval_prime_by_sieve_of_Erastosthenes():
    global n
    pos = 2
    while pos <= n:
        if not isPrime[pos]:
            num = pos * 2
            while num <= n:
                isPrime[num] = True
                num += pos
        pos += 1
    for i in range(n + 1):
        if not isPrime[i]:
            primeList.append(i)
    # print(primeList)


def two_pointer_sum_cal():
    global n
    end, partial_sum, ans = 0, 0, 0
    for start in range(len(primeList)):
        while partial_sum < n and end < len(primeList):
            partial_sum += primeList[end]
            end += 1
        if partial_sum == n:
            ans += 1
        partial_sum -= primeList[start]
    print(ans)


eval_prime_by_sieve_of_Erastosthenes()
two_pointer_sum_cal()
