from copy import deepcopy

ans, apeach_arrows = [0 for _ in range(11)], []
max_score_diff = 0

def solution(n, info):
    global apeach_arrows, ans
    apeach_arrows = info
    
    dfs(0, n, [0 for __ in range(11)])
    print(max_score_diff)
    
    return ans if max_score_diff > 0 else [-1]


def dfs(depth, left_arrows, ryan_arrows):
    if depth == 11 or left_arrows == 0:
        global max_score_diff, ans
        ryan_arrows[10] += left_arrows
        
        cur_score_diff = calaulate_score_diff(ryan_arrows)
        if (max_score_diff < cur_score_diff or (max_score_diff == cur_score_diff and is_cur_ryan_smaller(ryan_arrows))):
            max_score_diff = cur_score_diff
            # ans = ryan_arrows
            ans = deepcopy(ryan_arrows)
            # print(max_score_diff, ans)
        
        ryan_arrows[10] -= left_arrows
        return
    
    dfs(depth + 1, left_arrows, ryan_arrows)
    if left_arrows > apeach_arrows[depth]:
        tmp = apeach_arrows[depth] + 1
        ryan_arrows[depth] = tmp
        dfs(depth + 1, left_arrows - tmp, ryan_arrows)
        ryan_arrows[depth] = 0
        
    
def calaulate_score_diff(ryan):
    score_diff = 0
    for i in range(11):
        if ryan[i] == 0 and apeach_arrows[i] == 0:
            continue
        score_diff += 10 - i if ryan[i] > apeach_arrows[i] else i - 10
    return score_diff


def is_cur_ryan_smaller(ryan):
    for i in range(10, -1, -1):
        if ryan[i] > ans[i]:
            return True
        elif ryan[i] < ans[i]:
            return False