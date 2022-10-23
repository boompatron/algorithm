import sys


def main():
    g = str(sys.stdin.readline().rstrip())
    g = g.replace('XXXX', 'AAAA').replace('XX', 'BB')
    print(g if 'X' not in g else -1)


if __name__ == '__main__':
    main()
