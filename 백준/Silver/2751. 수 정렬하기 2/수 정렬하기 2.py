import sys
n = int(input())
l = [0 for i in range(n)]
for i in range(n):
    t = int(sys.stdin.readline())
    l[i] = t
a = sorted(l, key=lambda x: x)
#print(a)
for i in a:
    print(i)