import sys


def main():
    n = int(sys.stdin.readline().rstrip())
    g, ans = [], 0
    for _ in range(n):
        tmp = int(sys.stdin.readline().rstrip())
        g.append(tmp)
    g.sort(reverse=True)
    for i in range(n):
        ans = max(ans, (i + 1) * g[i])
    print(ans)


if __name__ == '__main__':
    main()
