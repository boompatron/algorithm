import sys
n, m = map(int, sys.stdin.readline().split())
d = {}
ans = []
for i in range(n):
    name = str(sys.stdin.readline())
    d[name] = 1
for i in range(m):
    name = str(sys.stdin.readline())
    if name in d:
        ans.append(name)
ans.sort()
print(len(ans))
for i in ans:
    print(i, end="")