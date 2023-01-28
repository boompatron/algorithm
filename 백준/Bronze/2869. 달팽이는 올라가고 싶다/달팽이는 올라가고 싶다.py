import sys


a, b, v = map(int, sys.stdin.readline().rstrip().split())
print(((v - a) // (a - b) if (v - a) % (a - b) == 0 else (v - a) // (a - b) + 1) + 1)
