import sys


n = int(sys.stdin.readline())
B = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
w_cnt, b_cnt = 0, 0

def div_conq(x, y, N):
    global w_cnt, b_cnt
    tmp_cnt = 0
    for i in range(x, x + N):
        for j in range(y, y + N):
            if B[i][j]:
                tmp_cnt += 1
    if not tmp_cnt:
        w_cnt += 1
    elif tmp_cnt == N**2:
        b_cnt += 1
    else:
        div_conq(x, y, N // 2)
        div_conq(x + N // 2, y, N // 2)
        div_conq(x, y + N // 2, N // 2)
        div_conq(x + N // 2, y + N // 2, N // 2)
    return

div_conq(0, 0, n)
print(w_cnt)
print(b_cnt)