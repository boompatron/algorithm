import sys
INF = sys.maxsize


def solution(alp, cop, problems):
    target_al, target_co = 0, 0
    for problem in problems:
        target_al = max(target_al, problem[0])
        target_co = max(target_co, problem[1])

    dp = [[INF for _ in range(target_co + 1)] for __ in range(target_al + 1)]
    
    alp = min(alp, target_al)
    cop = min(cop, target_co)
    dp[alp][cop] = 0

    for i in range(alp, target_al + 1):
        for j in range(cop, target_co + 1):
            if i < target_al:
                dp[i + 1][j] = min(dp[i + 1][j], dp[i][j] + 1)
            if j < target_co:
                dp[i][j + 1] = min(dp[i][j + 1], dp[i][j] + 1)
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if i >= alp_req and j >= cop_req:
                    tmp_i = min(i + alp_rwd, target_al)
                    tmp_j = min(target_co, j + cop_rwd)
                    dp[tmp_i][tmp_j] = min(dp[tmp_i][tmp_j], dp[i][j] + cost)

    return dp[target_al][target_co]
