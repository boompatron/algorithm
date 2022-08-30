import sys


def promising_nums(g, x, y, check):
    for i in range(9):
        if g[i][x] in check:
            check.remove(g[i][x])
        if g[y][i] in check:
            check.remove(g[y][i])
    for r in range(y // 3 * 3, y // 3 * 3 + 3):
        for c in range(x // 3 * 3, x // 3 * 3 + 3):
            if g[r][c] in check:
                check.remove(g[r][c])


def sudoku(g, zero, depth):
    if len(zero) == depth:
        for i in g:
            for j in i:
                print(j, end=" ")
            print()
        exit(0)
    check = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    cur = zero[depth]
    promising_nums(g, *cur, check)
    for c in check:
        g[cur[1]][cur[0]] = c
        sudoku(g, zero, depth + 1)
        g[cur[1]][cur[0]] = 0


def solution():
    g = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(9)]
    zero = []
    for y, e1 in enumerate(g):
        for x, e2 in enumerate(e1):
            if not e2:
                zero.append([x, y])
    sudoku(g, zero, 0)


if __name__ == "__main__":
    solution()
