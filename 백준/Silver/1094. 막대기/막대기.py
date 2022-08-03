import sys


def solution():
    print(bin(int(sys.stdin.readline().rstrip())).count('1'))


if __name__ == "__main__":
    solution()
