def solution(board, skill):
    n, m, cnt = len(board), len(board[0]), 0
    prefix_sum = [[0 for _ in range(m + 1)] for __ in range(n + 1)]
    for attak_type, y1, x1, y2, x2, degree in skill:
        val = -degree if attak_type == 1 else degree
        prefix_sum[y1][x1] += val
        prefix_sum[y2 + 1][x2 + 1] += val
        prefix_sum[y1][x2 + 1] -= val
        prefix_sum[y2 + 1][x1] -= val
    for i in range(n + 1):
        for j in range(m):
            prefix_sum[i][j + 1] += prefix_sum[i][j]
    for j in range(m + 1):
        for i in range(n):
            prefix_sum[i + 1][j] += prefix_sum[i][j]
    for i in range(n):
        for j in range(m):
            if board[i][j] > -prefix_sum[i][j]:
                cnt += 1
    return cnt