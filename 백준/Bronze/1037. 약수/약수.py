import sys
from functools import reduce


def factorization(a, g): # 인수분해
    tmp, cur = a, 2
    while tmp > 1:
        if tmp % cur == 0:
            if cur in g:
                g[cur] += 1
            else:
                g[cur] = 1
            tmp //= cur
            cur = 2
        else:
            cur += 1


def solution():
    a = int(sys.stdin.readline().rstrip())
    g = list(map(int, sys.stdin.readline().rstrip().split()))
    d_g, ans_d = [{} for _ in range(a)], {}
    for i in range(a):
        factorization(g[i], d_g[i])
    lcm_factor = reduce(lambda m, n: set(m) | set(n), d_g)
    for d in d_g:
        for k in d.keys():
            if k not in ans_d or ans_d[k] < d[k]:
                ans_d[k] = d[k]
    ans = reduce(lambda m, n: m * n, [k ** ans_d[k] for k in ans_d.keys()])
    if ans in g:
        ans *= min(g)
    print(ans)


if __name__ == "__main__":
    solution()
