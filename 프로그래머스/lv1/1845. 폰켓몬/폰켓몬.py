from collections import defaultdict


def solution(nums):
    d = defaultdict(int)
    ans = 0
    for n in nums:
        d[n] += 1
    return min(len(nums) // 2, len(d.keys()))