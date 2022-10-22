import sys


def main():
    n, k = map(int, sys.stdin.readline().rstrip().split())
    a1, a2 = 1, 1
    for i in range(n, n - k, -1):
        a1 *= i
    for i in range(k, 0, -1):
        a2 *= i
    print(a1 // a2 % 10007)


if __name__ == '__main__':
    main()