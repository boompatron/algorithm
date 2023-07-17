def solution(A, B):
    A.sort()
    B.sort()
    n = len(A)
    cnt = 0
    idx = n - 1
    for i in range(n - 1, -1, -1):
        if A[i] < B[idx]:
            idx -= 1
            cnt += 1
    return cnt