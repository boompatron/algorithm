import sys
n = int(sys.stdin.readline())
i = 665
while n:
    l = str(i)
    if "666" in l:
        n -= 1
    i += 1
print(i - 1)