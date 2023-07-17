cnt = 0


def dfs(l: int, flag: int, n: int):
    if l == n:
        if flag == 0:
            global cnt
            cnt += 1
        return
    dfs(l + 1, flag + 1, n)
    if flag > 0:
        dfs(l + 1, flag - 1, n)


def solution(n):
    global cnt
    dfs(0, 0, n * 2)
    return cnt