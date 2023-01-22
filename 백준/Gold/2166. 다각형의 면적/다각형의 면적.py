import sys


def cross_product(dot0, dot1, dot2):
    a = dot1[0] - dot0[0]
    b = dot1[1] - dot0[1]
    c = dot2[0] - dot0[0]
    d = dot2[1] - dot0[1]
    return a * d - b * c # abs(a * d - b * c)


def solution():
    n = int(sys.stdin.readline().rstrip())
    coord = [[0, 0] for _ in range(n)]
    for i in range(n):
        coord[i][0], coord[i][1] = map(int, sys.stdin.readline().rstrip().split())
    ans = 0
    for i in range(1, n - 1):
        ans += cross_product(coord[0], coord[i], coord[i + 1])
    print(abs(ans / 2))


if __name__ == "__main__":
    solution()
