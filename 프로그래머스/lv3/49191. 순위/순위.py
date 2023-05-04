def solution(n, results):
    result = [[0 for _ in range(n + 1)] for __ in range(n + 1)]
    
    for winner, loser in results:
        result[winner][loser] = 1;
        result[loser][winner] = -1;
    
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if result[i][k] == 1 and result[k][j] == 1:
                    result[i][j] = 1
                    result[j][i] = -1
                elif result[i][k] == -1 and result[k][j] == -1:
                    result[i][j] = -1
                    result[j][i] = 1
    
    cnt = 0
    for i in range(1, n + 1):
        tmp = 0
        for j in range(1, n + 1):
            if result[i][j]:
                tmp += 1
        if tmp == n - 1:
            cnt += 1
    return cnt