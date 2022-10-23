import sys


def main():
    print(''.join(bin(int(sys.stdin.readline().rstrip(), 8))[2:]))


if __name__ == '__main__':
    main()
