import sys
cnt = 0
row = []
# row   [0] [2] [1] [3]
#       O   X   X   X
#       X   X   O   X
#       X   O   X   X
#       X   X   X   O


def is_promising(x):
    global row
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            # 첫번째 조건은 같은 행에 위치하는지 확인
            # 두 번째 조건은 대각선에 위치하는지 확인
            return False
    return True


def n_queen(x, n):
    global cnt
    if x == n:
        cnt += 1
        return
    for i in range(n):
        global row
        row[x] = i
        if is_promising(x):
            n_queen(x + 1, n)


def solution():
    global row, cnt
    n = int(sys.stdin.readline().rstrip())
    row = [0 for _ in range(n)]
    n_queen(0, n)
    print(cnt)


if __name__ == "__main__":
    solution()
