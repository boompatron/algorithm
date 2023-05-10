end_num = 0
nums = []
cnt = 0


def dfs(cur, depth):
    global end_num
    if depth == len(nums):
        if cur == end_num:
            global cnt
            cnt += 1
        return
    dfs(cur + nums[depth], depth + 1)
    dfs(cur - nums[depth], depth + 1)


def solution(numbers, target):
    global end_num, nums
    end_num = target
    nums = numbers
    answer = 0
    dfs(0, 0)
    return cnt