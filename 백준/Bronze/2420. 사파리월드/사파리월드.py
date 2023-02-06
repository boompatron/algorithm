import sys


l = list(map(int, sys.stdin.readline().rstrip().split()))
print(abs(l[0] - l[1]))