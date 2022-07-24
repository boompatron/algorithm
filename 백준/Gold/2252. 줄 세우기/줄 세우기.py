import sys


def solution():
    n, m = map(int, sys.stdin.readline().rstrip().split())
    in_degree, g = [0 for _ in range(n + 1)], [[] for _ in range(n + 1)]
    while m:
        a, b = map(int, sys.stdin.readline().rstrip().split())
        in_degree[b] += 1
        g[a].append(b)
        m -= 1
    q, ans = [], []

    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.append(i)

    while q:
        cur = q.pop()
        ans.append(cur)
        for i in g[cur]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                q.append(i)
    print(" ".join(map(str, ans)))


if __name__ == "__main__":
    solution()
