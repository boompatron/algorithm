import sys


def solution():
    n = int(sys.stdin.readline().rstrip())
    g = [[] for _ in range(n)]
    for i in range(n):
        g[i] = list(map(int, sys.stdin.readline().rstrip().split()))
    for i in sorted(g, key=lambda x: (x[0], x[1])): # 우선 x 좌표를 오름차순으로 정렬하고
																										# x 좌표가 같으면 y 좌표를 오름차순으로 정렬한다
        print(' '.join(map(str, i)))


if __name__ == "__main__":
    solution()