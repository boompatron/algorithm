def solution(board, skill):
    n, m = len(board), len(board[0])
    prefix_sum_board = [[0 for _ in range(m + 1)] for __ in range(n + 1)]
    for is_attack, y1, x1, y2, x2, degree in skill:
        val = -degree if is_attack == 1 else degree
        prefix_sum_board[y1][x1] += val
        prefix_sum_board[y2 + 1][x2 + 1] += val
        prefix_sum_board[y2 + 1][x1] += -val
        prefix_sum_board[y1][x2 + 1] += -val
    for i in range(n):
        for j in range(1, m):
            prefix_sum_board[i][j] += prefix_sum_board[i][j - 1]
    for j in range(m):
        for i in range(1, n):
            prefix_sum_board[i][j] += prefix_sum_board[i - 1][j]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] + prefix_sum_board[i][j] > 0:
                cnt += 1
    return cnt