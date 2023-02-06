import sys

visited = [False for _ in range(31)]
for i in range(28):
    a = int(sys.stdin.readline().rstrip())
    visited[a] = True
for i in range(1, 31):
    if not visited[i]:
        print(i)