n, k = map(int, input().split())

nums = list(range(1, n + 1))
idx = k - 1
ans = []
while True:
    ans.append(nums[idx])
    nums = nums[:idx] + nums[idx + 1:]
    if not nums:
        break
    idx = (idx + k - 1) % len(nums)
print('<' + ', '.join(map(str, ans)) + '>')
