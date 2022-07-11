import sys


def solution():
    n = int(sys.stdin.readline().rstrip())
    g = []
    for i in range(n):
        num = int(sys.stdin.readline().rstrip())
        g.append(num)
    g.sort()
    for i in range(n):
        print(g[i])
    

if __name__ == "__main__":
    solution()
